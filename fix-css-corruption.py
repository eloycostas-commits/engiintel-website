#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix CSS corruption in index.html
Removes BOM and fixes corrupted characters
"""

import re

print("🔧 Fixing CSS corruption...\n")

# Read with error handling
try:
    with open("index.html", "r", encoding="utf-8-sig") as f:
        content = f.read()
except UnicodeDecodeError:
    print("⚠️  UTF-8 decode failed, trying with latin-1...")
    with open("index.html", "r", encoding="latin-1") as f:
        content = f.read()

print(f"📖 Read {len(content)} bytes")

# Remove any remaining BOM characters
content = content.replace('\ufeff', '')
content = content.replace('´╗┐', '')

# Fix corrupted checkmark
content = content.replace("content: 'Ô£ô'", "content: '✓'")
content = content.replace("content: 'ÔÇô'", "content: '✓'")

# Fix corrupted bullet
content = content.replace("content: 'ÔåÆ'", "content: '•'")
content = content.replace("content: 'Ô£ö'", "content: '•'")

# Fix corrupted em dash
content = content.replace('ÔÇö', '—')
content = content.replace('ÔÇô', '–')

# Fix corrupted box drawing characters
content = content.replace('ÔòöÔòÉÔòÉÔòÉ', '╔═══')
content = content.replace('ÔòÜÔòÉÔòÉÔòÉ', '╚═══')
content = content.replace('Ôòæ', '║')
content = content.replace('Ôòù', '╗')
content = content.replace('ÔòØ', '╝')

# Remove any JavaScript code that got mixed into CSS
# Look for patterns like "const webhookUrl" in CSS sections
css_pattern = r'(<style>.*?)(const webhookUrl.*?fetch\(webhookUrl.*?\})(.*?</style>)'
content = re.sub(css_pattern, r'\1\3', content, flags=re.DOTALL)

# Fix incomplete CSS rules
# Find .lang-switch { display: flex; followed by .module-features
content = re.sub(
    r'(\.lang-switch \{\s*display: flex;)\s*(\.module-features)',
    r'\1\n  gap: 4px;\n  margin-left: 20px;\n}\n\n\2',
    content
)

# Fix incomplete .lang-btn rule
content = re.sub(
    r'(\.lang-btn \{[^}]*font-size: 0\.75rem;)\s*(\.pricing-features)',
    r'\1\n  cursor: pointer;\n  transition: all 0.2s;\n}\n\n\2',
    content
)

# Write back with clean UTF-8
with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.write(content)

print(f"✅ Fixed! Wrote {len(content)} bytes")
print("🔍 Check diagnostics to verify CSS is clean")
