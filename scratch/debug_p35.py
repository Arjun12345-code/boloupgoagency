import requests
import json

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

# Update functions.php to output exact elementor data for 35
edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
import re
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

func_code = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.3
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.1.3'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');

add_action('init', function() {
    if (isset($_GET['dump_p35']) && current_user_can('manage_options')) {
        $meta = get_post_meta(35, '_elementor_data', true);
        echo $meta;
        exit;
    }
});
"""

session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': func_code,
    'submit': 'Update File'
})

r_dump = session.get("https://boloupgoagency.com/?dump_p35=1")
print("Dump status:", r_dump.status_code)
print("Dump len:", len(r_dump.text))
data = r_dump.json()
print("Top-level items:", len(data))
print("First item keys:", data[0].keys())
print("First item elements:", len(data[0].get('elements', [])))
if len(data[0].get('elements', [])) > 0:
    first_el = data[0]['elements'][0]
    print("Inner element keys:", first_el.keys())
    print("Inner element widgetType:", first_el.get('widgetType'))
    print("HTML length:", len(first_el.get('settings', {}).get('html', '')))
    print("HTML snippet:", first_el.get('settings', {}).get('html', '')[:300])

