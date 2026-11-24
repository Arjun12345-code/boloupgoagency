import requests
import re

url = "https://boloupgoagency.com/"
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print("Status:", r.status_code)
html = r.text

print("\n--- 1. Verification of Navbar ---")
# Check logo and name
brand_matches = re.findall(r'<a[^>]+class=[\"\']brand-logo[\"\'][^>]*>([\s\S]*?)</a>', html)
print(f"Found {len(brand_matches)} brand-logo elements:")
for b in brand_matches:
    print("  Brand inner:", b.strip()[:100])

# Check nav links
nav_links = re.findall(r'<a[^>]+class=[\"\']nav-link[^\"\']*[\"\'][^>]*>(.*?)</a>', html)
print("Nav links in navbar:", nav_links)

# Check Download App and Start Agency links
btn_dl = re.findall(r'<a[^>]+id=[\"\']btn-header-download[\"\'][^>]*href=[\"\']([^\"\']+)[\"\']', html)
btn_start = re.findall(r'<a[^>]+id=[\"\']btn-header-agent[\"\'][^>]*href=[\"\']([^\"\']+)[\"\']', html)
print("Header Download link:", btn_dl)
print("Header Start Agency link:", btn_start)

print("\n--- 2. Verification of Footer ---")
# Check tagline
tagline = re.findall(r'<p class=[\"\']footer-desc[\"\']>([\s\S]*?)</p>', html)
print("Footer tagline:", tagline[0].strip() if tagline else "Not found")

# Check Agency Program links
agency_prog = re.findall(r'<h3>Agency Program</h3>\s*<ul class=[\"\']footer-links[\"\']>([\s\S]*?)</ul>', html)
if agency_prog:
    print("Agency Program links:")
    for a in re.findall(r'<a[^>]+href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', agency_prog[0]):
        print(f"  {a[1]} -> {a[0]}")

# Check BoloUp App links
app_links = re.findall(r'<h3>BoloUp App</h3>\s*<ul class=[\"\']footer-links[\"\']>([\s\S]*?)</ul>', html)
if app_links:
    print("BoloUp App links:")
    for a in re.findall(r'<a[^>]+href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', app_links[0]):
        print(f"  {a[1]} -> {a[0]}")

print("\n--- 3. Verification of Final CTA ---")
cta_h2 = re.findall(r'<h2 class=[\"\']cta-headline[\"\']>([\s\S]*?)</h2>', html)
print("Final CTA headline:", cta_h2[0].strip() if cta_h2 else "Not found")
cta_btn = re.findall(r'<a[^>]+id=[\"\']final-cta-btn[\"\'][^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>([\s\S]*?)</a>', html)
if cta_btn:
    print(f"Final CTA button: \"{cta_btn[0][1].strip()}\" -> {cta_btn[0][0]}")

print("\n--- 4. Verification of Style CSS ---")
css_links = re.findall(r'<link[^>]+href=[\"\']([^\"\']*style\.css[^\"\']*)[\"\']', html)
print("Style CSS link in head:", css_links)
if css_links:
    css_res = requests.get(css_links[0])
    print("CSS fetch status:", css_res.status_code)
    print("CSS version in header:", "2.3.0" in css_res.text[:500])
    print("Contains pink gradient #f20374:", "#f20374" in css_res.text)

