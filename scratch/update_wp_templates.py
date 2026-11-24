import urllib.request
import urllib.parse
import re

cookies_str = (
    "wordpress_sec_8b901ec78b385dd04c88c5fc4e3f554b=webdev%7C1793955397%7CPrdntkkCwzhA1wCZ51cmnK6jrD9nlgcaosyb6O6jDU2%7Ca8c4b76558f93a89d4b8e71dbe1b3b6aea68db90e67c4bb9e0492f3b2937bfe5; "
    "wordpress_logged_in_8b901ec78b385dd04c88c5fc4e3f554b=webdev%7C1793955397%7CPrdntkkCwzhA1wCZ51cmnK6jrD9nlgcaosyb6O6jDU2%7C67e64aec0ac617d8e8aa7c67ba63665361881a4cbf6d3e03fc12aa09afcc5f12; "
    "wordpress_test_cookie=WP%20Cookie%20check"
)

def update_file(filename, new_content):
    url = f"https://boloupgoagency.com/wp-admin/theme-editor.php?file={filename}&theme=hello-elementor-child"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookies_str})
    resp = urllib.request.urlopen(req)
    html = resp.read().decode('utf-8')

    nonce = re.search(r'id="nonce" name="nonce" value="([^"]+)"', html).group(1)
    print(f"[{filename}] Got nonce: {nonce}")

    post_data = urllib.parse.urlencode({
        'nonce': nonce,
        '_wp_http_referer': f'/wp-admin/theme-editor.php?file={filename}&theme=hello-elementor-child',
        'action': 'update',
        'file': filename,
        'theme': 'hello-elementor-child',
        'newcontent': new_content,
        'submit': 'Update File'
    }).encode('utf-8')

    post_req = urllib.request.Request(url, data=post_data, headers={
        'User-Agent': 'Mozilla/5.0',
        'Cookie': cookies_str,
        'Content-Type': 'application/x-www-form-urlencoded'
    })

    post_resp = urllib.request.urlopen(post_req)
    post_html = post_resp.read().decode('utf-8')
    if "File edited successfully" in post_html or "id=\"message\"" in post_html:
        print(f"SUCCESS: {filename} updated!")
    else:
        print(f"WARNING: error updating {filename}")

with open('scratch/wp_template.php', 'r', encoding='utf-8') as f:
    template_code = f.read()

# Update template-landing.php
update_file('template-landing.php', template_code)

# Update front-page.php
update_file('front-page.php', template_code)
