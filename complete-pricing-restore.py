#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace pricing section HTML
pricing_start = content.find('<div id="pricing" class="tab-content">')
pricing_end = content.find('</div>\n\n\n<div id="resources"', pricing_start)

new_pricing_html = '''<div id="pricing" class="tab-content">
  <div class="section-label" data-en="Pricing" data-es="Precios">Pricing</div>
  <h2 data-en="Scales with your team.<br>Not with your queries." data-es="Escala con tu equipo.<br>No con tus consultas.">Scales with your team.<br>Not with your queries.</h2>
  <p class="section-sub" data-en="Core is always included. Add only the modules your team actually uses — the calculator below shows your exact price." data-es="El Core siempre está incluido. Añade solo los módulos que tu equipo realmente usa — la calculadora muestra tu precio exacto.">Core is always included. Add only the modules your team actually uses — the calculator below shows your exact price.</p>

  <!-- Interactive pricing calculator -->
  <div class="pricing-calc fade-in">
    <div class="calc-header">
      <div>
        <div class="calc-header-title" data-en="Configure your plan" data-es="Configura tu plan">Configure your plan</div>
        <div class="calc-header-sub" data-en="Select seats and modules — price updates in real time" data-es="Selecciona seats y módulos — el precio se actualiza en tiempo real">Select seats and modules — price updates in real time</div>
      </div>
    </div>
    <div class="calc-body">
      <div class="calc-left">
        <div class="calc-section-label" data-en="Number of seats" data-es="Número de seats">Number of seats</div>
        <div class="calc-seats">
          <button class="seats-btn" onclick="adjustSeats(-1)">−</button>
          <input class="seats-input" type="number" id="seatsInput" value="5" min="1" max="500" oninput="calcPrice()">
          <button class="seats-btn" onclick="adjustSeats(1)">+</button>
          <span class="calc-seats-label" style="font-family:'DM Mono',monospace;font-size:0.72rem;color:var(--text-dim)" data-en="users" data-es="usuarios">users</span>
        </div>

        <div class="calc-section-label" data-en="Select modules" data-es="Selecciona módulos">Select modules</div>
        <div class="calc-modules-grid">
          <div class="calc-module-toggle core-mod">
            <span class="calc-mod-icon">●</span>
            <span class="calc-mod-name" data-en="Core (RAG)" data-es="Core (RAG)">Core (RAG)</span>
            <span class="calc-mod-check">✓</span>
          </div>
          <div class="calc-module-toggle" id="mod-ops" onclick="toggleMod('ops')">
            <span class="calc-mod-icon">●</span>
            <span class="calc-mod-name" data-en="Operations" data-es="Operaciones">Operations</span>
            <span class="calc-mod-check" id="chk-ops"></span>
          </div>
          <div class="calc-module-toggle" id="mod-excel" onclick="toggleMod('excel')">
            <span class="calc-mod-icon">●</span>
            <span class="calc-mod-name" data-en="Excel Copilot" data-es="Copiloto Excel">Excel Copilot</span>
            <span class="calc-mod-check" id="chk-excel"></span>
          </div>
          <div class="calc-module-toggle" id="mod-wiki" onclick="toggleMod('wiki')">
            <span class="calc-mod-icon">●</span>
            <span class="calc-mod-name" data-en="Wiki" data-es="Wiki">Wiki</span>
            <span class="calc-mod-check" id="chk-wiki"></span>
          </div>
          <div class="calc-module-toggle" id="mod-incidents" onclick="toggleMod('incidents')">
            <span class="calc-mod-icon">●</span>
            <span class="calc-mod-name" data-en="Incidents" data-es="Incidencias">Incidents</span>
            <span class="calc-mod-check" id="chk-incidents"></span>
          </div>
          <div class="calc-module-toggle" id="mod-agent" onclick="toggleMod('agent')">
            <span class="calc-mod-icon">●</span>
            <span class="calc-mod-name" data-en="AI Agent" data-es="Agente IA">AI Agent</span>
            <span class="calc-mod-check" id="chk-agent"></span>
          </div>
          <div class="calc-module-toggle" id="mod-analytics" onclick="toggleMod('analytics')">
            <span class="calc-mod-icon">●</span>
            <span class="calc-mod-name" data-en="Analytics" data-es="Analítica">Analytics</span>
            <span class="calc-mod-check" id="chk-analytics"></span>
          </div>
        </div>
      </div>
      <div class="calc-right">
        <div class="calc-section-label" data-en="Your plan" data-es="Tu plan">Your plan</div>
        <div class="calc-summary-line">
          <span class="calc-summary-key" data-en="Core · per seat" data-es="Core · por seat">Core · per seat</span>
          <span class="calc-summary-val">€8<span style="font-size:0.75rem;font-weight:400;color:var(--text-dim)">/mo</span></span>
        </div>
        <div class="calc-summary-line" id="sum-modules-row" style="display:none">
          <span class="calc-summary-key" id="sum-modules-label">+ 0 modules · per seat</span>
          <span class="calc-summary-val" id="sum-modules-val">€0/mo</span>
        </div>
        <div class="calc-summary-line">
          <span class="calc-summary-key" id="sum-seats-label" data-en="× seats" data-es="× seats">× seats</span>
          <span class="calc-summary-val" id="sum-seats-val">5</span>
        </div>
        <div class="calc-summary-line" id="sum-discount-row" style="display:none">
          <span class="calc-summary-key" id="sum-discount-label" style="color:var(--accent3)">Volume discount</span>
          <span class="calc-summary-val" id="sum-discount-val" style="color:var(--accent3)">−€0</span>
        </div>
        <div class="calc-total-row">
          <div>
            <div class="calc-total-label" data-en="Total / month" data-es="Total / mes">Total / month</div>
            <div class="calc-total-period" data-en="billed monthly · cancel anytime" data-es="factura mensual · cancela cuando quieras">billed monthly · cancel anytime</div>
          </div>
          <div class="calc-total-price" id="calcTotal">€40</div>
        </div>
        <button class="calc-cta" onclick="switchTab('resources')" data-en="Request this plan →" data-es="Solicitar este plan →">Request this plan →</button>
        <div class="calc-note" id="calcNote" data-en="On-premise · no per-query costs · Docker install" data-es="On-premise · sin coste por consulta · instalación Docker">On-premise · no per-query costs · Docker install</div>
      </div>
    </div>
  </div>

  <!-- Tier reference cards -->
  <div class="pricing-grid fade-in">
    <div class="pricing-card">
      <div class="pricing-plan">Starter</div>
      <div class="pricing-price"><sup>€</sup>8</div>
      <div class="pricing-period" data-en="per seat / month · Core only" data-es="por seat / mes · solo Core">per seat / month · Core only</div>
      <ul class="pricing-features">
        <li data-en="Core module (RAG + connectors + OCR)" data-es="Módulo Core (RAG + conectores + OCR)">Core module (RAG + connectors + OCR)</li>
        <li data-en="From 1 seat — no minimum" data-es="Desde 1 seat — sin mínimo">From 1 seat — no minimum</li>
        <li data-en="Unlimited documents & AI queries" data-es="Documentos y consultas IA ilimitados">Unlimited documents & AI queries</li>
        <li data-en="Add any module: +€4/seat each" data-es="Añade cualquier módulo: +€4/seat cada uno">Add any module: +€4/seat each</li>
        <li data-en="On-premise — your infrastructure" data-es="On-premise — tu infraestructura">On-premise — your infrastructure</li>
        <li class="muted" data-en="No SSO / Entra ID" data-es="Sin SSO / Entra ID">No SSO / Entra ID</li>
      </ul>
      <button class="pricing-cta ghost" onclick="switchTab('resources')" data-en="Start Free Trial" data-es="Iniciar Prueba Gratuita">Start Free Trial</button>
    </div>
    <div class="pricing-card featured">
      <div class="pricing-badge" data-en="MOST POPULAR" data-es="MÁS POPULAR">MOST POPULAR</div>
      <div class="pricing-plan">Team</div>
      <div class="pricing-price"><sup>€</sup>20</div>
      <div class="pricing-period" data-en="per seat / month · Core + 3 modules" data-es="por seat / mes · Core + 3 módulos">per seat / month · Core + 3 modules</div>
      <ul class="pricing-features">
        <li data-en="Core + choose any 3 modules (+€4 each)" data-es="Core + elige 3 módulos (+€4 cada uno)">Core + choose any 3 modules (+€4 each)</li>
        <li data-en="Volume discount from 15 seats (−10%)" data-es="Descuento por volumen desde 15 seats (−10%)">Volume discount from 15 seats (−10%)</li>
        <li data-en="Unlimited documents & AI queries" data-es="Documentos y consultas IA ilimitados">Unlimited documents & AI queries</li>
        <li data-en="Public REST API + Webhooks" data-es="API REST pública + Webhooks">Public REST API + Webhooks</li>
        <li data-en="On-premise — your infrastructure" data-es="On-premise — tu infraestructura">On-premise — your infrastructure</li>
        <li data-en="Priority support" data-es="Soporte prioritario">Priority support</li>
      </ul>
      <button class="pricing-cta solid" onclick="switchTab('resources')" data-en="Start Team Trial" data-es="Iniciar Prueba Team">Start Team Trial</button>
    </div>
    <div class="pricing-card">
      <div class="pricing-plan">Enterprise</div>
      <div class="pricing-price"><sup>€</sup>32</div>
      <div class="pricing-period" data-en="per seat / month · all 6 modules" data-es="por seat / mes · los 6 módulos">per seat / month · all 6 modules</div>
      <ul class="pricing-features">
        <li data-en="Core + all 6 modules (+€4 each)" data-es="Core + los 6 módulos (+€4 cada uno)">Core + all 6 modules (+€4 each)</li>
        <li data-en="Volume discount from 15 seats (−10%)" data-es="Descuento volumen desde 15 seats (−10%)">Volume discount from 15 seats (−10%)</li>
        <li data-en="Microsoft Entra ID SSO" data-es="SSO Microsoft Entra ID">Microsoft Entra ID SSO</li>
        <li data-en="Dedicated SLA + 24h support" data-es="SLA dedicado + soporte 24h">Dedicated SLA + 24h support</li>
        <li data-en="Custom onboarding + ERP integration" data-es="Onboarding personalizado + integración ERP">Custom onboarding + ERP integration</li>
        <li data-en="Multi-site / multi-department" data-es="Multi-sede / multi-departamento">Multi-site / multi-department</li>
      </ul>
      <button class="pricing-cta ghost" onclick="switchTab('resources')" data-en="Request Enterprise Demo" data-es="Solicitar Demo Enterprise">Request Enterprise Demo</button>
    </div>
  </div>
  <p class="pricing-note" data-en="All plans: on-premise · Core €8/seat · each module +€4/seat · volume discounts from 15 seats · no per-query costs · cancel anytime" data-es="Todos los planes: on-premise · Core €8/seat · cada módulo +€4/seat · descuentos desde 15 seats · sin coste por consulta · cancela cuando quieras">All plans: on-premise · Core €8/seat · each module +€4/seat · volume discounts from 15 seats · no per-query costs · cancel anytime</p>
</div>'''

content = content[:pricing_start] + new_pricing_html + content[pricing_end:]

# 2. Add CSS before </style>
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

style_end = content.find('</style>')
content = content[:style_end] + css_to_add + '\n' + content[style_end:]

# 3. Add JavaScript before closing </script>
js_to_add = '''
// Pricing calculator
const CORE_PER_SEAT = 8;
const MODULE_PRICE_PER_SEAT = 4;
const ALL_MODULES = ['ops','excel','wiki','incidents','agent','analytics'];
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
'''

# Find the last script tag before </body>
script_end = content.rfind('</script>')
content = content[:script_end] + js_to_add + '\n' + content[script_end:]

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Restored pricing calculator HTML")
print("✓ Added pricing calculator CSS")
print("✓ Added pricing calculator JavaScript functions")
print("✓ Updated CTA buttons to navigate to Resources tab")
