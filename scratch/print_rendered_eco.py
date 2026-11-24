import requests

session = requests.Session()
login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

res = session.get("https://boloupgoagency.com/wp-json/wp/v2/pages/26")
c = res.json().get('content', {}).get('rendered', '')
idx = c.find('ecosystem')
print("Snippet around ecosystem in Post 26 rendered:")
print(c[max(0, idx-100):idx+200])

