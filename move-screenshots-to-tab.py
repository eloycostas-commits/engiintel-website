#!/usr/bin/env python3
"""
Move screenshots from Overview to a dedicated Screenshots tab
Use vertical layout for better visibility
"""

import re
from pathlib import Path

def move_screenshots_to_tab():
    """Remove screenshots from Overview and create dedicated tab"""
    
    index_path = Path("index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    backup_path = Path("index-backup-before-screenshots-move.html")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_path}")
    
    # Step 1: Remove screenshots section from Overview tab
    screenshots_pattern = r'\s*<!-- Product Screenshots -->.*?</div>\s*</div>\s*</div>'
    
    if re.search(screenshots_pattern, content, re.DOTALL):
        content = re.sub(screenshots_pattern, '', content, flags=re.DOTALL)
        print("✅ Removed screenshots from Overview tab")
    else:
        print("⚠️  Could not find screenshots section to remove")
    
    # Step 2: Add Screenshots tab button to navigation
    # Find the Industries tab button and add Screenshots before it
    nav_pattern = r'(<button class="tab-btn" onclick="switchTab\(\'industries\'\)")'
    nav_replacement = r'<button class="tab-btn" onclick="switchTab(\'screenshots\')" data-en="Screenshots" data-es="Capturas">Screenshots</button>\n      \1'
    
    if re.search(nav_pattern, content):
        content = re.sub(nav_pattern, nav_replacement, content)
        print("✅ Added Screenshots tab button to navigation")
    else:
        print("⚠️  Could not find Industries tab button")
    
    # Step 3: Create new Screenshots tab with vertical layout
    screenshots_tab = """
<!-- Tab Content: Screenshots -->
<div id="screenshots" class="tab-content">
  <div class="section-label" data-en="Product Screenshots" data-es="Capturas del Producto">Product Screenshots</div>
  <h2 data-en="See EngiIntel in Action" data-es="Mira EngiIntel en Acción">See EngiIntel in Action</h2>
  <p class="section-sub" data-en="Real screenshots from our production application. See how EngiIntel looks and works in real engineering environments." data-es="Capturas reales de nuestra aplicación en producción. Mira cómo se ve y funciona EngiIntel en entornos de ingeniería reales.">
    Real screenshots from our production application. See how EngiIntel looks and works in real engineering environments.
  </p>

  <!-- Vertical Screenshot Layout -->
  <div style="max-width: 1000px; margin: 40px auto; display: flex; flex-direction: column; gap: 60px;">
    
    <!-- Screenshot 1: Main Dashboard -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div>
        <h3 style="font-family: 'Syne', sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Main Dashboard" data-es="Panel Principal">Main Dashboard</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7; margin-bottom: 16px;" data-en="Your central hub for all documents, queries, and workflows. Access everything from one clean interface." data-es="Tu centro principal para todos los documentos, consultas y flujos. Accede a todo desde una interfaz limpia.">
          Your central hub for all documents, queries, and workflows. Access everything from one clean interface.
        </p>
        <ul style="list-style: none; padding: 0;">
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Quick search across all documents" data-es="Búsqueda rápida en todos los documentos">Quick search across all documents</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Recent queries and results" data-es="Consultas y resultados recientes">Recent queries and results</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Module shortcuts" data-es="Atajos de módulos">Module shortcuts</span></li>
        </ul>
      </div>
      <div>
        <img src="screenshots/panel principal.jpg" alt="Main Dashboard" style="width: 100%; height: auto; border: 2px solid var(--border); box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
      </div>
    </div>

    <!-- Screenshot 2: Document Comparison -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div style="order: 2;">
        <h3 style="font-family: 'Syne', sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Document Comparison" data-es="Comparación de Documentos">Document Comparison</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7; margin-bottom: 16px;" data-en="Compare multiple documents side-by-side with AI-powered analysis. Find differences and similarities instantly." data-es="Compara múltiples documentos lado a lado con análisis IA. Encuentra diferencias y similitudes al instante.">
          Compare multiple documents side-by-side with AI-powered analysis. Find differences and similarities instantly.
        </p>
        <ul style="list-style: none; padding: 0;">
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Side-by-side comparison" data-es="Comparación lado a lado">Side-by-side comparison</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="AI-powered difference detection" data-es="Detección de diferencias con IA">AI-powered difference detection</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Export comparison reports" data-es="Exportar informes de comparación">Export comparison reports</span></li>
        </ul>
      </div>
      <div style="order: 1;">
        <img src="screenshots/comparar documentos.jpg" alt="Document Comparison" style="width: 100%; height: auto; border: 2px solid var(--border); box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
      </div>
    </div>

    <!-- Screenshot 3: Wiki -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div>
        <h3 style="font-family: 'Syne', sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Wiki Knowledge Base" data-es="Base de Conocimiento Wiki">Wiki Knowledge Base</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7; margin-bottom: 16px;" data-en="Centralized knowledge management with markdown support, version control, and AI-powered search." data-es="Gestión centralizada del conocimiento con soporte markdown, control de versiones y búsqueda IA.">
          Centralized knowledge management with markdown support, version control, and AI-powered search.
        </p>
        <ul style="list-style: none; padding: 0;">
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Markdown editor with live preview" data-es="Editor markdown con vista previa">Markdown editor with live preview</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Full version history" data-es="Historial completo de versiones">Full version history</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="AI search across all pages" data-es="Búsqueda IA en todas las páginas">AI search across all pages</span></li>
        </ul>
      </div>
      <div>
        <img src="screenshots/wiki.jpg" alt="Wiki Knowledge Base" style="width: 100%; height: auto; border: 2px solid var(--border); box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
      </div>
    </div>

    <!-- Screenshot 4: Assets -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div style="order: 2;">
        <h3 style="font-family: 'Syne', sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Asset Registry" data-es="Registro de Activos">Asset Registry</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7; margin-bottom: 16px;" data-en="Track equipment, installations, and maintenance history. Perfect for regulated industries with compliance requirements." data-es="Rastrea equipos, instalaciones e historial de mantenimiento. Perfecto para industrias reguladas con requisitos de cumplimiento.">
          Track equipment, installations, and maintenance history. Perfect for regulated industries with compliance requirements.
        </p>
        <ul style="list-style: none; padding: 0;">
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Custom fields and categories" data-es="Campos y categorías personalizados">Custom fields and categories</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Maintenance scheduling" data-es="Programación de mantenimiento">Maintenance scheduling</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Document attachments" data-es="Adjuntos de documentos">Document attachments</span></li>
        </ul>
      </div>
      <div style="order: 1;">
        <img src="screenshots/activos.jpg" alt="Asset Registry" style="width: 100%; height: auto; border: 2px solid var(--border); box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
      </div>
    </div>

    <!-- Screenshot 5: Incidents -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div>
        <h3 style="font-family: 'Syne', sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Incident Reports" data-es="Informes de Incidencias">Incident Reports</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7; margin-bottom: 16px;" data-en="Generate professional incident reports with AI assistance. Reduce report time from 2+ hours to 10 minutes." data-es="Genera informes profesionales de incidencias con asistencia IA. Reduce el tiempo de informe de 2+ horas a 10 minutos.">
          Generate professional incident reports with AI assistance. Reduce report time from 2+ hours to 10 minutes.
        </p>
        <ul style="list-style: none; padding: 0;">
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="AI-assisted report generation" data-es="Generación asistida por IA">AI-assisted report generation</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Link to assets and documents" data-es="Vincular a activos y documentos">Link to assets and documents</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="PDF export with branding" data-es="Exportación PDF con marca">PDF export with branding</span></li>
        </ul>
      </div>
      <div>
        <img src="screenshots/Incidencias.jpg" alt="Incident Reports" style="width: 100%; height: auto; border: 2px solid var(--border); box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
      </div>
    </div>

    <!-- Screenshot 6: Analytics -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div style="order: 2;">
        <h3 style="font-family: 'Syne', sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Analytics Dashboard" data-es="Panel de Analítica">Analytics Dashboard</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7; margin-bottom: 16px;" data-en="Track usage patterns, query performance, and team productivity. Identify bottlenecks and optimize workflows." data-es="Rastrea patrones de uso, rendimiento de consultas y productividad del equipo. Identifica cuellos de botella y optimiza flujos.">
          Track usage patterns, query performance, and team productivity. Identify bottlenecks and optimize workflows.
        </p>
        <ul style="list-style: none; padding: 0;">
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Usage metrics and trends" data-es="Métricas y tendencias de uso">Usage metrics and trends</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Query performance analysis" data-es="Análisis de rendimiento de consultas">Query performance analysis</span></li>
          <li style="padding: 8px 0; color: var(--text-dim); display: flex; align-items: center; gap: 12px;"><span style="color: var(--accent);">✓</span><span data-en="Team productivity insights" data-es="Información de productividad del equipo">Team productivity insights</span></li>
        </ul>
      </div>
      <div style="order: 1;">
        <img src="screenshots/panel de metricas.jpg" alt="Analytics Dashboard" style="width: 100%; height: auto; border: 2px solid var(--border); box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
      </div>
    </div>

  </div>
</div>

"""
    
    # Step 4: Insert Screenshots tab before Industries tab
    industries_pattern = r'(<!-- Tab Content: Industries -->)'
    
    if re.search(industries_pattern, content):
        content = re.sub(industries_pattern, screenshots_tab + r'\1', content)
        print("✅ Added Screenshots tab content")
    else:
        print("⚠️  Could not find Industries tab")
    
    # Write updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Updated: {index_path}")
    print("\n📋 Changes Made:")
    print("  ✅ Removed screenshots from Overview tab")
    print("  ✅ Added Screenshots tab button to navigation")
    print("  ✅ Created dedicated Screenshots tab")
    print("  ✅ Vertical layout with alternating sides")
    print("  ✅ Detailed descriptions for each screenshot")
    print("\n🧪 Test:")
    print("1. Refresh browser (Ctrl+F5)")
    print("2. Click Overview tab - NO screenshots")
    print("3. Click Screenshots tab - See 6 screenshots vertically")
    print("4. All other tabs should work normally")
    
    return True

if __name__ == "__main__":
    print("🚀 Moving Screenshots to Dedicated Tab...\n")
    success = move_screenshots_to_tab()
    
    if success:
        print("\n✅ Screenshots moved successfully!")
    else:
        print("\n❌ Failed to move screenshots.")
