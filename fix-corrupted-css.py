#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove JavaScript code that's mixed into CSS
# Pattern: CSS rule followed by JavaScript comments/code followed by closing brace
corrupted_pattern = r'(\.lang-btn \{[^}]*?font-size: 0\.75rem;)\s*//[^}]*?const response = await fetch\(webhookUrl, \{\s*\}'

# Replace with clean CSS
clean_css = r'\1\n  cursor: pointer;\n  transition: all 0.2s;\n}'

content = re.sub(corrupted_pattern, clean_css, content, flags=re.DOTALL)

# Also fix any HTML that got mixed into CSS
# Remove any <div> tags that appear in the CSS section
style_start = content.find('<style>')
style_end = content.find('</style>')
if style_start != -1 and style_end != -1:
    css_section = content[style_start:style_end]
    # Remove HTML tags from CSS
    css_section = re.sub(r'<div[^>]*>.*?</div>', '', css_section, flags=re.DOTALL)
    css_section = re.sub(r'<button[^>]*>.*?</button>', '', css_section, flags=re.DOTALL)
    content = content[:style_start] + css_section + content[style_end:]

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Fixed corrupted CSS sections")
