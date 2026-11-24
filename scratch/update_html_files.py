import re

def update_html(filepath, is_wp=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Clean hero visual: remove hero-glow-backdrop and floating elements
    # Locate hero-visual
    old_hero_visual_re = r'<div class="hero-visual"[^>]*>[\s\S]*?</div>\s*</div>\s*</div>\s*</section>'
    
    hero_img_src = "https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png" if is_wp else "assets/images/boloupgoagency-nobg.png"
    hero_webp_src = "https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg-v3.png" if is_wp else "assets/images/boloupgoagency-nobg.webp"
    
    clean_hero_visual = f'''<div class="hero-visual" id="hero-visual-agency">
            <div class="hero-visual-frame">
              <div class="hero-img-wrap">
                <picture>
                  <source srcset="{hero_webp_src}" type="image/webp">
                  <img src="{hero_img_src}"
                       alt="Build a Team That Grows with BoloUp Go Agency"
                       class="hero-img"
                       width="1024"
                       height="1536"
                       fetchpriority="high">
                </picture>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''

    html = re.sub(old_hero_visual_re, clean_hero_visual, html)

    # 2. Update Benefits section to include [BoloUp Agent Role]
    agent_role_src = "https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agent-Role.png" if is_wp else "assets/images/boloup-agent-role.png"
    
    old_benefits_re = r'<section class="section" id="benefits">[\s\S]*?</section>'
    new_benefits = f'''<section class="section" id="benefits">
      <div class="container">
        <div class="section-title-wrap">
          <h2 class="section-title">
            Why Build Your Own <span class="text-gradient">BoloUp Go Agency?</span>
          </h2>
        </div>

        <div class="benefits-layout-grid">
          <div class="benefits-cards-wrap">
            <!-- Benefit 1 -->
            <article class="benefit-card" id="benefit-card-1">
              <div class="benefit-number" aria-hidden="true">01</div>
              <div class="benefit-icon-box" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
              </div>
              <h3 class="benefit-title">1. Grow a Host Network of Your Own</h3>
              <p class="benefit-desc">
                Recruit hosts with potential and gradually build a team you can guide and manage as your agency develops.
              </p>
            </article>

            <!-- Benefit 2 -->
            <article class="benefit-card" id="benefit-card-2">
              <div class="benefit-number" aria-hidden="true">02</div>
              <div class="benefit-icon-box" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                </svg>
              </div>
              <h3 class="benefit-title">2. Help Hosts Perform at Their Best</h3>
              <p class="benefit-desc">
                A good agency does more than invite people. Give your hosts direction, encouragement, and to receive various weekly or monthly agency rewards.
              </p>
            </article>

            <!-- Benefit 3 -->
            <article class="benefit-card" id="benefit-card-3">
              <div class="benefit-number" aria-hidden="true">03</div>
              <div class="benefit-icon-box" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="12" y1="1" x2="12" y2="23"></line>
                  <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
              </div>
              <h3 class="benefit-title">3. Create Growth Beyond Your Own Account</h3>
              <p class="benefit-desc">
                Your progress as an agent is connected to the team you build, giving you a way to grow your team and earnings at the same time.
              </p>
            </article>
          </div>

          <div class="benefits-visual-wrap">
            <div class="benefits-image-card">
              <img src="{agent_role_src}"
                   alt="Why Build Your Own BoloUp Go Agency - BoloUp Agent Role"
                   class="benefits-agent-img"
                   width="1350"
                   height="860"
                   loading="lazy">
            </div>
          </div>
        </div>
      </div>
    </section>'''

    html = re.sub(old_benefits_re, new_benefits, html)

    # 3. Add favicon links to head if not present
    if '<link rel="icon"' not in html:
        fav_tags = '''  <link rel="icon" type="image/png" sizes="32x32" href="assets/images/boloup-avatar-32x32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="assets/images/boloup-avatar-192x192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="assets/images/cropped-boloup.png">
'''
        html = html.replace('  <link rel="stylesheet" href="style.css">', fav_tags + '  <link rel="stylesheet" href="style.css">')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filepath} successfully!")

update_html('index.html', is_wp=False)
update_html('preview.html', is_wp=False)

