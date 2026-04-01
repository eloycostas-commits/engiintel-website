#!/usr/bin/env python3
"""
Fix tab structure - screenshots are bleeding into other tabs
Need to properly close the Overview tab
"""

import re
from pathlib import Path

def fix_tab_structure():
    """Fix the Overview tab closing div"""
    
    index_path = Path("index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    backup_path = Path("index-backup-before-tab-fix.html")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_path}")
    
    # Find the end of the screenshots section and add closing div for Overview tab
    # Pattern: end of last screenshot div, then we need to close the screenshots container and the overview tab
    pattern = r'(</div>\s*</div>\s*</div>\s*\n\s*\n\s*\n)(<!-- Tab Content: Features -->)'
    
    # Replace with proper closing divs
    replacement = r'\1  </div>\n\n\2'
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        print("✅ Added closing div for Overview tab")
    else:
        print("⚠️  Pattern not found, trying alternative approach...")
        
        # Alternative: Find the screenshots section end and add closing div before Features tab
        alt_pattern = r'(Track usage patterns.*?</div>\s*\n\s*</div>\s*\n\s*</div>\s*\n\s*\n\s*\n)(<!-- Tab Content: Features -->)'
        
        if re.search(alt_pattern, content, re.DOTALL):
            content = re.sub(alt_pattern, r'\1  </div>\n\n\2', content, flags=re.DOTALL)
            print("✅ Added closing div for Overview tab (alternative method)")
        else:
            print("❌ Could not find pattern to fix")
            return False
    
    # Write updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Updated: {index_path}")
    print("\n📋 Fix Applied:")
    print("  ✅ Added closing </div> for Overview tab")
    print("  ✅ Screenshots now contained within Overview tab")
    print("\n🧪 Test:")
    print("1. Open index.html")
    print("2. Click Overview tab - should see screenshots")
    print("3. Click Features tab - should NOT see screenshots")
    print("4. Click other tabs - should work normally")
    
    return True

if __name__ == "__main__":
    print("🚀 Fixing Tab Structure...\n")
    success = fix_tab_structure()
    
    if success:
        print("\n✅ Tab structure fixed!")
    else:
        print("\n❌ Failed to fix tab structure.")
