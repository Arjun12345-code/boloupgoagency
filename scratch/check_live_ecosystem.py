import requests, re

r = requests.get('https://boloupgoagency.com/?nocache=999')
matches = re.findall(r'<img[^>]*ecosystem[^>]*>', r.text, re.IGNORECASE)
for m in matches:
    print("Found img tag:", m)

