import requests, re

r = requests.get('https://boloupgoagency.com/?nocache=1', headers={'User-Agent': 'Mozilla/5.0'})
text = r.text

footer_m = re.search(r'(<footer[^>]*>.*?</footer>)', text, re.DOTALL)
if footer_m:
    print("Footer HTML found! Length:", len(footer_m.group(1)))
    print(footer_m.group(1)[:400])
else:
    print("No <footer> tag found directly")

header_m = re.search(r'(<header[^>]*>.*?</header>)', text, re.DOTALL)
if header_m:
    print("\nHeader HTML found! Length:", len(header_m.group(1)))
    print(header_m.group(1)[:400])