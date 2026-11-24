import re

def clean_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Hero badge
    content = re.sub(r'\s*<div class="hero-badge">.*?</div>', '', content)

    # 2. Remove Hero secondary button "Download BoloUp Go"
    content = re.sub(r'\s*<a href="https://share\.bololinks\.com/home/scode/47282"[^>]*id="hero-btn-download"[^>]*>.*?</a>', '', content)

    # 3. Remove What is boloup badge
    content = re.sub(r'\s*<div class="section-badge">Platform &amp; Role Overview</div>', '', content)

    # 4. Remove about-feature-tags
    content = re.sub(r'\s*<div class="about-feature-tags">[\s\S]*?</div>\s*</div>\s*</div>', '\n            </div>\n          </div>', content)

    # 5. Remove Benefits badge
    content = re.sub(r'\s*<div class="section-badge">Exclusive Agent Advantages</div>', '', content)

    # 6. Remove Earnings badge
    content = re.sub(r'\s*<div class="section-badge">Revenue Potential</div>', '', content)

    # 7. Remove earning-badges
    content = re.sub(r'\s*<div class="earning-badge">Direct Revenue</div>', '', content)
    content = re.sub(r'\s*<div class="earning-badge">Network Expansion</div>', '', content)
    content = re.sub(r'\s*<div class="earning-badge">Bonus Incentives</div>', '', content)

    # 8. Clean Registration badge -> "Step by step"
    content = re.sub(r'<div class="section-badge">Step by Step Onboarding</div>', '<p class="section-subtitle">Step by step</p>', content)

    # 9. Remove FAQs badge
    content = re.sub(r'\s*<div class="section-badge">Help &amp; Clarification</div>', '', content)

    # 10. Align CTA section strictly to brief
    # Brief: Headline: Become a BoloUp Go Agent
    # CTA: Your Next Great Team & Side Income Could Start Here
    old_cta_block = '''          <div class="cta-content-inner">
            <h2 class="cta-headline">
              Become a <span class="text-gradient">BoloUp Go Agent</span>
            </h2>
            <p class="cta-tagline">
              Your Next Great Team &amp; Side Income Could Start Here
            </p>
            <div class="cta-actions">
              <a href="#registration" class="btn btn-primary btn-lg" id="final-cta-btn">
                Start Your BoloUp Agency
              </a>
            </div>
          </div>'''

    new_cta_block = '''          <div class="cta-content-inner">
            <h2 class="cta-headline">
              Become a <span class="text-gradient">BoloUp Go Agent</span>
            </h2>
            <div class="cta-actions">
              <a href="#registration" class="btn btn-primary btn-lg" id="final-cta-btn">
                Your Next Great Team &amp; Side Income Could Start Here
              </a>
            </div>
          </div>'''

    if old_cta_block in content:
        content = content.replace(old_cta_block, new_cta_block)
    else:
        # regex replace
        cta_pattern = r'<div class="cta-content-inner">[\s\S]*?</div>\s*</div>\s*</div>\s*</section>'
        new_cta_full = '''<div class="cta-content-inner">
            <h2 class="cta-headline">
              Become a <span class="text-gradient">BoloUp Go Agent</span>
            </h2>
            <div class="cta-actions">
              <a href="#registration" class="btn btn-primary btn-lg" id="final-cta-btn">
                Your Next Great Team &amp; Side Income Could Start Here
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>'''
        content = re.sub(cta_pattern, new_cta_full, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{filepath} cleaned successfully!")

clean_html('index.html')
clean_html('preview.html')

