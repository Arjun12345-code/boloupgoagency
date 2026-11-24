import requests
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

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

func_code = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.4
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.1.4'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');

// Purge all caches hook
add_action('init', function() {
    if (isset($_GET['hard_purge_all']) && current_user_can('manage_options')) {
        if (class_exists('\\LiteSpeed\\Purge')) {
            \\LiteSpeed\\Purge::purge_all();
        }
        do_action('litespeed_purge_all');
        if (function_exists('wp_cache_flush')) {
            wp_cache_flush();
        }
        if (class_exists('\\Elementor\\Plugin')) {
            \\Elementor\\Plugin::$instance->files_manager->clear_cache();
        }
        echo json_encode(array('purged' => true));
        exit;
    }
});
"""

r_save = session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': func_code,
    'submit': 'Update File'
})
print("Added hard purge hook:", "File edited successfully" in r_save.text)

# Execute hard purge
r_purge = session.get("https://boloupgoagency.com/?hard_purge_all=1")
print("Hard purge response:", r_purge.status_code, r_purge.text)

# Also update style.css version to 2.1.4
edit_style_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
r_style = session.get(edit_style_url)
style_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_style.text).group(1)
with open('style.css', 'r', encoding='utf-8') as f:
    local_css = f.read()

theme_header = """/*
Theme Name: Hello Elementor Child - BoloUp Agency
Theme URI: https://boloupgoagency.com/
Description: Custom high-conversion one-page design for BoloUp Go Agency - Atmospheric Smoke & Fire Palette
Author: BoloUp Agency Development Team
Author URI: https://boloupgoagency.com/
Template: hello-elementor
Version: 2.1.4
Text Domain: hello-elementor-child
*/

"""
session.post(edit_style_url, data={
    'nonce': style_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child',
    'action': 'update',
    'file': 'style.css',
    'theme': 'hello-elementor-child',
    'newcontent': theme_header + local_css,
    'submit': 'Update File'
})
print("Updated style.css to 2.1.4!")

# Re-run purge
session.get("https://boloupgoagency.com/?hard_purge_all=1")
print("Final hard purge complete!")

