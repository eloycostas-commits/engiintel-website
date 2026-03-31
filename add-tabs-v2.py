#!/usr/bin/env python3
"""
Add Phase 1 tabs - Version 2
Uses div IDs as markers instead of comments
"""

print("🚀 Adding Phase 1 Tabs (v2)\n")

# Read files
print("📖 Reading files...")
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

with open("tabs/overview.html", "r", encoding="utf-8") as f:
    overview = f.read()
with open("tabs/features.html", "r", encoding="utf-8") as f:
    features = f.read()
with open("tabs/industries.html", "r", encoding="utf-8") as f:
    industries = f.read()
with open("tabs/resources.html", "r", encoding="utf-8") as f:
    resources = f.read()

# Step 1: Update navigation (find and replace the button list)
print("✏️  Step 1: Updating navigation...")
# Find the tabs div and replace its content
import re

# Pattern to match the entire tabs button list
pattern = r'(<div class="tabs">)(.*?)(</div>\s*</div>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    new_buttons = '''
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
  '''
    content = content[:match.start(2)] + new_buttons + content[match.end(2):]
    print("   ✅ Navigation updated (11 tabs)")
else:
    print("   ⚠️  Navigation not found")

# Step 2: Make document-intelligence inactive
print("✏️  Step 2: Making document-intelligence inactive...")
content = content.replace(
    '<div id="document-intelligence" class="tab-content active">',
    '<div id="document-intelligence" class="tab-content">'
)
print("   ✅ Updated")

# Step 3: Insert Overview tab BEFORE document-intelligence
print("✏️  Step 3: Inserting Overview tab...")
marker = '<div id="document-intelligence" class="tab-content">'
if marker in content:
    insertion = f'{overview}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Overview tab inserted")
else:
    print("   ⚠️  Marker not found")

# Step 4: Insert Features tab
print("✏️  Step 4: Inserting Features tab...")
marker = '<div id="document-intelligence" class="tab-content">'
if marker in content:
    insertion = f'{features}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Features tab inserted")
else:
    print("   ⚠️  Marker not found")

# Step 5: Insert Industries tab BEFORE pricing
print("✏️  Step 5: Inserting Industries tab...")
marker = '<div id="pricing" class="tab-content">'
if marker in content:
    insertion = f'{industries}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Industries tab inserted")
else:
    print("   ⚠️  Marker not found")

# Step 6: Insert Resources tab
print("✏️  Step 6: Inserting Resources tab...")
marker = '<div id="pricing" class="tab-content">'
if marker in content:
    insertion = f'{resources}\n\n{marker}'
    content = content.replace(marker, insertion, 1)
    print("   ✅ Resources tab inserted")
else:
    print("   ⚠️  Marker not found")

# Save
print("\n💾 Saving...")
with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.write(content)

print(f"✅ Done! File size: {len(content)} bytes")
print("\n🎯 Next: Test locally, then commit and push")
