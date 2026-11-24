import requests
from PIL import Image
import io

# Local
im_local = Image.open('assets/images/boloup-ecosystem.png')
print("Local boloup-ecosystem.png size:", im_local.size)

# WordPress
r = requests.get('https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png')
print("WP BoloUp-Ecosystem.png status:", r.status_code, "length:", len(r.content))
im_wp = Image.open(io.BytesIO(r.content))
print("WP BoloUp-Ecosystem.png size:", im_wp.size)

