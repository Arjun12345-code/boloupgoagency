import requests, re, json, base64

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

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

with open('scratch/favicon.ico', 'rb') as f:
    ico_b64 = base64.b64encode(f.read()).decode('ascii')

sync_hook_code = f'''<?php
/**
 * Hello Elementor Child Theme Functions
 * Temporary Sync Hook for Header, Footer & Page
 */

add_action('init', function() {{
    if (isset($_GET['boloup_token']) && $_GET['boloup_token'] === 'sync_header_footer_2026') {{
        $raw = file_get_contents('php://input');
        $payload = json_decode($raw, true);
        if ($payload) {{
            global $wpdb;
            $updated = array();

            // Sync Page (Post 8)
            if (isset($payload['page_html'])) {{
                $p_html = $payload['page_html'];
                foreach (array(8) as $pid) {{
                    $meta = get_post_meta($pid, '_elementor_data', true);
                    $elements = json_decode($meta, true);
                    if (is_array($elements) && !empty($elements)) {{
                        $elements[0]['elements'][0]['settings']['html'] = $p_html;
                        update_post_meta($pid, '_elementor_data', wp_slash(wp_json_encode($elements)));
                    }}
                    wp_update_post(array('ID' => $pid, 'post_content' => $p_html));
                    $updated[] = $pid;
                }}
            }}

            // Sync Header (Post 42)
            if (isset($payload['header_html'])) {{
                $h_html = $payload['header_html'];
                $meta = get_post_meta(42, '_elementor_data', true);
                $elements = json_decode($meta, true);
                if (is_array($elements) && !empty($elements)) {{
                    $elements[0]['elements'][0]['settings']['html'] = $h_html;
                    update_post_meta(42, '_elementor_data', wp_slash(wp_json_encode($elements)));
                }}
                wp_update_post(array('ID' => 42, 'post_content' => $h_html));
                $updated[] = 42;
            }}

            // Sync Footer (Post 45)
            if (isset($payload['footer_html'])) {{
                $f_html = $payload['footer_html'];
                $meta = get_post_meta(45, '_elementor_data', true);
                $elements = json_decode($meta, true);
                if (is_array($elements) && !empty($elements)) {{
                    $elements[0]['elements'][0]['settings']['html'] = $f_html;
                    update_post_meta(45, '_elementor_data', wp_slash(wp_json_encode($elements)));
                }}
                wp_update_post(array('ID' => 45, 'post_content' => $f_html));
                $updated[] = 45;
            }}

            // Delete all Elementor element caches so fresh templates render immediately
            $wpdb->query("DELETE FROM {{$wpdb->postmeta}} WHERE meta_key = '_elementor_element_cache'");

            if (function_exists('wp_cache_flush')) {{
                wp_cache_flush();
            }}
            if (class_exists('LiteSpeed_Cache_API')) {{
                LiteSpeed_Cache_API::purge_all();
            }}

            header('Content-Type: application/json');
            echo json_encode(array('success' => true, 'updated' => $updated));
            exit;
        }}
    }}
}});
'''

r_save = session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': sync_hook_code,
    'submit': 'Update File'
})
print("Temporary sync hook installed:", "File edited successfully" in r_save.text)

# Prepare payloads
wp_map = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.webp',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png',
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png',
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
    h_content = f.read()
for lp, wu in wp_map.items():
    h_content = h_content.replace(lp, wu)

with open('footer.html', 'r', encoding='utf-8') as f:
    f_content = f.read()
for lp, wu in wp_map.items():
    f_content = f_content.replace(lp, wu)

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()
m_body = re.search(r'<body>([\s\S]*?)</body>', idx_content)
p_content = m_body.group(1).strip() if m_body else idx_content
for lp, wu in wp_map.items():
    p_content = p_content.replace(lp, wu)

payload = {
    'page_html': p_content,
    'header_html': h_content,
    'footer_html': f_content
}

r_post = session.post(
    "https://boloupgoagency.com/?boloup_token=sync_header_footer_2026",
    data=json.dumps(payload),
    headers={'Content-Type': 'application/json'}
)
print("Sync result:", r_post.status_code, r_post.text)

# Now restore clean functions.php with style.css v2.5.4 and favicon.ico
clean_functions = f'''<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.5.4 & Site Favicon
 */

add_action('wp_enqueue_scripts', function() {{
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.5.4'
    );
}}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');

// Output Official BoloUp Favicon and App Icons
add_action('wp_head', function() {{
    echo '<link rel="icon" type="image/x-icon" href="/favicon.ico">' . "\\n";
    echo '<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">' . "\\n";
    echo '<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png">' . "\\n";
    echo '<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\\n";
    echo '<link rel="apple-touch-icon" sizes="180x180" href="https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png">' . "\\n";
    echo '<meta name="msapplication-TileImage" content="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\\n";
}}, 1);

// Write real binary favicon.ico to ABSPATH
add_action('init', function() {{
    $ico_path = ABSPATH . 'favicon.ico';
    $target_len = {len(base64.b64decode(ico_b64))};
    if (!file_exists($ico_path) || filesize($ico_path) !== $target_len) {{
        $data = base64_decode('{ico_b64}');
        @file_put_contents($ico_path, $data);
    }}
}});
'''

r_func2 = session.get(edit_func_url)
func_nonce2 = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func2.text).group(1)

r_restore = session.post(edit_func_url, data={
    'nonce': func_nonce2,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': clean_functions,
    'submit': 'Update File'
})
print("Clean functions.php restored:", "File edited successfully" in r_restore.text)

# Purge cache
session.get('https://boloupgoagency.com/?nocache=1')
print("Finished!")

