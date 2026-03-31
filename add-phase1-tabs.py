#!/usr/bin/env python3
"""
Add Phase 1 tabs to existing tab-based website
Uses careful string replacement with UTF-8 encoding
"""

print("🚀 Adding Phase 1 Tabs\n")

# Read current index.html
print("📖 Reading index.html...")
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Read tab content files
print("📖 Reading tab content files...")
with open("tabs/overview.html", "r", encoding="utf-8") as f:
    overview = f.read()
with open("tabs/features.html", "r", encoding="utf-8") as f:
    features = f.read()
with open("tabs/industries.html", "r", encoding="utf-8") as f:
    industries = f.read()
with open("tabs/resources.html", "r", encoding="utf-8") as f:
    resources = f.read()

# Step 1: Update tabs navigation
print("✏️  Step 1: Updating tabs navigation...")
old_tabs = '''    <button class="tab-btn active" onclick="switchTab('document-intelligence')" data-en="Document Intelligence" data-es="Inteligencia Documental">Document Intelligence</button>
    <button class="tab-btn" onclick="switchTab('excel-copilot')" data-en="Excel Copilot" data-es="Excel Copilot">Excel Copilot</button>
    <button class="tab-btn" onclick="switchTab('wiki')" data-en="Wiki" data-es="Wiki">Wiki</button>
    <button class="tab-btn" onclick="switchTab('assets')" data-en="Assets" data-es="Activos">Assets</button>
    <button class="tab-btn" onclick="switchTab('incidents')" data-en="Incidents" data-es="Incidencias">Incidents</button>
    <button class="tab-btn" onclick="switchTab('ai-agent')" data-en="AI Agent" data-es="Agente IA">AI Agent</button>
    <button class="tab-btn" onclick="switchTab('pricing')" data-en="Pricing" data-es="Precios">Pricing</button>'''

new_tabs = '''    <button class="tab-btn active" onclick="switchTab('overview')" data-en="Overview" data-es="Resumen">Overview</button>
    <button class="tab-btn" onclick="switchTab('features')" data-en="Features" data-es="Características">Features</button>
    <button class="tab-btn" onclick="switchTab('document-intelligence')" data-en="Document Intelligence" data-es="Inteligencia Documental">Document Intelligence</button>
    <button class="tab-btn" onclick="switchTab('excel-copilot')" data-en="Excel Copilot" data-es="Excel Copilot">Excel Copilot</button>
    <button class="tab-btn" onclick="switchTab('wiki')" data-en="Wiki" data-es="Wiki">Wiki</button>
    <button class="tab-btn" onclick="switchTab('assets')" data-en="Assets" data-es="Activos">Assets</button>
    <button class="tab-btn" onclick="switchTab('incidents')" data-en="Incidents" data-es="Incidencias">Incidents</button>
    <button class="tab-btn" onclick="switchTab('ai-agent')" data-en="AI Agent" data-es="Agente IA">AI Agent</button>
    <button class="tab-btn" onclick="switchTab('industries')" data-en="Industries" data-es="Industrias">Industries</button>
    <button class="tab-btn" onclick="switchTab('pricing')" data-en="Pricing" data-es="Precios">Pricing</button>
    <button class="tab-btn" onclick="switchTab('resources')" data-en="Resources" data-es="Recursos">Resources</button>'''

if old_tabs in content:
    content = content.replace(old_tabs, new_tabs)
    print("   ✅ Navigation updated (11 tabs)")
else:
    print("   ⚠️  Old tabs not found - checking for variations...")
    # Try without exact whitespace
    if "'document-intelligence')" in content and "'pricing')" in content:
        print("   ℹ️  Tabs exist but whitespace differs - manual fix needed")

# Step 2: Make document-intelligence inactive
print("✏️  Step 2: Making document-intelligence inactive...")
content = content.replace(
    '<div id="document-intelligence" class="tab-content active">',
    '<div id="document-intelligence" class="tab-content">'
)
print("   ✅ Updated")

# Step 3: Insert Overview tab BEFORE document-intelligence
print("✏️  Step 3: Inserting Overview tab...")
marker = '<!-- Tab Content: Document Intelligence -->\n<div id="document-intelligence" class="tab-content">'
if marker in content:
    insertion = f'{overview}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Overview tab inserted")
else:
    print("   ⚠️  Marker not found")

# Step 4: Insert Features tab
print("✏️  Step 4: Inserting Features tab...")
marker = '<!-- Tab Content: Document Intelligence -->\n<div id="document-intelligence" class="tab-content">'
if marker in content:
    insertion = f'{features}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Features tab inserted")
else:
    print("   ⚠️  Marker not found")

# Step 5: Insert Industries tab BEFORE pricing
print("✏️  Step 5: Inserting Industries tab...")
marker = '<!-- Tab Content: Pricing -->\n<div id="pricing" class="tab-content">'
if marker in content:
    insertion = f'{industries}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Industries tab inserted")
else:
    print("   ⚠️  Marker not found")

# Step 6: Insert Resources tab
print("✏️  Step 6: Inserting Resources tab...")
marker = '<!-- Tab Content: Pricing -->\n<div id="pricing" class="tab-content">'
if marker in content:
    insertion = f'{resources}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Resources tab inserted")
else:
    print("   ⚠️  Marker not found")

# Save with UTF-8
print("\n💾 Saving index.html...")
with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.write(content)

print("✅ Done! File size:", len(content), "bytes")
