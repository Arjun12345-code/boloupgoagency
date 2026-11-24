import requests
import json
import re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0'
})

session.get(login_url)
r_login = session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'testcookie': '1'
}, allow_redirects=True)
print("Logged in:", "wp-admin" in r_login.url)

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

func_code_ajax = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.6
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.1.6'
    );
}, 20);

add_filter('show_admin_bar', '__return_false');

add_action('wp_ajax_sync_boloup_content', function() {
    if (!current_user_can('manage_options')) {
        wp_send_json_error('forbidden', 403);
    }
    $raw = file_get_contents('php://input');
    $payload = json_decode($raw, true);
    if (!$payload || !isset($payload['html'])) {
        wp_send_json_error('missing_html', 400);
    }
    $html = $payload['html'];
    $updated = array();
    foreach (array(26, 35) as $pid) {
        $meta = get_post_meta($pid, '_elementor_data', true);
        $elements = json_decode($meta, true);
        if (is_array($elements) && !empty($elements)) {
            $elements[0]['elements'][0]['settings']['html'] = $html;
            update_post_meta($pid, '_elementor_data', wp_slash(wp_json_encode($elements)));
        }
        wp_update_post(array('ID' => $pid, 'post_content' => $html));
        $updated[] = $pid;
    }
    if (class_exists('\\\\Elementor\\\\Plugin')) {
        \\\\Elementor\\\\Plugin::$instance->files_manager->clear_cache();
    }
    if (class_exists('\\\\LiteSpeed\\\\Purge')) {
        \\\\LiteSpeed\\\\Purge::purge_all();
    }
    do_action('litespeed_purge_all');
    wp_cache_flush();
    wp_send_json_success(array('updated' => $updated));
});
"""

session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': func_code_ajax,
    'submit': 'Update File'
})
print("Added ajax hook to functions.php!")

# Prepare HTML from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

wp_map = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.webp',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png',
    'assets/images/boloupgoagency.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png',
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png',
    'assets/images/BoloUp-Agency-Registration-Step-1-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-1-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-2-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-2-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-3-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-3-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-4.jpg': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-4.jpg'
}

for local_path, wp_url in wp_map.items():
    idx_content = idx_content.replace(local_path, wp_url)

body_m = re.search(r'<body[^>]*>(.*?)</body>', idx_content, re.DOTALL)
page_html_wp = body_m.group(1).strip() if body_m else idx_content

r_ajax = session.post(
    "https://boloupgoagency.com/wp-admin/admin-ajax.php?action=sync_boloup_content",
    data=json.dumps({'html': page_html_wp}),
    headers={'Content-Type': 'application/json'}
)
print("AJAX response:", r_ajax.status_code, r_ajax.text)

# Clean functions.php back to clean production code
clean_func = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.6
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.1.6'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');
"""

r_func2 = session.get(edit_func_url)
func_nonce2 = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func2.text).group(1)

session.post(edit_func_url, data={
    'nonce': func_nonce2,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': clean_func,
    'submit': 'Update File'
})
print("Cleaned functions.php to production code v2.1.6!")

# Purge LiteSpeed Cache
session.get("https://boloupgoagency.com/?LSCWP_CTRL=purge_all")
print("LiteSpeed cache purge requested!")

