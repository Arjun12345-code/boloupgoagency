import urllib.request
import os

urls = [
    ('https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-1-1.png', 'assets/images/BoloUp-Agency-Registration-Step-1-1.png'),
    ('https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-2-1.png', 'assets/images/BoloUp-Agency-Registration-Step-2-1.png'),
    ('https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-3-1.png', 'assets/images/BoloUp-Agency-Registration-Step-3-1.png'),
    ('https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-4.jpg', 'assets/images/BoloUp-Agency-Registration-Step-4.jpg')
]

for url, dest in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            content = res.read()
            with open(dest, 'wb') as f:
                f.write(content)
            print(f"SUCCESS: {url} -> saved to {dest} ({len(content)} bytes)")
    except Exception as e:
        print(f"FAILED: {url} -> {e}")

