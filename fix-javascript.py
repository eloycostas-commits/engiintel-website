#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the script section
old_script_start = content.find('<script>')
old_script_end = content.find('</script>') + len('</script>')

if old_script_start == -1:
    print("ERROR: Could not find <script> tag")
    exit(1)

new_script = '''<script>
let currentLang = 'en';

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
  document.getElementById(tabId).classList.add('active');
  
  // Add active class to corresponding tab button
  const targetBtn = document.querySelector(`[onclick="switchTab('${tabId}')"]`);
  if (targetBtn) {
    targetBtn.classList.add('active');
  }
  
  // Scroll to tabs container
  document.querySelector('.tabs-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Form submission handler
document.addEventListener('DOMContentLoaded', () => {
  setLang('en');
  
  // Handle contact form submission
  const contactForm = document.querySelector('.contact-form');
  if (contactForm) {
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
});
</script>'''

# Replace the script section
content = content[:old_script_start] + new_script + content[old_script_end:]

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Fixed switchTab function")
print("✓ Added form submission handler")
print("✓ Form will now send data to n8n webhook at http://localhost:5678/webhook/contact-form")
