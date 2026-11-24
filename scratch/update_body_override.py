with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update hero-img filter to !important
css = css.replace(
    'filter: drop-shadow(0 15px 25px rgba(0, 0, 0, 0.45));',
    'filter: drop-shadow(0 15px 25px rgba(0, 0, 0, 0.45)) !important;'
)

css = css.replace(
    'filter: drop-shadow(0 20px 30px rgba(0, 0, 0, 0.60));',
    'filter: drop-shadow(0 20px 30px rgba(0, 0, 0, 0.60)) !important;'
)

# Override body background-image with html body selector
if 'html body {' not in css:
    body_override = """
/* Force Clean Obsidian Background with Zero Radial Gradients behind Hero */
html body {
  background-color: var(--color-bg-base) !important;
  background-image: linear-gradient(180deg, #06090e 0%, #030508 50%, #06090e 100%) !important;
}
"""
    css = css.replace('body {', body_override + '\nbody {')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css updated with html body background override!")

