import requests, re

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})
r = s.get('https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child')
content = re.search(r'<textarea[^>]*id=["\']newcontent["\'][^>]*>([\s\S]*?)</textarea>', r.text)
if content:
    print(content.group(1))

