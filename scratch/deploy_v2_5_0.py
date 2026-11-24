import requests, re, json, html

session = requests.Session()
login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
res = session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgoagency.com/wp-admin/',
    'testcookie': '1'
}, timeout=15)

print("1. Login status:", res.status_code)
admin_text = session.get("https://boloupgoagency.com/wp-admin/").text
nonce_match = re.search(r'wpApiSettings\s*=\s*\{[^}]*"nonce":"([^"]+)"', admin_text)
if not nonce_match:
    nonce_match = re.search(r'"nonce":"([a-f0-9]{10})"', admin_text)
nonce = nonce_match.group(1) if nonce_match else None
print("REST Nonce:", nonce)

# Update style.css in child theme
theme_edit_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor-child"
r = session.get(theme_edit_url)
nonce_theme = re.search(r'name="nonce"\s+value="([^"]+)"', r.text).group(1)
print("style.css edit nonce:", nonce_theme)

with open('style.css', 'r', encoding='utf-8') as f:
    local_css = f.read()

# Update header version comment in css
local_css = re.sub(r'Version:\s*[\d\.]+', 'Version: 2.5.0', local_css)

post_data = {
    'newcontent': local_css,
    'action': 'update',
    'file': 'style.css',
    'theme': 'hello-elementor-child',
    'scrollto': '0',
    'nonce': nonce_theme,
    'docs-list': '',
    'submit': 'Update File'
}
post_r = session.post("https://boloupgoagency.com/wp-admin/theme-editor.php", data=post_data)
print("2. style.css updated in child theme! Status:", post_r.status_code)

# Update functions.php in child theme (version 2.5.0 + favicon.ico redirect)
func_edit_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(func_edit_url)
nonce_func = re.search(r'name="nonce"\s+value="([^"]+)"', r_func.text).group(1)
print("functions.php edit nonce:", nonce_func)

new_functions_php = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.5.0 & Site Favicon
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.5.0'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');

// Output Official BoloUp Favicon and App Icons
add_action('wp_head', function() {
    echo '<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png">' . "\\n";
    echo '<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\\n";
    echo '<link rel="apple-touch-icon" sizes="180x180" href="https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png">' . "\\n";
    echo '<meta name="msapplication-TileImage" content="https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png">' . "\\n";
}, 1);

// Handle direct /favicon.ico request by redirecting to 32x32 BoloUp Icon
add_action('init', function() {
    if (isset($_SERVER['REQUEST_URI']) && strpos($_SERVER['REQUEST_URI'], 'favicon.ico') !== false) {
        wp_redirect('https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-32x32-1.png', 301);
        exit;
    }
});
"""

post_data_func = {
    'newcontent': new_functions_php,
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'scrollto': '0',
    'nonce': nonce_func,
    'docs-list': '',
    'submit': 'Update File'
}
post_rf = session.post("https://boloupgoagency.com/wp-admin/theme-editor.php", data=post_data_func)
print("3. functions.php updated in child theme! Status:", post_rf.status_code)

# 4. Prepare Body Content for Pages 26 & 35
with open('index.html', 'r', encoding='utf-8') as f:
    local_index = f.read()

wp_replacements = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png',
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-ecosystem.png',
    'assets/images/boloup-agent-role.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agent-Role.png',
    'assets/images/boloup-avatar-192x192.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png',
    'assets/images/cropped-boloup.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/cropped-boloup.png',
}

wp_page_html = local_index
for k, v in wp_replacements.items():
    wp_page_html = wp_page_html.replace(k, v)

start_marker = '<!-- Background Ambient Glow Orbs -->'
end_marker = '</body>'
start_idx = wp_page_html.find(start_marker)
end_idx = wp_page_html.find(end_marker)
extracted_body = wp_page_html[start_idx:end_idx].strip()

# Update Page 26 and Page 35
for pid in [26, 35]:
    up_res = session.post(f"https://boloupgoagency.com/wp-json/wp/v2/pages/{pid}", headers={'X-WP-Nonce': nonce}, json={
        'content': extracted_body
    })
    print(f"4. Page {pid} updated via REST API! Status: {up_res.status_code}")

# 5. Update Header Post 42 and Footer Post 45
with open('header.html', 'r', encoding='utf-8') as f:
    h_content = f.read()
h_content = h_content.replace('assets/images/boloup-avatar-192x192.png', 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png')

h_res = session.post("https://boloupgoagency.com/wp-json/wp/v2/posts/42", headers={'X-WP-Nonce': nonce}, json={
    'content': h_content
})
print("5. Header Post 42 updated! Status:", h_res.status_code)

with open('footer.html', 'r', encoding='utf-8') as f:
    f_content = f.read()
f_content = f_content.replace('assets/images/boloup-avatar-192x192.png', 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-avatar-192x192-1.png')

f_res = session.post("https://boloupgoagency.com/wp-json/wp/v2/posts/45", headers={'X-WP-Nonce': nonce}, json={
    'content': f_content
})
print("6. Footer Post 45 updated! Status:", f_res.status_code)

# 6. Purge LiteSpeed Cache
try:
    admin_bar_html = session.get("https://boloupgoagency.com/wp-admin/").text
    purge_match = re.search(r'href="([^"]*litespeed-purge-all[^"]*)"', admin_bar_html)
    if purge_match:
        purge_url = html.unescape(purge_match.group(1))
        p_res = session.get(purge_url)
        print("7. LiteSpeed cache purged! Status:", p_res.status_code)
    else:
        print("7. LiteSpeed purge URL not found directly.")
except Exception as e:
    print("Purge error:", e)

print("Deployment v2.5.0 Complete!")
