with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update brand tokens to vibrant authentic Bolo logo colors
css = css.replace(
    '--color-primary: #f93a8c;\n  --color-primary-light: #ff60a8;\n  --color-primary-dark: #e02476;\n  --color-secondary: #ff7a00;\n  --color-secondary-light: #ff9433;',
    '--color-primary: #ff0281;\n  --color-primary-light: #ff3b90;\n  --color-primary-dark: #d6006c;\n  --color-secondary: #ff7a00;\n  --color-secondary-light: #ff9433;'
)

css = css.replace(
    '--grad-primary: linear-gradient(135deg, #f93a8c 0%, #ff5252 50%, #ff7a00 100%);\n  --grad-primary-hover: linear-gradient(135deg, #ff4c9b 0%, #ff6868 50%, #ff8c1a 100%);\n  --grad-hero-badge: linear-gradient(135deg, rgba(249, 58, 140, 0.22) 0%, rgba(255, 122, 0, 0.22) 100%);',
    '--grad-primary: linear-gradient(135deg, #ff0281 0%, #ff4d36 50%, #ff7a00 100%);\n  --grad-primary-hover: linear-gradient(135deg, #ff1a90 0%, #ff6048 50%, #ff8c1a 100%);\n  --grad-hero-badge: linear-gradient(135deg, rgba(255, 2, 129, 0.25) 0%, rgba(255, 122, 0, 0.25) 100%);'
)

css = css.replace(
    '--border-card: rgba(249, 58, 140, 0.22);',
    '--border-card: rgba(255, 2, 129, 0.32);'
)

css = css.replace(
    '--glow-accent: 0 0 35px rgba(249, 58, 140, 0.45);\n  --glow-button: 0 8px 25px rgba(249, 58, 140, 0.45);\n  --glow-button-hover: 0 12px 35px rgba(255, 122, 0, 0.60);',
    '--glow-accent: 0 0 35px rgba(255, 2, 129, 0.45);\n  --glow-button: 0 8px 25px rgba(255, 2, 129, 0.45);\n  --glow-button-hover: 0 12px 35px rgba(255, 122, 0, 0.65);'
)

# 2. Replace all remaining purple instances (rgba(166, 58, 254, ...))
css = css.replace('rgba(166, 58, 254, 0.16)', 'rgba(255, 122, 0, 0.16)')
css = css.replace('rgba(166, 58, 254, 0.22)', 'rgba(255, 122, 0, 0.22)')
css = css.replace('rgba(166, 58, 254, 0.25)', 'rgba(255, 122, 0, 0.25)')
css = css.replace('rgba(166, 58, 254, 0.30)', 'rgba(255, 122, 0, 0.30)')
css = css.replace('rgba(166, 58, 254, 0.45)', 'rgba(255, 122, 0, 0.45)')
css = css.replace('rgba(166, 58, 254, 0.50)', 'rgba(255, 122, 0, 0.50)')
css = css.replace('rgba(166, 58, 254, 0.65)', 'rgba(255, 122, 0, 0.65)')
css = css.replace('rgba(166, 58, 254, 0.70)', 'rgba(255, 122, 0, 0.70)')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with authentic vibrant Bolo logo colors successfully!")

