import requests
import re
import json

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

print("1. Logging into WordPress...")
r_page = session.get(login_url)
r_login = session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgoagency.com/wp-admin/',
    'testcookie': '1'
}, allow_redirects=True)

print("Logged in successfully:", "wp-admin" in r_login.url)

# 2. Upload WebP version
upload_page = session.get("https://boloupgoagency.com/wp-admin/media-new.php")
async_nonce = re.search(r'"_wpnonce":"([^"]+)"', upload_page.text).group(1)

webp_path = "assets/images/boloupgoagency-nobg.webp"
with open(webp_path, 'rb') as f_webp:
    res_webp = session.post(
        "https://boloupgoagency.com/wp-admin/async-upload.php",
        data={'name': 'boloupgoagency-nobg.webp', 'action': 'upload-attachment', '_wpnonce': async_nonce},
        files={'async-upload': ('boloupgoagency-nobg.webp', f_webp, 'image/webp')}
    )
print("Uploaded webp status:", res_webp.status_code)
webp_url = "https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.webp"
try:
    data_webp = res_webp.json()
    if data_webp.get('success'):
        webp_url = data_webp['data']['url'].replace('http://', 'https://')
        print("Webp URL:", webp_url)
except Exception as e:
    print("Webp response parse note:", e)

# 3. Update style.css in hello-elementor-child
edit_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
r_edit = session.get(edit_url)
nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_edit.text).group(1)
print("Got theme editor nonce for style.css:", nonce)

with open('style.css', 'r', encoding='utf-8') as f:
    local_css = f.read()

theme_header = """/*
Theme Name: Hello Elementor Child - BoloUp Agency
Theme URI: https://boloupgoagency.com/
Description: Custom high-conversion one-page design for BoloUp Go Agency - Atmospheric Smoke & Fire Palette
Author: BoloUp Agency Development Team
Author URI: https://boloupgoagency.com/
Template: hello-elementor
Version: 2.1.0
Text Domain: hello-elementor-child
*/

"""

full_style_content = theme_header + local_css

post_data = {
    'nonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child',
    'action': 'update',
    'file': 'style.css',
    'theme': 'hello-elementor-child',
    'newcontent': full_style_content,
    'submit': 'Update File'
}

r_save_style = session.post(edit_url, data=post_data)
print("Updated style.css, status:", r_save_style.status_code, "in text:", "File edited successfully" in r_save_style.text)

# 4. Prepare updated template-landing.php and front-page.php
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace local relative asset paths with WordPress upload URLs
png_nobg_url = "https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png"
index_html = index_html.replace('assets/images/boloupgoagency-nobg.png', png_nobg_url)
index_html = index_html.replace('assets/images/boloupgoagency-nobg.webp', webp_url)
index_html = index_html.replace('assets/images/boloupgoagency.png', png_nobg_url)

# Replace other assets with WP uploads URLs if needed
asset_map = {
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-ecosystem.png',
    'assets/images/boloup-agent-role.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-agent-role.png',
    'assets/images/boloup-agency-registration-step-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-agency-registration-step-1.png',
    'assets/images/boloup-agency-registration-step-2.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-agency-registration-step-2.png',
    'assets/images/boloup-agency-registration-step-3.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-agency-registration-step-3.png',
    'assets/images/boloup-agency-registration-step-4.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-agency-registration-step-4.png',
    'assets/images/boloup-agency-registration-step-5.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-agency-registration-step-5.png',
    'assets/images/boloup-agency-registration-step-6.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-agency-registration-step-6.png'
}

for local_p, wp_p in asset_map.items():
    index_html = index_html.replace(local_p, wp_p)

landing_template_code = f"""<?php
/**
 * Template Name: BoloUp Go Agency Landing Page
 * Template Post Type: page
 * Description: Standalone semantic HTML high-converting one page design for BoloUp Go Agency
 */
?>
{index_html}
"""

# Update template-landing.php
edit_tpl_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=template-landing.php&theme=hello-elementor-child"
r_tpl = session.get(edit_tpl_url)
tpl_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_tpl.text).group(1)

post_tpl_data = {
    'nonce': tpl_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=template-landing.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'template-landing.php',
    'theme': 'hello-elementor-child',
    'newcontent': landing_template_code,
    'submit': 'Update File'
}
r_save_tpl = session.post(edit_tpl_url, data=post_tpl_data)
print("Updated template-landing.php:", "File edited successfully" in r_save_tpl.text)

# Update front-page.php
front_page_code = f"""<?php
/**
 * Front Page Template for BoloUp Go Agency
 */
?>
{index_html}
"""

edit_front_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=front-page.php&theme=hello-elementor-child"
r_front = session.get(edit_front_url)
front_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_front.text).group(1)

post_front_data = {
    'nonce': front_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=front-page.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'front-page.php',
    'theme': 'hello-elementor-child',
    'newcontent': front_page_code,
    'submit': 'Update File'
}
r_save_front = session.post(edit_front_url, data=post_front_data)
print("Updated front-page.php:", "File edited successfully" in r_save_front.text)

# 5. Update functions.php version string to '2.1.0'
edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

func_code = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.0
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.1.0'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');
"""

post_func_data = {
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': func_code,
    'submit': 'Update File'
}
r_save_func = session.post(edit_func_url, data=post_func_data)
print("Updated functions.php:", "File edited successfully" in r_save_func.text)

# 6. Purge LiteSpeed Cache
purge_urls = [
    "https://boloupgoagency.com/?LSCWP_CTRL=purge",
    "https://boloupgoagency.com/?LSCWP_CTRL=purge_all",
    "https://boloupgoagency.com/wp-admin/admin.php?page=litespeed-purge&_wpnonce="
]
for p_url in purge_urls:
    try:
        session.get(p_url)
    except Exception:
        pass
print("Purged LiteSpeed cache!")

