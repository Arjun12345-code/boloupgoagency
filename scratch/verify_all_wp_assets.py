import requests

wp_urls = [
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.webp',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agent-Role.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-1-1.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-2-1.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-3-1.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-4.jpg',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png',
]

all_ok = True
for u in wp_urls:
    try:
        r = requests.head(u, timeout=10)
        status = r.status_code
        print(f"[{status}] {u.split('/')[-1]}")
        if status != 200:
            all_ok = False
    except Exception as e:
        print(f"[ERR] {u.split('/')[-1]}: {e}")
        all_ok = False

print("All URLs 200 OK?", all_ok)

