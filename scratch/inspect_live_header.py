import requests
import re

r = requests.get('https://boloupgoagency.com/', headers={'User-Agent': 'Mozilla/5.0'})
match = re.search(r'<div class="header-actions">[\s\S]*?</div>\s*</div>\s*</header>', r.text)
if match:
    print("Found header actions:")
    print(match.group(0))
else:
    print("Not found, printing header snippet:")
    hdr = re.search(r'<header id="header"[\s\S]*?</header>', r.text)
    if hdr:
        print(hdr.group(0))

