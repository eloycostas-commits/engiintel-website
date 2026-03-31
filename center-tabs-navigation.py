#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Center the tabs navigation to match the centered content layout
"""

import re

print("🔧 Centering Tabs Navigation\n")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📖 Read {len(content)} bytes")

# Find and update tabs-container CSS
print("\n🔧 Updating tabs-container CSS...")

# Find the .tabs-container style
tabs_container_pattern = r'\.tabs-container \{[^}]+\}'
match = re.search(tabs_container_pattern, content, re.DOTALL)

if match:
    old_css = match.group(0)
    
    # Create new centered version
    new_css = """.tabs-container {
  position: sticky;
  top: 70px;
  z-index: 90;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  padding: 0 120px;
  max-width: 1400px;
  margin: 0 auto;
}"""
    
    content = content.replace(old_css, new_css)
    print("   ✓ Updated .tabs-container to be centered")
else:
    print("   ⚠️  Could not find .tabs-container CSS")

# Also update .tabs to center the buttons
print("\n🔧 Centering tab buttons...")

tabs_pattern = r'\.tabs \{[^}]+\}'
match = re.search(tabs_pattern, content, re.DOTALL)

if match:
    old_css = match.group(0)
    
    new_css = """.tabs {
  display: flex;
  gap: 0;
  overflow-x: auto;
  scrollbar-width: none;
  justify-content: center;
  flex-wrap: wrap;
}"""
    
    content = content.replace(old_css, new_css)
    print("   ✓ Centered tab buttons")
else:
    print("   ⚠️  Could not find .tabs CSS")

# Add responsive behavior
print("\n🔧 Adding responsive CSS...")

responsive_tabs_css = """
/* Responsive tabs alignment */
@media (max-width: 1200px) {
  .tabs-container {
    padding: 0 60px;
  }
}

@media (max-width: 900px) {
  .tabs-container {
    padding: 0 30px;
  }
  
  .tabs {
    justify-content: flex-start;
    flex-wrap: nowrap;
  }
}
"""

# Insert before closing </style>
style_end = content.rfind('</style>')
if style_end > 0:
    content = content[:style_end] + responsive_tabs_css + '\n' + content[style_end:]
    print("   ✓ Added responsive tabs CSS")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f"\n✅ Done! Wrote {len(content)} bytes")
print("\n📋 Changes made:")
print("  ✓ Centered tabs-container (matches content width)")
print("  ✓ Centered tab buttons with flex justify-content")
print("  ✓ Added flex-wrap for better responsive behavior")
print("  ✓ Maintained horizontal scroll on mobile")
print("\n🚀 Tabs navigation now aligns with content!")
