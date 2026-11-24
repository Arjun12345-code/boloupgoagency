with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update brand palette & gradients to authentic pink + orange
css = css.replace(
    '--color-secondary: #a63afe;\n  --color-secondary-light: #c266fe;\n  --color-accent-pink: #f93a8c;\n  --color-accent-purple: #a63afe;\n  --color-accent-magenta: #dc3ab4;',
    '--color-secondary: #ff7a00;\n  --color-secondary-light: #ff9433;\n  --color-accent-pink: #f93a8c;\n  --color-accent-orange: #ff7a00;\n  --color-accent-coral: #ff5252;\n  --color-accent-magenta: #dc3ab4;'
)

css = css.replace(
    '--grad-primary: linear-gradient(135deg, #f93a8c 0%, #dc3ab4 48%, #a63afe 100%);\n  --grad-primary-hover: linear-gradient(135deg, #ff4c9b 0%, #e84cc2 48%, #b652fe 100%);\n  --grad-hero-badge: linear-gradient(135deg, rgba(249, 58, 140, 0.22) 0%, rgba(166, 58, 254, 0.22) 100%);',
    '--grad-primary: linear-gradient(135deg, #f93a8c 0%, #ff5252 50%, #ff7a00 100%);\n  --grad-primary-hover: linear-gradient(135deg, #ff4c9b 0%, #ff6868 50%, #ff8c1a 100%);\n  --grad-hero-badge: linear-gradient(135deg, rgba(249, 58, 140, 0.22) 0%, rgba(255, 122, 0, 0.22) 100%);'
)

css = css.replace(
    '--grad-cta-banner: linear-gradient(135deg, rgba(8, 10, 24, 0.96) 0%, rgba(249, 58, 140, 0.85) 45%, rgba(166, 58, 254, 0.90) 100%);',
    '--grad-cta-banner: linear-gradient(135deg, rgba(8, 10, 24, 0.96) 0%, rgba(249, 58, 140, 0.85) 45%, rgba(255, 122, 0, 0.90) 100%);'
)

css = css.replace(
    '--border-card-hover: rgba(166, 58, 254, 0.60);\n  --glow-accent: 0 0 35px rgba(249, 58, 140, 0.45);\n  --glow-button: 0 8px 25px rgba(249, 58, 140, 0.45);\n  --glow-button-hover: 0 12px 35px rgba(166, 58, 254, 0.65);',
    '--border-card-hover: rgba(255, 122, 0, 0.55);\n  --glow-accent: 0 0 35px rgba(249, 58, 140, 0.45);\n  --glow-button: 0 8px 25px rgba(249, 58, 140, 0.45);\n  --glow-button-hover: 0 12px 35px rgba(255, 122, 0, 0.60);'
)

# 2. Hero CSS - remove hero-glow-backdrop completely and remove colored halo from hero-img
old_hero_visual_block = """.hero-visual {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
}

.hero-glow-backdrop {
  position: absolute;
  width: 520px;
  height: 520px;
  border-radius: 50%;
  background: radial-gradient(circle at 50% 50%, rgba(249, 58, 140, 0.45) 0%, rgba(166, 58, 254, 0.38) 48%, rgba(220, 58, 180, 0.18) 70%, transparent 80%);
  filter: blur(65px);
  z-index: 1;
  pointer-events: none;
  animation: pulseGlow 4.5s ease-in-out infinite alternate;
}

@keyframes pulseGlow {
  0% {
    transform: scale(0.92);
    opacity: 0.65;
  }

  100% {
    transform: scale(1.08);
    opacity: 1;
  }
}

.hero-visual-frame {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 460px;
  animation: heroLevitate 6s ease-in-out infinite alternate;
  perspective: 1000px;
}

@keyframes heroLevitate {
  0% {
    transform: translateY(0px) rotate(0deg);
  }

  100% {
    transform: translateY(-12px) rotate(0.6deg);
  }
}

.hero-img-wrap {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  background: transparent !important;
  border: none !important;
  border-radius: 0 !important;
  overflow: visible !important;
  box-shadow: none !important;
  padding: 0 !important;
}

.hero-img-wrap::after {
  display: none !important;
}

.hero-img {
  width: 100%;
  height: auto;
  max-height: 560px;
  object-fit: contain;
  border-radius: 0 !important;
  filter: drop-shadow(0 25px 35px rgba(0, 0, 0, 0.85)) drop-shadow(0 0 50px rgba(249, 58, 140, 0.40));
  transition: transform 0.4s ease, filter 0.4s ease;
}

.hero-visual:hover .hero-img {
  transform: translateY(-6px) scale(1.02);
  filter: drop-shadow(0 30px 45px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 65px rgba(166, 58, 254, 0.55));
}"""

new_hero_visual_block = """.hero-visual {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

/* Hero truly has NO background: backdrop is disabled */
.hero-glow-backdrop {
  display: none !important;
}

.hero-visual-frame {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 480px;
  animation: heroLevitate 6s ease-in-out infinite alternate;
  perspective: 1000px;
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

@keyframes heroLevitate {
  0% {
    transform: translateY(0px) rotate(0deg);
  }

  100% {
    transform: translateY(-12px) rotate(0.6deg);
  }
}

.hero-img-wrap {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  background: transparent !important;
  border: none !important;
  border-radius: 0 !important;
  overflow: visible !important;
  box-shadow: none !important;
  padding: 0 !important;
}

.hero-img-wrap::after {
  display: none !important;
}

/* Pure transparent hero cutout with natural depth, zero colored background glow */
.hero-img {
  width: 100%;
  height: auto;
  max-height: 560px;
  object-fit: contain;
  border-radius: 0 !important;
  background: transparent !important;
  filter: drop-shadow(0 15px 25px rgba(0, 0, 0, 0.45));
  transition: transform 0.4s ease, filter 0.4s ease;
}

.hero-visual:hover .hero-img {
  transform: translateY(-6px) scale(1.02);
  filter: drop-shadow(0 20px 30px rgba(0, 0, 0, 0.60));
}

/* Floating elements in hero hidden for clean no-background aesthetic */
.hero-float-element {
  display: none !important;
}"""

if old_hero_visual_block in css:
    css = css.replace(old_hero_visual_block, new_hero_visual_block)
    print("Replaced hero visual block successfully!")
else:
    print("WARNING: old_hero_visual_block not found exactly, doing regex or partial replace")

# 3. Benefits section CSS: add layout for benefits image [BoloUp Agent Role]
benefits_css_addition = """
/* Benefits Section with [BoloUp Agent Role] Layout */
.benefits-layout-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 48px;
  align-items: center;
}

.benefits-cards-wrap {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.benefits-visual-wrap {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.benefits-image-card {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--border-card);
  background: var(--color-bg-card);
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.5);
  transition: var(--transition);
}

.benefits-image-card:hover {
  border-color: var(--border-card-hover);
  box-shadow: 0 25px 55px rgba(0, 0, 0, 0.65), 0 0 30px rgba(255, 122, 0, 0.25);
  transform: translateY(-4px);
}

.benefits-agent-img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
  border-radius: var(--radius-lg);
}

@media (max-width: 991px) {
  .benefits-layout-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
}
"""

if '.benefits-layout-grid' not in css:
    # insert before 10. Earnings Section
    css = css.replace('/* ==========================================================================\n   10. Earnings Section', benefits_css_addition + '\n/* ==========================================================================\n   10. Earnings Section')
    print("Added benefits layout CSS successfully!")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css updated successfully!")

