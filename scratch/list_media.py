import urllib.request
import json

try:
    req = urllib.request.Request('https://boloupgoagency.com/wp-json/wp/v2/media?per_page=100', headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)
    media = json.loads(res.read().decode('utf-8'))
    print(f'Found {len(media)} media items on WordPress:')
    for m in media:
        print(f" - ID: {m.get('id')}, title: {m.get('title', {}).get('rendered')}, URL: {m.get('source_url')}")
except Exception as e:
    print('Error:', e)
