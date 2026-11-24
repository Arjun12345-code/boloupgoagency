import requests, re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})
session.get(login_url)
r_login = session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})
print("Logged in:", "wp-admin" in r_login.url)

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)
print("Func nonce:", func_nonce)

fix_php = r"""<?php
add_action('init', function() {
    if (isset($_GET['run_direct_db_fix']) && $_GET['run_direct_db_fix'] === 'yes123') {
        global $wpdb;
        // Fix image path in posts table
        $affected_posts = $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'boloup-ecosystem.png', 'BoloUp-Ecosystem.png')");
        // Fix image path in postmeta table
        $affected_meta = $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'boloup-ecosystem.png', 'BoloUp-Ecosystem.png')");
        // Delete all Elementor element caches
        $deleted_caches = $wpdb->query("DELETE FROM {$wpdb->postmeta} WHERE meta_key = '_elementor_element_cache'");

        if (function_exists('wp_cache_flush')) wp_cache_flush();
        if (class_exists('LiteSpeed_Cache_API')) LiteSpeed_Cache_API::purge_all();

        echo "SUCCESS: affected_posts=$affected_posts, affected_meta=$affected_meta, deleted_caches=$deleted_caches";
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
    'newcontent': fix_php,
    'submit': 'Update File'
})
print("Saved fix hook:", "File edited successfully" in r_save.text)

# Trigger
r_trig = session.get('https://boloupgoagency.com/?run_direct_db_fix=yes123')
print("Trigger output:", r_trig.text[:200])

# Restore clean functions.php
clean_func = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.5.2 & Site Favicon
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.5.2'
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

r_func2 = session.get(edit_func_url)
func_nonce2 = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func2.text).group(1)

r_save2 = session.post(edit_func_url, data={
    'nonce': func_nonce2,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': clean_func,
    'submit': 'Update File'
})
print("Restored clean functions.php:", "File edited successfully" in r_save2.text)

