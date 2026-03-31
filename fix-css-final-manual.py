#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix line by line
fixed_lines = []
skip_mode = False

for i, line in enumerate(lines):
    # If we find the .lang-btn rule
    if '.lang-btn {' in line:
        fixed_lines.append(line)
        # Add the next lines until font-size
        continue
    
    # If we're in the corrupted section (after font-size: 0.75rem;)
    if i > 0 and 'font-size: 0.75rem;' in lines[i-1] and '// Send to n8n webhook' in line:
        # Add the missing properties
        fixed_lines.append('  cursor: pointer;\n')
        fixed_lines.append('  transition: all 0.2s;\n')
        fixed_lines.append('}\n')
        skip_mode = True
        continue
    
    # Skip until we find .lang-btn.active
    if skip_mode:
        if '.lang-btn.active' in line:
            skip_mode = False
            fixed_lines.append(line)
        continue
    
    # Also remove the stray .pricing-features line that appears in the wrong place
    if '.pricing-features li::before' in line and i < 100:  # If it's in the CSS section (early in file)
        # Check if this is in the wrong place (not after .pricing-features definition)
        if i > 0 and '.pricing-features {' not in lines[i-5:i]:
            continue  # Skip this line
    
    fixed_lines.append(line)

# Write back
with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.writelines(fixed_lines)

print("✓ Fixed CSS corruption manually")
