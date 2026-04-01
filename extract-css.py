#!/usr/bin/env python3
"""Extract CSS from index-clean-backup.html to css/styles.css"""

import re

# Read the clean backup
with open('index-clean-backup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all CSS between <style> and </style>
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if not style_match:
    print("ERROR: No <style> tag found")
    exit(1)

css_content = style_match.group(1).strip()

# Write to css/styles.css
with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print(f"✓ Extracted {len(css_content)} characters of CSS")
print(f"✓ Wrote css/styles.css")
