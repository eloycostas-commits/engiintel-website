#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix layout issues:
1. Remove duplicate "Book a Demo" button
2. Expand content width (less cramped)
3. Make cards wider for better text flow
"""

import re

print("🔧 Fixing Layout Issues\n")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📖 Read {len(content)} bytes")

# Step 1: Find and remove duplicate Book a Demo button
print("\n🔧 Step 1: Removing duplicate button...")

# Find hero-actions section
hero_actions_pattern = r'<div class="hero-actions">.*?</div>'
matches = list(re.finditer(hero_actions_pattern, content, re.DOTALL))

if len(matches) > 1:
    print(f"   Found {len(matches)} hero-actions sections")
    # Keep only the first one, remove duplicates
    for match in matches[1:]:
        content = content.replace(match.group(0), '')
        print(f"   ✓ Removed duplicate at position {match.start()}")
else:
    print("   ℹ️  No duplicate found, checking for duplicate buttons...")
    # Look for duplicate Book a Demo buttons
    book_demo_pattern = r'<button[^>]*onclick="switchTab\(\'resources\'\)"[^>]*data-en="Book a Demo"[^>]*>.*?</button>'
    demo_buttons = list(re.finditer(book_demo_pattern, content, re.DOTALL))
    if len(demo_buttons) > 2:  # More than 2 (primary + secondary is ok)
        print(f"   Found {len(demo_buttons)} Book a Demo buttons")
        # Keep first 2, remove rest
        for match in demo_buttons[2:]:
            content = content.replace(match.group(0), '')
            print(f"   ✓ Removed duplicate button")

# Step 2: Expand content width
print("\n🔧 Step 2: Expanding content width...")

# Update tab-content padding to use more horizontal space
old_padding = '.tab-content {\n  padding: 100px 60px !important;\n}'
new_padding = '.tab-content {\n  padding: 100px 120px !important;\n  max-width: 1400px;\n  margin: 0 auto;\n}'

if old_padding in content:
    content = content.replace(old_padding, new_padding)
    print("   ✓ Expanded tab-content width")

# Step 3: Make capability cards wider
print("\n🔧 Step 3: Improving card layouts...")

# Update capabilities grid to use more space
old_cap_grid = 'grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))'
new_cap_grid = 'grid-template-columns: repeat(3, 1fr)'

content = content.replace(old_cap_grid, new_cap_grid)
print("   ✓ Made capabilities grid 3 equal columns")

# Update problem stats grid
old_prob_grid = 'grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))'
new_prob_grid = 'grid-template-columns: repeat(3, 1fr)'

content = content.replace(old_prob_grid, new_prob_grid)
print("   ✓ Made problem stats 3 equal columns")

# Update solution cards grid
old_sol_grid = 'grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))'
new_sol_grid = 'grid-template-columns: repeat(3, 1fr)'

content = content.replace(old_sol_grid, new_sol_grid)
print("   ✓ Made solution cards 3 equal columns")

# Update how it works grid
old_how_grid = 'grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))'
new_how_grid = 'grid-template-columns: repeat(3, 1fr)'

content = content.replace(old_how_grid, new_how_grid)
print("   ✓ Made how it works 3 equal columns")

# Step 4: Add responsive CSS for better mobile handling
print("\n🔧 Step 4: Adding responsive CSS...")

responsive_css = """
/* Better responsive layout */
@media (max-width: 1200px) {
  .tab-content {
    padding: 80px 60px !important;
  }
}

@media (max-width: 900px) {
  .capabilities-grid,
  .problem-section > div:last-child,
  .solution-section > div:last-child,
  .how-it-works-grid {
    grid-template-columns: 1fr !important;
  }
  
  .tab-content {
    padding: 60px 30px !important;
  }
}

/* Ensure text doesn't wrap unnecessarily */
.capability-card,
.problem-stat,
.solution-card,
.how-it-works-step {
  min-width: 0; /* Allow flex items to shrink */
}

.capability-card > div:first-child,
.problem-stat > div:first-child {
  white-space: nowrap; /* Keep numbers on one line */
}
"""

# Insert before closing </style>
style_end = content.rfind('</style>')
if style_end > 0:
    content = content[:style_end] + responsive_css + '\n' + content[style_end:]
    print("   ✓ Added responsive CSS")

# Step 5: Fix any inline styles that might be causing cramping
print("\n🔧 Step 5: Adjusting inline styles...")

# Update problem section padding
content = content.replace(
    'style="margin-top: 80px; padding: 60px;',
    'style="margin-top: 80px; padding: 60px 80px;'
)

# Update how it works padding
content = content.replace(
    'style="margin-top: 80px; padding: 60px;',
    'style="margin-top: 80px; padding: 60px 80px;'
)

print("   ✓ Adjusted section padding")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f"\n✅ Done! Wrote {len(content)} bytes")
print("\n📋 Changes made:")
print("  ✓ Removed duplicate button")
print("  ✓ Expanded content width (60px → 120px padding)")
print("  ✓ Made all grids 3 equal columns (no auto-fit)")
print("  ✓ Added responsive breakpoints")
print("  ✓ Improved section padding")
print("\n🚀 Layout should be much cleaner now!")
