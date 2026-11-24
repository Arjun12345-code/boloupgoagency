import requests, json

session = requests.Session()
login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
res = session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgoagency.com/wp-admin/',
    'testcookie': '1'
}, timeout=15)

admin_text = session.get("https://boloupgoagency.com/wp-admin/").text
import re
nonce_match = re.search(r'wpApiSettings\s*=\s*\{[^}]*"nonce":"([^"]+)"', admin_text)
if not nonce_match:
    nonce_match = re.search(r'"nonce":"([a-f0-9]{10})"', admin_text)
nonce = nonce_match.group(1) if nonce_match else None
print("REST Nonce:", nonce)

# Upload clean boloupgoagency-nobg.png
with open('assets/images/boloupgoagency-nobg.png', 'rb') as f:
    file_data = f.read()

headers = {
    'X-WP-Nonce': nonce,
    'Content-Disposition': 'attachment; filename="boloupgoagency-nobg-v3.png"',
    'Content-Type': 'image/png'
}
upload_res = session.post('https://boloupgoagency.com/wp-json/wp/v2/media', headers=headers, data=file_data)
print("Upload status:", upload_res.status_code)
if upload_res.status_code == 201:
    media_json = upload_res.json()
    print("New Hero Image URL:", media_json.get('source_url'))
    print("Attachment ID:", media_json.get('id'))
else:
    print("Error:", upload_res.text[:300])

