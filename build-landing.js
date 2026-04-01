/**
 * Build script to combine modular components into single HTML file
 * This allows us to edit small component files but deploy a single HTML
 */

const fs = require('fs');
const path = require('path');

// Read all component files
const components = {
  header: fs.readFileSync('components/header.html', 'utf8'),
  hero: fs.readFileSync('components/hero.html', 'utf8'),
  tabs: fs.readFileSync('components/tabs.html', 'utf8'),
  'overview-tab': fs.readFileSync('components/overview-tab.html', 'utf8'),
  'features-tab': fs.readFileSync('components/features-tab.html', 'utf8'),
  'document-intelligence-tab': fs.readFileSync('components/document-intelligence-tab.html', 'utf8'),
  'excel-copilot-tab': fs.readFileSync('components/excel-copilot-tab.html', 'utf8'),
  'wiki-tab': fs.readFileSync('components/wiki-tab.html', 'utf8'),
  'assets-tab': fs.readFileSync('components/assets-tab.html', 'utf8'),
  'incidents-tab': fs.readFileSync('components/incidents-tab.html', 'utf8'),
  'ai-agent-tab': fs.readFileSync('components/ai-agent-tab.html', 'utf8'),
  'industries-tab': fs.readFileSync('components/industries-tab.html', 'utf8'),
  'pricing-tab': fs.readFileSync('components/pricing-tab.html', 'utf8'),
  'resources-tab': fs.readFileSync('components/resources-tab.html', 'utf8'),
  footer: fs.readFileSync('components/footer.html', 'utf8')
};

// Read CSS and JS
const css = fs.readFileSync('css/styles.css', 'utf8');
const js = fs.readFileSync('js/app.js', 'utf8');

// Build the complete HTML
const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EngiIntel — AI Document Intelligence for Regulated Industries</title>
  <meta name="description" content="Self-hosted AI platform for regulated industries. Query regulations, manage knowledge base, track assets, generate incident reports, automate workflows with n8n and run autonomous AI agents.">
  <meta name="keywords" content="AI document intelligence, engineering knowledge base, RAG, self-hosted AI, regulated industries, elevator regulations, incident reports, asset registry, AI agent, on-premise AI">
  <link rel="canonical" href="https://engiintel.com/">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-5P3VL8DTRG"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-5P3VL8DTRG');
  </script>
  
  <style>
${css}
  </style>
</head>
<body>
${components.header}
${components.hero}
${components.tabs}
${components['overview-tab']}
${components['features-tab']}
${components['document-intelligence-tab']}
${components['excel-copilot-tab']}
${components['wiki-tab']}
${components['assets-tab']}
${components['incidents-tab']}
${components['ai-agent-tab']}
${components['industries-tab']}
${components['pricing-tab']}
${components['resources-tab']}
${components.footer}

<!-- GDPR Banner -->
<div id="gdpr-banner" style="position: fixed; bottom: 0; left: 0; right: 0; background: var(--surface2); border-top: 2px solid var(--accent); padding: 24px; z-index: 1000; display: none;">
  <div style="max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 300px;">
      <p style="font-size: 0.9rem; color: var(--text); margin: 0;" data-en="We use cookies to improve your experience and analyze site usage. By continuing to use this site, you consent to our use of cookies." data-es="Usamos cookies para mejorar tu experiencia y analizar el uso del sitio. Al continuar usando este sitio, consientes nuestro uso de cookies.">
        We use cookies to improve your experience and analyze site usage. By continuing to use this site, you consent to our use of cookies.
      </p>
      <a href="privacy-policy.html" style="color: var(--accent); font-size: 0.85rem; text-decoration: none;" data-en="Learn more" data-es="Más información">Learn more</a>
    </div>
    <div style="display: flex; gap: 12px;">
      <button onclick="acceptCookies()" style="background: var(--accent); color: var(--bg); border: none; padding: 12px 24px; font-family: 'Syne', sans-serif; font-weight: 600; font-size: 0.85rem; cursor: pointer; transition: all 0.2s;" data-en="Accept" data-es="Aceptar">Accept</button>
      <button onclick="declineCookies()" style="background: transparent; color: var(--text-mid); border: 1px solid var(--border); padding: 12px 24px; font-family: 'Syne', sans-serif; font-weight: 600; font-size: 0.85rem; cursor: pointer; transition: all 0.2s;" data-en="Decline" data-es="Rechazar">Decline</button>
    </div>
  </div>
</div>

<script>
${js}
</script>
</body>
</html>
`;

// Create public directory if it doesn't exist
if (!fs.existsSync('public')) {
  fs.mkdirSync('public');
}

// Write the built file to both root and public
fs.writeFileSync('index.html', html, 'utf8');
fs.writeFileSync('public/index.html', html, 'utf8');
console.log('✅ Built index.html from components');
console.log(`   Size: ${Math.round(html.length / 1024)}KB`);
console.log(`   Components: ${Object.keys(components).length}`);
