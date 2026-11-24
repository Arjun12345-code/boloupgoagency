import re

def update_stylesheet():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Header Container to full width & sleek styling
    old_header_block = r'/\* ==========================================================================\s*8\. Header Component \(header\.html\)[\s\S]*?/\* ==========================================================================\s*9\. Hero Section'
    
    new_header_block = """/* ==========================================================================
   8. Header Component (header.html) - World-Class Glassmorphism & Full Width
   ========================================================================== */
.header {
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: rgba(6, 9, 14, 0.88) !important;
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid rgba(255, 69, 0, 0.22);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45), 0 1px 0 rgba(255, 255, 255, 0.05);
  transition: background 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.header.header-scrolled {
  background: rgba(4, 6, 10, 0.96) !important;
  border-bottom-color: rgba(255, 69, 0, 0.45);
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6), 0 0 20px rgba(255, 69, 0, 0.2);
}

header.elementor-location-header,
header.elementor-location-header .e-con,
header.elementor-location-header .e-con-inner,
header.elementor-location-header .elementor-container {
  width: 100% !important;
  max-width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}

.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: var(--header-height);
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 auto;
  padding: 0 clamp(20px, 4vw, 64px) !important;
}

.header .brand-logo,
.brand-logo {
  display: flex !important;
  align-items: center !important;
  gap: 12px;
  text-decoration: none !important;
  z-index: 1001;
  transition: transform 0.3s ease;
}

.brand-logo:hover {
  transform: translateY(-1px);
}

.header .brand-logo-icon,
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
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  background: var(--grad-primary);
  color: var(--color-white);
  padding: 3px 8px;
  border-radius: var(--radius-pill);
  box-shadow: 0 2px 8px rgba(255, 69, 0, 0.4);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.brand-logo:hover .brand-badge {
  box-shadow: 0 0 16px rgba(255, 69, 0, 0.8), 0 0 24px rgba(6, 182, 212, 0.5);
  transform: translateY(-1px);
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 26px;
}

.nav-link {
  color: var(--text-body);
  font-size: 0.95rem;
  font-weight: 600;
  transition: color 0.3s ease, text-shadow 0.3s ease;
  position: relative;
  padding: 8px 0;
}

.nav-link:hover,
.nav-link.active {
  color: var(--color-white);
  text-shadow: 0 0 14px rgba(255, 69, 0, 0.45);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0%;
  height: 2.5px;
  background: linear-gradient(90deg, #ff4500, #06b6d4);
  border-radius: var(--radius-pill);
  box-shadow: 0 0 10px rgba(255, 69, 0, 0.6);
  transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.nav-link:hover::after,
.nav-link.active::after {
  width: 100%;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 14px;
}

#btn-header-download {
  border: 1.5px solid rgba(255, 69, 0, 0.45);
  background: rgba(255, 69, 0, 0.08);
  color: var(--color-white);
  border-radius: var(--radius-pill);
  padding: 8px 18px;
  font-size: 0.88rem;
  font-weight: 700;
  transition: all 0.3s ease;
}

#btn-header-download:hover {
  background: rgba(255, 69, 0, 0.2);
  border-color: var(--color-primary-light);
  box-shadow: 0 0 18px rgba(255, 69, 0, 0.35);
  transform: translateY(-2px);
}

#btn-header-agent {
  background: var(--grad-primary);
  color: var(--color-white);
  border-radius: var(--radius-pill);
  padding: 8px 20px;
  font-size: 0.88rem;
  font-weight: 700;
  box-shadow: 0 4px 18px rgba(255, 69, 0, 0.45);
  transition: all 0.3s ease;
}

#btn-header-agent:hover {
  background: var(--grad-primary-hover);
  box-shadow: 0 6px 24px rgba(255, 69, 0, 0.65);
  transform: translateY(-2px);
}

.menu-toggle {
  display: none;
  font-size: 1.7rem;
  color: var(--color-white);
  padding: 6px 10px;
  line-height: 1;
  border-radius: 8px;
  background: rgba(255, 69, 0, 0.14);
  border: 1px solid rgba(255, 69, 0, 0.35);
}

.mobile-nav-actions {
  display: none;
}

/* ==========================================================================
   9. Hero Section"""

    content = re.sub(old_header_block, new_header_block, content)

    # 2. Update Registration Timeline & Card Side-by-Side (2 kanan, 2 kiri)
    old_reg_css = r'/\* ==========================================================================\s*13\. Registration Timeline \(Step by Step\)[\s\S]*?/\* ==========================================================================\s*14\. FAQs Accordion'

    new_reg_css = """/* ==========================================================================
   13. Registration Timeline (Step by Step) - Side-by-Side (2 Kanan, 2 Kiri)
   ========================================================================== */
.registration-timeline-wrap {
  max-width: 1040px;
  margin: 0 auto;
  position: relative;
}

.reg-steps-flow {
  display: flex;
  flex-direction: column;
  gap: 48px;
  position: relative;
}

/* Glowing central spine connector */
.reg-steps-flow::before {
  content: '';
  position: absolute;
  top: 50px;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  width: 2px;
  background: linear-gradient(180deg, 
    rgba(255, 69, 0, 0.25) 0%, 
    rgba(255, 69, 0, 0.85) 30%, 
    rgba(6, 182, 212, 0.85) 70%, 
    rgba(6, 182, 212, 0.25) 100%
  );
  box-shadow: 0 0 16px rgba(255, 69, 0, 0.5);
  z-index: 1;
  pointer-events: none;
}

.reg-step-card {
  position: relative;
  background: var(--grad-card);
  border: 1px solid var(--border-card);
  border-radius: 28px;
  padding: 38px 44px;
  box-shadow: 0 20px 48px rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 48px;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease, border-color 0.4s ease;
  overflow: hidden;
  z-index: 2;
}

/* 2 KIRI: Step 1 & Step 3 -> Text on Left, Media on Right */
.reg-step-card.step-layout-left {
  flex-direction: row;
}

/* 2 KANAN: Step 2 & Step 4 -> Media on Left, Text on Right (Teks di Kanan) */
.reg-step-card.step-layout-right {
  flex-direction: row-reverse;
}

.reg-step-text {
  flex: 1 1 56%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  z-index: 2;
}

.reg-step-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 14px;
}

.reg-step-num {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(255, 69, 0, 0.9), rgba(249, 115, 22, 0.95));
  color: var(--color-white);
  font-size: 1.25rem;
  font-weight: 800;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 20px rgba(255, 69, 0, 0.5);
  flex-shrink: 0;
  border: 1.5px solid rgba(255, 255, 255, 0.6);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
}

.reg-step-card:hover .reg-step-num {
  transform: scale(1.1) rotate(6deg);
  box-shadow: 0 0 25px rgba(6, 182, 212, 0.8), 0 0 18px rgba(255, 69, 0, 0.8);
}

.reg-step-title {
  color: var(--text-title);
  font-size: clamp(1.25rem, 2.2vw, 1.55rem);
  font-weight: 800;
  line-height: 1.35;
  letter-spacing: -0.015em;
  margin: 0;
}

.reg-step-desc {
  color: var(--text-body);
  font-size: 1.05rem;
  line-height: 1.75;
  margin: 0;
}

.reg-step-desc a {
  color: var(--color-secondary-light);
  text-decoration: underline;
  font-weight: 600;
  transition: var(--transition);
}

.reg-step-desc a:hover {
  color: var(--color-white);
}

/* Media Mockup Container */
.reg-step-media {
  flex: 0 0 250px;
  max-width: 250px;
  width: 100%;
  position: relative;
  border-radius: 22px;
  overflow: hidden;
  border: 1.5px solid rgba(255, 69, 0, 0.45);
  background: radial-gradient(ellipse at 50% 25%, rgba(18, 27, 42, 0.7) 0%, rgba(8, 12, 20, 0.98) 100%);
  box-shadow: 
    0 20px 45px rgba(0, 0, 0, 0.65),
    0 0 28px rgba(255, 69, 0, 0.22),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  padding: 8px;
  margin: 0;
  cursor: zoom-in;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease, border-color 0.4s ease;
}

/* Floating zoom hint */
.reg-step-media::before {
  content: '';
  position: absolute;
  top: 14px;
  right: 14px;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: rgba(10, 15, 24, 0.88) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3Cline x1='11' y1='8' x2='11' y2='14'%3E%3C/line%3E%3Cline x1='8' y1='11' x2='14' y2='11'%3E%3C/line%3E%3C/svg%3E") no-repeat center;
  border: 1px solid rgba(255, 69, 0, 0.6);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 12px rgba(255, 69, 0, 0.4);
  opacity: 0;
  transform: scale(0.8);
  transition: opacity 0.3s ease, transform 0.3s ease;
  z-index: 6;
  pointer-events: none;
}

.reg-step-card:hover .reg-step-media::before {
  opacity: 1;
  transform: scale(1);
}

/* Shimmer reflection */
.reg-step-media::after {
  content: '';
  position: absolute;
  top: -60%;
  left: -80%;
  width: 140%;
  height: 220%;
  background: linear-gradient(
    105deg,
    transparent 35%,
    rgba(255, 255, 255, 0.08) 46%,
    rgba(6, 182, 212, 0.22) 50%,
    rgba(255, 255, 255, 0.08) 54%,
    transparent 65%
  );
  transform: rotate(25deg);
  pointer-events: none;
  z-index: 5;
  animation: shimmerSweep 7.5s infinite ease-in-out;
}

.reg-step-media img {
  width: 100%;
  height: auto;
  max-height: 440px;
  object-fit: contain;
  display: block;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
  transition: transform 0.5s ease, filter 0.4s ease;
}

/* Hover Card Animation */
.reg-step-card:hover {
  border-color: var(--border-card-hover);
  background: var(--grad-card-hover);
  transform: translateY(-6px);
  box-shadow: 0 28px 65px rgba(0, 0, 0, 0.6), var(--glow-accent);
}

.reg-step-card.step-layout-left:hover .reg-step-media {
  transform: scale(1.03) rotate(1.5deg);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.75), 0 0 35px rgba(255, 69, 0, 0.45);
}

.reg-step-card.step-layout-right:hover .reg-step-media {
  transform: scale(1.03) rotate(-1.5deg);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.75), 0 0 35px rgba(6, 182, 212, 0.45);
}

/* Ambient corner glow */
.reg-step-card::before {
  content: '';
  position: absolute;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  filter: blur(75px);
  pointer-events: none;
  opacity: 0.16;
  transition: opacity 0.5s ease;
  z-index: 0;
}

.reg-step-card.step-layout-left::before {
  top: -70px;
  right: -70px;
  background: rgba(255, 69, 0, 0.55);
}

.reg-step-card.step-layout-right::before {
  bottom: -70px;
  left: -70px;
  background: rgba(6, 182, 212, 0.55);
}

.reg-step-card:hover::before {
  opacity: 0.35;
}

/* Scroll Reveal Animations */
.reg-step-card.reveal-init {
  opacity: 0;
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.reg-step-card.step-layout-left.reveal-init {
  transform: translateX(-40px) scale(0.97);
}

.reg-step-card.step-layout-right.reveal-init {
  transform: translateX(40px) scale(0.97);
}

.reg-step-card.revealed {
  opacity: 1 !important;
  transform: translateX(0) translateY(0) scale(1) !important;
}

/* ==========================================================================
   14. FAQs Accordion"""

    content = re.sub(old_reg_css, new_reg_css, content)

    # 3. Update Footer CSS to Full Width
    old_footer_css = r'/\* ==========================================================================\s*16\. Footer Component \(footer\.html\)[\s\S]*?/\* ==========================================================================\s*17\. Image Lightbox Modal'

    new_footer_css = """/* ==========================================================================
   16. Footer Component (footer.html) - Full Width Edge-to-Edge
   ========================================================================== */
.footer {
  background-color: var(--color-bg-deep) !important;
  color: var(--text-body);
  border-top: 1px solid rgba(255, 69, 0, 0.25);
  padding: 80px 0 35px;
  position: relative;
  z-index: 2;
  width: 100% !important;
  max-width: 100% !important;
}

.footer-container,
.footer .container {
  width: 100% !important;
  max-width: 100% !important;
  padding: 0 clamp(24px, 5vw, 80px) !important;
  margin: 0 auto;
}

footer.elementor-location-footer,
footer.elementor-location-footer .e-con,
footer.elementor-location-footer .e-con-inner,
footer.elementor-location-footer .elementor-container {
  width: 100% !important;
  max-width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.8fr 1fr 1fr 1.2fr;
  gap: clamp(32px, 4vw, 64px);
  margin-bottom: 56px;
  width: 100%;
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.footer-desc {
  color: var(--text-muted);
  font-size: 0.95rem;
  line-height: 1.7;
  max-width: 360px;
}

.footer-col h3 {
  color: var(--text-title);
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 20px;
  letter-spacing: -0.01em;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-links a {
  color: var(--text-body);
  font-size: 0.95rem;
  transition: var(--transition);
}

.footer-links a:hover {
  color: var(--color-primary-light);
  transform: translateX(3px);
  display: inline-block;
}

.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid rgba(255, 69, 0, 0.18);
  padding-top: 28px;
  color: var(--text-muted);
  font-size: 0.9rem;
  flex-wrap: wrap;
  gap: 16px;
  width: 100%;
}

.footer .brand-logo-icon,
.footer .brand-logo img {
  height: 36px !important;
  max-height: 36px !important;
  width: auto !important;
  max-width: 140px !important;
}

/* ==========================================================================
   17. Image Lightbox Modal"""

    content = re.sub(old_footer_css, new_footer_css, content)

    # 4. Update mobile media query for cards
    old_mob_reg = r'\.reg-step-card \{\s*padding: 26px 20px;\s*\}\s*\.reg-step-media \{\s*max-width: 240px;[\s\S]*?margin: 14px auto 0;\s*\}'
    new_mob_reg = """  .reg-steps-flow::before {
    display: none;
  }

  .reg-step-card,
  .reg-step-card.step-layout-left,
  .reg-step-card.step-layout-right {
    flex-direction: column !important;
    padding: 30px 22px;
    gap: 26px;
    text-align: center;
  }

  .reg-step-header {
    justify-content: center;
  }

  .reg-step-media {
    margin: 0 auto;
    max-width: 240px;
  }

  .reg-step-card.step-layout-left.reveal-init,
  .reg-step-card.step-layout-right.reveal-init {
    transform: translateY(35px) scale(0.97);
  }"""

    content = re.sub(old_mob_reg, new_mob_reg, content)

    # 5. Bump version to 2.1.8
    content = re.sub(r'Version: 2\.\d+\.\d+', 'Version: 2.1.8', content)

    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("style.css updated to v2.1.8 successfully!")

update_stylesheet()

