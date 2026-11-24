import requests, re

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.get(login_url)
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'}, allow_redirects=True)
edit_func_url = 'https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child'
r = s.get(edit_func_url)
m = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
if m:
    print('functions.php content:\n', m.group(1))
else:
    print('textarea not found')

