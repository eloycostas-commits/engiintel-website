#!/usr/bin/env python3
"""
Safe HTML modification using BeautifulSoup
Adds accordion system, tooltips, and pricing presets to index.html
"""

from bs4 import BeautifulSoup
import sys

def add_accordion_styles(soup):
    """Add accordion CSS to the style tag"""
    style_tag = soup.find('style')
    if not style_tag:
        print("ERROR: No style tag found")
        return False
    
    accordion_css = """

/* Accordion System Styles */
.capabilities-accordion {
  max-width: 1200px;
  margin: 0 auto;
}

.accordion-item {
  border: 1px solid var(--border);
  margin-bottom: 16px;
  background: var(--surface);
  transition: all 0.3s;
  border-radius: 4px;
  overflow: hidden;
}

.accordion-item:hover {
  border-color: rgba(0, 212, 255, 0.3);
}

.accordion-item.active {
  border-color: var(--accent);
  box-shadow: 0 4px 20px rgba(0, 212, 255, 0.15);
}

.accordion-header {
  width: 100%;
  padding: 28px 36px;
  background: none;
  border: none;
  display: flex;
  align-items: center;
  gap: 20px;
  cursor: pointer;
  text-align: left;
  transition: all 0.2s;
}

.accordion-header:hover {
  background: rgba(0, 212, 255, 0.05);
}

.accordion-icon {
  font-size: 2.5rem;
  flex-shrink: 0;
}

.accordion-title {
  flex: 1;
}

.accordion-title h3 {
  font-family: 'Syne', sans-serif;
  font-size: 1.4rem;
  font-weight: 700;
  margin: 0 0 6px 0;
  color: var(--text);
}

.accordion-title p {
  font-size: 0.9rem;
  color: var(--text-dim);
  margin: 0;
  line-height: 1.4;
}

.accordion-arrow {
  margin-left: auto;
  font-size: 1.3rem;
  color: var(--text-dim);
  transition: transform 0.3s ease;
  flex-shrink: 0;
}

.accordion-item.active .accordion-arrow {
  transform: rotate(180deg);
  color: var(--accent);
}

.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease-out;
  padding: 0 36px;
}

.accordion-item.active .accordion-content {
  max-height: 3000px;
  padding: 0 36px 36px;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .accordion-header {
    padding: 20px 24px;
    gap: 16px;
  }
  
  .accordion-icon {
    font-size: 2rem;
  }
  
  .accordion-title h3 {
    font-size: 1.1rem;
  }
  
  .accordion-title p {
    font-size: 0.8rem;
  }
  
  .accordion-content {
    padding: 0 24px;
  }
  
  .accordion-item.active .accordion-content {
    padding: 0 24px 24px;
  }
}

/* Tooltip Styles */
.tooltip-wrapper {
  position: relative;
  display: inline-block;
}

.tooltip-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--accent);
  color: var(--bg);
  font-size: 0.7rem;
  font-weight: 700;
  cursor: help;
  margin-left: 6px;
  vertical-align: middle;
}

.tooltip-text {
  visibility: hidden;
  opacity: 0;
  position: absolute;
  bottom: 125%;
  left: 50%;
  transform: translateX(-50%);
  background: var(--surface2);
  color: var(--text);
  padding: 12px 16px;
  border-radius: 4px;
  border: 1px solid var(--accent);
  font-size: 0.85rem;
  line-height: 1.5;
  white-space: nowrap;
  z-index: 1000;
  transition: opacity 0.3s, visibility 0.3s;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.tooltip-text::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: var(--accent);
}

.tooltip-wrapper:hover .tooltip-text {
  visibility: visible;
  opacity: 1;
}

/* Pricing Preset Buttons */
.pricing-presets {
  display: flex;
  gap: 12px;
  justify-content: center;
  margin-bottom: 32px;
  flex-wrap: wrap;
}

.preset-btn {
  padding: 12px 24px;
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text-mid);
  font-family: 'Syne', sans-serif;
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  border-radius: 4px;
}

.preset-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
  background: rgba(0, 212, 255, 0.05);
}

.preset-btn.active {
  border-color: var(--accent);
  background: var(--accent);
  color: var(--bg);
}
"""
    
    style_tag.string = style_tag.string + accordion_css
    print("✓ Added accordion CSS")
    return True


def add_accordion_javascript(soup):
    """Add accordion toggle JavaScript"""
    # Find the last script tag in head
    head = soup.find('head')
    if not head:
        print("ERROR: No head tag found")
        return False
    
    accordion_js = soup.new_tag('script')
    accordion_js.string = """
// Accordion Toggle Logic
function toggleAccordion(id) {
  const item = document.querySelector(`#accordion-${id}`).parentElement;
  const isActive = item.classList.contains('active');
  
  // Close all accordions
  document.querySelectorAll('.accordion-item').forEach(el => {
    el.classList.remove('active');
  });
  
  // Open clicked accordion if it wasn't active
  if (!isActive) {
    item.classList.add('active');
  }
}

// Open first accordion by default when Features tab is shown
const originalSwitchTab = switchTab;
switchTab = function(tabId) {
  originalSwitchTab(tabId);
  if (tabId === 'features') {
    setTimeout(() => {
      const firstAccordion = document.querySelector('#features .accordion-item');
      if (firstAccordion && !firstAccordion.classList.contains('active')) {
        firstAccordion.classList.add('active');
      }
    }, 100);
  }
};
"""
    head.append(accordion_js)
    print("✓ Added accordion JavaScript")
    return True


def replace_features_tab_with_accordion(soup):
    """Replace the Features tab content with accordion system"""
    features_tab = soup.find('div', id='features')
    if not features_tab:
        print("ERROR: Features tab not found")
        return False
    
    # Clear existing content
    features_tab.clear()
    features_tab['class'] = 'tab-content'
    features_tab['id'] = 'features'
    
    # Add section header
    section_label = soup.new_tag('div', **{'class': 'section-label', 'data-en': 'Platform Capabilities', 'data-es': 'Capacidades de la Plataforma'})
    section_label.string = 'Platform Capabilities'
    features_tab.append(section_label)
    
    h2 = soup.new_tag('h2', **{'data-en': 'Everything You Need, On Your Own Terms', 'data-es': 'Todo lo que Necesitas, en Tus Propios Términos'})
    h2.string = 'Everything You Need, On Your Own Terms'
    features_tab.append(h2)
    
    section_sub = soup.new_tag('p', **{'class': 'section-sub', 'data-en': 'EngiIntel organizes 22 powerful capabilities into 4 strategic pillars. Expand each to discover how we solve your engineering challenges.', 'data-es': 'EngiIntel organiza 22 capacidades potentes en 4 pilares estratégicos. Expande cada uno para descubrir cómo resolvemos tus desafíos de ingeniería.'})
    section_sub.string = 'EngiIntel organizes 22 powerful capabilities into 4 strategic pillars. Expand each to discover how we solve your engineering challenges.'
    features_tab.append(section_sub)
    
    # Create accordion container
    accordion_container = soup.new_tag('div', **{'class': 'capabilities-accordion', 'style': 'margin-top: 60px;'})
    
    # PILLAR 1: Core Engine
    accordion_container.append(create_accordion_pillar(soup, 'core', '🔥', 
        'Core Engine', 'Motor Principal',
        'Foundation of AI-powered document intelligence', 'Fundamento de inteligencia documental con IA',
        [
            ('🔍', 'RAG Document Search', 'Búsqueda RAG de Documentos', 
             'Query 10,000+ documents in seconds with page-level citations. Hybrid semantic + keyword search.',
             'Consulta 10,000+ documentos en segundos con citas a nivel de página. Búsqueda híbrida semántica + palabras clave.'),
            ('💬', 'Natural Language Queries', 'Consultas en Lenguaje Natural',
             'Ask questions in plain Spanish or English. Get precise answers with exact page references.',
             'Haz preguntas en castellano o inglés. Obtén respuestas precisas con referencias exactas de página.'),
            ('📄', 'OCR for Scanned Documents', 'OCR para Documentos Escaneados',
             'Process scanned PDFs and image-based documents. Legacy manuals work just as well as native PDFs.',
             'Procesa PDFs escaneados y documentos basados en imagen. Los manuales heredados funcionan igual que PDFs nativos.'),
            ('🌍', 'Multi-language Support', 'Soporte Multi-idioma',
             'Works with Spanish, English, and other European languages. Automatic language detection.',
             'Funciona con español, inglés y otros idiomas europeos. Detección automática de idioma.'),
        ]
    ))
    
    # PILLAR 2: Security & Privacy
    accordion_container.append(create_accordion_pillar(soup, 'security', '🔒',
        'Security & Privacy', 'Seguridad y Privacidad',
        'Your primary differentiator - zero data risk', 'Tu diferenciador principal - cero riesgo de datos',
        [
            ('🏢', '100% On-Premise', '100% On-Premise',
             'Your data never leaves your infrastructure. Complete air-gapped deployment with zero cloud dependencies.',
             'Tus datos nunca salen de tu infraestructura. Despliegue completamente aislado sin dependencias en la nube.'),
            ('🛡️', 'Air-gapped Architecture', 'Arquitectura Aislada',
             'No external API calls. No internet connection required. Complete data sovereignty.',
             'Sin llamadas API externas. Sin conexión a internet requerida. Soberanía completa de datos.'),
            ('✅', 'GDPR Compliance', 'Cumplimiento GDPR',
             'Built-in compliance with GDPR and ISO 27001. Complete audit trails and data retention policies.',
             'Cumplimiento integrado con GDPR e ISO 27001. Registros de auditoría completos y políticas de retención.'),
            ('🔐', 'Role-Based Access Control', 'Control de Acceso por Roles',
             'Granular permissions and user management. Control who can access what data and perform which actions.',
             'Permisos granulares y gestión de usuarios. Controla quién puede acceder a qué datos y realizar qué acciones.'),
            ('📋', 'Audit Trails', 'Registros de Auditoría',
             'Complete activity logging for compliance. Track every query, document access, and user action.',
             'Registro completo de actividad para cumplimiento. Rastrea cada consulta, acceso a documento y acción de usuario.'),
        ]
    ))
    
    # PILLAR 3: Connectivity
    accordion_container.append(create_accordion_pillar(soup, 'connectivity', '🔗',
        'Connectivity', 'Conectividad',
        'Integrate with your existing tools and workflows', 'Integra con tus herramientas y flujos existentes',
        [
            ('🐘', 'PostgreSQL Support', 'Soporte PostgreSQL',
             'Native PostgreSQL integration. Query databases alongside documents with natural language.',
             'Integración nativa con PostgreSQL. Consulta bases de datos junto con documentos en lenguaje natural.'),
            ('🐳', 'Docker Deployment', 'Despliegue Docker',
             'One-command deployment with Docker Compose. Production-ready in minutes, not days.',
             'Despliegue con un comando usando Docker Compose. Listo para producción en minutos, no días.'),
            ('🔄', 'n8n Workflows', 'Flujos n8n',
             'Visual workflow builder with 300+ integrations. Connect to your existing tools without code.',
             'Constructor visual de flujos con 300+ integraciones. Conecta con tus herramientas existentes sin código.'),
            ('📡', 'REST API', 'API REST',
             'Complete REST API for custom integrations. Build your own tools on top of EngiIntel.',
             'API REST completa para integraciones personalizadas. Construye tus propias herramientas sobre EngiIntel.'),
            ('☁️', 'Cloud Connectors', 'Conectores Cloud',
             'Sync from SharePoint, Google Drive, and Confluence. Documents stay up to date automatically.',
             'Sincroniza desde SharePoint, Google Drive y Confluence. Los documentos se mantienen actualizados automáticamente.'),
            ('📊', 'Excel Integration', 'Integración Excel',
             'AI-powered Excel analysis. Query spreadsheets in natural language and generate charts with one command.',
             'Análisis de Excel potenciado por IA. Consulta hojas de cálculo en lenguaje natural y genera gráficos con un comando.'),
        ]
    ))
    
    # PILLAR 4: Analysis Tools
    accordion_container.append(create_accordion_pillar(soup, 'analysis', '📊',
        'Analysis Tools', 'Herramientas de Análisis',
        'Boost productivity and automate workflows', 'Aumenta productividad y automatiza flujos',
        [
            ('📚', 'Wiki Knowledge Base', 'Base de Conocimiento Wiki',
             'Centralized knowledge management with AI search. Keep your team\'s expertise accessible.',
             'Gestión centralizada del conocimiento con búsqueda IA. Mantén la experiencia de tu equipo accesible.'),
            ('🏗️', 'Asset Registry', 'Registro de Activos',
             'Track equipment, installations, and maintenance history. Replace spreadsheets with AI-powered search.',
             'Rastrea equipos, instalaciones e historial de mantenimiento. Reemplaza hojas de cálculo con búsqueda IA.'),
            ('📝', 'Incident Reports', 'Informes de Incidencias',
             'Generate incident reports in one click. Reduce 2+ hours to 10 minutes with automated templates.',
             'Genera informes de incidencias en un clic. Reduce 2+ horas a 10 minutos con plantillas automatizadas.'),
            ('🤖', 'AI Agent Mode', 'Modo Agente IA',
             'Autonomous AI agents that execute multi-step tasks. From data extraction to workflow automation.',
             'Agentes IA autónomos que ejecutan tareas multi-paso. Desde extracción de datos hasta automatización de flujos.'),
            ('📈', 'Analytics Dashboard', 'Panel de Analítica',
             'Track usage, query patterns, and team productivity. Identify bottlenecks and optimize workflows.',
             'Rastrea uso, patrones de consulta y productividad del equipo. Identifica cuellos de botella y optimiza flujos.'),
            ('⚡', 'Automated Reports', 'Informes Automatizados',
             'Schedule automated report generation. Daily, weekly, or monthly compliance reports without manual work.',
             'Programa generación automática de informes. Informes de cumplimiento diarios, semanales o mensuales sin trabajo manual.'),
        ]
    ))
    
    features_tab.append(accordion_container)
    print("✓ Replaced Features tab with accordion system")
    return True


def create_accordion_pillar(soup, pillar_id, icon, title_en, title_es, desc_en, desc_es, modules):
    """Create an accordion pillar with modules"""
    accordion_item = soup.new_tag('div', **{'class': 'accordion-item'})
    
    # Header button
    header_btn = soup.new_tag('button', **{'class': 'accordion-header', 'onclick': f'toggleAccordion(\'{pillar_id}\')'})
    
    icon_span = soup.new_tag('span', **{'class': 'accordion-icon'})
    icon_span.string = icon
    header_btn.append(icon_span)
    
    title_div = soup.new_tag('div', **{'class': 'accordion-title'})
    h3 = soup.new_tag('h3', **{'data-en': title_en, 'data-es': title_es})
    h3.string = title_en
    title_div.append(h3)
    
    p = soup.new_tag('p', **{'data-en': desc_en, 'data-es': desc_es})
    p.string = desc_en
    title_div.append(p)
    header_btn.append(title_div)
    
    arrow_span = soup.new_tag('span', **{'class': 'accordion-arrow'})
    arrow_span.string = '▼'
    header_btn.append(arrow_span)
    
    accordion_item.append(header_btn)
    
    # Content
    content_div = soup.new_tag('div', **{'id': f'accordion-{pillar_id}', 'class': 'accordion-content'})
    modules_grid = soup.new_tag('div', **{'class': 'modules-grid', 'style': 'margin-top: 24px;'})
    
    for mod_icon, mod_name_en, mod_name_es, mod_desc_en, mod_desc_es in modules:
        module_card = soup.new_tag('div', **{'class': 'module-card'})
        
        icon_span = soup.new_tag('span', **{'class': 'module-icon'})
        icon_span.string = mod_icon
        module_card.append(icon_span)
        
        name_div = soup.new_tag('div', **{'class': 'module-name', 'data-en': mod_name_en, 'data-es': mod_name_es})
        name_div.string = mod_name_en
        module_card.append(name_div)
        
        desc_div = soup.new_tag('div', **{'class': 'module-desc', 'data-en': mod_desc_en, 'data-es': mod_desc_es})
        desc_div.string = mod_desc_en
        module_card.append(desc_div)
        
        modules_grid.append(module_card)
    
    content_div.append(modules_grid)
    accordion_item.append(content_div)
    
    return accordion_item


def add_pricing_tooltips(soup):
    """Add tooltips to pricing calculator modules"""
    tooltips = {
        'Operations': ('Workflow automation, task management, and team collaboration tools', 
                      'Automatización de flujos, gestión de tareas y herramientas de colaboración'),
        'Excel Copilot': ('AI-powered Excel analysis with chart generation and macro system',
                         'Análisis de Excel con IA, generación de gráficos y sistema de macros'),
        'Wiki': ('Internal knowledge base with version history and full-text search',
                'Base de conocimiento interna con historial de versiones y búsqueda'),
        'Incidents': ('AI-assisted incident report generation with asset linking and PDF export',
                     'Generación de informes de incidencias asistida por IA con vinculación de activos'),
        'AI Agent': ('Autonomous agent that executes multi-step workflows and automates tasks',
                    'Agente autónomo que ejecuta flujos multi-paso y automatiza tareas'),
        'Analytics': ('Usage tracking, query patterns, and team productivity metrics',
                     'Seguimiento de uso, patrones de consulta y métricas de productividad'),
    }
    
    # Find all module toggle elements in pricing calculator
    for module_name, (tooltip_en, tooltip_es) in tooltips.items():
        # Find the module name span
        module_spans = soup.find_all('span', class_='calc-mod-name')
        for span in module_spans:
            if span.get('data-en') == module_name or module_name.lower() in span.get_text().lower():
                # Wrap in tooltip
                wrapper = soup.new_tag('span', **{'class': 'tooltip-wrapper'})
                span.wrap(wrapper)
                
                # Add tooltip icon
                tooltip_icon = soup.new_tag('span', **{'class': 'tooltip-icon'})
                tooltip_icon.string = 'i'
                wrapper.append(tooltip_icon)
                
                # Add tooltip text
                tooltip_text = soup.new_tag('span', **{'class': 'tooltip-text', 'data-en': tooltip_en, 'data-es': tooltip_es})
                tooltip_text.string = tooltip_en
                wrapper.append(tooltip_text)
                
                print(f"✓ Added tooltip to {module_name}")
    
    return True


def add_pricing_presets(soup):
    """Add pricing preset buttons"""
    # Find the pricing calculator
    pricing_calc = soup.find('div', class_='pricing-calc')
    if not pricing_calc:
        print("ERROR: Pricing calculator not found")
        return False
    
    # Find calc-header and add presets after it
    calc_header = pricing_calc.find('div', class_='calc-header')
    if not calc_header:
        print("ERROR: Calc header not found")
        return False
    
    # Create presets container
    presets_container = soup.new_tag('div', **{'class': 'pricing-presets', 'style': 'padding: 24px 36px; border-bottom: 1px solid var(--border); background: var(--bg);'})
    
    # Add preset buttons
    presets = [
        ('starter', 'Starter', 'Inicial', '5', ['excel']),
        ('professional', 'Professional', 'Profesional', '15', ['excel', 'wiki', 'incidents']),
        ('enterprise', 'Enterprise', 'Empresa', '50', ['ops', 'excel', 'wiki', 'incidents', 'agent', 'analytics']),
    ]
    
    for preset_id, name_en, name_es, seats, modules in presets:
        btn = soup.new_tag('button', **{
            'class': 'preset-btn',
            'onclick': f'applyPreset({seats}, {modules})',
            'data-en': name_en,
            'data-es': name_es
        })
        btn.string = name_en
        presets_container.append(btn)
    
    # Insert after header
    calc_header.insert_after(presets_container)
    
    # Add preset JavaScript
    head = soup.find('head')
    preset_js = soup.new_tag('script')
    preset_js.string = """
function applyPreset(seats, modules) {
  // Clear all selections
  selected.clear();
  document.querySelectorAll('.calc-module-toggle.selected').forEach(el => {
    el.classList.remove('selected');
    const id = el.id.replace('mod-', '');
    const chk = document.getElementById('chk-' + id);
    if (chk) chk.textContent = '';
  });
  
  // Set seats
  document.getElementById('seatsInput').value = seats;
  
  // Select modules
  modules.forEach(id => {
    const el = document.getElementById('mod-' + id);
    const chk = document.getElementById('chk-' + id);
    if (el && chk) {
      selected.add(id);
      el.classList.add('selected');
      chk.textContent = '✓';
    }
  });
  
  // Update price
  calcPrice();
  
  // Visual feedback
  document.querySelectorAll('.preset-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
}
"""
    head.append(preset_js)
    
    print("✓ Added pricing presets")
    return True


def main():
    print("Starting safe HTML modification with BeautifulSoup...")
    print()
    
    # Read the working backup
    input_file = 'index-backup-before-accordion.html'
    output_file = 'index.html'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        print(f"✓ Read {input_file} ({len(html_content)} characters)")
    except Exception as e:
        print(f"ERROR reading file: {e}")
        return 1
    
    # Parse with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    print("✓ Parsed HTML with BeautifulSoup")
    print()
    
    # Apply modifications
    print("Applying modifications...")
    print()
    
    if not add_accordion_styles(soup):
        return 1
    
    if not add_accordion_javascript(soup):
        return 1
    
    if not replace_features_tab_with_accordion(soup):
        return 1
    
    if not add_pricing_tooltips(soup):
        return 1
    
    if not add_pricing_presets(soup):
        return 1
    
    print()
    print("All modifications applied successfully!")
    print()
    
    # Write output WITHOUT prettify to avoid corruption
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"✓ Wrote {output_file}")
        print()
        print("SUCCESS! File modified safely with BeautifulSoup")
        print()
        print("Next steps:")
        print("1. Open index.html in browser to test")
        print("2. Verify tabs are working")
        print("3. Test accordion expand/collapse")
        print("4. Test tooltips on hover")
        print("5. Test pricing presets")
        return 0
    except Exception as e:
        print(f"ERROR writing file: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
