import requests, re, html

login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={'log': 'webdev', 'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V', 'wp-submit': 'Log In', 'testcookie': '1'})

front_page = session.get("https://boloupgoagency.com/").text

# 1. Clear Elementor files cache
elem_cache_nonce = re.search(r'action=elementor_site_clear_cache&_wpnonce=([a-f0-9]+)', front_page)
if elem_cache_nonce:
    nonce = elem_cache_nonce.group(1)
    res = session.get(f"https://boloupgoagency.com/wp-admin/admin-post.php?action=elementor_site_clear_cache&_wpnonce={nonce}")
    print("Elementor cache cleared! Status:", res.status_code)
else:
    print("Elementor cache nonce not found on front page.")

# 2. LiteSpeed purge all
ls_links = re.findall(r'href="([^"]*litespeed[^"]*purge[^"]*)"', front_page, re.IGNORECASE)
print("LiteSpeed purge links:", len(ls_links))
for link in ls_links:
    clean_url = html.unescape(link)
    res = session.get(clean_url)
    print("Purged LiteSpeed link:", clean_url[:80], "Status:", res.status_code)

# Check LiteSpeed Toolbox Purge All URL
r_ls = session.get("https://boloupgoagency.com/wp-admin/admin.php?page=litespeed-toolbox")
print("LiteSpeed toolbox status:", r_ls.status_code)
purge_all_match = re.search(r'href="([^"]*purge_all[^"]*)"', r_ls.text)
if purge_all_match:
    purge_all_url = html.unescape(purge_all_match.group(1))
    p_res = session.get(purge_all_url)
    print("LiteSpeed Purge All triggered! Status:", p_res.status_code)
