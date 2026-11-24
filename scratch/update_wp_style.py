import urllib.request
import urllib.parse
import re

cookies_str = (
    "wordpress_sec_8b901ec78b385dd04c88c5fc4e3f554b=webdev%7C1793955397%7CPrdntkkCwzhA1wCZ51cmnK6jrD9nlgcaosyb6O6jDU2%7Ca8c4b76558f93a89d4b8e71dbe1b3b6aea68db90e67c4bb9e0492f3b2937bfe5; "
    "wordpress_logged_in_8b901ec78b385dd04c88c5fc4e3f554b=webdev%7C1793955397%7CPrdntkkCwzhA1wCZ51cmnK6jrD9nlgcaosyb6O6jDU2%7C67e64aec0ac617d8e8aa7c67ba63665361881a4cbf6d3e03fc12aa09afcc5f12; "
    "wordpress_test_cookie=WP%20Cookie%20check"
)

# 1. GET page to obtain fresh nonce
edit_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
req = urllib.request.Request(edit_url, headers={
    'User-Agent': 'Mozilla/5.0',
    'Cookie': cookies_str
})

resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')
nonce = re.search(r'id="nonce" name="nonce" value="([^"]+)"', html).group(1)
print("Got nonce:", nonce)

# Read local style.css
with open('style.css', 'r', encoding='utf-8') as f:
    local_css = f.read()

theme_header = """/*
Theme Name: Hello Elementor Child - BoloUp Agency
Theme URI: https://boloupgoagency.com/
Description: Custom high-conversion one-page design for BoloUp Go Agency
Author: BoloUp Agency Development Team
Author URI: https://boloupgoagency.com/
Template: hello-elementor
Version: 2.0.0
Text Domain: hello-elementor-child
*/

"""

full_content = theme_header + local_css

# 2. POST update
post_data = urllib.parse.urlencode({
    'nonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child',
    'action': 'update',
    'file': 'style.css',
    'theme': 'hello-elementor-child',
    'newcontent': full_content,
    'submit': 'Update File'
}).encode('utf-8')

post_req = urllib.request.Request(edit_url, data=post_data, headers={
    'User-Agent': 'Mozilla/5.0',
    'Cookie': cookies_str,
    'Content-Type': 'application/x-www-form-urlencoded'
})

post_resp = urllib.request.urlopen(post_req)
post_html = post_resp.read().decode('utf-8')
if "File edited successfully" in post_html or "id=\"message\"" in post_html:
    print("SUCCESS: style.css updated on WordPress!")
    msg = re.search(r'<div id="message"[^>]*><p>(.*?)</p></div>', post_html)
    if msg:
        print("Notice:", msg.group(1))
else:
    print("WARNING: check response for errors")
