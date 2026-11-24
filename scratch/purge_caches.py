import requests, re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

purge_and_clean_func = r"""<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.5.1 & Site Favicon
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.5.1'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');

// Output Official BoloUp Favicon and App Icons
add_action('wp_head', function() {
    echo '<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png">' . "\n";
    echo '<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\n";
    echo '<link rel="apple-touch-icon" sizes="180x180" href="https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png">' . "\n";
    echo '<meta name="msapplication-TileImage" content="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\n";
}, 1);

// Handle direct /favicon.ico request by redirecting to 32x32 BoloUp Icon
add_action('init', function() {
    if (isset($_SERVER['REQUEST_URI']) && strpos($_SERVER['REQUEST_URI'], 'favicon.ico') !== false) {
        wp_redirect('https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png', 301);
        exit;
    }

    if (isset($_GET['purge_all_caches'])) {
        if (function_exists('wp_cache_flush')) {
            wp_cache_flush();
        }
        if (class_exists('LiteSpeed_Cache_API')) {
            LiteSpeed_Cache_API::purge_all();
        }
        if (class_exists('\\Elementor\\Plugin')) {
            \\Elementor\\Plugin::$instance->files_manager->clear_cache();
        }
        echo "ALL_CACHES_PURGED";
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
    'newcontent': purge_and_clean_func,
    'submit': 'Update File'
})
print("Updated functions.php with purge hook:", "File edited successfully" in r_save.text)

# Trigger purge
p_res = session.get('https://boloupgoagency.com/?purge_all_caches=1')
print("Purge response:", p_res.text)

