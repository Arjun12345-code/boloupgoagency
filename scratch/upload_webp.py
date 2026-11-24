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

admin_text = session.get("https://boloupgoagency.com/wp-admin/").text
nonce = re.search(r'"nonce":"([a-f0-9]{10})"', admin_text).group(1)

with open('assets/images/boloupgoagency-nobg.webp', 'rb') as f:
    file_data = f.read()

headers = {
    'X-WP-Nonce': nonce,
    'Content-Disposition': 'attachment; filename="boloupgoagency-nobg-v3.webp"',
    'Content-Type': 'image/webp'
}
res = session.post('https://boloupgoagency.com/wp-json/wp/v2/media', headers=headers, data=file_data)
print("Upload status:", res.status_code)
if res.status_code == 201:
    print("New WebP URL:", res.json().get('source_url'))
else:
    print("Error:", res.text[:300])

