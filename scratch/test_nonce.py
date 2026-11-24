import urllib.request
import re

cookies_str = (
    "wordpress_sec_8b901ec78b385dd04c88c5fc4e3f554b=webdev%7C1793955397%7CPrdntkkCwzhA1wCZ51cmnK6jrD9nlgcaosyb6O6jDU2%7Ca8c4b76558f93a89d4b8e71dbe1b3b6aea68db90e67c4bb9e0492f3b2937bfe5; "
    "wordpress_logged_in_8b901ec78b385dd04c88c5fc4e3f554b=webdev%7C1793955397%7CPrdntkkCwzhA1wCZ51cmnK6jrD9nlgcaosyb6O6jDU2%7C67e64aec0ac617d8e8aa7c67ba63665361881a4cbf6d3e03fc12aa09afcc5f12; "
    "wordpress_test_cookie=WP%20Cookie%20check"
)

url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0',
    'Cookie': cookies_str
})

resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

form = re.search(r'<form[^>]+id="template"[^>]*>(.*?)</form>', html, re.DOTALL)
if form:
    print("Found form!")
    inputs = re.findall(r'<input[^>]+>', form.group(1))
    for inp in inputs:
        print("Input:", inp)
else:
    print("No form #template found")
