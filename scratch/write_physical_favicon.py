import requests
import re
import base64

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})
session.get(login_url)
session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'testcookie': '1'
}, allow_redirects=True)

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

# Read 32x32 png icon bytes
with open('assets/images/boloup-avatar-32x32.png', 'rb') as f:
    icon_b64 = base64.b64encode(f.read()).decode('ascii')

func_code = f'''<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.5.3 & Site Favicon
 */

add_action('wp_enqueue_scripts', function() {{
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.5.3'
    );
}}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');

// Output Official BoloUp Favicon and App Icons
add_action('wp_head', function() {{
    echo '<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png">' . "\\n";
    echo '<link rel="shortcut icon" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png">' . "\\n";
    echo '<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\\n";
    echo '<link rel="apple-touch-icon" sizes="180x180" href="https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png">' . "\\n";
    echo '<meta name="msapplication-TileImage" content="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\\n";
}}, 1);

// Ensure physical favicon.ico exists in ABSPATH
if (!file_exists(ABSPATH . 'favicon.ico') || filesize(ABSPATH . 'favicon.ico') === 0) {{
    $icon_data = base64_decode('{icon_b64}');
    @file_put_contents(ABSPATH . 'favicon.ico', $icon_data);
}}
'''

r_save = session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': func_code,
    'submit': 'Update File'
})
print("functions.php saved:", "File edited successfully" in r_save.text)

