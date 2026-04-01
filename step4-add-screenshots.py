#!/usr/bin/env python3
"""
Step 4: Add Screenshots tab with vertical layout
"""

import re
from pathlib import Path

# Read current version
with open("index.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Create backup
with open("index-backup-step4.html", 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Backup created: index-backup-step4.html")

# Step 1: Add Screenshots tab button to navigation
nav_pattern = r'(<button class="tab-btn" onclick="switchTab\(\'industries\'\)")'
nav_replacement = r'<button class="tab-btn" onclick="switchTab(\'screenshots\')" data-en="Screenshots" data-es="Capturas">Screenshots</button>\n    ' + r'\1'

if re.search(nav_pattern, content):
    content = re.sub(nav_pattern, nav_replacement, content)
    print("✅ Added Screenshots tab button")
else:
    print("❌ Could not find Industries button")
    exit(1)

# Step 2: Create Screenshots tab content
screenshots_tab = '''
<!-- Tab Content: Screenshots -->
<div id="screenshots" class="tab-content">
  <div class="section-label" data-en="Product Screenshots" data-es="Capturas del Producto">Product Screenshots</div>
  <h2 data-en="See EngiIntel in Action" data-es="Mira EngiIntel en Acción">See EngiIntel in Action</h2>
  <p class="section-sub" data-en="Real screenshots from our production application." data-es="Capturas reales de nuestra aplicación en producción.">
    Real screenshots from our production application.
  </p>

  <div style="max-width: 1000px; margin: 40px auto; display: flex; flex-direction: column; gap: 60px;">
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div>
        <h3 style="font-family: Syne, sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Main Dashboard" data-es="Panel Principal">Main Dashboard</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7;">Your central hub for documents and queries.</p>
      </div>
      <div>
        <img src="screenshots/panel principal.jpg" alt="Main Dashboard" style="width: 100%; height: auto; border: 2px solid var(--border);">
      </div>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div style="order: 2;">
        <h3 style="font-family: Syne, sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Document Comparison" data-es="Comparación">Document Comparison</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7;">Compare documents with AI analysis.</p>
      </div>
      <div style="order: 1;">
        <img src="screenshots/comparar documentos.jpg" alt="Document Comparison" style="width: 100%; height: auto; border: 2px solid var(--border);">
      </div>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
      <div>
        <h3 style="font-family: Syne, sans-serif; font-size: 1.4rem; margin-bottom: 16px; color: var(--accent);" data-en="Wiki" data-es="Wiki">Wiki</h3>
        <p style="font-size: 1rem; color: var(--text-mid); line-height: 1.7;">Knowledge management with AI search.</p>
      </div>
      <div>
        <img src="screenshots/wiki.jpg" alt="Wiki" style="width: 100%; height: auto; border: 2px solid var(--border);">
      </div>
    </div>

  </div>
</div>

'''

# Find Industries tab and insert Screenshots before it
industries_pattern = r'(<div id="industries" class="tab-content">)'

if re.search(industries_pattern, content):
    content = re.sub(industries_pattern, screenshots_tab + r'\1', content)
    print("✅ Added Screenshots tab content")
else:
    print("❌ Could not find Industries tab")
    exit(1)

# Step 3: Add responsive CSS
screenshot_css = """
@media (max-width: 768px) {
  #screenshots div[style*="grid-template-columns"] {
    grid-template-columns: 1fr !important;
  }
  #screenshots div[style*="order: 2"] {
    order: 1 !important;
  }
  #screenshots div[style*="order: 1"] {
    order: 2 !important;
  }
}
"""

# Add CSS before last </style>
head_end = content.find('</head>')
head_content = content[:head_end]
last_style_pos = head_content.rfind('</style>')

content = content[:last_style_pos] + "\n" + screenshot_css + "\n" + content[last_style_pos:]
print("✅ Added screenshot responsive CSS")

# Write updated content
with open("index.html", 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Step 4 Complete: Screenshots tab added")
print("📋 Test: Click Screenshots tab")
