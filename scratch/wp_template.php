<?php
/**
 * Template Name: BoloUp Agency One Page
 * Description: High-conversion semantic standalone landing page for BoloUp Go Agency
 */
?><!DOCTYPE html>
<html <?php language_attributes(); ?> class="scroll-smooth">
<head>
  <meta charset="<?php bloginfo('charset'); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BoloUp Go Agency – Build, Manage &amp; Grow Your Team from Everywhere</title>
  <meta name="description" content="Join BoloUp Go Agency, recruit and support hosts, grow your team, and unlock earning opportunities through team performance from everywhere.">
  <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

  <!-- Ambient Glow Orbs -->
  <div class="ambient-glow-orb orb-1" aria-hidden="true"></div>
  <div class="ambient-glow-orb orb-2" aria-hidden="true"></div>
  <div class="ambient-glow-orb orb-3" aria-hidden="true"></div>
  <div class="ambient-glow-orb orb-4" aria-hidden="true"></div>

  <!-- Header Component -->
  <header class="header" id="header">
    <div class="header-container">
      <a href="#hero" class="brand-logo" id="brand-logo" aria-label="BoloUp Go Agency Official">
        <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/boloup-header-logo.png' ) ); ?>"
             alt="BoloUp Go Official Logo"
             class="brand-logo-icon"
             width="117"
             height="64">
        <span class="brand-badge">Agency</span>
      </a>

      <nav class="nav-menu" id="nav-menu" aria-label="Main Navigation">
        <a href="#hero" class="nav-link active" id="nav-home">Home</a>
        <a href="#what-is-boloup" class="nav-link" id="nav-about">About</a>
        <a href="#benefits" class="nav-link" id="nav-benefits">Benefits</a>
        <a href="#earnings" class="nav-link" id="nav-earnings">Earnings</a>
        <a href="#registration" class="nav-link" id="nav-registration">How to Join</a>
        <a href="#faqs" class="nav-link" id="nav-faqs">FAQs</a>

        <div class="mobile-nav-actions">
          <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer" class="btn btn-outline" id="btn-mobile-download">Download BoloUp Go</a>
          <a href="#registration" class="btn btn-primary" id="btn-mobile-agent">Start Your BoloUp Agency</a>
        </div>
      </nav>

      <div class="header-actions">
        <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm" id="btn-header-download">Download App</a>
        <a href="#registration" class="btn btn-primary btn-sm" id="btn-header-agent">Start Agency</a>
        <button type="button" class="menu-toggle" id="menu-toggle" aria-label="Toggle Navigation Menu" aria-expanded="false" aria-controls="nav-menu">&#9776;</button>
      </div>
    </div>
  </header>

  <main>
    <!-- Hero Section -->
    <section class="hero-section" id="hero">
      <div class="container">
        <div class="hero-grid">
          <div class="hero-content">
            <div class="hero-badge">BoloUp Go Official Agency Program</div>
            <h1 class="hero-title">
              Build a Team That Grows with <span class="text-gradient">BoloUp Go Agency</span>
            </h1>
            <p class="hero-desc">
              Turn your network into something bigger. With BoloUp Go Agency, discover promising hosts, bring them into your team, and earn from your agency alongside the host you grow.
            </p>
            <div class="hero-actions">
              <a href="#registration" class="btn btn-primary btn-lg" id="hero-cta-agency">
                Start Your BoloUp Agency
              </a>
              <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-lg" id="hero-btn-download">
                Download BoloUp Go
              </a>
            </div>
          </div>

          <!-- Hero Visual Frame with Floating Elements -->
          <div class="hero-visual" id="hero-visual-agency">
            <div class="hero-glow-backdrop" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-img-wrap">
                <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/boloupgoagency.png' ) ); ?>"
                     alt="Build a Team That Grows with BoloUp Go Agency"
                     class="hero-img"
                     width="1024"
                     height="1536"
                     fetchpriority="high">
              </div>
            </div>

            <!-- Floating 3D Elements -->
            <div class="hero-float-element float-team" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <div class="hero-float-element float-growth" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
                <polyline points="17 6 23 6 23 12"></polyline>
              </svg>
            </div>
            <div class="hero-float-element float-rewards" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="8" width="18" height="12" rx="2"></rect>
                <path d="M12 8v12"></path>
                <path d="M12 8H7.5a2.5 2.5 0 0 1 0-5C11 3 12 8 12 8z"></path>
                <path d="M12 8h4.5a2.5 2.5 0 0 0 0-5C13 3 12 8 12 8z"></path>
              </svg>
            </div>
            <div class="hero-float-element float-star" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- What is boloup go and agency Section -->
    <section class="section section-alt" id="what-is-boloup">
      <div class="container">
        <div class="about-split-grid">
          <div class="about-content-col">
            <div class="section-badge">Platform &amp; Role Overview</div>
            <h2 class="section-title">
              <span class="text-gradient">Live Entertainment</span> Meets Team-Building
            </h2>
            <div class="about-text-paragraphs">
              <p class="about-desc">
                BoloUp Go is a social entertainment app where people meet through live video, voice rooms, chat, virtual gifts, and interactive experiences.
              </p>
              <div class="about-agency-highlight">
                <p class="about-desc">
                  The agency side gives you a different way to take part. Instead of being the person in front of the camera, a BoloUp Go Agency agent works behind the scenes, recruiting hosts, helping them get started, and building a stronger team.
                </p>
              </div>
              <p class="about-desc">
                It’s a role for people who enjoy spotting potential, helping creators, and earning on the side.
              </p>
            </div>
          </div>

          <div class="about-visual-col">
            <div class="about-card-frame">
              <div class="about-img-wrap">
                <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/BoloUp-Ecosystem.png' ) ); ?>"
                     alt="Live Entertainment Meets Team-Building - BoloUp Ecosystem"
                     class="about-img"
                     width="1350"
                     height="860"
                     loading="lazy">
              </div>
              <div class="about-feature-tags">
                <span class="about-tag">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect></svg>
                  Live Video
                </span>
                <span class="about-tag">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
                  Voice Rooms
                </span>
                <span class="about-tag">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                  Real-Time Chat
                </span>
                <span class="about-tag">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 12v10H4V12"></path><rect x="2" y="7" width="20" height="5"></rect><line x1="12" y1="22" x2="12" y2="7"></line></svg>
                  Virtual Gifts
                </span>
                <span class="about-tag">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                  Team-Building
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Benefits Section -->
    <section class="section" id="benefits">
      <div class="container">
        <div class="section-title-wrap">
          <div class="section-badge">Exclusive Agent Advantages</div>
          <h2 class="section-title">
            Why Build Your Own <span class="text-gradient">BoloUp Go Agency?</span>
          </h2>
        </div>

        <div class="benefits-grid">
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
      </div>
    </section>

    <!-- Earnings Section -->
    <section class="section section-alt" id="earnings">
      <div class="container">
        <div class="section-title-wrap">
          <div class="section-badge">Revenue Potential</div>
          <h2 class="section-title">
            How Can a <span class="text-gradient">BoloUp Go Agency</span> Earn?
          </h2>
        </div>

        <div class="earnings-grid">
          <!-- Earning Stream 1 -->
          <article class="earning-card" id="earning-card-1">
            <div class="earning-badge">Direct Revenue</div>
            <div class="earning-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="12" y1="1" x2="12" y2="23"></line>
                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
              </svg>
            </div>
            <h3 class="earning-title">1. Host Performance Commission</h3>
            <p class="earning-desc">
              Agents can earn commission based on eligible activity and income generated by hosts within their agency.
            </p>
          </article>

          <!-- Earning Stream 2 -->
          <article class="earning-card" id="earning-card-2">
            <div class="earning-badge">Network Expansion</div>
            <div class="earning-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="18" cy="5" r="3"></circle>
                <circle cx="6" cy="12" r="3"></circle>
                <circle cx="18" cy="19" r="3"></circle>
                <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line>
                <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
              </svg>
            </div>
            <h3 class="earning-title">2. Network and Sub-Agency Growth</h3>
            <p class="earning-desc">
              Agents may expand their network through sub-agencies and earn the applicable commission structure.
            </p>
          </article>

          <!-- Earning Stream 3 -->
          <article class="earning-card" id="earning-card-3">
            <div class="earning-badge">Bonus Incentives</div>
            <div class="earning-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
              </svg>
            </div>
            <h3 class="earning-title">3. Agency Rewards and Incentives</h3>
            <p class="earning-desc">
              Receive or participate in weekly, monthly, or seasonal events as an agent.
            </p>
          </article>
        </div>

        <div class="earnings-cta-wrap">
          <a href="https://boloupgo.live" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-lg" id="btn-learn-host">
            Learn more about Host [boloupgo.live]
          </a>
        </div>
      </div>
    </section>

    <!-- Registration Section -->
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
                Install BoloUp Go <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer">using this link</a> and create your account using one of the available sign-up methods.
              </p>

              <div class="reg-step-media">
                <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-1.png' ) ); ?>"
                     alt="Step 1 – Download BoloUp Go"
                     width="1080"
                     height="1920"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 2 -->
            <article class="reg-step-card" id="step-2">
              <div class="reg-step-header">
                <span class="reg-step-num">2</span>
                <h3 class="reg-step-title">Step 2 – Complete Your Profile and Verification</h3>
              </div>
              <p class="reg-step-desc">
                Set up your account information and complete face verification when required.
              </p>

              <div class="reg-step-media">
                <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-2.png' ) ); ?>"
                     alt="Step 2 – Complete Your Profile and Verification"
                     width="1080"
                     height="1920"
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
                Use the agency registration link provided to you (contact us for the link) and check the related invitation or notice inside BoloUp.
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
                <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-3.png' ) ); ?>"
                     alt="Step 3 – Open Your Agency Registration Invitation"
                     width="1080"
                     height="1920"
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
                Review the agency information and confirm that you want to continue with the registration.
              </p>

              <div class="reg-step-media">
                <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/BoloUp-Agency-Registration-Step-4.png' ) ); ?>"
                     alt="Step 4 – Accept the Agency Invitation"
                     width="1080"
                     height="1920"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 5 -->
            <article class="reg-step-card" id="step-5">
              <div class="reg-step-header">
                <span class="reg-step-num">5</span>
                <h3 class="reg-step-title">Step 5 – Add Your Agency Details</h3>
              </div>
              <p class="reg-step-desc">
                Enter the requested agency name and contact information carefully before submitting your application.
              </p>

              <div class="reg-step-media">
                <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/boloup-agent-add-new-host-part-1.jpg' ) ); ?>"
                     alt="Step 5 – Add Your Agency Details"
                     width="1080"
                     height="1920"
                     loading="lazy">
              </div>
            </article>

            <!-- Step 6 -->
            <article class="reg-step-card" id="step-6">
              <div class="reg-step-header">
                <span class="reg-step-num">6</span>
                <h3 class="reg-step-title">Step 6 – Complete the Registration Process</h3>
              </div>
              <p class="reg-step-desc">
                Finish any remaining verification or approval steps shown in the app. Once approved, you can access your agency tools and begin building your team.
              </p>

              <div class="reg-step-media">
                <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/BoloUp-Agent-Role.png' ) ); ?>"
                     alt="Step 6 – Complete the Registration Process"
                     width="1350"
                     height="860"
                     loading="lazy">
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQs Section -->
    <section class="section section-alt" id="faqs">
      <div class="container">
        <div class="section-title-wrap">
          <div class="section-badge">Help &amp; Clarification</div>
          <h2 class="section-title">
            Frequently Asked <span class="text-gradient">Questions</span>
          </h2>
        </div>

        <div class="faq-accordion" id="faq-accordion">
          <!-- FAQ 1 -->
          <article class="faq-item active" id="faq-item-1">
            <button type="button" class="faq-question" id="faq-btn-1" aria-expanded="true" aria-controls="faq-ans-1">
              <div class="faq-q-text">
                <span class="faq-q-num">1</span>
                <span>What is a BoloUp Go Agency?</span>
              </div>
              <span class="faq-icon" aria-hidden="true">+</span>
            </button>
            <div class="faq-answer" id="faq-ans-1">
              <div class="faq-answer-inner">
                <p>
                  A BoloUp Go Agency is a team structure that allows agents to recruit, manage, and support hosts on the platform. Instead of focusing mainly on hosting, agents focus on helping their team grow.
                </p>
              </div>
            </div>
          </article>

          <!-- FAQ 2 -->
          <article class="faq-item" id="faq-item-2">
            <button type="button" class="faq-question" id="faq-btn-2" aria-expanded="false" aria-controls="faq-ans-2">
              <div class="faq-q-text">
                <span class="faq-q-num">2</span>
                <span>What does a BoloUp Go agent actually do?</span>
              </div>
              <span class="faq-icon" aria-hidden="true">+</span>
            </button>
            <div class="faq-answer" id="faq-ans-2">
              <div class="faq-answer-inner">
                <p>
                  An agent looks for potential hosts, helps them join the agency, provides ongoing guidance, and supports their development. Managing a healthy and active host team is a key part of the role.
                </p>
              </div>
            </div>
          </article>

          <!-- FAQ 3 -->
          <article class="faq-item" id="faq-item-3">
            <button type="button" class="faq-question" id="faq-btn-3" aria-expanded="false" aria-controls="faq-ans-3">
              <div class="faq-q-text">
                <span class="faq-q-num">3</span>
                <span>How does a BoloUp Go Agency make money?</span>
              </div>
              <span class="faq-icon" aria-hidden="true">+</span>
            </button>
            <div class="faq-answer" id="faq-ans-3">
              <div class="faq-answer-inner">
                <p>
                  Agency earnings can be linked to eligible host activity, commissions, network performance, and other rewards available under the current BoloUp agency program. Actual earnings depend on performance and applicable program rules.
                </p>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Final CTA Section -->
    <section class="section cta-section-wrapper" id="cta">
      <div class="container">
        <div class="cta-banner-epic">
          <div class="cta-glow-element top-left" aria-hidden="true"></div>
          <div class="cta-glow-element bottom-right" aria-hidden="true"></div>
          <div class="cta-content-inner">
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
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer Component -->
  <footer class="footer" id="footer">
    <div class="container">
      <div class="footer-grid">
        <!-- Brand Overview -->
        <div class="footer-brand">
          <a href="#hero" class="brand-logo" id="footer-brand-logo" aria-label="BoloUp Go Agency Home">
            <img src="<?php echo esc_url( home_url( '/wp-content/uploads/2026/11/boloup-header-logo.png' ) ); ?>"
                 alt="BoloUp Go Official Logo"
                 class="brand-logo-icon"
                 width="117"
                 height="64"
                 loading="lazy">
            <span class="brand-badge">Agency</span>
          </a>
          <p class="footer-desc">
            BoloUp Go is a social entertainment app where people meet through live video, voice rooms, chat, virtual gifts, and interactive experiences. Turn your network into something bigger and grow your team with BoloUp Go Agency.
          </p>
        </div>

        <!-- Quick Sections -->
        <div class="footer-col">
          <h3>Navigation</h3>
          <ul class="footer-links">
            <li><a href="#hero">Home</a></li>
            <li><a href="#what-is-boloup">About BoloUp Go</a></li>
            <li><a href="#benefits">Agency Benefits</a></li>
            <li><a href="#earnings">How Agents Earn</a></li>
          </ul>
        </div>

        <!-- Agency & Host Resources -->
        <div class="footer-col">
          <h3>Agency Program</h3>
          <ul class="footer-links">
            <li><a href="#registration">How to Join Agency</a></li>
            <li><a href="#faqs">Frequently Asked Questions</a></li>
            <li><a href="https://boloupgo.live" target="_blank" rel="noopener noreferrer">Host Program [boloupgo.live]</a></li>
            <li><a href="https://boloup.id" target="_blank" rel="noopener noreferrer">BoloUp Official Website</a></li>
          </ul>
        </div>

        <!-- Platform Links -->
        <div class="footer-col">
          <h3>BoloUp App</h3>
          <ul class="footer-links">
            <li><a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer">Download BoloUp Go App</a></li>
            <li><a href="#registration">Agency ID: 2527626</a></li>
            <li><a href="https://boloup.onelink.me/PDV4/je5ueb58" target="_blank" rel="noopener noreferrer">Alternative Download Link</a></li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom">
        <div>&copy; 2026 BoloUp Go Agency (boloupgoagency.com). All rights reserved.</div>
        <div>Build, Manage &amp; Grow Your Team from Everywhere</div>
      </div>
    </div>
  </footer>

  <!-- Image Lightbox Modal Component -->
  <div class="lightbox-modal" id="lightbox-modal" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Image Preview">
    <div class="lightbox-backdrop" id="lightbox-backdrop"></div>
    <div class="lightbox-content">
      <button type="button" class="lightbox-close" id="lightbox-close" aria-label="Close image preview">&times;</button>
      <div class="lightbox-image-wrap">
        <img src="" alt="" class="lightbox-img" id="lightbox-img">
      </div>
      <div class="lightbox-caption" id="lightbox-caption"></div>
    </div>
  </div>

  <!-- Internal JavaScript at the end of body -->
  <script>
    (function () {
      // Header scroll blur
      const header = document.getElementById('header');
      if (header) {
        window.addEventListener('scroll', function () {
          if (window.scrollY > 20) {
            header.classList.add('header-scrolled');
          } else {
            header.classList.remove('header-scrolled');
          }
        });
      }

      // Mobile Menu Drawer
      const menuToggle = document.getElementById('menu-toggle');
      const navMenu = document.getElementById('nav-menu');
      if (menuToggle && navMenu) {
        function toggleMenu(open) {
          const shouldOpen = open !== undefined ? open : !navMenu.classList.contains('active');
          navMenu.classList.toggle('active', shouldOpen);
          menuToggle.textContent = shouldOpen ? '\u2715' : '\u2630';
          menuToggle.setAttribute('aria-expanded', shouldOpen ? 'true' : 'false');
        }

        menuToggle.addEventListener('click', function (e) {
          e.stopPropagation();
          toggleMenu();
        });

        document.addEventListener('click', function (e) {
          if (!navMenu.contains(e.target) && !menuToggle.contains(e.target)) {
            toggleMenu(false);
          }
        });

        navMenu.querySelectorAll('a').forEach(function (link) {
          link.addEventListener('click', function () {
            toggleMenu(false);
          });
        });

        document.addEventListener('keydown', function (e) {
          if (e.key === 'Escape' && navMenu.classList.contains('active')) {
            toggleMenu(false);
          }
        });
      }

      // Active state highlighting on scroll
      const sections = document.querySelectorAll('section[id]');
      const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
      window.addEventListener('scroll', function () {
        let current = '';
        const scrollY = window.pageYOffset;
        sections.forEach(function (section) {
          const sectionTop = section.offsetTop - 120;
          const sectionHeight = section.offsetHeight;
          if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
            current = section.getAttribute('id');
          }
        });

        navLinks.forEach(function (link) {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + current) {
            link.classList.add('active');
          }
        });
      });

      // FAQ Accordion Handler
      const faqItems = document.querySelectorAll('.faq-item');
      faqItems.forEach(function (item) {
        const btn = item.querySelector('.faq-question');
        const ans = item.querySelector('.faq-answer');
        if (btn && ans) {
          if (item.classList.contains('active')) {
            ans.style.maxHeight = ans.scrollHeight + 'px';
          }

          btn.addEventListener('click', function () {
            const isActive = item.classList.contains('active');

            // Close all items
            faqItems.forEach(function (otherItem) {
              otherItem.classList.remove('active');
              const otherBtn = otherItem.querySelector('.faq-question');
              const otherAns = otherItem.querySelector('.faq-answer');
              if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
              if (otherAns) otherAns.style.maxHeight = null;
            });

            // Toggle current item
            if (!isActive) {
              item.classList.add('active');
              btn.setAttribute('aria-expanded', 'true');
              ans.style.maxHeight = ans.scrollHeight + 'px';
            }
          });
        }
      });

      // Agency ID Copy Handler
      const copyBtn = document.getElementById('btn-copy-agency-id');
      const copyText = document.getElementById('copy-btn-text');
      const copyToast = document.getElementById('copy-toast');
      if (copyBtn && copyText) {
        copyBtn.addEventListener('click', function () {
          const code = '2527626';
          function showSuccess() {
            copyBtn.classList.add('copied');
            copyText.textContent = 'Copied!';
            if (copyToast) copyToast.classList.add('show');
            setTimeout(function () {
              copyBtn.classList.remove('copied');
              copyText.textContent = 'Copy Agency ID';
              if (copyToast) copyToast.classList.remove('show');
            }, 3000);
          }

          if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(code).then(showSuccess).catch(function () {
              fallbackCopy();
            });
          } else {
            fallbackCopy();
          }

          function fallbackCopy() {
            try {
              const textArea = document.createElement('textarea');
              textArea.value = code;
              textArea.style.position = 'fixed';
              textArea.style.left = '-9999px';
              textArea.style.top = '0';
              document.body.appendChild(textArea);
              textArea.focus();
              textArea.select();
              const successful = document.execCommand('copy');
              document.body.removeChild(textArea);
              if (successful) showSuccess();
            } catch (err) {
              copyText.textContent = code;
            }
          }
        });
      }

      // Lightbox Modal Functionality
      var lightbox = document.getElementById('lightbox-modal');
      var lightboxImg = document.getElementById('lightbox-img');
      var lightboxCaption = document.getElementById('lightbox-caption');
      var lightboxClose = document.getElementById('lightbox-close');
      var lightboxBackdrop = document.getElementById('lightbox-backdrop');

      function openLightbox(src, alt) {
        if (!lightbox || !lightboxImg) return;
        lightboxImg.src = src;
        lightboxImg.alt = alt || '';
        if (lightboxCaption) {
          lightboxCaption.textContent = alt || '';
        }
        lightbox.classList.add('active');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }

      function closeLightbox() {
        if (!lightbox) return;
        lightbox.classList.remove('active');
        lightbox.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        if (lightboxImg) lightboxImg.src = '';
      }

      if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
      if (lightboxBackdrop) lightboxBackdrop.addEventListener('click', closeLightbox);

      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && lightbox && lightbox.classList.contains('active')) {
          closeLightbox();
        }
      });

      // Attach click handlers to registration media images and ecosystem images
      document.querySelectorAll('.reg-step-media, .about-img-wrap').forEach(function (frame) {
        frame.addEventListener('click', function () {
          var img = frame.querySelector('img');
          if (img) {
            openLightbox(img.currentSrc || img.src, img.alt);
          }
        });
      });
    })();
  </script>
<?php wp_footer(); ?>
</body>
</html>
