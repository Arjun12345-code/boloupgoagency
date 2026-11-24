import re

def update_registration_section(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_reg_pattern = r'<!-- Registration Section -->[\s\S]*?<!-- FAQs Section -->'

    new_reg_section = '''<!-- Registration Section -->
    <section class="section" id="registration">
      <div class="container">
        <div class="section-title-wrap">
          <p class="section-subtitle">Step by step</p>
          <h2 class="section-title">
            How to Join <span class="text-gradient">BoloUp Go Agency</span>
          </h2>
        </div>

        <div class="registration-timeline-wrap">
          <div class="reg-steps-flow">
            <!-- Step 1 (Text Left, Image Right) -->
            <article class="reg-step-card step-layout-left" id="step-1" data-step="1">
              <div class="reg-step-text">
                <div class="reg-step-header">
                  <span class="reg-step-num">1</span>
                  <h3 class="reg-step-title">Step 1 – Download BoloUp Go</h3>
                </div>
                <p class="reg-step-desc">
                  First, install BoloUp Go from the Play Store or App Store
                </p>
              </div>
              <div class="reg-step-media">
                <img src="assets/images/BoloUp-Agency-Registration-Step-1-1.png"
                     alt="Step 1 – Download BoloUp Go"
                     width="513"
                     height="912"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 2 (Image Left, Text Right) -->
            <article class="reg-step-card step-layout-right" id="step-2" data-step="2">
              <div class="reg-step-text">
                <div class="reg-step-header">
                  <span class="reg-step-num">2</span>
                  <h3 class="reg-step-title">Step 2 – Register &amp; Finish and Verification</h3>
                </div>
                <p class="reg-step-desc">
                  Set up your account information and complete face verification when required.
                </p>
              </div>
              <div class="reg-step-media">
                <img src="assets/images/BoloUp-Agency-Registration-Step-2-1.png"
                     alt="Step 2 – Register &amp; Finish and Verification"
                     width="513"
                     height="912"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 3 (Text Left, Image Right) -->
            <article class="reg-step-card step-layout-left" id="step-3" data-step="3">
              <div class="reg-step-text">
                <div class="reg-step-header">
                  <span class="reg-step-num">3</span>
                  <h3 class="reg-step-title">Step 3 – Open Your Agency Registration Invitation</h3>
                </div>
                <p class="reg-step-desc">
                  Use the agency registration link provided <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer">right here</a> and check the invitation or notice inside BoloUp.
                </p>
              </div>
              <div class="reg-step-media">
                <img src="assets/images/BoloUp-Agency-Registration-Step-3-1.png"
                     alt="Step 3 – Open Your Agency Registration Invitation"
                     width="513"
                     height="912"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 4 (Image Left, Text Right) -->
            <article class="reg-step-card step-layout-right" id="step-4" data-step="4">
              <div class="reg-step-text">
                <div class="reg-step-header">
                  <span class="reg-step-num">4</span>
                  <h3 class="reg-step-title">Step 4 – Accept the Agency Invitation</h3>
                </div>
                <p class="reg-step-desc">
                  Review the agency information and confirm that you want to continue with the registration, add your agency details once you accept the invite.
                </p>
              </div>
              <div class="reg-step-media">
                <img src="assets/images/BoloUp-Agency-Registration-Step-4.jpg"
                     alt="Step 4 – Accept the Agency Invitation"
                     width="444"
                     height="912"
                     loading="lazy">
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQs Section -->'''

    content = re.sub(old_reg_pattern, new_reg_section, content)

    # Add scroll reveal IntersectionObserver in script
    old_script_start = "    (function () {\n      // FAQ Accordion Handler"
    new_script_start = """    (function () {
      // Scroll Reveal Animation for Registration Step Cards
      if ('IntersectionObserver' in window) {
        const stepCards = document.querySelectorAll('.reg-step-card');
        stepCards.forEach(function (card) {
          card.classList.add('reveal-init');
        });

        const cardObserver = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('revealed');
              cardObserver.unobserve(entry.target);
            }
          });
        }, { threshold: 0.15 });

        stepCards.forEach(function (card) {
          cardObserver.observe(card);
        });
      }

      // FAQ Accordion Handler"""

    if old_script_start in content:
        content = content.replace(old_script_start, new_script_start)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath} successfully!")

update_registration_section('index.html')
update_registration_section('preview.html')

