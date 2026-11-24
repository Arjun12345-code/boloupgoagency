import requests
import re

url = 'https://drive.google.com/drive/folders/13KbSdIf-SujL29y2svvuKKkGUFpXTdC3'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print('Status:', r.status_code)
# Search for names inside google drive page
names = set(re.findall(r'\["([A-Za-z0-9_\-\.\s]+?\.(?:png|jpg|jpeg|webp|svg|pdf))"', r.text, re.I))
for n in sorted(names):
    print("Drive file:", n)

