#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Read the calculator HTML from the old backup
with open('index-old-backup.html', 'r', encoding='utf-8') as f:
    backup_content = f.read()

# Extract calculator HTML from backup (just the div, not the surrounding content)
calc_start = backup_content.find('<div class="pricing-calc fade-in">')
calc_end = backup_content.find('</div>\n  </div>\n\n  <!-- Tier reference cards -->')
calculator_html = backup_content[calc_start:calc_end + 13]  # Include the closing </div></div>

# Find the pricing section and insert calculator
new_lines = []
in_pricing = False
pricing_sub_found = False

for i, line in enumerate(lines):
    new_lines.append(line)
    
    # Check if we're in the pricing section
    if '<div id="pricing" class="tab-content">' in line:
        in_pricing = True
    
    # After the section-sub paragraph, insert the calculator
    if in_pricing and not pricing_sub_found and '</p>' in line and 'section-sub' in lines[i-1] if i > 0 else False:
        pricing_sub_found = True
        new_lines.append('\n  ' + calculator_html + '\n\n')

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.writelines(new_lines)

print("✓ Added calculator HTML")

# Now add CSS
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

css_to_add = '''
/* MODULE PRICING CALCULATOR */
.pricing-calc { border: 1px solid var(--border); background: var(--surface); margin-bottom: 48px; overflow: hidden; }
.calc-header { padding: 28px 36px; border-bottom: 1px solid var(--border); background: var(--surface2); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; }
.calc-header-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1rem; }
.calc-header-sub { font-family: 'DM Mono', monospace; font-size: 0.72rem; color: var(--text-dim); letter-spacing: 0.04em; }
.calc-body { display: grid; grid-template-columns: 1fr 300px; }
.calc-left { padding: 28px 36px; border-right: 1px solid var(--border); }
.calc-right { padding: 28px 28px; display: flex; flex-direction: column; gap: 0; }
.calc-section-label { font-family: 'DM Mono', monospace; font-size: 0.68rem; color: var(--accent); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 14px; }
.calc-seats { display: flex; align-items: center; gap: 12px; margin-bottom: 28px; }
.calc-seats-label { font-size: 0.88rem; color: var(--text-mid); min-width: 60px; }
.seats-input { background: var(--bg); border: 1px solid var(--border); color: var(--text); font-family: 'DM Mono', monospace; font-size: 1rem; padding: 8px 14px; width: 80px; text-align: center; appearance: none; -moz-appearance: textfield; }
.seats-input::-webkit-inner-spin-button { display: none; }
.seats-btn { width: 32px; height: 32px; background: var(--surface2); border: 1px solid var(--border); color: var(--text-mid); font-size: 1.1rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.15s; font-family: 'DM Mono', monospace; }
.seats-btn:hover { border-color: var(--accent); color: var(--accent); }
.calc-modules-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.calc-module-toggle { border: 1px solid var(--border); padding: 14px 16px; cursor: pointer; transition: all 0.2s; background: var(--bg); display: flex; align-items: center; justify-content: space-between; gap: 8px; user-select: none; }
.calc-module-toggle:hover { border-color: rgba(0,212,255,0.3); }
.calc-module-toggle.selected { border-color: var(--accent); background: rgba(0,212,255,0.05); }
.calc-module-toggle.core-mod { border-color: rgba(0,212,255,0.4); background: rgba(0,212,255,0.04); cursor: default; }
.calc-mod-name { font-family: 'Syne', sans-serif; font-weight: 600; font-size: 0.82rem; color: var(--text); }
.calc-mod-icon { font-size: 1rem; flex-shrink: 0; }
.calc-mod-check { width: 18px; height: 18px; border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; font-size: 0.7rem; flex-shrink: 0; color: var(--accent3); transition: all 0.15s; }
.calc-module-toggle.selected .calc-mod-check { background: var(--accent3); color: var(--bg); border-color: var(--accent3); }
.calc-module-toggle.core-mod .calc-mod-check { background: var(--accent); color: var(--bg); border-color: var(--accent); }
.calc-summary-line { display: flex; justify-content: space-between; align-items: baseline; padding: 10px 0; border-bottom: 1px solid var(--border); }
.calc-summary-line:last-of-type { border-bottom: none; }
.calc-summary-key { font-family: 'DM Mono', monospace; font-size: 0.72rem; color: var(--text-dim); letter-spacing: 0.04em; }
.calc-summary-val { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.9rem; color: var(--text); }
.calc-total-row { margin-top: 20px; padding-top: 20px; border-top: 2px solid var(--accent); display: flex; justify-content: space-between; align-items: baseline; }
.calc-total-label { font-family: 'DM Mono', monospace; font-size: 0.72rem; color: var(--accent); letter-spacing: 0.1em; text-transform: uppercase; }
.calc-total-price { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 2rem; color: var(--accent); line-height: 1; }
.calc-total-period { font-family: 'DM Mono', monospace; font-size: 0.65rem; color: var(--text-dim); }
.calc-cta { display: block; text-align: center; padding: 13px; background: var(--accent2); color: white; font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.82rem; letter-spacing: 0.05em; text-decoration: none; text-transform: uppercase; margin-top: 20px; transition: all 0.2s; border: none; cursor: pointer; width: 100%; }
.calc-cta:hover { background: #0055dd; box-shadow: 0 0 20px rgba(0,102,255,0.35); }
.calc-note { font-family: 'DM Mono', monospace; font-size: 0.65rem; color: var(--text-dim); text-align: center; margin-top: 10px; line-height: 1.5; }

@media (max-width: 768px) {
  .calc-body { grid-template-columns: 1fr; }
  .calc-left { border-right: none; border-bottom: 1px solid var(--border); }
  .calc-modules-grid { grid-template-columns: 1fr; }
  .calc-header { padding: 20px; }
  .calc-left, .calc-right { padding: 20px; }
}
'''

# Find </style> and add CSS before it
style_end_pos = content.find('</style>')
if style_end_pos != -1:
    content = content[:style_end_pos] + css_to_add + '\n' + content[style_end_pos:]
    print("✓ Added calculator CSS")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

# Now add JavaScript
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_to_add = '''
<script>
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
  document.querySelectorAll('.tab-content').forEach(content => {
    content.classList.remove('active');
  });
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  const targetTab = document.getElementById(tabId);
  if (targetTab) {
    targetTab.classList.add('active');
    event.target.classList.add('active');
    document.querySelector('.tabs-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Pricing calculator
const CORE_PER_SEAT = 8;
const MODULE_PRICE_PER_SEAT = 4;
const selected = new Set();

function toggleMod(id){
  const el=document.getElementById('mod-'+id), chk=document.getElementById('chk-'+id);
  if(selected.has(id)){ selected.delete(id); el.classList.remove('selected'); chk.textContent=''; }
  else { selected.add(id); el.classList.add('selected'); chk.textContent='✓'; }
  calcPrice();
}

function adjustSeats(delta){
  const inp=document.getElementById('seatsInput');
  const v=Math.max(1,Math.min(500,(parseInt(inp.value)||1)+delta));
  inp.value=v; calcPrice();
}

function calcPrice(){
  const seats=Math.max(1,parseInt(document.getElementById('seatsInput').value)||1);
  const modCount=selected.size;
  const pricePerSeat=CORE_PER_SEAT+(modCount*MODULE_PRICE_PER_SEAT);
  let subtotal=pricePerSeat*seats;
  let discountPct=0;
  if(seats>=50) discountPct=20;
  else if(seats>=25) discountPct=15;
  else if(seats>=15) discountPct=10;
  const discount=Math.round(subtotal*discountPct/100);
  const total=subtotal-discount;

  document.getElementById('calcTotal').textContent='€'+total;
  document.getElementById('sum-seats-val').textContent=seats;

  const modRow=document.getElementById('sum-modules-row');
  if(modCount>0){
    modRow.style.display='flex';
    const isEs=currentLang==='es';
    document.getElementById('sum-modules-label').textContent='+ '+modCount+(isEs?' módulo'+(modCount>1?'s':'')+' · por seat':' module'+(modCount>1?'s':'')+' · per seat');
    document.getElementById('sum-modules-val').textContent='€'+(modCount*MODULE_PRICE_PER_SEAT)+'/seat';
  } else { modRow.style.display='none'; }

  const discRow=document.getElementById('sum-discount-row');
  if(discount>0){
    discRow.style.display='flex';
    const isEs=currentLang==='es';
    document.getElementById('sum-discount-label').textContent=(isEs?'Descuento volumen':'Volume discount')+' ('+discountPct+'%)';
    document.getElementById('sum-discount-val').textContent='−€'+discount;
  } else { discRow.style.display='none'; }

  const note=document.getElementById('calcNote');
  const isEs=currentLang==='es';
  if(discountPct>0) note.textContent=(isEs?'Descuento '+discountPct+'% por volumen aplicado':'Volume discount '+discountPct+'% applied');
  else note.textContent=isEs?'On-premise · sin coste por consulta · instalación Docker':'On-premise · no per-query costs · Docker install';
}

// Contact form submission
document.addEventListener('DOMContentLoaded', () => {
  setLang('en');
  
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.textContent = currentLang === 'es' ? 'Enviando...' : 'Sending...';
      
      const formData = {
        name: form.name.value,
        email: form.email.value,
        company: form.company.value || '',
        industry: form.industry.value || '',
        interests: Array.from(form.querySelectorAll('input[name="interests"]:checked')).map(cb => cb.value),
        message: form.message.value || '',
        language: currentLang,
        timestamp: new Date().toISOString()
      };
      
      try {
        // Send directly to Resend API
        const response = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer re_43jiWP48_3vxjr9PnCFKBaQCrY4UvdJNJ'
          },
          body: JSON.stringify({
            from: 'EngiIntel Website <onboarding@resend.dev>',
            to: ['eloycostas@engiintel.com'],
            subject: `New Contact Form Submission from ${formData.name}`,
            html: `
              <h2>New Contact Form Submission</h2>
              <p><strong>Name:</strong> ${formData.name}</p>
              <p><strong>Email:</strong> ${formData.email}</p>
              <p><strong>Company:</strong> ${formData.company}</p>
              <p><strong>Industry:</strong> ${formData.industry}</p>
              <p><strong>Interests:</strong> ${formData.interests.join(', ')}</p>
              <p><strong>Message:</strong></p>
              <p>${formData.message}</p>
              <p><strong>Language:</strong> ${formData.language}</p>
              <p><strong>Timestamp:</strong> ${formData.timestamp}</p>
            `
          })
        });
        
        if (response.ok) {
          alert(currentLang === 'es' 
            ? '¡Gracias! Tu mensaje ha sido enviado. Te contactaremos pronto.' 
            : 'Thank you! Your message has been sent. We will contact you soon.');
          form.reset();
        } else {
          throw new Error('Server error');
        }
      } catch (error) {
        console.error('Form submission error:', error);
        alert(currentLang === 'es'
          ? 'Error al enviar el formulario. Por favor, intenta de nuevo o contacta directamente a eloycostas@engiintel.com'
          : 'Error sending form. Please try again or contact directly at eloycostas@engiintel.com');
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    });
  }
});
</script>
'''

# Add CSS before </style>
style_end = content.find('</style>')
if style_end != -1 and '.calc-header' not in content:
    content = content[:style_end] + css_to_add + '\n' + content[style_end:]
    print("✓ Added calculator CSS")

# Add JavaScript before </body>
body_end = content.find('</body>')
if body_end != -1 and 'function toggleMod' not in content:
    content = content[:body_end] + js_to_add + '\n' + content[body_end:]
    print("✓ Added calculator JavaScript and form handler")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Complete! Calculator and form handler added")
print("✓ Form sends to: eloycostas@engiintel.com")
