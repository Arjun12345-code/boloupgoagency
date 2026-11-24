import requests, re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

sql_fix_code = r"""<?php
add_action('init', function() {
    if (isset($_GET['fix_all_image_db'])) {
        global $wpdb;

        // 1. Replace lowercase boloup-ecosystem.png with BoloUp-Ecosystem.png
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'boloup-ecosystem.png', 'BoloUp-Ecosystem.png')");
        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'boloup-ecosystem.png', 'BoloUp-Ecosystem.png')");

        // 2. Delete all elementor element caches so Elementor re-renders fresh
        $wpdb->query("DELETE FROM {$wpdb->postmeta} WHERE meta_key = '_elementor_element_cache'");

        // 3. Purge LiteSpeed & WP Object Cache
        if (function_exists('wp_cache_flush')) {
            wp_cache_flush();
        }
        if (class_exists('LiteSpeed_Cache_API')) {
            LiteSpeed_Cache_API::purge_all();
        }
        if (class_exists('\\Elementor\\Plugin')) {
            \\Elementor\\Plugin::$instance->files_manager->clear_cache();
        }

        echo "DB_FIX_SUCCESSFUL";
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
    'newcontent': sql_fix_code,
    'submit': 'Update File'
})

r_run = session.get('https://boloupgoagency.com/?fix_all_image_db=1')
print("Fix result:", r_run.text)

