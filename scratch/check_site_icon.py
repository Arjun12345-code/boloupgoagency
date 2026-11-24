import requests, re

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

r = s.get('https://boloupgoagency.com/wp-admin/options.php')
matches = re.findall(r'<input[^>]*name=["\']site_icon["\'][^>]*>', r.text)
print('Site icon inputs:', matches)
for m in re.finditer(r'site_icon', r.text):
    start = max(0, m.start() - 50)
    end = min(len(r.text), m.end() + 100)
    print(r.text[start:end])

