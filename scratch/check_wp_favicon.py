import requests

session = requests.Session()
login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
res = session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgoagency.com/wp-admin/',
    'testcookie': '1'
}, timeout=15)

# Check theme files
theme_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r = session.get(theme_url)
print("Theme editor functions.php status:", r.status_code)
# Search for site_icon or favicon in functions.php
if 'favicon' in r.text.lower() or 'site_icon' in r.text.lower():
    print("Found favicon in functions.php!")

