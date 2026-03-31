#!/usr/bin/env python3
"""
Final attempt - Add Phase 1 tabs to clean tab-based version
Fixes encoding issues and adds new tabs
"""

print("🚀 Final Phase 1 Integration\n")

# Read the tab-based file
print("📖 Reading tab-based index...")
with open("index-tab-based.html", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

# Read new tab content
print("📖 Reading new tab files...")
with open("tabs/overview.html", "r", encoding="utf-8") as f:
    overview = f.read()
with open("tabs/features.html", "r", encoding="utf-8") as f:
    features = f.read()
with open("tabs/industries.html", "r", encoding="utf-8") as f:
    industries = f.read()
with open("tabs/resources.html", "r", encoding="utf-8") as f:
    resources = f.read()

# Fix common encoding issues
print("✏️  Fixing encoding issues...")
content = content.replace("ÔÇö", "—")
content = content.replace("├│", "ó")
content = content.replace("├®", "é")
content = content.replace("├¡", "á")
content = content.replace("├▒", "ñ")
content = content.replace("├¡", "í")
content = content.replace("├║", "ú")
content = content.replace("­ƒöì", "🔍")
content = content.replace("­ƒôä", "📄")
content = content.replace("­ƒöù", "🔗")
print("   ✅ Encoding fixed")

# Step 1: Update navigation
print("✏️  Step 1: Updating navigation...")
old_nav = '''    <button class="tab-btn active" onclick="switchTab('document-intelligence')" data-en="Document Intelligence" data-es="Inteligencia Documental">Document Intelligence</button>
    <button class="tab-btn" onclick="switchTab('excel-copilot')" data-en="Excel Copilot" data-es="Excel Copilot">Excel Copilot</button>
    <button class="tab-btn" onclick="switchTab('wiki')" data-en="Wiki" data-es="Wiki">Wiki</button>
    <button class="tab-btn" onclick="switchTab('assets')" data-en="Assets" data-es="Activos">Assets</button>
    <button class="tab-btn" onclick="switchTab('incidents')" data-en="Incidents" data-es="Incidencias">Incidents</button>
    <button class="tab-btn" onclick="switchTab('ai-agent')" data-en="AI Agent" data-es="Agente IA">AI Agent</button>
    <button class="tab-btn" onclick="switchTab('pricing')" data-en="Pricing" data-es="Precios">Pricing</button>'''

new_nav = '''    <button class="tab-btn active" onclick="switchTab('overview')" data-en="Overview" data-es="Resumen">Overview</button>
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

if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print("   ✅ Navigation updated (11 tabs)")
else:
    print("   ⚠️  Navigation not found")

# Step 2: Make document-intelligence inactive
print("✏️  Step 2: Updating document-intelligence...")
content = content.replace(
    '<div id="document-intelligence" class="tab-content active">',
    '<div id="document-intelligence" class="tab-content">'
)
print("   ✅ Updated")

# Step 3: Insert Overview tab
print("✏️  Step 3: Inserting Overview tab...")
marker = '<div id="document-intelligence" class="tab-content">'
if marker in content:
    insertion = f'{overview}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Overview inserted")
else:
    print("   ⚠️  Marker not found")

# Step 4: Insert Features tab
print("✏️  Step 4: Inserting Features tab...")
if marker in content:
    insertion = f'{features}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Features inserted")
else:
    print("   ⚠️  Marker not found")

# Step 5: Insert Industries tab
print("✏️  Step 5: Inserting Industries tab...")
marker = '<div id="pricing" class="tab-content">'
if marker in content:
    insertion = f'{industries}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Industries inserted")
else:
    print("   ⚠️  Marker not found")

# Step 6: Insert Resources tab
print("✏️  Step 6: Inserting Resources tab...")
if marker in content:
    insertion = f'{resources}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Resources inserted")
else:
    print("   ⚠️  Marker not found")

# Save to index.html
print("\n💾 Saving to index.html...")
with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.write(content)

print(f"✅ Done! File size: {len(content)} bytes")
print("\n🎯 Ready to commit and deploy!")
