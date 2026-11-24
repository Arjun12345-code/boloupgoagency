import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Header comment
css = re.sub(
    r'Signature Cyber Brand: Deep Obsidian.*?Fiery Orange \(#FF7A00\)',
    'Authentic BoloUp Brand Identity: Deep Obsidian (#06090E) with Neon Pink (#F93A8C) to Electric Purple (#A63AFE)',
    css
)

# 2. Update :root variables
root_old = """  /* Accent Tones: BoloUp Brand Neon Pink & Fiery Orange */
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
  --grad-cta-banner: linear-gradient(135deg, rgba(8, 12, 20, 0.96) 0%, rgba(242, 3, 116, 0.88) 45%, rgba(255, 122, 0, 0.92) 100%);

  /* Text & Typography */
  --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --color-white: #ffffff;
  --text-title: #ffffff;
  --text-body: rgba(243, 244, 246, 0.92);
  --text-muted: rgba(209, 213, 219, 0.72);

  /* Borders & Glow Effects */
  --border-card: rgba(242, 3, 116, 0.22);
  --border-card-hover: rgba(255, 122, 0, 0.55);
  --glow-accent: 0 0 35px rgba(242, 3, 116, 0.45);
  --glow-button: 0 8px 25px rgba(242, 3, 116, 0.45);
  --glow-button-hover: 0 12px 35px rgba(255, 122, 0, 0.65);"""

root_new = """  /* Accent Tones: Authentic Bolo Logo Palette (Neon Pink to Electric Purple) */
  --color-primary: #f93a8c;
  --color-primary-light: #ff5ba4;
  --color-primary-dark: #d81b74;
  --color-secondary: #a63afe;
  --color-secondary-light: #c266fe;
  --color-accent-pink: #f93a8c;
  --color-accent-purple: #a63afe;
  --color-accent-magenta: #dc3ab4;
  --color-accent-rose: #f23b9e;
  --color-accent-cyan: #06b6d4;
  --color-accent-emerald: #10b981;

  /* Primary Gradients: Signature Bolo Logo Pink-to-Purple */
  --grad-primary: linear-gradient(135deg, #f93a8c 0%, #dc3ab4 48%, #a63afe 100%);
  --grad-primary-hover: linear-gradient(135deg, #ff4c9b 0%, #e84cc2 48%, #b652fe 100%);
  --grad-hero-badge: linear-gradient(135deg, rgba(249, 58, 140, 0.22) 0%, rgba(166, 58, 254, 0.22) 100%);
  --grad-card: rgba(12, 18, 28, 0.72);
  --grad-card-hover: rgba(18, 27, 42, 0.85);
  --grad-cta-banner: linear-gradient(135deg, rgba(8, 10, 24, 0.96) 0%, rgba(249, 58, 140, 0.85) 45%, rgba(166, 58, 254, 0.90) 100%);

  /* Text & Typography */
  --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --color-white: #ffffff;
  --text-title: #ffffff;
  --text-body: rgba(243, 244, 246, 0.92);
  --text-muted: rgba(209, 213, 219, 0.72);

  /* Borders & Glow Effects */
  --border-card: rgba(249, 58, 140, 0.22);
  --border-card-hover: rgba(166, 58, 254, 0.60);
  --glow-accent: 0 0 35px rgba(249, 58, 140, 0.45);
  --glow-button: 0 8px 25px rgba(249, 58, 140, 0.45);
  --glow-button-hover: 0 12px 35px rgba(166, 58, 254, 0.65);"""

css = css.replace(root_old, root_new)

# 3. Update body background
body_bg_old = """    radial-gradient(circle at 15% 15%, rgba(242, 3, 116, 0.24) 0%, transparent 45%),
    radial-gradient(circle at 85% 25%, rgba(255, 122, 0, 0.26) 0%, transparent 45%),
    radial-gradient(circle at 50% 50%, rgba(225, 29, 72, 0.20) 0%, transparent 50%),
    radial-gradient(circle at 12% 70%, rgba(242, 3, 116, 0.22) 0%, transparent 45%),
    radial-gradient(circle at 88% 85%, rgba(255, 122, 0, 0.26) 0%, transparent 48%),"""

body_bg_new = """    radial-gradient(circle at 15% 15%, rgba(249, 58, 140, 0.24) 0%, transparent 45%),
    radial-gradient(circle at 85% 25%, rgba(166, 58, 254, 0.26) 0%, transparent 45%),
    radial-gradient(circle at 50% 50%, rgba(220, 58, 180, 0.20) 0%, transparent 50%),
    radial-gradient(circle at 12% 70%, rgba(249, 58, 140, 0.22) 0%, transparent 45%),
    radial-gradient(circle at 88% 85%, rgba(166, 58, 254, 0.26) 0%, transparent 48%),"""

css = css.replace(body_bg_old, body_bg_new)

# 4. Update Orbs
css = css.replace(
    "background: rgba(242, 3, 116, 0.32);",
    "background: rgba(249, 58, 140, 0.35);"
)
css = css.replace(
    "background: rgba(255, 122, 0, 0.28);\n  animation-delay: -3s;",
    "background: rgba(166, 58, 254, 0.30);\n  animation-delay: -3s;"
)

# 5. Update header borders and glows
css = css.replace(
    "border-bottom: 1px solid rgba(242, 3, 116, 0.22);",
    "border-bottom: 1px solid rgba(249, 58, 140, 0.22);"
)
css = css.replace(
    "border-bottom-color: rgba(242, 3, 116, 0.45);\n  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6), 0 0 20px rgba(255, 122, 0, 0.2);",
    "border-bottom-color: rgba(249, 58, 140, 0.45);\n  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6), 0 0 20px rgba(166, 58, 254, 0.25);"
)
css = css.replace(
    "box-shadow: 0 4px 15px rgba(242, 3, 116, 0.35);",
    "box-shadow: 0 4px 15px rgba(249, 58, 140, 0.4);"
)
css = css.replace(
    "filter: drop-shadow(0 0 14px rgba(242, 3, 116, 0.75));",
    "filter: drop-shadow(0 0 14px rgba(249, 58, 140, 0.8));"
)

# 6. Update header action buttons
css = css.replace(
    "border: 1.5px solid rgba(242, 3, 116, 0.45);",
    "border: 1.5px solid rgba(249, 58, 140, 0.45);"
)
css = css.replace(
    "background: rgba(242, 3, 116, 0.08);",
    "background: rgba(249, 58, 140, 0.08);"
)
css = css.replace(
    "background: linear-gradient(135deg, rgba(242, 3, 116, 0.22), rgba(255, 122, 0, 0.22));",
    "background: linear-gradient(135deg, rgba(249, 58, 140, 0.22), rgba(166, 58, 254, 0.22));"
)
css = css.replace(
    "border-color: var(--color-accent-orange);",
    "border-color: var(--color-secondary);"
)
css = css.replace(
    "box-shadow: 0 0 18px rgba(242, 3, 116, 0.4);",
    "box-shadow: 0 0 18px rgba(249, 58, 140, 0.45);"
)
css = css.replace(
    "box-shadow: 0 4px 18px rgba(242, 3, 116, 0.45);",
    "box-shadow: 0 4px 18px rgba(249, 58, 140, 0.45);"
)
css = css.replace(
    "box-shadow: 0 6px 24px rgba(255, 122, 0, 0.65);",
    "box-shadow: 0 6px 24px rgba(166, 58, 254, 0.65);"
)
css = css.replace(
    "background: rgba(242, 3, 116, 0.14);",
    "background: rgba(249, 58, 140, 0.14);"
)
css = css.replace(
    "border: 1px solid rgba(242, 3, 116, 0.35);",
    "border: 1px solid rgba(249, 58, 140, 0.35);"
)

# 7. Update hero section visual glow & elements
css = css.replace(
    "background: radial-gradient(circle at 50% 50%, rgba(242, 3, 116, 0.45) 0%, rgba(255, 122, 0, 0.35) 45%, rgba(242, 3, 116, 0.15) 70%, transparent 80%);",
    "background: radial-gradient(circle at 50% 50%, rgba(249, 58, 140, 0.45) 0%, rgba(166, 58, 254, 0.38) 48%, rgba(220, 58, 180, 0.18) 70%, transparent 80%);"
)
css = css.replace(
    "filter: drop-shadow(0 25px 35px rgba(0, 0, 0, 0.85)) drop-shadow(0 0 50px rgba(242, 3, 116, 0.35));",
    "filter: drop-shadow(0 25px 35px rgba(0, 0, 0, 0.85)) drop-shadow(0 0 50px rgba(249, 58, 140, 0.40));"
)
css = css.replace(
    "filter: drop-shadow(0 30px 45px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 65px rgba(255, 122, 0, 0.5));",
    "filter: drop-shadow(0 30px 45px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 65px rgba(166, 58, 254, 0.55));"
)
css = css.replace(
    "border: 1.5px solid rgba(242, 3, 116, 0.55);\n  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6), 0 0 24px rgba(242, 3, 116, 0.4);",
    "border: 1.5px solid rgba(249, 58, 140, 0.55);\n  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6), 0 0 24px rgba(249, 58, 140, 0.45);"
)
css = css.replace(
    "box-shadow: 0 0 20px rgba(242, 3, 116, 0.25);",
    "box-shadow: 0 0 20px rgba(249, 58, 140, 0.25);"
)

# 8. Update badges & cards
css = css.replace(
    "background: linear-gradient(135deg, rgba(242, 3, 116, 0.16), rgba(255, 122, 0, 0.16));",
    "background: linear-gradient(135deg, rgba(249, 58, 140, 0.16), rgba(166, 58, 254, 0.16));"
)
css = css.replace(
    "color: rgba(242, 3, 116, 0.25);",
    "color: rgba(249, 58, 140, 0.25);"
)
css = css.replace(
    "color: var(--color-accent-orange);\n  text-shadow: 0 0 20px rgba(255, 122, 0, 0.6);",
    "color: var(--color-secondary-light);\n  text-shadow: 0 0 20px rgba(166, 58, 254, 0.65);"
)
css = css.replace(
    "background: linear-gradient(135deg, rgba(242, 3, 116, 0.22), rgba(255, 122, 0, 0.22));",
    "background: linear-gradient(135deg, rgba(249, 58, 140, 0.22), rgba(166, 58, 254, 0.22));"
)
css = css.replace(
    "box-shadow: 0 4px 15px rgba(242, 3, 116, 0.35);",
    "box-shadow: 0 4px 15px rgba(249, 58, 140, 0.35);"
)

# 9. Update Registration Timeline
css = css.replace(
    "background: linear-gradient(180deg, \n    rgba(242, 3, 116, 0.25) 0%,\n    rgba(242, 3, 116, 0.85) 35%,\n    rgba(255, 122, 0, 0.85) 65%,\n    rgba(255, 122, 0, 0.25) 100%\n  );",
    "background: linear-gradient(180deg, \n    rgba(249, 58, 140, 0.25) 0%,\n    rgba(249, 58, 140, 0.85) 35%,\n    rgba(166, 58, 254, 0.85) 65%,\n    rgba(166, 58, 254, 0.25) 100%\n  );"
)
css = css.replace(
    "box-shadow: 0 0 16px rgba(242, 3, 116, 0.5);",
    "box-shadow: 0 0 16px rgba(249, 58, 140, 0.5);"
)
css = css.replace(
    "box-shadow: 0 0 20px rgba(242, 3, 116, 0.5);",
    "box-shadow: 0 0 20px rgba(249, 58, 140, 0.5);"
)
css = css.replace(
    "0 0 28px rgba(242, 3, 116, 0.22),",
    "0 0 28px rgba(249, 58, 140, 0.25),"
)
css = css.replace(
    "border: 1px solid rgba(255, 122, 0, 0.6);",
    "border: 1px solid rgba(166, 58, 254, 0.65);"
)
css = css.replace(
    "box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 12px rgba(242, 3, 116, 0.4);",
    "box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 12px rgba(166, 58, 254, 0.45);"
)
css = css.replace(
    "box-shadow: 0 24px 50px rgba(0, 0, 0, 0.75), 0 0 35px rgba(242, 3, 116, 0.45);",
    "box-shadow: 0 24px 50px rgba(0, 0, 0, 0.75), 0 0 35px rgba(249, 58, 140, 0.50);"
)
css = css.replace(
    "box-shadow: 0 24px 50px rgba(0, 0, 0, 0.75), 0 0 35px rgba(255, 122, 0, 0.45);",
    "box-shadow: 0 24px 50px rgba(0, 0, 0, 0.75), 0 0 35px rgba(166, 58, 254, 0.50);"
)

# 10. Update Final CTA Banner
css = css.replace(
    "background: rgba(242, 3, 116, 0.65);",
    "background: rgba(249, 58, 140, 0.70);"
)
css = css.replace(
    "background: rgba(255, 122, 0, 0.65);",
    "background: rgba(166, 58, 254, 0.70);"
)

# 11. Update FAQ
css = css.replace(
    "box-shadow: 0 10px 30px rgba(242, 3, 116, 0.3);",
    "box-shadow: 0 10px 30px rgba(249, 58, 140, 0.3);"
)
css = css.replace(
    "background: linear-gradient(135deg, rgba(242, 3, 116, 0.25), rgba(255, 122, 0, 0.25));",
    "background: linear-gradient(135deg, rgba(249, 58, 140, 0.25), rgba(166, 58, 254, 0.25));"
)
css = css.replace(
    "background: rgba(242, 3, 116, 0.22);",
    "background: rgba(249, 58, 140, 0.25);"
)

# 12. Update Footer
css = css.replace(
    "border-top: 1px solid rgba(242, 3, 116, 0.2);",
    "border-top: 1px solid rgba(249, 58, 140, 0.25);"
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css successfully updated to Authentic BoloUp Pink-to-Purple brand palette!")

