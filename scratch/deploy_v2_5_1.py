import requests
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update style.css locally with !important on body background and explicit hero zero-bg rules
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Ensure body background-image has !important
css = re.sub(
    r'background-image:\s*radial-gradient[\s\S]*?linear-gradient\(180deg,\s*#06090e\s*0%,\s*#030508\s*50%,\s*#06090e\s*100%\);',
    '''background-image:
    radial-gradient(circle at 8% 55%, rgba(249, 58, 140, 0.08) 0%, transparent 40%),
    radial-gradient(circle at 92% 75%, rgba(255, 122, 0, 0.08) 0%, transparent 40%),
    linear-gradient(180deg, #06090e 0%, #030508 50%, #06090e 100%) !important;''',
    css
)

# Ensure hero section explicitly has no background
if '/* Zero Background for Hero Section */' not in css:
    hero_zero_bg = """
/* Zero Background for Hero Section */
.hero-section {
  position: relative;
  padding: 70px 0 100px;
  overflow: hidden;
  z-index: 2;
  background: transparent !important;
  background-color: transparent !important;
  background-image: none !important;
}

.hero-visual,
.hero-visual-frame,
.hero-img-wrap {
  background: transparent !important;
  background-color: transparent !important;
  background-image: none !important;
  box-shadow: none !important;
  border: none !important;
}

.hero-glow-backdrop,
.hero-float-element {
  display: none !important;
}
"""
    css = css.replace('.hero-section {', hero_zero_bg + '\n.hero-section {')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Local style.css updated for v2.5.1!")

# 2. Login to WordPress
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
print("Logged in to WordPress:", "wp-admin" in r_login.url)

# 3. Update style.css to v2.5.1 in theme editor
edit_style_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
r_style = session.get(edit_style_url)
style_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_style.text).group(1)

theme_header = """/*
Theme Name: Hello Elementor Child - BoloUp Agency
Theme URI: https://boloupgoagency.com/
Description: Custom high-conversion one-page design for BoloUp Go Agency
Author: BoloUp Agency Development Team
Author URI: https://boloupgoagency.com/
Template: hello-elementor
Version: 2.5.1
Text Domain: hello-elementor-child
*/

"""
full_style = theme_header + css

r_save_style = session.post(edit_style_url, data={
    'nonce': style_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child',
    'action': 'update',
    'file': 'style.css',
    'theme': 'hello-elementor-child',
    'newcontent': full_style,
    'submit': 'Update File'
})
print("style.css v2.5.1 updated in theme:", "File edited successfully" in r_save_style.text)

# 4. Update functions.php with sync hook and version 2.5.1
edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

func_code_sync = r"""<?php
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

add_filter('show_admin_bar', '__return_false');

add_action('wp_head', function() {
    echo '<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png">' . "\n";
    echo '<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\n";
    echo '<link rel="apple-touch-icon" sizes="180x180" href="https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png">' . "\n";
    echo '<meta name="msapplication-TileImage" content="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\n";
}, 1);

add_action('init', function() {
    if (isset($_GET['boloup_token']) && $_GET['boloup_token'] === 'sync_v251_boloupgo') {
        $raw = file_get_contents('php://input');
        $payload = json_decode($raw, true);
        if ($payload) {
            $updated = array();

            // Sync Page Content (Posts 26 & 35)
            if (isset($payload['page_html'])) {
                $p_html = $payload['page_html'];
                foreach (array(26, 35) as $pid) {
                    $meta = get_post_meta($pid, '_elementor_data', true);
                    $elements = json_decode($meta, true);
                    if (is_array($elements) && !empty($elements)) {
                        $elements[0]['elements'][0]['settings']['html'] = $p_html;
                        update_post_meta($pid, '_elementor_data', wp_slash(wp_json_encode($elements)));
                    }
                    wp_update_post(array('ID' => $pid, 'post_content' => $p_html));
                    $updated[] = $pid;
                }
            }

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

            if (function_exists('wp_cache_flush')) {
                wp_cache_flush();
            }
            if (class_exists('LiteSpeed_Cache_API')) {
                LiteSpeed_Cache_API::purge_all();
            }

            header('Content-Type: application/json');
            echo json_encode(array('success' => true, 'updated' => $updated));
            exit;
        }
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
print("functions.php sync hook added:", "File edited successfully" in r_save_func.text)

# 5. Prepare clean payloads with correct image mapping
wp_map = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.webp',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png',
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-ecosystem.png',
    'assets/images/boloup-agent-role.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agent-Role.png',
    'assets/images/boloup-header-logo.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-header-logo.png',
    'assets/images/boloup-avatar-192x192.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png',
    'assets/images/boloup-avatar-32x32.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png',
    'assets/images/cropped-boloup.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png',
    'assets/images/BoloUp-Agency-Registration-Step-1-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-1-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-2-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-2-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-3-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-3-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-4.jpg': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-4.jpg',
}

with open('header.html', 'r', encoding='utf-8') as f:
    header_content = f.read()
for local_path, wp_url in wp_map.items():
    header_content = header_content.replace(local_path, wp_url)

with open('footer.html', 'r', encoding='utf-8') as f:
    footer_content = f.read()
for local_path, wp_url in wp_map.items():
    footer_content = footer_content.replace(local_path, wp_url)

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

match_body = re.search(r'<body>([\s\S]*?)</body>', index_content)
page_content = match_body.group(1).strip() if match_body else index_content

for local_path, wp_url in wp_map.items():
    page_content = page_content.replace(local_path, wp_url)

payload = {
    'page_html': page_content,
    'header_html': header_content,
    'footer_html': footer_content
}

r_sync = session.post(
    "https://boloupgoagency.com/?boloup_token=sync_v251_boloupgo",
    data=json.dumps(payload),
    headers={'Content-Type': 'application/json'}
)
print("Sync response:", r_sync.status_code, r_sync.text)

# 6. Save clean production functions.php with v2.5.1 and favicon 301 redirect
clean_func = """<?php
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

r_func_clean_page = session.get(edit_func_url)
func_nonce_clean = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func_clean_page.text).group(1)

r_save_clean = session.post(edit_func_url, data={
    'nonce': func_nonce_clean,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': clean_func,
    'submit': 'Update File'
})
print("Clean functions.php saved:", "File edited successfully" in r_save_clean.text)
print("Deployment v2.5.1 finished successfully!")

