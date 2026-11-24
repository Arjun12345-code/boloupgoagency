import requests, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})
session.get(login_url)
r_login = session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'testcookie': '1'
}, allow_redirects=True)
print("Logged in:", "wp-admin" in r_login.url)

# 1. Update style.css
edit_style_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
r_style = session.get(edit_style_url)
style_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_style.text).group(1)

with open('style.css', 'r', encoding='utf-8') as f:
    local_css = f.read()

theme_header = """/*
Theme Name: Hello Elementor Child - BoloUp Agency
Theme URI: https://boloupgoagency.com/
Description: Custom high-conversion one-page design for BoloUp Go Agency
Author: BoloUp Agency Development Team
Author URI: https://boloupgoagency.com/
Template: hello-elementor
Version: 2.2.0
Text Domain: hello-elementor-child
*/

"""
full_style = theme_header + local_css

r_save_style = session.post(edit_style_url, data={
    'nonce': style_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child',
    'action': 'update',
    'file': 'style.css',
    'theme': 'hello-elementor-child',
    'newcontent': full_style,
    'submit': 'Update File'
})
print("style.css v2.2.0 updated:", "File edited successfully" in r_save_style.text)

# 2. Update functions.php with sync hook
edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

func_code_sync = r"""<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.2.0
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.2.0'
    );
}, 20);

add_filter('show_admin_bar', '__return_false');

add_action('init', function() {
    if (isset($_GET['boloup_token']) && $_GET['boloup_token'] === 'sync_v220_nobadge') {
        $raw = file_get_contents('php://input');
        $payload = json_decode($raw, true);
        if ($payload) {
            $updated = array();

            // Sync Header (Post 42)
            if (isset($payload['header_html'])) {
                $h_html = $payload['header_html'];
                $meta = get_post_meta(42, '_elementor_data', true);
                $elements = json_decode($meta, true);
                if (is_array($elements) && !empty($elements)) {
                    $elements[0]['elements'][0]['settings']['html'] = $h_html;
                    update_post_meta(42, '_elementor_data', wp_slash(wp_json_encode($elements)));
                }
                wp_update_post(array('ID' => 42, 'post_content' => $h_html));
                $updated[] = 42;
            }

            // Sync Footer (Post 45)
            if (isset($payload['footer_html'])) {
                $f_html = $payload['footer_html'];
                $meta = get_post_meta(45, '_elementor_data', true);
                $elements = json_decode($meta, true);
                if (is_array($elements) && !empty($elements)) {
                    $elements[0]['elements'][0]['settings']['html'] = $f_html;
                    update_post_meta(45, '_elementor_data', wp_slash(wp_json_encode($elements)));
                }
                wp_update_post(array('ID' => 45, 'post_content' => $f_html));
                $updated[] = 45;
            }

            if (class_exists('\Elementor\Plugin')) {
                \Elementor\Plugin::$instance->files_manager->clear_cache();
            }
            if (class_exists('\LiteSpeed\Purge')) {
                \LiteSpeed\Purge::purge_all();
            }
            do_action('litespeed_purge_all');
            wp_cache_flush();
            header('Content-Type: application/json');
            echo json_encode(array('success' => true, 'updated' => $updated));
            exit;
        }
        header('Content-Type: application/json');
        echo json_encode(array('success' => false, 'error' => 'no_payload'));
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
    'newcontent': func_code_sync,
    'submit': 'Update File'
})
print("Added sync hook to functions.php:", "File edited successfully" in r_save_func.text)

# 3. Prepare clean HTML payloads
wp_map = {
    'assets/images/boloup-header-logo.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-header-logo.png'
}

with open('header.html', 'r', encoding='utf-8') as f:
    header_content = f.read()
for local_path, wp_url in wp_map.items():
    header_content = header_content.replace(local_path, wp_url)

with open('footer.html', 'r', encoding='utf-8') as f:
    footer_content = f.read()
for local_path, wp_url in wp_map.items():
    footer_content = footer_content.replace(local_path, wp_url)

payload = {
    'header_html': header_content,
    'footer_html': footer_content
}

r_sync = session.post(
    "https://boloupgoagency.com/?boloup_token=sync_v220_nobadge",
    data=json.dumps(payload),
    headers={'Content-Type': 'application/json'}
)
print("Sync request response:", r_sync.status_code, r_sync.text)

# 4. Clean functions.php back to clean production code v2.2.0
clean_func = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.2.0
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.2.0'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');
"""

r_func2 = session.get(edit_func_url)
func_nonce2 = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func2.text).group(1)

r_save_clean = session.post(edit_func_url, data={
    'nonce': func_nonce2,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': clean_func,
    'submit': 'Update File'
})
print("Cleaned functions.php status:", "File edited successfully" in r_save_clean.text)

# 5. Hard purge LiteSpeed Cache
session.get("https://boloupgoagency.com/?LSCWP_CTRL=purge_all")
print("Purge all cache done!")

