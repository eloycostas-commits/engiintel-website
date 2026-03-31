#!/usr/bin/env python3
"""
Final Clean Integration - Phase 1
Properly integrates all tabs with clean UTF-8 encoding
"""

import sys

print("🚀 Phase 1 Final Clean Integration\n")

# 1. Read the clean base file
print("📖 Reading clean base index.html...")
try:
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    print("   ✅ Base file loaded")
except Exception as e:
    print(f"   ❌ Error reading base file: {e}")
    sys.exit(1)

# 2. Read tab content files
print("📖 Reading tab content files...")
try:
    with open("tabs/overview.html", "r", encoding="utf-8") as f:
        overview = f.read()
    with open("tabs/features.html", "r", encoding="utf-8") as f:
        features = f.read()
    with open("tabs/industries.html", "r", encoding="utf-8") as f:
        industries = f.read()
    with open("tabs/resources.html", "r", encoding="utf-8") as f:
        resources = f.read()
    print("   ✅ All tab files loaded")
except Exception as e:
    print(f"   ❌ Error reading tab files: {e}")
    sys.exit(1)

# 3. Update tabs navigation - add 4 new tabs
print("✏️  Updating tabs navigation...")
old_nav = '''<div class="tabs-container">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('document-intelligence')" data-en="Document Intelligence" data-es="Inteligencia Documental">Document Intelligence</button>
    <button class="tab-btn" onclick="switchTab('excel-copilot')" data-en="Excel Copilot" data-es="Excel Copilot">Excel Copilot</button>
    <button class="tab-btn" onclick="switchTab('wiki')" data-en="Wiki" data-es="Wiki">Wiki</button>
    <button class="tab-btn" onclick="switchTab('assets')" data-en="Assets" data-es="Activos">Assets</button>
    <button class="tab-btn" onclick="switchTab('incidents')" data-en="Incidents" data-es="Incidencias">Incidents</button>
    <button class="tab-btn" onclick="switchTab('ai-agent')" data-en="AI Agent" data-es="Agente IA">AI Agent</button>
    <button class="tab-btn" onclick="switchTab('pricing')" data-en="Pricing" data-es="Precios">Pricing</button>
  </div>
</div>'''

new_nav = '''<div class="tabs-container">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('overview')" data-en="Overview" data-es="Resumen">Overview</button>
    <button class="tab-btn" onclick="switchTab('features')" data-en="Features" data-es="Características">Features</button>
    <button class="tab-btn" onclick="switchTab('document-intelligence')" data-en="Document Intelligence" data-es="Inteligencia Documental">Document Intelligence</button>
    <button class="tab-btn" onclick="switchTab('excel-copilot')" data-en="Excel Copilot" data-es="Excel Copilot">Excel Copilot</button>
    <button class="tab-btn" onclick="switchTab('wiki')" data-en="Wiki" data-es="Wiki">Wiki</button>
    <button class="tab-btn" onclick="switchTab('assets')" data-en="Assets" data-es="Activos">Assets</button>
    <button class="tab-btn" onclick="switchTab('incidents')" data-en="Incidents" data-es="Incidencias">Incidents</button>
    <button class="tab-btn" onclick="switchTab('ai-agent')" data-en="AI Agent" data-es="Agente IA">AI Agent</button>
    <button class="tab-btn" onclick="switchTab('industries')" data-en="Industries" data-es="Industrias">Industries</button>
    <button class="tab-btn" onclick="switchTab('pricing')" data-en="Pricing" data-es="Precios">Pricing</button>
    <button class="tab-btn" onclick="switchTab('resources')" data-en="Resources" data-es="Recursos">Resources</button>
  </div>
</div>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print("   ✅ Navigation updated (11 tabs)")
else:
    print("   ⚠️  Navigation marker not found")

# 4. Make document-intelligence inactive
print("✏️  Updating document-intelligence tab...")
content = content.replace(
    '<div id="document-intelligence" class="tab-content active">',
    '<div id="document-intelligence" class="tab-content">'
)
print("   ✅ Document-intelligence now inactive")

# 5. Insert Overview tab BEFORE document-intelligence
print("✏️  Inserting Overview tab...")
marker = '<div id="document-intelligence" class="tab-content">'
if marker in content:
    insertion = f'''{overview}

{marker}'''
    content = content.replace(marker, insertion, 1)
    print("   ✅ Overview tab inserted (active)")
else:
    print("   ⚠️  Marker not found for Overview")

# 6. Insert Features tab
print("✏️  Inserting Features tab...")
marker = '<div id="document-intelligence" class="tab-content">'
if marker in content:
    insertion = f'''{features}

{marker}'''
    content = content.replace(marker, insertion, 1)
    print("   ✅ Features tab inserted")
else:
    print("   ⚠️  Marker not found for Features")

# 7. Insert Industries tab BEFORE pricing
print("✏️  Inserting Industries tab...")
marker = '<div id="pricing" class="tab-content">'
if marker in content:
    insertion = f'''{industries}

{marker}'''
    content = content.replace(marker, insertion, 1)
    print("   ✅ Industries tab inserted")
else:
    print("   ⚠️  Marker not found for Industries")

# 8. Insert Resources tab
print("✏️  Inserting Resources tab...")
marker = '<div id="pricing" class="tab-content">'
if marker in content:
    insertion = f'''{resources}

{marker}'''
    content = content.replace(marker, insertion, 1)
    print("   ✅ Resources tab inserted")
else:
    print("   ⚠️  Marker not found for Resources")

# 9. Save with UTF-8 encoding
print("\n💾 Saving index.html...")
try:
    with open("index.html", "w", encoding="utf-8", newline='\n') as f:
        f.write(content)
    print("   ✅ File saved with UTF-8 encoding")
except Exception as e:
    print(f"   ❌ Error saving file: {e}")
    sys.exit(1)

print("\n✅ Integration Complete!")
print(f"📊 File size: {len(content)} bytes")
print("🎯 Ready to commit and deploy!")
