import re
import json
import requests

# 1. Update index.html and preview.html
new_reg_section = '''    <!-- Registration Section -->
    <section class="section" id="registration">
      <div class="container">
        <div class="section-title-wrap">
          <div class="section-badge">Step by Step Onboarding</div>
          <h2 class="section-title">
            How to Join <span class="text-gradient">BoloUp Go Agency</span>
          </h2>
        </div>

        <div class="registration-timeline-wrap">
          <div class="reg-steps-flow">
            <!-- Step 1 -->
            <article class="reg-step-card" id="step-1">
              <div class="reg-step-header">
                <span class="reg-step-num">1</span>
                <h3 class="reg-step-title">Step 1 – Download BoloUp Go</h3>
              </div>
              <p class="reg-step-desc">
                First, install BoloUp Go from the Play Store or App Store
              </p>

              <div class="reg-step-media">
                <img src="assets/images/BoloUp-Agency-Registration-Step-1-1.png"
                     alt="Step 1 – Download BoloUp Go"
                     width="513"
                     height="912"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 2 -->
            <article class="reg-step-card" id="step-2">
              <div class="reg-step-header">
                <span class="reg-step-num">2</span>
                <h3 class="reg-step-title">Step 2 – Register &amp; Finish and Verification</h3>
              </div>
              <p class="reg-step-desc">
                Set up your account information and complete face verification when required.
              </p>

              <div class="reg-step-media">
                <img src="assets/images/BoloUp-Agency-Registration-Step-2-1.png"
                     alt="Step 2 – Register &amp; Finish and Verification"
                     width="513"
                     height="912"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 3 -->
            <article class="reg-step-card" id="step-3">
              <div class="reg-step-header">
                <span class="reg-step-num">3</span>
                <h3 class="reg-step-title">Step 3 – Open Your Agency Registration Invitation</h3>
              </div>
              <p class="reg-step-desc">
                Use the agency registration link provided <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer">right here</a> and check the invitation or notice inside BoloUp.
              </p>

              <div class="agency-id-callout">
                <div class="agency-id-label">Official BoloUp Agency ID</div>
                <div class="agency-id-row">
                  <span class="agency-id-code" id="agency-code-text">2527626</span>
                  <button type="button" class="btn-copy-id" id="btn-copy-agency-id" aria-label="Copy Agency ID 2527626">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    <span id="copy-btn-text">Copy Agency ID</span>
                  </button>
                </div>
                <div class="copy-feedback-toast" id="copy-toast">Agency ID copied to clipboard!</div>
              </div>

              <div class="reg-step-media">
                <img src="assets/images/BoloUp-Agency-Registration-Step-3-1.png"
                     alt="Step 3 – Open Your Agency Registration Invitation"
                     width="513"
                     height="912"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 4 -->
            <article class="reg-step-card" id="step-4">
              <div class="reg-step-header">
                <span class="reg-step-num">4</span>
                <h3 class="reg-step-title">Step 4 – Accept the Agency Invitation</h3>
              </div>
              <p class="reg-step-desc">
                Review the agency information and confirm that you want to continue with the registration, add your agency details once you accept the invite.
              </p>

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
    </section>'''

reg_pattern = r'<!-- Registration Section -->\s*<section class="section" id="registration">.*?</section>'

for fname in ['index.html', 'preview.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if re.search(reg_pattern, content, re.DOTALL):
        updated = re.sub(reg_pattern, new_reg_section, content, flags=re.DOTALL)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated {fname} successfully!")
    else:
        print(f"FAILED to find registration section pattern in {fname}")

# 2. Deploy to WordPress Elementor (Post 35)
login_url = "https://boloupgoagency.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0'
})

session.post(login_url, data={
    'log': 'webdev',
    'pwd': '1tR^#1Xq@jGpEErBSw0^Pv0V',
    'wp-submit': 'Log In',
    'testcookie': '1'
}, allow_redirects=True)

# Read index.html for WP
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace local image paths with full WP upload URLs
wp_map = {
    'assets/images/boloupgoagency-nobg.webp': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.webp',
    'assets/images/boloupgoagency-nobg.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png',
    'assets/images/boloupgoagency.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloupgoagency-nobg.png',
    'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png',
    'assets/images/BoloUp-Agency-Registration-Step-1-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-1-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-2-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-2-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-3-1.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-3-1.png',
    'assets/images/BoloUp-Agency-Registration-Step-4.jpg': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-4.jpg'
}

for local_path, wp_url in wp_map.items():
    idx_content = idx_content.replace(local_path, wp_url)

body_m = re.search(r'<body[^>]*>(.*?)</body>', idx_content, re.DOTALL)
page_html_wp = body_m.group(1).strip() if body_m else idx_content

# Get existing elementor structure for post 35
# Add temporary endpoint in functions.php or update directly
edit_func_url = "https://boloupgoagency.com/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child"
r_func = session.get(edit_func_url)
func_nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func.text).group(1)

func_code_updater = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.3
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.1.3'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');

// One-time Elementor updater
add_action('init', function() {
    if (isset($_GET['apply_page35_update']) && current_user_can('manage_options')) {
        $raw = file_get_contents('php://input');
        $payload = json_decode($raw, true);
        if ($payload && isset($payload['html'])) {
            $data = get_post_meta(35, '_elementor_data', true);
            $elements = json_decode($data, true);
            $elements[0]['elements'][0]['settings']['html'] = $payload['html'];
            update_post_meta(35, '_elementor_data', wp_slash(wp_json_encode($elements)));
            wp_update_post(array('ID' => 35, 'post_content' => $payload['html']));
            if (class_exists('\\Elementor\\Plugin')) {
                \\Elementor\\Plugin::$instance->files_manager->clear_cache();
            }
            echo json_encode(array('success' => true));
            exit;
        }
        echo json_encode(array('success' => false));
        exit;
    }
});
"""

r_save_func = session.post(edit_func_url, data={
    'nonce': func_nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': func_code_updater,
    'submit': 'Update File'
})
print("Added updater to functions.php:", "File edited successfully" in r_save_func.text)

# Send update payload
r_up = session.post(
    "https://boloupgoagency.com/?apply_page35_update=1",
    data=json.dumps({'html': page_html_wp}),
    headers={'Content-Type': 'application/json'}
)
print("Page 35 update response:", r_up.status_code, r_up.text)

# Clean functions.php back to clean production code
clean_func = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css v2.1.3
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-agency-theme-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '2.1.3'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean landing view
add_filter('show_admin_bar', '__return_false');
"""

r_func2 = session.get(edit_func_url)
func_nonce2 = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_func2.text).group(1)

session.post(edit_func_url, data={
    'nonce': func_nonce2,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor-child',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor-child',
    'newcontent': clean_func,
    'submit': 'Update File'
})
print("Cleaned functions.php to production code v2.1.3!")

# Purge cache
session.get("https://boloupgoagency.com/?LSCWP_CTRL=purge_all")
print("Purged LiteSpeed cache!")

