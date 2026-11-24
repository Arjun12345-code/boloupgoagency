import requests
import json
import re

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
r_login = s.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'testcookie': '1'
}, allow_redirects=True)
print("Logged in:", "wp-admin" in r_login.url)

# Get upload nonce from media-new.php
r_upload_page = s.get('https://boloupgoagency.com/wp-admin/media-new.php')
nonce_match = re.search(r'name="_wpnonce"\s+value="([^"]+)"', r_upload_page.text)
if not nonce_match:
    nonce_match = re.search(r'id="_wpnonce"\s+value="([^"]+)"', r_upload_page.text)
print("Found nonce:", nonce_match.group(1) if nonce_match else "None")

# Check if wp_rest nonce exists
rest_nonce = re.search(r'wpApiSettings\s*=\s*\{"root":"[^"]*","nonce":"([^"]+)"', r_upload_page.text)
print("Rest nonce:", rest_nonce.group(1) if rest_nonce else "None")

# Try upload via async-upload.php
with open('assets/images/cropped-boloup.png', 'rb') as f:
    files = {
        'async-upload': ('cropped-boloup.png', f, 'image/png')
    }
    data = {
        'name': 'cropped-boloup.png',
        'action': 'upload-attachment',
        '_wpnonce': nonce_match.group(1) if nonce_match else '',
    }
    r_up = s.post('https://boloupgoagency.com/wp-admin/async-upload.php', data=data, files=files)
    print("Async upload status:", r_up.status_code)
    print("Async upload response:", r_up.text[:500])

