#!/usr/bin/env python3
"""
Final Phase 1 Integration - Proper UTF-8 handling
"""

from pathlib import Path

print("🚀 Phase 1 Integration - UTF-8 Safe Version\n")

# Read files with explicit UTF-8 encoding
print("📖 Reading clean base file...")
with open("index-clean-base.html", "r", encoding="utf-8") as f:
    content = f.read()

print("📖 Reading new tab content files...")
with open("tabs/overview.html", "r", encoding="utf-8") as f:
    overview = f.read()
with open("tabs/features.html", "r", encoding="utf-8") as f:
    features = f.read()
with open("tabs/industries.html", "r", encoding="utf-8") as f:
    industries = f.read()
with open("tabs/resources.html", "r", encoding="utf-8") as f:
    resources = f.read()

# Update tabs navigation
print("✏️  Updating tabs navigation...")
old_tabs_nav = '''<div class="tabs-container">
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

new_tabs_nav = '''<div class="tabs-container">
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

content = content.replace(old_tabs_nav, new_tabs_nav)
print("   ✅ Navigation updated")

# Change document-intelligence from active to inactive
print("✏️  Updating document-intelligence tab...")
content = content.replace(
    '<div id="document-intelligence" class="tab-content active">',
    '<div id="document-intelligence" class="tab-content">'
)
print("   ✅ Updated")

# Insert Overview tab
print("✏️  Inserting Overview tab...")
marker = '<div id="document-intelligence" class="tab-content">'
new_section = f'''<div id="overview" class="tab-content active">
{overview}
</div>

{marker}'''
content = content.replace(marker, new_section, 1)
print("   ✅ Inserted")

# Insert Features tab
print("✏️  Inserting Features tab...")
marker = '<div id="document-intelligence" class="tab-content">'
new_section = f'''<div id="features" class="tab-content">
{features}
</div>

{marker}'''
content = content.replace(marker, new_section, 1)
print("   ✅ Inserted")

# Insert Industries tab
print("✏️  Inserting Industries tab...")
marker = '<div id="pricing" class="tab-content">'
new_section = f'''<div id="industries" class="tab-content">
{industries}
</div>

{marker}'''
content = content.replace(marker, new_section, 1)
print("   ✅ Inserted")

# Insert Resources tab
print("✏️  Inserting Resources tab...")
marker = '<div id="pricing" class="tab-content">'
new_section = f'''<div id="resources" class="tab-content">
{resources}
</div>

{marker}'''
content = content.replace(marker, new_section, 1)
print("   ✅ Inserted")

# Save with explicit UTF-8 encoding
print("\n💾 Saving to index.html with UTF-8 encoding...")
with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.write(content)

print("\n✅ Integration Complete!")
print("📊 File saved with UTF-8 encoding")
