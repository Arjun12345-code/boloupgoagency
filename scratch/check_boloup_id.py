import requests
import re

try:
    r = requests.get('https://boloup.id', headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
    print("Status boloup.id:", r.status_code)
    # search for hex colors or gradients
    hex_colors = set(re.findall(r'#[0-9a-fA-F]{6}', r.text))
    print("Found colors in boloup.id:", sorted(hex_colors)[:20])
    # search for linear-gradient
    grads = set(re.findall(r'linear-gradient\([^)]+\)', r.text))
    print("Found gradients in boloup.id:")
    for g in grads:
        print(" ", g)
except Exception as e:
    print("Error fetching boloup.id:", e)

