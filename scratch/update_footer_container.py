def update_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<footer class="footer" id="footer">\n  <div class="container">', '<footer class="footer" id="footer">\n  <div class="footer-container">')
    c = c.replace('<footer class="footer" id="footer">\n    <div class="container">', '<footer class="footer" id="footer">\n    <div class="footer-container">')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated footer in {filepath}")

update_footer('footer.html')
update_footer('preview.html')

