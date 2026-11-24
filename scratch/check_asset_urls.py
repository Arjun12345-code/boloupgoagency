import requests

urls = [
    'https://boloupgoagency.com/favicon.ico',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agent-Role.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png'
]

for u in urls:
    try:
        r = requests.head(u, timeout=10)
        print(f"{r.status_code} : {u}")
    except Exception as e:
        print(f"ERR : {u} - {e}")

