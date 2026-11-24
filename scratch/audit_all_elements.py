import html.parser
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

badges = re.findall(r'<div[^>]*class="[^"]*badge[^"]*"[^>]*>(.*?)</div>', content, re.DOTALL)
print("=== BADGES FOUND ===")
for b in badges:
    print(re.sub(r'<[^>]+>', '', b).strip())

tags = re.findall(r'<span[^>]*class="about-tag"[^>]*>(.*?)</span>', content, re.DOTALL)
print("\n=== ABOUT TAGS ===")
for t in tags:
    print(re.sub(r'<[^>]+>', '', t).strip())

buttons = re.findall(r'<(?:a|button)[^>]*class="[^"]*btn[^"]*"[^>]*>(.*?)</(?:a|button)>', content, re.DOTALL)
print("\n=== BUTTONS FOUND ===")
for btn in buttons:
    print(re.sub(r'<[^>]+>', '', btn).strip())
