#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the file as binary to see actual bytes
with open('index.html', 'rb') as f:
    content = f.read()

# Decode with UTF-8
content = content.decode('utf-8', errors='replace')

# Fix all corrupted characters
replacements = {
    # CSS content properties
    "'ÔåÆ'": "'•'",
    "'Ô£ô'": "'•'",
    
    # Euro symbols
    'Ôé¼': '€',
    
    # Module icons
    'ÔÜá´©Å': '●',
    
    # Any other corrupted emoji patterns
    'ƒôè': '●',
    'ƒôê': '●',
    'ƒÆ¥': '●',
    'ƒôÜ': '●',
    'ƒòÉ': '●',
    'ƒÅó': '●',
    'ƒöº': '●',
    'ƒôÄ': '●',
    'ƒñû': '●',
    'ƒøá´©Å': '●',
    'ƒöä': '●',
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Write back with UTF-8 encoding
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Fixed all corrupted characters")
print("✓ Replaced CSS bullet characters with •")
print("✓ Replaced corrupted euro symbols with €")
print("✓ Replaced corrupted module icons with ●")
