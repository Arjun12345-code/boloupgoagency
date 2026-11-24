import requests, re, json

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.get(login_url)
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

edit_func_url = 'https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child'
r_func = s.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

func_code_f = r"""<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.6
 */
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style('boloup-agency-theme-style', get_stylesheet_directory_uri() . '/style.css', array(), '2.1.6');
}, 20);
add_filter('show_admin_bar', '__return_false');

add_action('init', function() {
    if (isset($_GET['clean_footer']) && $_GET['clean_footer'] === 'yes123') {
        $meta = get_post_meta(45, '_elementor_data', true);
        if ($meta) {
            $raw = str_replace('Agency ID: 2527626', 'How to Join', $meta);
            $raw = str_replace('2527626', '', $raw);
            update_post_meta(45, '_elementor_data', wp_slash($raw));
        }
        $post = get_post(45);
        if ($post) {
            $c = str_replace('Agency ID: 2527626', 'How to Join', $post->post_content);
            wp_update_post(array('ID' => 45, 'post_content' => $c));
        }
        if (class_exists('\Elementor\Plugin')) {
            \Elementor\Plugin::$instance->files_manager->clear_cache();
        }
        if (class_exists('\LiteSpeed\Purge')) {
            \LiteSpeed\Purge::purge_all();
        }
        do_action('litespeed_purge_all');
        wp_cache_flush();
        echo json_encode(array('success' => true));
        exit;
    }
});
"""

s.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': func_code_f,
    'submit': 'Update File'
})

r_clean = s.get('https://boloupgoagency.com/?clean_footer=yes123')
print('Clean footer response:', r_clean.text)

clean_func = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.6
 */
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style('boloup-agency-theme-style', get_stylesheet_directory_uri() . '/style.css', array(), '2.1.6');
}, 20);
add_filter('show_admin_bar', '__return_false');
"""

r_func2 = s.get(edit_func_url)
func_nonce2 = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func2.text).group(1)
s.post(edit_func_url, data={
    'nonce': func_nonce2,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': clean_func,
    'submit': 'Update File'
})
s.get('https://boloupgoagency.com/?LSCWP_CTRL=purge_all')
print('Cleaned functions.php & purged cache!')

