import requests, re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

test_code = r"""<?php
add_action('init', function() {
    if (isset($_GET['get_widget_eco'])) {
        $meta = get_post_meta(26, '_elementor_data', true);
        $data = json_decode($meta, true);
        $html = $data[0]['elements'][0]['settings']['html'];
        preg_match('/<img[^>]*ecosystem[^>]*>/i', $html, $m);
        echo isset($m[0]) ? $m[0] : 'NOT_FOUND';
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

r_eco = session.get('https://boloupgoagency.com/?get_widget_eco=1')
print("Widget HTML ecosystem img tag:")
print(r_eco.text)

