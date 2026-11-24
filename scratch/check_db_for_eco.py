import requests, re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

test_code = r"""<?php
add_action('init', function() {
    if (isset($_GET['check_front'])) {
        echo "show_on_front: " . get_option('show_on_front') . "\n";
        echo "page_on_front: " . get_option('page_on_front') . "\n";
        echo "page_for_posts: " . get_option('page_for_posts') . "\n";
        
        // Find which post content contains 'boloup-ecosystem.png'
        global $wpdb;
        $rows = $wpdb->get_results("SELECT ID, post_title, post_type, post_status FROM {$wpdb->posts} WHERE post_content LIKE '%boloup-ecosystem.png%'");
        echo "Posts containing lowercase boloup-ecosystem.png in post_content:\n";
        foreach ($rows as $r) {
            echo "  ID: {$r->ID}, Title: {$r->post_title}, Type: {$r->post_type}\n";
        }

        $meta_rows = $wpdb->get_results("SELECT post_id, meta_key FROM {$wpdb->postmeta} WHERE meta_value LIKE '%boloup-ecosystem.png%'");
        echo "Postmeta containing lowercase boloup-ecosystem.png:\n";
        foreach ($meta_rows as $mr) {
            echo "  Post ID: {$mr->post_id}, Key: {$mr->meta_key}\n";
        }
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
    'newcontent': test_code,
    'submit': 'Update File'
})

r_check = session.get('https://boloupgoagency.com/?check_front=1')
print("Database check result:")
print(r_check.text)

