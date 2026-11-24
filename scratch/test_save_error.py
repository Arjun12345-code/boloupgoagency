import requests, re, sys
sys.stdout.reconfigure(encoding='utf-8')

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})
session.get(login_url)
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

test_code = """<?php
// test
"""

r_post = session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': test_code,
    'submit': 'Update File'
})

m = re.findall(r'<div[^>]*class="[^"]*notice[^"]*"[^>]*>.*?</div>', r_post.text, re.DOTALL)
for n in m:
    text = re.sub(r'<[^>]+>', ' ', n).strip()
    if 'File edited' in text or 'Unable' in text or 'error' in text.lower():
        print("Relevant notice:", text)

m2 = re.findall(r'<div id="message"[^>]*>.*?</div>', r_post.text, re.DOTALL)
for n in m2:
    print("Message text:", re.sub(r'<[^>]+>', ' ', n).strip())
