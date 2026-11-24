import re

def update_index_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove agency-id-callout block
    callout_pattern = r'\s*<div class="agency-id-callout">[\s\S]*?</div>\s*</div>'
    new_content = re.sub(callout_pattern, '', content)

    # If pattern didn't match cleanly, check exact substring
    if '<div class="agency-id-callout">' in new_content:
        # manual slice
        start_idx = new_content.find('<div class="agency-id-callout">')
        # find end after copy-toast div
        toast_marker = '<div class="copy-feedback-toast" id="copy-toast">Agency ID copied to clipboard!</div>\n              </div>'
        end_idx = new_content.find(toast_marker)
        if end_idx != -1:
            end_idx += len(toast_marker)
            new_content = new_content[:start_idx] + new_content[end_idx:]

    # Remove Agency ID Copy Handler JS
    js_pattern = r'\s*// Agency ID Copy Handler[\s\S]*?if \(copyBtn && copyText\) \{[\s\S]*?\n      \}\n'
    new_content = re.sub(js_pattern, '\n', new_content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("index.html updated successfully!")

def update_preview_html():
    with open('preview.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove agency-id-callout block
    if '<div class="agency-id-callout">' in content:
        start_idx = content.find('<div class="agency-id-callout">')
        toast_marker = '<div class="copy-feedback-toast" id="copy-toast">Agency ID copied to clipboard!</div>\n              </div>'
        end_idx = content.find(toast_marker)
        if end_idx != -1:
            end_idx += len(toast_marker)
            content = content[:start_idx] + content[end_idx:]

    # Remove Agency ID from preview footer
    content = content.replace('            <li><a href="#registration">Agency ID: 2527626</a></li>\n', '')

    # Remove Agency ID Copy Handler JS
    js_pattern = r'\s*// Agency ID Copy Handler[\s\S]*?if \(copyBtn && copyText\) \{[\s\S]*?\n      \}\n'
    content = re.sub(js_pattern, '\n', content)

    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("preview.html updated successfully!")

def update_footer_html():
    with open('footer.html', 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('          <li><a href="#registration">Agency ID: 2527626</a></li>\n', '')
    with open('footer.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("footer.html updated successfully!")

if __name__ == '__main__':
    update_index_html()
    update_preview_html()
    update_footer_html()

