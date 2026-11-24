import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .brand-badge definition
old_badge_block = """.brand-badge {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  background: var(--grad-primary);
  color: var(--color-white);
  padding: 3px 8px;
  border-radius: var(--radius-pill);
  box-shadow: 0 2px 8px rgba(255, 69, 0, 0.4);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.brand-logo:hover .brand-badge {
  box-shadow: 0 0 16px rgba(255, 69, 0, 0.8), 0 0 24px rgba(6, 182, 212, 0.5);
  transform: translateY(-1px);
}"""

new_badge_block = """.brand-badge {
  display: none !important;
}"""

if old_badge_block in content:
    content = content.replace(old_badge_block, new_badge_block)
else:
    content = re.sub(r'\.brand-badge\s*\{[\s\S]*?transform:\s*translateY\(-1px\);\s*\}', '.brand-badge {\n  display: none !important;\n}', content)

content = re.sub(r'Version: 2\.\d+\.\d+', 'Version: 2.2.0', content)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated style.css to v2.2.0 with brand-badge hidden!")

