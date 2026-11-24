import requests, re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})
session.get(login_url)
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

with open('style.css', 'r', encoding='utf-8') as f:
    local_css = f.read()

# Update version in style.css
local_css = re.sub(r'Version:\s*[\d\.]+', 'Version: 2.5.3', local_css)

theme_header = """/*
Theme Name: Hello Elementor Child - BoloUp Agency
Theme URI: https://boloupgoagency.com/
Description: Custom high-conversion one-page design for BoloUp Go Agency
Author: BoloUp Agency Development Team
Author URI: https://boloupgoagency.com/
Template: hello-elementor
Version: 2.5.3
Text Domain: hello-elementor-child
*/

"""
full_style = theme_header + local_css

edit_style_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
r_style = session.get(edit_style_url)
style_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_style.text).group(1)

r_save_style = session.post(edit_style_url, data={
    'nonce': style_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child',
    'action': 'update',
    'file': 'style.css',
    'theme': 'hello-elementor-child',
    'newcontent': full_style,
    'submit': 'Update File'
})
print("style.css v2.5.3 saved:", "File edited successfully" in r_save_style.text)

# Update functions.php with 2.5.3
edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

clean_func = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.5.3 & Site Favicon
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.5.3'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');

// Output Official BoloUp Favicon and App Icons
add_action('wp_head', function() {
    echo '<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png">' . "\\n";
    echo '<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\\n";
    echo '<link rel="apple-touch-icon" sizes="180x180" href="https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png">' . "\\n";
    echo '<meta name="msapplication-TileImage" content="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\\n";
}, 1);

// Handle direct /favicon.ico request by redirecting to 32x32 BoloUp Icon
add_action('init', function() {
    if (isset($_SERVER['REQUEST_URI']) && strpos($_SERVER['REQUEST_URI'], 'favicon.ico') !== false) {
        wp_redirect('https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png', 301);
        exit;
    }
});
"""

r_save_func = session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': clean_func,
    'submit': 'Update File'
})
print("functions.php v2.5.3 saved:", "File edited successfully" in r_save_func.text)

