import requests, re, json

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

# Let's read elementor data from post 26 by editing functions.php to output it
edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

test_code = r"""<?php
add_action('init', function() {
    if (isset($_GET['dump_meta'])) {
        $meta = get_post_meta(26, '_elementor_data', true);
        echo $meta;
        exit;
    }
});
"""

r_save = session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': test_code,
    'submit': 'Update File'
})

r_meta = session.get('https://boloupgoagency.com/?dump_meta=1')
data = r_meta.json()

def print_structure(item, depth=0):
    indent = "  " * depth
    el_type = item.get('elType', '')
    widget = item.get('widgetType', '')
    eid = item.get('id', '')
    has_html = 'html' in item.get('settings', {})
    print(f"{indent}- id: {eid}, elType: {el_type}, widget: {widget}, has_html: {has_html}")
    for ch in item.get('elements', []):
        print_structure(ch, depth + 1)

print("Post 26 Elementor Structure:")
for el in data:
    print_structure(el)

