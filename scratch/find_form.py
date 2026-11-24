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

forms = re.findall(r'<form[^>]*id="template"[^>]*>.*?</form>', r.text, re.DOTALL)
if forms:
    print("Found form id='template':")
    # print input fields inside form
    inputs = re.findall(r'<input[^>]+>', forms[0])
    for inp in inputs:
        print("  ", inp)
else:
    print("No form id='template' found!")
    # search any form
    all_forms = re.findall(r'<form[^>]*>.*?</form>', r.text, re.DOTALL)
    print("Total forms:", len(all_forms))
    for f in all_forms[:3]:
        print(f[:200])

