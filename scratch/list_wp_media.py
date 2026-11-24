import requests
import json

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

res = s.get('https://boloupgoagency.com/wp-json/wp/v2/media?per_page=100')
print('Media status:', res.status_code)
if res.status_code == 200:
    items = res.json()
    print('Found media items:', len(items))
    for it in items:
        print(f"{it.get('id')}: {it.get('slug')} -> {it.get('source_url')}")

