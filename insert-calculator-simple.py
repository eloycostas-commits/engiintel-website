#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Calculator HTML to insert
calculator_html = '''
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

  <!-- Tier reference cards -->'''

# Find where to insert - right after the section-sub paragraph in pricing
insert_marker = '''  </p>
  <div class="pricing-grid">'''

if insert_marker in content:
    content = content.replace(insert_marker, '  </p>' + calculator_html + '\n  <div class="pricing-grid">')
    print("✓ Inserted calculator HTML")
else:
    print("✗ Could not find insertion point")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
