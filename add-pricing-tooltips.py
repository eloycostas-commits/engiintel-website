#!/usr/bin/env python3
"""
Add tooltips to pricing calculator modules
"""

import re
from pathlib import Path

def add_pricing_tooltips():
    """Add info tooltips to pricing calculator modules"""
    
    index_path = Path("index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    backup_path = Path("index-backup-before-tooltips.html")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_path}")
    
    # Define tooltips for each module
    tooltips = {
        'Core (RAG)': {
            'en': 'AI document search with page-level citations. Always included.',
            'es': 'Búsqueda IA de documentos con citas de página. Siempre incluido.'
        },
        'Operations': {
            'en': 'Task management, projects, and workflow automation',
            'es': 'Gestión de tareas, proyectos y automatización de flujos'
        },
        'Excel Copilot': {
            'en': 'Query Excel in natural language, generate charts with one command',
            'es': 'Consulta Excel en lenguaje natural, genera gráficos con un comando'
        },
        'Wiki': {
            'en': 'Knowledge base with markdown, version control, and AI search',
            'es': 'Base de conocimiento con markdown, control de versiones y búsqueda IA'
        },
        'Incidents': {
            'en': 'Generate incident reports with AI assistance and PDF export',
            'es': 'Genera informes de incidencias con asistencia IA y exportación PDF'
        },
        'AI Agent': {
            'en': 'Autonomous AI agents for multi-step tasks and workflow automation',
            'es': 'Agentes IA autónomos para tareas multi-paso y automatización'
        },
        'Analytics': {
            'en': 'Usage tracking, query patterns, and team productivity metrics',
            'es': 'Seguimiento de uso, patrones de consulta y métricas de productividad'
        }
    }
    
    # Replace each module toggle to add tooltip
    replacements = [
        # Core (RAG) - already included, just add tooltip
        (
            r'(<div class="calc-module-toggle core-mod">.*?<span class="calc-mod-name"[^>]*>Core \(RAG\)</span>)',
            r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Core (RAG)']['en'] + '">ⓘ</span>'
        ),
        # Operations
        (
            r'(<div class="calc-module-toggle" id="mod-ops"[^>]*>.*?<span class="calc-mod-name"[^>]*>Operations</span>)',
            r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Operations']['en'] + '">ⓘ</span>'
        ),
        # Excel Copilot
        (
            r'(<div class="calc-module-toggle" id="mod-excel"[^>]*>.*?<span class="calc-mod-name"[^>]*>Excel Copilot</span>)',
            r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Excel Copilot']['en'] + '">ⓘ</span>'
        ),
        # Wiki
        (
            r'(<div class="calc-module-toggle" id="mod-wiki"[^>]*>.*?<span class="calc-mod-name"[^>]*>Wiki</span>)',
            r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Wiki']['en'] + '">ⓘ</span>'
        ),
        # Incidents
        (
            r'(<div class="calc-module-toggle" id="mod-incidents"[^>]*>.*?<span class="calc-mod-name"[^>]*>Incidents</span>)',
            r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Incidents']['en'] + '">ⓘ</span>'
        ),
        # AI Agent
        (
            r'(<div class="calc-module-toggle" id="mod-agent"[^>]*>.*?<span class="calc-mod-name"[^>]*>AI Agent</span>)',
            r'\1<span class="info-tooltip" data-tooltip="' + tooltips['AI Agent']['en'] + '">ⓘ</span>'
        ),
        # Analytics
        (
            r'(<div class="calc-module-toggle" id="mod-analytics"[^>]*>.*?<span class="calc-mod-name"[^>]*>Analytics</span>)',
            r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Analytics']['en'] + '">ⓘ</span>'
        ),
    ]
    
    # Apply replacements
    for pattern, replacement in replacements:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            print(f"✅ Added tooltip to module")
        else:
            print(f"⚠️  Pattern not found for module")
    
    # Write updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Updated: {index_path}")
    print("\n📋 Tooltips Added:")
    print("  ✅ Core (RAG)")
    print("  ✅ Operations")
    print("  ✅ Excel Copilot")
    print("  ✅ Wiki")
    print("  ✅ Incidents")
    print("  ✅ AI Agent")
    print("  ✅ Analytics")
    print("\n🧪 Test:")
    print("1. Open index.html")
    print("2. Go to Pricing tab")
    print("3. Scroll to module selector")
    print("4. Hover over the ⓘ icons")
    print("5. Tooltips should appear with descriptions")
    
    return True

if __name__ == "__main__":
    print("🚀 Adding Pricing Tooltips...\n")
    success = add_pricing_tooltips()
    
    if success:
        print("\n✅ Tooltips added successfully!")
    else:
        print("\n❌ Failed to add tooltips.")
