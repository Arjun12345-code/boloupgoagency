import requests, re, html

session = requests.Session()
login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgoagency.com/wp-admin/',
    'testcookie': '1'
}, timeout=15)

theme_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r = session.get(theme_url)
m = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
if m:
    content = html.unescape(m.group(1))
    print(content[:1500])
