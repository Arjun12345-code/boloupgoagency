import requests
import re

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'testcookie': '1'
}, allow_redirects=True)

r_upload_page = s.get('https://boloupgoagency.com/wp-admin/media-new.php')
nonce_match = re.search(r'id="_wpnonce"\s+value="([^"]+)"', r_upload_page.text)
if not nonce_match:
    nonce_match = re.search(r'name="_wpnonce"\s+value="([^"]+)"', r_upload_page.text)
nonce = nonce_match.group(1)

for fname in ['boloup-avatar-32x32.png', 'boloup-avatar-192x192.png']:
    with open('assets/images/' + fname, 'rb') as f:
        files = {'async-upload': (fname, f, 'image/png')}
        data = {
            'name': fname,
            'action': 'upload-attachment',
            '_wpnonce': nonce,
        }
        res = s.post('https://boloupgoagency.com/wp-admin/async-upload.php', data=data, files=files)
        print(fname, res.status_code, res.json().get('data', {}).get('url'))

