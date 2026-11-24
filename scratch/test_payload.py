import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

match_body = re.search(r'<body>([\s\S]*?)</body>', index_content)
page_content = match_body.group(1).strip() if match_body else index_content

wp_map = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.webp',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png',
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png',
    'assets/images/boloup-agent-role.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agent-Role.png',
}

for local_path, wp_url in wp_map.items():
    page_content = page_content.replace(local_path, wp_url)

m = re.findall(r'<img[^>]*ecosystem[^>]*>', page_content, re.I)
print("Result in page_content:", m)

