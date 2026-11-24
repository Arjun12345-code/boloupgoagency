import requests, re, json

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.get(login_url)
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

for pid in [42, 45]:
    r = s.get(f'https://boloupgoagency.com/wp-admin/post.php?post={pid}&action=edit')
    print(f"Post {pid} edit status:", r.status_code)
    m = re.search(r'<textarea[^>]*id="content"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
    if m:
        print(f"Post {pid} content:\n", m.group(1)[:300])
    else:
        print(f"No textarea for post {pid}")

