import requests
import json
import re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0'
})

session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'testcookie': '1'
}, allow_redirects=True)

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace stylesheet link with WordPress get_stylesheet_directory_uri()
idx_content = re.sub(
    r'<link rel="stylesheet" href="style\.css">',
    r'<link rel="stylesheet" href="<?php echo get_stylesheet_directory_uri(); ?>/style.css?ver=2.1.3">',
    idx_content
)

wp_map = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.webp',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png',
    'assets/images/boloupgoagency.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png',
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png',
    'assets/images/BoloUp-Agency-Registration-Step-1-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-1-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-2-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-2-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-3-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-3-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-4.jpg': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-4.jpg'
}

for local_path, wp_url in wp_map.items():
    idx_content = idx_content.replace(local_path, wp_url)

landing_code = f"""<?php
/**
 * Template Name: BoloUp Go Agency Landing Page
 * Template Post Type: page
 * Description: Standalone semantic HTML high-converting one page design for BoloUp Go Agency
 */
?>
{idx_content}
"""

edit_tpl_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=template-landing.php&theme=hello-elementor-child"
r_tpl = session.get(edit_tpl_url)
tpl_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_tpl.text).group(1)

session.post(edit_tpl_url, data={
    'nonce': tpl_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=template-landing.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'template-landing.php',
    'theme': 'hello-elementor-child',
    'newcontent': landing_code,
    'submit': 'Update File'
})
print("Updated template-landing.php!")

# Purge cache
session.get("https://boloupgoagency.com/?LSCWP_CTRL=purge_all")
print("Purged LiteSpeed cache!")

