import requests
import re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

r_login = session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgoagency.com/wp-admin/',
    'testcookie': '1'
}, allow_redirects=True)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace stylesheet link with WordPress stylesheet directory URI
content = re.sub(
    r'<link rel="stylesheet" href="style\.css">',
    r'<link rel="stylesheet" href="<?php echo get_stylesheet_directory_uri(); ?>/style.css?ver=2.1.0">',
    content
)

# Map exact verified WordPress media URLs
wp_mappings = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.webp',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png',
    'assets/images/boloupgoagency.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png',
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png',
    'assets/images/boloup-agent-role.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agent-Role.png',
    'assets/images/boloup-agency-registration-step-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-1.png',
    'assets/images/boloup-agency-registration-step-2.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-2.png',
    'assets/images/boloup-agency-registration-step-3.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-3.png',
    'assets/images/boloup-agency-registration-step-4.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-4.png',
    'assets/images/boloup-agency-registration-step-5.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-agent-add-new-host-part-1.jpg',
    'assets/images/boloup-agency-registration-step-6.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agent-Role.png',
}

for local_path, wp_url in wp_mappings.items():
    content = content.replace(local_path, wp_url)

# Also ensure any lowercase variant of BoloUp-Ecosystem.png is updated
content = content.replace(
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-ecosystem.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png'
)

landing_code = f"""<?php
/**
 * Template Name: BoloUp Go Agency Landing Page
 * Template Post Type: page
 * Description: Standalone semantic HTML high-converting one page design for BoloUp Go Agency
 */
?>
{content}
"""

front_code = f"""<?php
/**
 * Front Page Template for BoloUp Go Agency
 */
?>
{content}
"""

for fname, code in [('template-landing.php', landing_code), ('front-page.php', front_code)]:
    edit_url = f"https://boloupgoagency.com/wp-admin/theme-editor.php?file={fname}&theme=hello-elementor-child"
    r_get = session.get(edit_url)
    nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_get.text).group(1)
    r_post = session.post(edit_url, data={
        'nonce': nonce,
        '_wp_http_referer': f'/wp-admin/theme-editor.php?file={fname}&theme=hello-elementor-child',
        'action': 'update',
        'file': fname,
        'theme': 'hello-elementor-child',
        'newcontent': code,
        'submit': 'Update File'
    })
    print(f"Updated {fname}:", "File edited successfully" in r_post.text)

# Purge cache
session.get("https://boloupgoagency.com/?LSCWP_CTRL=purge_all")
print("Purged LiteSpeed cache!")

