import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

wp_map = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.webp',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png',
}

for k, v in wp_map.items():
    print(k, "in index_content?", k in index_content)
    index_content = index_content.replace(k, v)

idx = index_content.find('<picture>')
print(index_content[idx:idx+350])

