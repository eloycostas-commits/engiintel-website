#!/usr/bin/env python3
"""Extract components from index-clean-backup.html"""

import re

# Read the clean backup
with open('index-clean-backup.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Extracting components from index-clean-backup.html...")
print()

# 1. Extract Header (nav)
nav_match = re.search(r'(<nav>.*?</nav>)', html, re.DOTALL)
if nav_match:
    with open('components/header.html', 'w', encoding='utf-8') as f:
        f.write(nav_match.group(1))
    print("✓ components/header.html")

# 2. Extract Hero (section.hero)
hero_match = re.search(r'(<section class="hero">.*?</section>)', html, re.DOTALL)
if hero_match:
    with open('components/hero.html', 'w', encoding='utf-8') as f:
        f.write(hero_match.group(1))
    print("✓ components/hero.html")

# 3. Extract Tabs navigation
tabs_match = re.search(r'(<div class="tabs-container">.*?</div>\s*</div>)', html, re.DOTALL)
if tabs_match:
    with open('components/tabs.html', 'w', encoding='utf-8') as f:
        f.write(tabs_match.group(1))
    print("✓ components/tabs.html")

# 4. Extract Overview tab
overview_match = re.search(r'(<div id="overview" class="tab-content active">.*?)(?=<div id="features" class="tab-content">)', html, re.DOTALL)
if overview_match:
    with open('components/overview-tab.html', 'w', encoding='utf-8') as f:
        f.write(overview_match.group(1))
    print("✓ components/overview-tab.html")

# 5. Extract Features tab
features_match = re.search(r'(<div id="features" class="tab-content">.*?)(?=<div id="document-intelligence" class="tab-content">)', html, re.DOTALL)
if features_match:
    with open('components/features-tab.html', 'w', encoding='utf-8') as f:
        f.write(features_match.group(1))
    print("✓ components/features-tab.html")

# 6. Extract Document Intelligence tab
doc_intel_match = re.search(r'(<div id="document-intelligence" class="tab-content">.*?)(?=<div id="excel-copilot" class="tab-content">)', html, re.DOTALL)
if doc_intel_match:
    with open('components/document-intelligence-tab.html', 'w', encoding='utf-8') as f:
        f.write(doc_intel_match.group(1))
    print("✓ components/document-intelligence-tab.html")

# 7. Extract Excel Copilot tab
excel_match = re.search(r'(<div id="excel-copilot" class="tab-content">.*?)(?=<div id="wiki" class="tab-content">)', html, re.DOTALL)
if excel_match:
    with open('components/excel-copilot-tab.html', 'w', encoding='utf-8') as f:
        f.write(excel_match.group(1))
    print("✓ components/excel-copilot-tab.html")

# 8. Extract Wiki tab
wiki_match = re.search(r'(<div id="wiki" class="tab-content">.*?)(?=<div id="assets" class="tab-content">)', html, re.DOTALL)
if wiki_match:
    with open('components/wiki-tab.html', 'w', encoding='utf-8') as f:
        f.write(wiki_match.group(1))
    print("✓ components/wiki-tab.html")

# 9. Extract Assets tab
assets_match = re.search(r'(<div id="assets" class="tab-content">.*?)(?=<div id="incidents" class="tab-content">)', html, re.DOTALL)
if assets_match:
    with open('components/assets-tab.html', 'w', encoding='utf-8') as f:
        f.write(assets_match.group(1))
    print("✓ components/assets-tab.html")

# 10. Extract Incidents tab
incidents_match = re.search(r'(<div id="incidents" class="tab-content">.*?)(?=<div id="ai-agent" class="tab-content">)', html, re.DOTALL)
if incidents_match:
    with open('components/incidents-tab.html', 'w', encoding='utf-8') as f:
        f.write(incidents_match.group(1))
    print("✓ components/incidents-tab.html")

# 11. Extract AI Agent tab
agent_match = re.search(r'(<div id="ai-agent" class="tab-content">.*?)(?=<div id="industries" class="tab-content">)', html, re.DOTALL)
if agent_match:
    with open('components/ai-agent-tab.html', 'w', encoding='utf-8') as f:
        f.write(agent_match.group(1))
    print("✓ components/ai-agent-tab.html")

# 12. Extract Industries tab
industries_match = re.search(r'(<div id="industries" class="tab-content">.*?)(?=<div id="resources" class="tab-content">)', html, re.DOTALL)
if industries_match:
    with open('components/industries-tab.html', 'w', encoding='utf-8') as f:
        f.write(industries_match.group(1))
    print("✓ components/industries-tab.html")

# 13. Extract Resources tab
resources_match = re.search(r'(<div id="resources" class="tab-content">.*?)(?=<div id="pricing" class="tab-content">)', html, re.DOTALL)
if resources_match:
    with open('components/resources-tab.html', 'w', encoding='utf-8') as f:
        f.write(resources_match.group(1))
    print("✓ components/resources-tab.html")

# 14. Extract Pricing tab
pricing_match = re.search(r'(<div id="pricing" class="tab-content">.*?)(?=<footer)', html, re.DOTALL)
if pricing_match:
    with open('components/pricing-tab.html', 'w', encoding='utf-8') as f:
        f.write(pricing_match.group(1))
    print("✓ components/pricing-tab.html")

# 15. Extract Footer
footer_match = re.search(r'(<footer.*?</footer>)', html, re.DOTALL)
if footer_match:
    with open('components/footer.html', 'w', encoding='utf-8') as f:
        f.write(footer_match.group(1))
    print("✓ components/footer.html")

print()
print("All components extracted successfully!")
print()
print("Component files created:")
print("  - components/header.html")
print("  - components/hero.html")
print("  - components/tabs.html")
print("  - components/overview-tab.html")
print("  - components/features-tab.html")
print("  - components/document-intelligence-tab.html")
print("  - components/excel-copilot-tab.html")
print("  - components/wiki-tab.html")
print("  - components/assets-tab.html")
print("  - components/incidents-tab.html")
print("  - components/ai-agent-tab.html")
print("  - components/industries-tab.html")
print("  - components/resources-tab.html")
print("  - components/pricing-tab.html")
print("  - components/footer.html")
