import requests, re

login_url = 'https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})
s.get(login_url)
s.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'}, allow_redirects=True)

for fname in ['front-page.php', 'template-landing.php', 'page.php', 'index.php']:
    url = f"https://boloupgoagency.com/wp-admin/theme-editor.php?file={fname}&theme=hello-elementor-child"
    r = s.get(url)
    m = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
    if m:
        content = m.group(1)
        print(f"File {fname} exists! Length: {len(content)}")
        print(f"Has agency-id in {fname}:", 'agency-id' in content)
    else:
        print(f"File {fname} not found or no textarea")

