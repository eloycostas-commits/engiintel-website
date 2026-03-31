#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 2 Website Improvements
- Update hero headline to results-focused copy
- Add product capability metrics
- Restructure Overview tab with problem/solution flow
- Add "How It Works" section
- Improve section spacing and visual separation
"""

import re

print("🚀 Implementing Phase 2 Improvements\n")

# Read current file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📖 Read {len(content)} bytes")

# Step 1: Update hero headline (find it in Overview tab)
print("\n🔧 Step 1: Updating hero headline...")

# Find the Overview tab content
overview_start = content.find('<div id="overview" class="tab-content active">')
if overview_start > 0:
    # Look for h1 in overview section
    h1_pattern = r'<h1[^>]*>.*?</h1>'
    overview_section = content[overview_start:overview_start + 5000]
    
    old_h1 = re.search(h1_pattern, overview_section, re.DOTALL)
    if old_h1:
        new_h1 = '''<h1 data-en="Reduce Engineering Document Search Time by 80%" data-es="Reduce el Tiempo de Búsqueda de Documentos en un 80%">Reduce Engineering Document Search Time by 80%</h1>'''
        content = content.replace(old_h1.group(0), new_h1)
        print("✓ Updated hero headline")
    else:
        print("⚠️  Could not find h1 in Overview")
else:
    print("⚠️  Could not find Overview tab")

# Step 2: Update hero subheadline to be more specific
print("\n🔧 Step 2: Updating hero subheadline...")

old_subs = [
    'Self-hosted AI that queries regulations',
    'AI-powered knowledge extraction for regulated industries'
]

new_sub = '''AI-powered knowledge extraction for regulated industries. Query regulations, generate reports, and automate workflows — all on-premise, zero data risk.'''

for old_sub in old_subs:
    if old_sub in content:
        # Find the full paragraph
        p_start = content.find(old_sub) - 100
        p_end = content.find('</p>', content.find(old_sub)) + 4
        if p_start > 0 and p_end > p_start:
            old_p = content[p_start:p_end]
            # Extract the data attributes
            if 'data-en=' in old_p and 'data-es=' in old_p:
                new_p = f'''<p class="hero-sub" data-en="{new_sub}" data-es="Extracción de conocimiento impulsada por IA para industrias reguladas. Consulta regulaciones, genera informes y automatiza flujos de trabajo — todo on-premise, sin riesgo de datos.">{new_sub}</p>'''
                content = content.replace(old_p, new_p)
                print("✓ Updated hero subheadline")
                break

# Step 3: Add product capabilities section after hero
print("\n🔧 Step 3: Adding product capabilities metrics...")

capabilities_section = '''
  <!-- Product Capabilities -->
  <div class="capabilities-grid" style="margin-top: 60px; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px;">
    <div class="capability-card" style="text-align: center; padding: 32px 24px; background: var(--surface); border: 1px solid var(--border); transition: all 0.3s;">
      <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 2.5rem; color: var(--accent); margin-bottom: 12px;">10,000+</div>
      <div style="font-family: 'DM Mono', monospace; font-size: 0.85rem; color: var(--text-mid);" data-en="Documents processed in seconds" data-es="Documentos procesados en segundos">Documents processed in seconds</div>
    </div>
    <div class="capability-card" style="text-align: center; padding: 32px 24px; background: var(--surface); border: 1px solid var(--border); transition: all 0.3s;">
      <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 2.5rem; color: var(--accent3); margin-bottom: 12px;">1-Click</div>
      <div style="font-family: 'DM Mono', monospace; font-size: 0.85rem; color: var(--text-mid);" data-en="Report generation" data-es="Generación de informes">Report generation</div>
    </div>
    <div class="capability-card" style="text-align: center; padding: 32px 24px; background: var(--surface); border: 1px solid var(--border); transition: all 0.3s;">
      <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 2.5rem; color: var(--accent2); margin-bottom: 12px;">100%</div>
      <div style="font-family: 'DM Mono', monospace; font-size: 0.85rem; color: var(--text-mid);" data-en="On-premise data privacy" data-es="Privacidad de datos on-premise">On-premise data privacy</div>
    </div>
  </div>
'''

# Find trust signal and add capabilities after it
trust_signal_marker = '<!-- Trust Signal -->'
if trust_signal_marker in content:
    # Find the end of trust signal div
    pos = content.find(trust_signal_marker)
    end_pos = content.find('</div>', pos)
    if end_pos > 0:
        # Find the next closing div (the outer one)
        end_pos = content.find('</div>', end_pos + 6)
        if end_pos > 0:
            content = content[:end_pos + 6] + capabilities_section + content[end_pos + 6:]
            print("✓ Added capabilities section")

# Step 4: Add "The Problem" section
print("\n🔧 Step 4: Adding problem section...")

problem_section = '''
  <!-- The Problem -->
  <div class="problem-section" style="margin-top: 80px; padding: 60px; background: var(--surface); border: 1px solid var(--border); border-left: 4px solid var(--accent3);">
    <div class="section-label" data-en="THE CHALLENGE" data-es="EL DESAFÍO">THE CHALLENGE</div>
    <h2 data-en="Engineering Teams Waste 15+ Hours Per Week on Documentation" data-es="Los Equipos de Ingeniería Pierden 15+ Horas por Semana en Documentación">Engineering Teams Waste 15+ Hours Per Week on Documentation</h2>
    <p style="font-size: 1.1rem; color: var(--text-mid); line-height: 1.8; margin-bottom: 40px;" data-en="Searching through regulations, generating compliance reports, and tracking assets manually creates bottlenecks that slow down your entire operation." data-es="Buscar en regulaciones, generar informes de cumplimiento y rastrear activos manualmente crea cuellos de botella que ralentizan toda tu operación.">
      Searching through regulations, generating compliance reports, and tracking assets manually creates bottlenecks that slow down your entire operation.
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 32px;">
      <div style="text-align: center;">
        <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 3rem; color: var(--text); margin-bottom: 8px;">2+ hrs</div>
        <div style="font-size: 0.9rem; color: var(--text-dim);" data-en="Average time per regulation query" data-es="Tiempo promedio por consulta de regulación">Average time per regulation query</div>
      </div>
      <div style="text-align: center;">
        <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 3rem; color: var(--text); margin-bottom: 8px;">73%</div>
        <div style="font-size: 0.9rem; color: var(--text-dim);" data-en="Say documentation is their #1 bottleneck" data-es="Dicen que la documentación es su cuello de botella #1">Say documentation is their #1 bottleneck</div>
      </div>
      <div style="text-align: center;">
        <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 3rem; color: var(--text); margin-bottom: 8px;">High</div>
        <div style="font-size: 0.9rem; color: var(--text-dim);" data-en="Compliance risk from outdated info" data-es="Riesgo de cumplimiento por info desactualizada">Compliance risk from outdated info</div>
      </div>
    </div>
  </div>
'''

# Add after capabilities section
if capabilities_section in content:
    pos = content.find(capabilities_section) + len(capabilities_section)
    content = content[:pos] + problem_section + content[pos:]
    print("✓ Added problem section")

# Step 5: Add "The Solution" section
print("\n🔧 Step 5: Adding solution section...")

solution_section = '''
  <!-- The Solution -->
  <div style="margin-top: 80px;">
    <div class="section-label" data-en="THE SOLUTION" data-es="LA SOLUCIÓN">THE SOLUTION</div>
    <h2 data-en="Your AI-Powered Engineering Command Center" data-es="Tu Centro de Comando de Ingeniería Impulsado por IA">Your AI-Powered Engineering Command Center</h2>
    <p style="font-size: 1.1rem; color: var(--text-mid); line-height: 1.8; margin-bottom: 48px;" data-en="EngiIntel transforms how engineering teams handle documentation, compliance, and knowledge management." data-es="EngiIntel transforma cómo los equipos de ingeniería manejan documentación, cumplimiento y gestión del conocimiento.">
      EngiIntel transforms how engineering teams handle documentation, compliance, and knowledge management.
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px;">
      <div style="padding: 32px; background: var(--surface); border: 1px solid var(--border); border-top: 3px solid var(--accent);">
        <div style="font-size: 2rem; margin-bottom: 16px;">⚡</div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.3rem; margin-bottom: 12px;" data-en="Instant Regulation Search" data-es="Búsqueda Instantánea de Regulaciones">Instant Regulation Search</h3>
        <p style="color: var(--text-dim); line-height: 1.7;" data-en="Query thousands of documents in natural language. Get answers with page-level citations in seconds, not hours." data-es="Consulta miles de documentos en lenguaje natural. Obtén respuestas con citas a nivel de página en segundos, no horas.">
          Query thousands of documents in natural language. Get answers with page-level citations in seconds, not hours.
        </p>
      </div>
      
      <div style="padding: 32px; background: var(--surface); border: 1px solid var(--border); border-top: 3px solid var(--accent3);">
        <div style="font-size: 2rem; margin-bottom: 16px;">📊</div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.3rem; margin-bottom: 12px;" data-en="Automated Report Generation" data-es="Generación Automatizada de Informes">Automated Report Generation</h3>
        <p style="color: var(--text-dim); line-height: 1.7;" data-en="Generate compliance reports, incident documentation, and technical summaries with one click. Always accurate, always up-to-date." data-es="Genera informes de cumplimiento, documentación de incidentes y resúmenes técnicos con un clic. Siempre preciso, siempre actualizado.">
          Generate compliance reports, incident documentation, and technical summaries with one click. Always accurate, always up-to-date.
        </p>
      </div>
      
      <div style="padding: 32px; background: var(--surface); border: 1px solid var(--border); border-top: 3px solid var(--accent2);">
        <div style="font-size: 2rem; margin-bottom: 16px;">🔒</div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.3rem; margin-bottom: 12px;" data-en="Real-Time Asset Tracking" data-es="Seguimiento de Activos en Tiempo Real">Real-Time Asset Tracking</h3>
        <p style="color: var(--text-dim); line-height: 1.7;" data-en="Maintain a complete registry of equipment, inspections, and maintenance history. Never miss a compliance deadline." data-es="Mantén un registro completo de equipos, inspecciones e historial de mantenimiento. Nunca pierdas una fecha límite de cumplimiento.">
          Maintain a complete registry of equipment, inspections, and maintenance history. Never miss a compliance deadline.
        </p>
      </div>
    </div>
  </div>
'''

# Add after problem section
if problem_section in content:
    pos = content.find(problem_section) + len(problem_section)
    content = content[:pos] + solution_section + content[pos:]
    print("✓ Added solution section")

# Step 6: Add "How It Works" section
print("\n🔧 Step 6: Adding how it works section...")

how_it_works_section = '''
  <!-- How It Works -->
  <div style="margin-top: 80px; padding: 60px; background: var(--bg); border: 1px solid var(--border);">
    <div class="section-label" data-en="HOW IT WORKS" data-es="CÓMO FUNCIONA">HOW IT WORKS</div>
    <h2 data-en="Get Started in 3 Simple Steps" data-es="Comienza en 3 Pasos Simples">Get Started in 3 Simple Steps</h2>
    <p style="font-size: 1.1rem; color: var(--text-mid); line-height: 1.8; margin-bottom: 48px;" data-en="Deploy EngiIntel on your infrastructure and start querying your documents immediately." data-es="Despliega EngiIntel en tu infraestructura y comienza a consultar tus documentos inmediatamente.">
      Deploy EngiIntel on your infrastructure and start querying your documents immediately.
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px;">
      <div style="text-align: center;">
        <div style="width: 60px; height: 60px; margin: 0 auto 20px; background: var(--accent); color: var(--bg); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.5rem;">1</div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.2rem; margin-bottom: 12px;" data-en="Deploy On-Premise" data-es="Despliega On-Premise">Deploy On-Premise</h3>
        <p style="color: var(--text-dim); line-height: 1.7;" data-en="Install EngiIntel on your servers with Docker. Your data never leaves your infrastructure." data-es="Instala EngiIntel en tus servidores con Docker. Tus datos nunca salen de tu infraestructura.">
          Install EngiIntel on your servers with Docker. Your data never leaves your infrastructure.
        </p>
      </div>
      
      <div style="text-align: center;">
        <div style="width: 60px; height: 60px; margin: 0 auto 20px; background: var(--accent3); color: var(--bg); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.5rem;">2</div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.2rem; margin-bottom: 12px;" data-en="Upload Your Documents" data-es="Sube Tus Documentos">Upload Your Documents</h3>
        <p style="color: var(--text-dim); line-height: 1.7;" data-en="Import regulations, manuals, and technical documentation. EngiIntel processes and indexes everything automatically." data-es="Importa regulaciones, manuales y documentación técnica. EngiIntel procesa e indexa todo automáticamente.">
          Import regulations, manuals, and technical documentation. EngiIntel processes and indexes everything automatically.
        </p>
      </div>
      
      <div style="text-align: center;">
        <div style="width: 60px; height: 60px; margin: 0 auto 20px; background: var(--accent2); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.5rem;">3</div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.2rem; margin-bottom: 12px;" data-en="Ask Questions" data-es="Haz Preguntas">Ask Questions</h3>
        <p style="color: var(--text-dim); line-height: 1.7;" data-en="Query in natural language. Get instant answers with citations. Generate reports. Track assets. All in one platform." data-es="Consulta en lenguaje natural. Obtén respuestas instantáneas con citas. Genera informes. Rastrea activos. Todo en una plataforma.">
          Query in natural language. Get instant answers with citations. Generate reports. Track assets. All in one platform.
        </p>
      </div>
    </div>
    
    <div style="text-align: center; margin-top: 48px;">
      <button class="btn-primary" onclick="switchTab('resources')" data-en="See It In Action" data-es="Ver en Acción">See It In Action</button>
    </div>
  </div>
'''

# Add after solution section
if solution_section in content:
    pos = content.find(solution_section) + len(solution_section)
    content = content[:pos] + how_it_works_section + content[pos:]
    print("✓ Added how it works section")

# Step 7: Add CSS for new components
print("\n🔧 Step 7: Adding CSS for new components...")

new_css = """
/* Phase 2 Components */
.capability-card:hover {
  border-color: rgba(0, 212, 255, 0.4);
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.problem-section {
  position: relative;
  overflow: hidden;
}

.problem-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, var(--accent3), var(--accent));
}

/* Better section spacing */
.tab-content > div {
  margin-bottom: 40px;
}

/* Improved readability */
p {
  max-width: 800px;
}

h2 + p {
  margin-top: 20px;
}

/* Number badges in how it works */
.how-it-works-step {
  transition: all 0.3s;
}

.how-it-works-step:hover {
  transform: scale(1.05);
}
"""

# Insert before closing </style>
style_end = content.rfind('</style>')
if style_end > 0:
    content = content[:style_end] + new_css + '\n' + content[style_end:]
    print("✓ Added Phase 2 CSS")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f"\n✅ Done! Wrote {len(content)} bytes")
print("\n📋 Phase 2 Changes:")
print("  ✓ Updated hero headline (results-focused)")
print("  ✓ Added product capabilities metrics")
print("  ✓ Added 'The Problem' section")
print("  ✓ Added 'The Solution' section")
print("  ✓ Added 'How It Works' 3-step process")
print("  ✓ Improved section spacing and visual hierarchy")
print("\n🚀 Ready to test and deploy!")
