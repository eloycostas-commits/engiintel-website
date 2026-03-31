#!/usr/bin/env python3
"""
Step 1: Carefully add accordion system to Features tab
"""

import re
from pathlib import Path

# Read the clean working version
with open("index.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Create backup
with open("index-backup-step1.html", 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Backup created: index-backup-step1.html")

# Read the accordion HTML
with open("capabilities-accordion.html", 'r', encoding='utf-8') as f:
    accordion_html = f.read()

# Extract just the Features tab div (without the style and script tags)
accordion_match = re.search(r'(<div id="features".*?</div>)\s*<style>', accordion_html, re.DOTALL)
if not accordion_match:
    print("❌ Could not extract accordion HTML")
    exit(1)

features_accordion = accordion_match.group(1)

# Extract the CSS
css_match = re.search(r'<style>(.*?)</style>', accordion_html, re.DOTALL)
if not css_match:
    print("❌ Could not extract CSS")
    exit(1)

accordion_css = css_match.group(1)

# Extract the JavaScript
js_match = re.search(r'<script>(.*?)</script>', accordion_html, re.DOTALL)
if not js_match:
    print("❌ Could not extract JavaScript")
    exit(1)

accordion_js = js_match.group(1)

# Step 1: Replace Features tab content
# Find the Features tab and replace it
features_pattern = r'<div id="features" class="tab-content">.*?(?=\n<div id="[^"]*" class="tab-content">)'

if not re.search(features_pattern, content, re.DOTALL):
    print("❌ Could not find Features tab")
    exit(1)

content = re.sub(features_pattern, features_accordion + '\n', content, flags=re.DOTALL)
print("✅ Replaced Features tab content")

# Step 2: Add CSS before closing </style> tag (find the LAST one in head)
# Find all </style> tags and add before the last one in <head>
head_end = content.find('</head>')
if head_end == -1:
    print("❌ Could not find </head>")
    exit(1)

# Find the last </style> before </head>
head_content = content[:head_end]
last_style_pos = head_content.rfind('</style>')

if last_style_pos == -1:
    print("❌ Could not find </style> in head")
    exit(1)

# Insert CSS before the last </style>
content = content[:last_style_pos] + "\n" + accordion_css + "\n" + content[last_style_pos:]
print("✅ Added accordion CSS")

# Step 3: Add JavaScript before closing </body> tag
body_end = content.rfind('</body>')
if body_end == -1:
    print("❌ Could not find </body>")
    exit(1)

# Insert JavaScript before </body>
content = content[:body_end] + "\n<script>\n" + accordion_js + "\n</script>\n\n" + content[body_end:]
print("✅ Added accordion JavaScript")

# Write the updated content
with open("index.html", 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Step 1 Complete: Accordion system added to Features tab")
print("📋 Test: Open index.html and click Features tab")
