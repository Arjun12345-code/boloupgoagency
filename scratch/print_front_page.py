import requests, re
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.get('https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk')
s.post('https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk', data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})
r = s.get('https://boloupgoagency.com/wp-admin/theme-editor.php?file=front-page.php&theme=hello-elementor-child')
m = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
if m:
    print(m.group(1))

