import urllib.request
import re

req = urllib.request.Request('https://boloupgoagency.com/', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

with open('live_boloupgoagency.html', 'w', encoding='utf-8') as f:
    f.write(html)

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f'Found {len(imgs)} images:')
for img in set(imgs):
    print(' -', img)

# Find CSS links
css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', html)
print(f'\nFound {len(css_links)} CSS links:')
for c in css_links:
    print(' -', c)
