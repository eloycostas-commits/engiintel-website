#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the corrupted section (around line 79)
# Look for .lang-btn { and fix it
in_lang_btn = False
fixed_lines = []
skip_until_closing_brace = False

for i, line in enumerate(lines):
    # Check if we're at the .lang-btn rule
    if '.lang-btn {' in line and not in_lang_btn:
        in_lang_btn = True
        fixed_lines.append(line)
        continue
    
    # If we're in .lang-btn and hit the JavaScript comment, start skipping
    if in_lang_btn and '// Send to n8n webhook' in line:
        # Add the missing CSS properties before the corruption
        fixed_lines.append('  cursor: pointer;\n')
        fixed_lines.append('  transition: all 0.2s;\n')
        fixed_lines.append('}\n')
        skip_until_closing_brace = True
        in_lang_btn = False
        continue
    
    # Skip lines until we find .lang-btn.active
    if skip_until_closing_brace:
        if '.lang-btn.active' in line:
            skip_until_closing_brace = False
            fixed_lines.append(line)
        continue
    
    fixed_lines.append(line)

# Write back
with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.writelines(fixed_lines)

print("✓ Fixed CSS corruption manually")
