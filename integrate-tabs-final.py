#!/usr/bin/env python3
"""
Final Phase 1 Integration - Add 4 new tabs to index.html
This script properly integrates Overview, Features, Industries, and Resources tabs
"""

from pathlib import Path
import re

print("🚀 Phase 1 Integration - Adding New Tabs\n")

# 1. Read the clean base file
print("📖 Reading clean index.html...")
try:
    content = Path("index-clean-from-git.html").read_text(encoding='utf-8')
except UnicodeDecodeError:
    content = Path("index-clean-from-git.html").read_text(encoding='latin-1')

# 2. Read new tab content
print("📖 Reading new tab content files...")
overview = Path("tabs/overview.html").read_text(encoding='utf-8')
features = Path("tabs/features.html").read_text(encoding='utf-8')
industries = Path("tabs/industries.html").read_text(encoding='utf-8')
resources = Path("tabs/resources.html").read_text(encoding='utf-8')

# 3. Update tabs navigation - add new tabs and reorder
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
print("   ✅ Navigation updated (11 tabs)")

# 4. Change document-intelligence from active to inactive
print("✏️  Updating document-intelligence tab...")
content = content.replace(
    '<div id="document-intelligence" class="tab-content active">',
    '<div id="document-intelligence" class="tab-content">'
)
print("   ✅ Document-intelligence is now inactive")

# 5. Insert Overview tab content BEFORE document-intelligence
print("✏️  Inserting Overview tab...")
marker = '<div id="document-intelligence" class="tab-content">'
new_section = f'''<div id="overview" class="tab-content active">
{overview}
</div>

{marker}'''
content = content.replace(marker, new_section, 1)
print("   ✅ Overview tab inserted (active by default)")

# 6. Insert Features tab AFTER Overview
print("✏️  Inserting Features tab...")
marker = '<div id="document-intelligence" class="tab-content">'
new_section = f'''<div id="features" class="tab-content">
{features}
</div>

{marker}'''
content = content.replace(marker, new_section, 1)
print("   ✅ Features tab inserted")

# 7. Insert Industries tab BEFORE Pricing
print("✏️  Inserting Industries tab...")
marker = '<div id="pricing" class="tab-content">'
new_section = f'''<div id="industries" class="tab-content">
{industries}
</div>

{marker}'''
content = content.replace(marker, new_section, 1)
print("   ✅ Industries tab inserted")

# 8. Insert Resources tab AFTER Industries, BEFORE Pricing
print("✏️  Inserting Resources tab...")
marker = '<div id="pricing" class="tab-content">'
new_section = f'''<div id="resources" class="tab-content">
{resources}
</div>

{marker}'''
content = content.replace(marker, new_section, 1)
print("   ✅ Resources tab inserted")

# 9. Save to index.html
print("\n💾 Saving to index.html...")
Path("index.html").write_text(content, encoding='utf-8')

print("\n✅ Phase 1 Integration Complete!\n")
print("📊 Summary:")
print("   - Total tabs: 11")
print("   - New tabs: Overview (active), Features, Industries, Resources")
print("   - Existing tabs: Document Intelligence, Excel, Wiki, Assets, Incidents, AI Agent, Pricing")
print("\n🎯 Next Steps:")
print("   1. Test locally: Open index.html in browser")
print("   2. git add index.html")
print("   3. git commit -m 'Phase 1: Integrate all new tabs into website'")
print("   4. git push origin main")
print("\n🌐 Vercel will auto-deploy in ~2 minutes!")
