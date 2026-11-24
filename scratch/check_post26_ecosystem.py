import requests, re

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

res = session.get("https://boloupgoagency.com/wp-json/wp/v2/pages/26")
rendered = res.json().get('content', {}).get('rendered', '')
m = re.findall(r'<img[^>]*ecosystem[^>]*>', rendered, re.IGNORECASE)
print("Page 26 REST rendered img:", m)
raw = res.json().get('content', {}).get('raw', '')
m2 = re.findall(r'<img[^>]*ecosystem[^>]*>', raw, re.IGNORECASE)
print("Page 26 REST raw img:", m2)

