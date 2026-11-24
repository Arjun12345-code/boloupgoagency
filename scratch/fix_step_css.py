import re

def update_css():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = "/* ==========================================================================\n   13. Registration Section (#registration)\n   ========================================================================== */"
    end_marker = "/* ==========================================================================\n   14. FAQ Section (#faqs)"

    assert start_marker in content, "start_marker not found"
    assert end_marker in content, "end_marker not found"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    new_section_css = """/* ==========================================================================
   13. Registration Section (#registration) - Side-by-Side (2 Kanan, 2 Kiri)
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
  flex-direction: row !important;
}

/* 2 KANAN: Step 2 & Step 4 -> Media on Left, Text on Right (Teks di Kanan) */
.reg-step-card.step-layout-right {
  flex-direction: row-reverse !important;
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
  flex: 0 0 250px !important;
  max-width: 250px !important;
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
  margin: 0 !important;
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

@keyframes shimmerSweep {
  0% { left: -80%; opacity: 0; }
  15% { opacity: 1; }
  45% { left: 120%; opacity: 1; }
  50%, 100% { left: 120%; opacity: 0; }
}

"""

    content = content[:start_idx] + new_section_css + content[end_idx:]

    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("style.css updated successfully with exact step section replacement!")

update_css()

