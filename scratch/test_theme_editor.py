import requests, re

session = requests.Session()
login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgoagency.com/wp-admin/',
    'testcookie': '1'
}, timeout=15)

theme_edit_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
r = session.get(theme_edit_url)
print("Status:", r.status_code)
# find all nonces in r.text
nonces = re.findall(r'_wpnonce[^>]*', r.text)
print("Nonces found:", nonces[:5])
if not nonces:
    print("Page title/snippet:", r.text[:500])

