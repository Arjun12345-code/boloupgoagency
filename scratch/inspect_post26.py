import requests, json

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

# Let's inspect post 26 meta using a quick hook or rest api
res = session.get("https://boloupgoagency.com/wp-json/wp/v2/pages/26")
print("Post 26 REST content snippet:")
print(res.json().get('content', {}).get('rendered', '')[:500])

