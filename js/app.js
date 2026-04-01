/**
 * EngiIntel Website - Main Application
 * Component loader and core functionality
 */

// Global state
let currentLang = 'en';
const CORE_PER_SEAT = 8;
const MODULE_PRICE_PER_SEAT = 4;
const ALL_MODULES = ['ops','excel','wiki','incidents','agent','analytics'];
const selected = new Set();

// Component loader
async function loadComponent(componentPath, containerId) {
  try {
    const response = await fetch(componentPath);
    if (!response.ok) throw new Error(`Failed to load ${componentPath}`);
    const html = await response.text();
    document.getElementById(containerId).innerHTML = html;
    return true;
  } catch (error) {
    console.error(`Error loading component ${componentPath}:`, error);
    return false;
  }
}

// Load all components
async function loadAllComponents() {
  const components = [
    { path: 'components/header.html', container: 'header-container' },
    { path: 'components/hero.html', container: 'hero-container' },
    { path: 'components/tabs.html', container: 'tabs-container' },
    { path: 'components/overview-tab.html', container: 'overview-tab-container' },
    { path: 'components/features-tab.html', container: 'features-tab-container' },
    { path: 'components/document-intelligence-tab.html', container: 'document-intelligence-tab-container' },
    { path: 'components/excel-copilot-tab.html', container: 'excel-copilot-tab-container' },
    { path: 'components/wiki-tab.html', container: 'wiki-tab-container' },
    { path: 'components/assets-tab.html', container: 'assets-tab-container' },
    { path: 'components/incidents-tab.html', container: 'incidents-tab-container' },
    { path: 'components/ai-agent-tab.html', container: 'ai-agent-tab-container' },
    { path: 'components/industries-tab.html', container: 'industries-tab-container' },
    { path: 'components/pricing-tab.html', container: 'pricing-tab-container' },
    { path: 'components/resources-tab.html', container: 'resources-tab-container' },
    { path: 'components/footer.html', container: 'footer-container' }
  ];

  // Load all components in parallel
  const results = await Promise.all(
    components.map(c => loadComponent(c.path, c.container))
  );

  // Check if all loaded successfully
  if (results.every(r => r)) {
    document.getElementById('loading').style.display = 'none';
    initializeApp();
  } else {
    document.getElementById('loading').textContent = 'Error loading components. Please refresh.';
  }
}

// Initialize app after components load
function initializeApp() {
  setLang('en');
  showGDPRBanner();
  calcPrice(); // Initialize pricing calculator
}

// Language switching
function setLang(lang) {
  currentLang = lang;
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.textContent.toLowerCase() === lang);
  });

  document.querySelectorAll('[data-en]').forEach(el => {
    const text = el.getAttribute(`data-${lang}`);
    if (text) {
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.placeholder = text;
      } else {
        el.innerHTML = text;
      }
    }
  });
}

// Tab switching
function switchTab(tabId) {
  // Remove active class from all tab contents
  document.querySelectorAll('.tab-content').forEach(content => {
    content.classList.remove('active');
  });

  // Remove active class from all tab buttons
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('active');
  });

  // Add active class to selected tab content
  const tabElement = document.getElementById(tabId);
  if (tabElement) {
    tabElement.classList.add('active');
  }
  
  // Add active class to corresponding tab button
  const targetBtn = document.querySelector(`[onclick="switchTab('${tabId}')"]`);
  if (targetBtn) {
    targetBtn.classList.add('active');
  }
  
  // Scroll to tabs container
  const tabsContainer = document.querySelector('.tabs-container');
  if (tabsContainer) {
    tabsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Pricing calculator functions
function toggleMod(id) {
  const el = document.getElementById('mod-'+id);
  const chk = document.getElementById('chk-'+id);
  
  if (selected.has(id)) {
    selected.delete(id);
    el.classList.remove('selected');
    chk.textContent = '';
  } else {
    selected.add(id);
    el.classList.add('selected');
    chk.textContent = '✓';
  }
  calcPrice();
}

function adjustSeats(delta) {
  const inp = document.getElementById('seatsInput');
  const v = Math.max(1, Math.min(500, (parseInt(inp.value) || 1) + delta));
  inp.value = v;
  calcPrice();
}

function calcPrice() {
  const seatsInput = document.getElementById('seatsInput');
  if (!seatsInput) return; // Not on pricing page yet
  
  const seats = Math.max(1, parseInt(seatsInput.value) || 1);
  const modCount = selected.size;
  const pricePerSeat = CORE_PER_SEAT + (modCount * MODULE_PRICE_PER_SEAT);
  let subtotal = pricePerSeat * seats;
  let discountPct = 0;
  
  if (seats >= 50) discountPct = 20;
  else if (seats >= 25) discountPct = 15;
  else if (seats >= 15) discountPct = 10;
  
  const discount = Math.round(subtotal * discountPct / 100);
  const total = subtotal - discount;

  document.getElementById('calcTotal').textContent = '€' + total;
  document.getElementById('sum-seats-val').textContent = seats;

  const modRow = document.getElementById('sum-modules-row');
  if (modCount > 0) {
    modRow.style.display = 'flex';
    const isEs = currentLang === 'es';
    document.getElementById('sum-modules-label').textContent = '+ ' + modCount + (isEs ? ' módulo' + (modCount > 1 ? 's' : '') + ' · por seat' : ' module' + (modCount > 1 ? 's' : '') + ' · per seat');
    document.getElementById('sum-modules-val').textContent = '€' + (modCount * MODULE_PRICE_PER_SEAT) + '/seat';
  } else {
    modRow.style.display = 'none';
  }

  const discRow = document.getElementById('sum-discount-row');
  if (discount > 0) {
    discRow.style.display = 'flex';
    const isEs = currentLang === 'es';
    document.getElementById('sum-discount-label').textContent = (isEs ? 'Descuento volumen' : 'Volume discount') + ' (' + discountPct + '%)';
    document.getElementById('sum-discount-val').textContent = '−€' + discount;
  } else {
    discRow.style.display = 'none';
  }

  const note = document.getElementById('calcNote');
  const isEs = currentLang === 'es';
  if (discountPct > 0) {
    note.textContent = (isEs ? 'Descuento ' + discountPct + '% por volumen aplicado' : 'Volume discount ' + discountPct + '% applied');
  } else {
    note.textContent = isEs ? 'On-premise · sin coste por consulta · instalación Docker' : 'On-premise · no per-query costs · Docker install';
  }
}

// Contact form handler
function initContactForm() {
  const contactForm = document.querySelector('.contact-form');
  if (!contactForm) return;
  
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const submitBtn = contactForm.querySelector('.form-submit');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = currentLang === 'en' ? 'Sending...' : 'Enviando...';
    submitBtn.disabled = true;
    
    // Collect form data
    const formData = {
      name: contactForm.querySelector('#name').value,
      email: contactForm.querySelector('#email').value,
      company: contactForm.querySelector('#company').value,
      industry: contactForm.querySelector('#industry').value,
      interests: Array.from(contactForm.querySelectorAll('input[name="interest"]:checked')).map(cb => cb.value),
      message: contactForm.querySelector('#message').value,
      language: currentLang,
      timestamp: new Date().toISOString()
    };
    
    try {
      // Send to n8n webhook
      const response = await fetch('http://localhost:5678/webhook/contact-form', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });
      
      if (response.ok) {
        alert(currentLang === 'en' 
          ? 'Thank you! Your message has been sent successfully. We will contact you soon.' 
          : '¡Gracias! Tu mensaje ha sido enviado exitosamente. Te contactaremos pronto.');
        contactForm.reset();
      } else {
        throw new Error('Failed to send message');
      }
    } catch (error) {
      console.error('Form submission error:', error);
      alert(currentLang === 'en'
        ? 'Sorry, there was an error sending your message. Please try again or email us directly at eloycostas@engiintel.com'
        : 'Lo sentimos, hubo un error al enviar tu mensaje. Por favor intenta de nuevo o envíanos un email directamente a eloycostas@engiintel.com');
    } finally {
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }
  });
}

// GDPR Cookie Consent
function showGDPRBanner() {
  const consent = localStorage.getItem('gdpr-consent');
  if (!consent) {
    document.getElementById('gdpr-banner').style.display = 'block';
  }
}

function acceptCookies() {
  localStorage.setItem('gdpr-consent', 'accepted');
  document.getElementById('gdpr-banner').style.display = 'none';
}

function declineCookies() {
  localStorage.setItem('gdpr-consent', 'declined');
  document.getElementById('gdpr-banner').style.display = 'none';
  // Disable Google Analytics if declined
  window['ga-disable-G-5P3VL8DTRG'] = true;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  loadAllComponents();
});

// Re-initialize form after components load
window.addEventListener('load', () => {
  setTimeout(initContactForm, 500);
});
