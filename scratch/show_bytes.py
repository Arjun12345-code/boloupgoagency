with open('index.html', 'rb') as f:
    text = f.read()

import re
m = re.search(rb'alt="Step 1[^"]*"', text)
if m:
    print('Raw bytes:', list(m.group(0)))

