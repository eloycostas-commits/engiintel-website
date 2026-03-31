#!/usr/bin/env python3
"""
Phase 1 Final Integration Script
Properly integrates all new tab content into index.html
"""

import re
from pathlib import Path

print("🚀 Starting Phase 1 Final Integration...")

# Read current index.html
print("📖 Reading index.html...")
index_path = Path("index.html")
content = index_path.read_text(encoding='utf-8')

# Read tab content files
print("📖 Reading tab content files...")
overview = Path("tabs/overview.html").read_text(encoding='utf-8')
features = Path("tabs/features.html").read_text(encoding='utf-8')
industries = Path("tabs/industries.html").read_text(encoding='utf-8')
resources = Path("tabs/resources.html").read_text(encoding='utf-8')

# Step 1: Insert Overview tab content BEFORE document-intelligence
print("✏️  Inserting Overview tab content...")
marker1 = '<!-- Tab Content: Document Intelligence -->'
if marker1 in content:
    new_section = f'''<!-- Tab Content: Overview -->
{overview}

{marker1}'''
    content = content.replace(marker1, new_section, 1)
    print("   ✅ Overview tab inserted")
else:
    print("   ⚠️  Marker not found for Overview")

# Step 2: Insert Features tab content AFTER Overview, BEFORE document-intelligence
print("✏️  Inserting Features tab content...")
marker2 = '<!-- Tab Content: Document Intelligence -->'
if marker2 in content:
    new_section = f'''<!-- Tab Content: Features -->
{features}

{marker2}'''
    content = content.replace(marker2, new_section, 1)
    print("   ✅ Features tab inserted")
else:
    print("   ⚠️  Marker not found for Features")

# Step 3: Change document-intelligence from active to inactive
print("✏️  Updating document-intelligence tab...")
content = content.replace(
    'id="document-intelligence" class="tab-content active"',
    'id="document-intelligence" class="tab-content"'
)
print("   ✅ Document-intelligence tab updated")

# Step 4: Insert Industries tab content BEFORE Pricing
print("✏️  Inserting Industries tab content...")
marker3 = '<!-- Tab Content: Pricing -->'
if marker3 in content:
    new_section = f'''<!-- Tab Content: Industries -->
{industries}

{marker3}'''
    content = content.replace(marker3, new_section, 1)
    print("   ✅ Industries tab inserted")
else:
    print("   ⚠️  Marker not found for Industries")

# Step 5: Insert Resources tab content AFTER Industries, BEFORE Pricing
print("✏️  Inserting Resources tab content...")
marker4 = '<!-- Tab Content: Pricing -->'
if marker4 in content:
    new_section = f'''<!-- Tab Content: Resources -->
{resources}

{marker4}'''
    content = content.replace(marker4, new_section, 1)
    print("   ✅ Resources tab inserted")
else:
    print("   ⚠️  Marker not found for Resources")

# Save the updated content
print("💾 Saving updated index.html...")
index_path.write_text(content, encoding='utf-8')

print("\n✅ Phase 1 Final Integration Complete!")
print("\n📊 Summary:")
print("   - Added Overview tab (active by default)")
print("   - Added Features tab")
print("   - Added Industries tab")
print("   - Added Resources tab")
print("   - Total tabs: 11")
print("\n🎯 Next steps:")
print("   1. Test: Open index.html in browser")
print("   2. Commit: git add index.html")
print("   3. Commit: git commit -m 'Phase 1: Add all new tab content to index.html'")
print("   4. Deploy: git push origin main")
print("\n🌐 Vercel will auto-deploy in ~2 minutes after push!")
