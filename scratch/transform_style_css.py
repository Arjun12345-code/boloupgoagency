import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Header comment
css = re.sub(
    r'Atmospheric Smoke & Fire: Deep Obsidian.*?Oceanic Cyan \(#06B6D4\)',
    'Signature Cyber Brand: Deep Obsidian (#06090E) with BoloUp Neon Pink (#F20374) to Fiery Orange (#FF7A00)',
    css
)

# 2. Update CSS Variables in :root
root_old = """  /* Accent Tones */
  --color-primary: #ff4500;
  --color-primary-light: #ff7043;
  --color-primary-dark: #dc2626;
  --color-secondary: #06b6d4;
  --color-secondary-light: #38bdf8;
  --color-accent-rose: #f43f5e;
  --color-accent-amber: #f59e0b;
  --color-accent-cyan: #06b6d4;
  --color-accent-emerald: #10b981;

  /* Primary Gradients */
  --grad-primary: linear-gradient(135deg, #ff4500 0%, #f97316 45%, #ef4444 100%);
  --grad-primary-hover: linear-gradient(135deg, #ff5722 0%, #fb923c 45%, #f43f5e 100%);
  --grad-hero-badge: linear-gradient(135deg, rgba(255, 69, 0, 0.22) 0%, rgba(6, 182, 212, 0.22) 100%);
  --grad-card: rgba(12, 18, 28, 0.72);
  --grad-card-hover: rgba(18, 27, 42, 0.85);
  --grad-cta-banner: linear-gradient(135deg, rgba(8, 12, 20, 0.96) 0%, rgba(185, 28, 28, 0.88) 45%, rgba(234, 88, 12, 0.92) 100%);"""

root_new = """  /* Accent Tones: BoloUp Brand Neon Pink & Fiery Orange */
  --color-primary: #f20374;
  --color-primary-light: #ff5238;
  --color-primary-dark: #d80063;
  --color-secondary: #ff7a00;
  --color-secondary-light: #ffa043;
  --color-accent-pink: #f20374;
  --color-accent-orange: #ff7a00;
  --color-accent-rose: #ff2a6d;
  --color-accent-amber: #f59e0b;
  --color-accent-cyan: #06b6d4;
  --color-accent-emerald: #10b981;

  /* Primary Gradients: Dynamic Pink to Orange (Matching Official Logo) */
  --grad-primary: linear-gradient(135deg, #f20374 0%, #ff5238 50%, #ff7a00 100%);
  --grad-primary-hover: linear-gradient(135deg, #ff1a82 0%, #ff6347 50%, #ff8f1f 100%);
  --grad-hero-badge: linear-gradient(135deg, rgba(242, 3, 116, 0.22) 0%, rgba(255, 122, 0, 0.22) 100%);
  --grad-card: rgba(12, 18, 28, 0.72);
  --grad-card-hover: rgba(18, 27, 42, 0.85);
  --grad-cta-banner: linear-gradient(135deg, rgba(8, 12, 20, 0.96) 0%, rgba(242, 3, 116, 0.88) 45%, rgba(255, 122, 0, 0.92) 100%);"""

css = css.replace(root_old, root_new)

# Update borders and glows in :root
glow_old = """  /* Borders & Glow Effects */
  --border-card: rgba(255, 69, 0, 0.18);
  --border-card-hover: rgba(6, 182, 212, 0.55);
  --glow-accent: 0 0 35px rgba(255, 69, 0, 0.4);
  --glow-button: 0 8px 25px rgba(255, 69, 0, 0.45);
  --glow-button-hover: 0 12px 35px rgba(249, 115, 22, 0.65);"""

glow_new = """  /* Borders & Glow Effects */
  --border-card: rgba(242, 3, 116, 0.22);
  --border-card-hover: rgba(255, 122, 0, 0.55);
  --glow-accent: 0 0 35px rgba(242, 3, 116, 0.45);
  --glow-button: 0 8px 25px rgba(242, 3, 116, 0.45);
  --glow-button-hover: 0 12px 35px rgba(255, 122, 0, 0.65);"""

css = css.replace(glow_old, glow_new)

# Update body radial backgrounds
body_bg_old = """    radial-gradient(circle at 15% 15%, rgba(6, 182, 212, 0.25) 0%, transparent 45%),
    radial-gradient(circle at 85% 25%, rgba(255, 69, 0, 0.28) 0%, transparent 45%),
    radial-gradient(circle at 50% 50%, rgba(225, 29, 72, 0.22) 0%, transparent 50%),
    radial-gradient(circle at 12% 70%, rgba(8, 145, 178, 0.22) 0%, transparent 45%),
    radial-gradient(circle at 88% 85%, rgba(249, 115, 22, 0.28) 0%, transparent 48%),"""

body_bg_new = """    radial-gradient(circle at 15% 15%, rgba(242, 3, 116, 0.24) 0%, transparent 45%),
    radial-gradient(circle at 85% 25%, rgba(255, 122, 0, 0.26) 0%, transparent 45%),
    radial-gradient(circle at 50% 50%, rgba(225, 29, 72, 0.20) 0%, transparent 50%),
    radial-gradient(circle at 12% 70%, rgba(242, 3, 116, 0.22) 0%, transparent 45%),
    radial-gradient(circle at 88% 85%, rgba(255, 122, 0, 0.26) 0%, transparent 48%),"""

css = css.replace(body_bg_old, body_bg_new)

# Update brand logo and add brand-name, brand-go
brand_old = """.header .brand-logo-icon,
.brand-logo img {
  height: 38px !important;
  width: auto !important;
  display: block !important;
  object-fit: contain !important;
  transition: transform 0.3s ease, filter 0.3s ease;
}

.brand-logo:hover .brand-logo-icon,
.brand-logo:hover img {
  transform: scale(1.05);
  filter: drop-shadow(0 0 12px rgba(255, 69, 0, 0.6));
}

.brand-badge {
  display: none !important;
}"""

brand_new = """.header .brand-logo-icon,
.brand-logo img {
  height: 40px !important;
  width: 40px !important;
  border-radius: 10px !important;
  display: block !important;
  object-fit: contain !important;
  transition: transform 0.3s ease, filter 0.3s ease;
  box-shadow: 0 4px 15px rgba(242, 3, 116, 0.35);
}

.brand-logo:hover .brand-logo-icon,
.brand-logo:hover img {
  transform: scale(1.08) rotate(-2deg);
  filter: drop-shadow(0 0 14px rgba(242, 3, 116, 0.75));
}

.brand-name {
  font-family: var(--font-main);
  font-weight: 800;
  font-size: 1.35rem;
  color: #ffffff;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  letter-spacing: -0.02em;
  white-space: nowrap;
}

.brand-go {
  background: var(--grad-primary) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  font-weight: 900;
  text-transform: uppercase;
}

.brand-badge {
  display: none !important;
}"""

css = css.replace(brand_old, brand_new)

# Also update footer logo icon styling
footer_brand_old = """.footer .brand-logo-icon,
.footer .brand-logo img {
  height: 36px;
  width: auto;
}"""

footer_brand_new = """.footer .brand-logo-icon,
.footer .brand-logo img {
  height: 40px;
  width: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(242, 3, 116, 0.35);
}"""

css = css.replace(footer_brand_old, footer_brand_new)

# Update nav link active glow
css = css.replace(
  "background: linear-gradient(90deg, #ff4500, #06b6d4);",
  "background: var(--grad-primary);"
)
css = css.replace(
  "text-shadow: 0 0 14px rgba(255, 69, 0, 0.45);",
  "text-shadow: 0 0 14px rgba(242, 3, 116, 0.55);"
)
css = css.replace(
  "box-shadow: 0 0 10px rgba(255, 69, 0, 0.6);",
  "box-shadow: 0 0 10px rgba(242, 3, 116, 0.6);"
)

# Update buttons border & hover
css = css.replace(
  "border: 1.5px solid rgba(255, 69, 0, 0.5);",
  "border: 1.5px solid rgba(242, 3, 116, 0.45);"
)
css = css.replace(
  "background: rgba(255, 69, 0, 0.22);",
  "background: linear-gradient(135deg, rgba(242, 3, 116, 0.22), rgba(255, 122, 0, 0.22));"
)
css = css.replace(
  "border-color: var(--color-secondary);",
  "border-color: var(--color-secondary); border-image: var(--grad-primary) 1;"
)

# Update timeline connector & glowing steps
css = css.replace(
  "rgba(255, 69, 0, 0.25) 0%,\n    rgba(255, 69, 0, 0.85) 30%,",
  "rgba(242, 3, 116, 0.25) 0%,\n    rgba(242, 3, 116, 0.85) 30%,"
)
css = css.replace(
  "background: linear-gradient(135deg, rgba(255, 69, 0, 0.9), rgba(249, 115, 22, 0.95));",
  "background: var(--grad-primary);"
)
css = css.replace(
  "box-shadow: 0 0 20px rgba(255, 69, 0, 0.5);",
  "box-shadow: 0 0 20px rgba(242, 3, 116, 0.5);"
)
css = css.replace(
  "box-shadow: 0 0 25px rgba(6, 182, 212, 0.8), 0 0 18px rgba(255, 69, 0, 0.8);",
  "box-shadow: 0 0 25px rgba(242, 3, 116, 0.8), 0 0 18px rgba(255, 122, 0, 0.8);"
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css transformed successfully!")

