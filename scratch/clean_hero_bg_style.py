with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace body background-image
old_body_bg = """body {
  font-family: var(--font-main);
  background-color: var(--color-bg-base) !important;
  color: var(--text-body);
  line-height: 1.65;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-image:
    radial-gradient(circle at 15% 15%, rgba(249, 58, 140, 0.24) 0%, transparent 45%),
    radial-gradient(circle at 85% 25%, rgba(166, 58, 254, 0.26) 0%, transparent 45%),
    radial-gradient(circle at 50% 50%, rgba(220, 58, 180, 0.20) 0%, transparent 50%),
    radial-gradient(circle at 12% 70%, rgba(249, 58, 140, 0.22) 0%, transparent 45%),
    radial-gradient(circle at 88% 85%, rgba(166, 58, 254, 0.26) 0%, transparent 48%),
    linear-gradient(180deg, #06090e 0%, #030508 50%, #06090e 100%);
  background-attachment: fixed;
  background-repeat: no-repeat;
  min-height: 100vh;
}"""

new_body_bg = """body {
  font-family: var(--font-main);
  background-color: var(--color-bg-base) !important;
  color: var(--text-body);
  line-height: 1.65;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-image:
    radial-gradient(circle at 8% 45%, rgba(249, 58, 140, 0.08) 0%, transparent 45%),
    radial-gradient(circle at 92% 70%, rgba(255, 122, 0, 0.08) 0%, transparent 45%),
    linear-gradient(180deg, #06090e 0%, #030508 50%, #06090e 100%);
  background-attachment: fixed;
  background-repeat: no-repeat;
  min-height: 100vh;
}"""

if old_body_bg in css:
    css = css.replace(old_body_bg, new_body_bg)
    print("Replaced body background successfully!")
else:
    print("old_body_bg not matched exactly")

# Disable orbs that sit in hero area
old_orbs = """.orb-1 {
  top: 5%;
  left: 8%;
  width: 480px;
  height: 480px;
  background: rgba(249, 58, 140, 0.35);
}

.orb-2 {
  top: 32%;
  right: 5%;
  width: 420px;
  height: 420px;
  background: rgba(166, 58, 254, 0.30);
  animation-delay: -3s;
}"""

new_orbs = """.orb-1 {
  display: none !important;
}

.orb-2 {
  display: none !important;
}"""

if old_orbs in css:
    css = css.replace(old_orbs, new_orbs)
    print("Disabled orb-1 and orb-2 successfully!")
else:
    print("old_orbs not matched exactly")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css updated with zero hero background!")

