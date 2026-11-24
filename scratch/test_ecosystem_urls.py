import requests

urls = [
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem-1.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-ecosystem.png',
    'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem-e1.png',
]

for u in urls:
    r = requests.get(u)
    print(r.status_code, len(r.content), u)

