import requests, re, base64

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = s.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

with open('scratch/favicon.ico', 'rb') as f:
    ico_b64 = base64.b64encode(f.read()).decode('ascii')

deploy_code = f'''<?php
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

s.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': deploy_code,
    'submit': 'Update File'
})

# Trigger home to write file
s.get('https://boloupgoagency.com/?nocache=1')
print("Deploy finished.")

