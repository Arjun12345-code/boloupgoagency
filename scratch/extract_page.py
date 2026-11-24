with open('live_boloupgoagency.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
if body_match:
    body = body_match.group(1)
    print("Body length:", len(body))
    # print first 1000 chars of body
    print("Body start:\n", body[:1500])
