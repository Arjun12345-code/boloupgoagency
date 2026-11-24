with open('index.html', 'rb') as f:
    raw = f.read()

import re
matches = re.findall(rb'alt="([^"]*)"', raw)
for m in matches:
    print(m.decode('utf-8', errors='replace'))

