import requests, re

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

# Let's check test query
edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = s.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

test_code = r"""<?php
add_action('init', function() {
    if (isset($_GET['test_fav_write'])) {
        $path = ABSPATH . 'favicon.ico';
        $exists_before = file_exists($path);
        $writable = is_writable(ABSPATH);
        $w_path = is_writable($path);
        $put = file_put_contents($path, 'test123');
        echo json_encode([
            'path' => $path,
            'exists_before' => $exists_before,
            'abspath_writable' => $writable,
            'path_writable' => $w_path,
            'put_result' => $put,
            'exists_after' => file_exists($path),
            'filesize' => file_exists($path) ? filesize($path) : null
        ]);
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
    'newcontent': test_code,
    'submit': 'Update File'
})

r_test = s.get('https://boloupgoagency.com/?test_fav_write=1')
print("Test write result:", r_test.text)

