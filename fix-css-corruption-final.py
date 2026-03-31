#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and fix the corrupted .lang-btn CSS rule
# Pattern: .lang-btn { ... font-size: 0.75rem; [JavaScript code] }
pattern = r'(\.lang-btn \{[^}]*?font-size: 0\.75rem;)\s*//[^}]*?const response = await fetch\(webhookUrl, \{\s*\}'

replacement = r'\1\n  cursor: pointer;\n  transition: all 0.2s;\n}'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Fixed CSS corruption")
