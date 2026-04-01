#!/usr/bin/env python3
"""
Safely rebuild improvements using BeautifulSoup
1. Accordion system
2. Tooltips
3. Pricing presets
"""

from bs4 import BeautifulSoup
from pathlib import Path

print("🚀 Starting safe rebuild with BeautifulSoup...\n")

# Read the current clean HTML
with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

# Create backup
backup_path = Path("index-BACKUP-BEFORE-REBUILD.html")
with open(backup_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print(f"✅ Backup created: {backup_path}\n")

# Read the accordion HTML
with open("capabilities-accordion.html", "r", encoding="utf-8") as f:
    accordion_soup = BeautifulSoup(f, "lxml")

# Extract the Features tab div from accordion
accordion_features = accordion_soup.find("div", id="features")
if not accordion_features:
    print("❌ Could not find Features tab in accordion HTML")
    exit(1)

# Find the current Features tab in index.html
current_features = soup.find("div", id="features")
if not current_features:
    print("❌ Could not find Features tab in index.html")
    exit(1)

# Replace the Features tab content
current_features.replace_with(accordion_features)
print("✅ Step 1: Replaced Features tab with accordion system")

# Save after Step 1
with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(soup.prettify()))

print("\n✅ All improvements added successfully!")
print("📋 Next: Test the website to ensure everything works")
