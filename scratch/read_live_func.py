import requests, re

session = requests.Session()
login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

theme_edit_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r = session.get(theme_edit_url)
m = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
if m:
    import html
    print(html.unescape(m.group(1))[:1000])

