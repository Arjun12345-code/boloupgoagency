import re

def update_css():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add .section-subtitle
    sub_code = """.section-subtitle {
  color: var(--color-primary-light);
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.section-title {"""
    content = content.replace('.section-title {', sub_code, 1)

    # 2. Remove .agency-id block
    callout_pattern = r'/\* Callout Box for Agency ID \*/[\s\S]*?\.copy-feedback-toast\.show \{\s*display: block;\s*\}\s*'
    content = re.sub(callout_pattern, '', content)

    # 3. Update version comment
    content = re.sub(r'Version: 2\.\d+\.\d+', 'Version: 2.1.7', content)

    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("style.css updated cleanly to v2.1.7!")

update_css()

