#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read the file with UTF-8 encoding
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix &euro; in URLs (should be ? for query parameters)
content = content.replace('&euro;', '?')

# Remove all corrupted emoji characters and replace with simple text bullets
emoji_replacements = {
    'ƒôè': '●',  # Document icon
    'ƒôê': '●',  # Lock icon
    'ƒÆ¥': '●',  # Page icon
    'ƒôÜ': '●',  # Chart icon
    'ƒòÉ': '●',  # Link icon
    'ƒÅó': '●',  # Clipboard icon
    'ƒöº': '●',  # Factory icon
    'ƒôÄ': '●',  # Plane icon
    'ƒñû': '●',  # Energy icon
    'ƒøá´©Å': '●',  # Building icon
    'ƒöä': '●',  # Ship icon
}

for old, new in emoji_replacements.items():
    content = content.replace(old, new)

# Write back with UTF-8 encoding
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Fixed &euro; in URLs")
print("✓ Replaced all corrupted emoji characters with bullets")
print("✓ File saved with UTF-8 encoding")
