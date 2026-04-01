#!/usr/bin/env python3
"""
Step 1: Add Accordion System to Features Tab
Carefully replace the Features tab content with accordion system
"""

import re
from pathlib import Path

def add_accordion_to_features():
    """Replace Features tab with accordion system"""
    
    index_path = Path("index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    backup_path = Path("index-backup-before-accordion-step1.html")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_path}")
    
    # Step 1: Add accordion CSS before </style>
    accordion_css = """
/* Accordion System */
.accordion-container {
  max-width: 1200px;
  margin: 40px auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.accordion-item {
  background: var(--surface);
  border: 1px solid var(--border);
  overflow: hidden;
  transition: all 0.3s ease;
}

.accordion-item.active {
  border-color: var(--accent);
}

.accordion-header {
  padding: 24px 32px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  user-select: none;
}

.accordion-header:hover {
  background: rgba(0, 212, 255, 0.05);
}

.accordion-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 1.3rem;
  color: var(--text);
  display: flex;
  align-items: center;
  gap: 16px;
}

.accordion-icon {
  font-size: 1.5rem;
}

.accordion-toggle {
  font-size: 1.5rem;
  color: var(--accent);
  transition: transform 0.3s ease;
}

.accordion-item.active .accordion-toggle {
  transform: rotate(180deg);
}

.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
}

.accordion-item.active .accordion-content {
  max-height: 5000px;
}

.accordion-body {
  padding: 0 32px 32px 32px;
}

.accordion-desc {
  font-size: 1rem;
  color: var(--text-mid);
  line-height: 1.7;
  margin-bottom: 24px;
}

.modules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.module-card {
  background: var(--bg);
  border: 1px solid var(--border);
  padding: 24px;
  transition: all 0.3s;
}

.module-card:hover {
  border-color: rgba(0, 212, 255, 0.3);
  transform: translateY(-2px);
}

.module-icon {
  font-size: 2rem;
  margin-bottom: 12px;
  display: block;
}

.module-name {
  font-family: 'Syne', sans-serif;
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 12px;
  color: var(--text);
}

.module-desc {
  font-size: 0.9rem;
  color: var(--text-dim);
  line-height: 1.6;
  margin-bottom: 16px;
}

.module-features {
  list-style: none;
  padding: 0;
  margin: 0;
}

.module-features li {
  font-size: 0.85rem;
  color: var(--text-mid);
  padding: 6px 0;
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.module-features li::before {
  content: '•';
  color: var(--accent);
  font-family: 'DM Mono', monospace;
  flex-shrink: 0;
}
"""

    # Find the closing </style> tag and insert CSS before it
    style_pattern = r'(</style>)'
    if re.search(style_pattern, content):
        content = re.sub(style_pattern, accordion_css + r'\n\1', content, count=1)
        print("✅ Added accordion CSS")
    else:
        print("❌ Could not find </style> tag")
        return False
    
    # Step 2: Find and replace Features tab content
    # Find the start of Features tab
    features_start = r'<div id="features" class="tab-content">'
    
    # Find the end (next tab or closing div)
    features_pattern = r'<div id="features" class="tab-content">.*?(?=<div id="[^"]*" class="tab-content">|<footer>)'
    
    if not re.search(features_pattern, content, re.DOTALL):
        print("❌ Could not find Features tab")
        return False
    
    # New accordion content
    accordion_html = '''<div id="features" class="tab-content">
  <div class="section-label" data-en="Platform Capabilities" data-es="Capacidades de la Plataforma">Platform Capabilities</div>
  <h2 data-en="Everything You Need for Document Intelligence" data-es="Todo lo que Necesitas para Inteligencia Documental">Everything You Need for Document Intelligence</h2>
  <p class="section-sub" data-en="22 capabilities organized into 4 strategic pillars. Start with Document Intelligence core, add modules as you grow." data-es="22 capacidades organizadas en 4 pilares estratégicos. Comienza con el núcleo de Inteligencia Documental, añade módulos a medida que creces.">
    22 capabilities organized into 4 strategic pillars. Start with Document Intelligence core, add modules as you grow.
  </p>

  <div class="accordion-container">
    
    <!-- Pillar 1: Document Intelligence -->
    <div class="accordion-item active">
      <div class="accordion-header" onclick="toggleAccordion('doc-intel')" id="accordion-doc-intel">
        <div class="accordion-title">
          <span class="accordion-icon">📚</span>
          <span data-en="Document Intelligence (Core)" data-es="Inteligencia Documental (Núcleo)">Document Intelligence (Core)</span>
        </div>
        <span class="accordion-toggle">▼</span>
      </div>
      <div class="accordion-content">
        <div class="accordion-body">
          <p class="accordion-desc" data-en="RAG-powered document search with page-level citations. The foundation of EngiIntel - always included in every plan." data-es="Búsqueda de documentos potenciada por RAG con citas a nivel de página. La base de EngiIntel - siempre incluido en cada plan.">
            RAG-powered document search with page-level citations. The foundation of EngiIntel - always included in every plan.
          </p>
          
          <div class="modules-grid">
            <div class="module-card">
              <span class="module-icon">🔍</span>
              <div class="module-name" data-en="Natural Language Queries" data-es="Consultas en Lenguaje Natural">Natural Language Queries</div>
              <div class="module-desc" data-en="Ask questions in plain Spanish or English. Get precise answers with exact page citations." data-es="Haz preguntas en castellano o inglés. Obtén respuestas precisas con citas de página exactas.">
                Ask questions in plain Spanish or English. Get precise answers with exact page citations.
              </div>
              <ul class="module-features">
                <li data-en="Hybrid search (semantic + keyword)" data-es="Búsqueda híbrida (semántica + palabras clave)">Hybrid search (semantic + keyword)</li>
                <li data-en="Page-level citations" data-es="Citas a nivel de página">Page-level citations</li>
                <li data-en="Multi-document context" data-es="Contexto multi-documento">Multi-document context</li>
              </ul>
            </div>
