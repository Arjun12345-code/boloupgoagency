import requests
import re
import os

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

print("1. Fetching login page...")
r = session.get(login_url)
print("Login page status:", r.status_code)

# Perform login
login_data = {
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgoagency.com/wp-admin/',
    'testcookie': '1'
}

print("2. Logging in...")
r_login = session.post(login_url, data=login_data, allow_redirects=True)
print("After login URL:", r_login.url, "Status:", r_login.status_code)

if 'wp-admin' in r_login.url:
    print("SUCCESS: Logged in to WordPress!")
else:
    print("WARNING: May not have reached wp-admin, cookies:", session.cookies.get_dict())

# 3. Check / Upload media: assets/images/boloupgoagency-nobg.png
upload_url = "https://boloupgoagency.com/wp-admin/media-new.php"
r_upload_page = session.get(upload_url)
nonce_match = re.search(r'name="_wpnonce"\s+value="([^"]+)"', r_upload_page.text)
if not nonce_match:
    nonce_match = re.search(r'id="_wpnonce"\s+name="_wpnonce"\s+value="([^"]+)"', r_upload_page.text)

print("Upload page nonce:", nonce_match.group(1) if nonce_match else "None")

# Let's check wp-json or async-upload.php
async_upload_url = "https://boloupgoagency.com/wp-admin/async-upload.php"
# Find async upload nonce
async_nonce_match = re.search(r'"_wpnonce":"([^"]+)"', r_upload_page.text)
if not async_nonce_match:
    async_nonce_match = re.search(r'wp-uploader-params\s*=\s*\{.*?"_wpnonce":"([^"]+)"', r_upload_page.text)

print("Async nonce:", async_nonce_match.group(1) if async_nonce_match else "None")

# Upload hero nobg image
hero_nobg_path = "assets/images/boloupgoagency-nobg.png"
if os.path.exists(hero_nobg_path) and async_nonce_match:
    with open(hero_nobg_path, 'rb') as f_img:
        files = {
            'async-upload': ('boloupgoagency-nobg.png', f_img, 'image/png')
        }
        data = {
            'name': 'boloupgoagency-nobg.png',
            'action': 'upload-attachment',
            '_wpnonce': async_nonce_match.group(1)
        }
        res_up = session.post(async_upload_url, data=data, files=files)
        print("Upload result status:", res_up.status_code)
        print("Upload response:", res_up.text[:300])

