#!/usr/bin/env python3
"""
Fix Overview tab - add missing closing div
"""

from pathlib import Path

def fix_overview_tab():
    """Add the missing closing div for Overview tab"""
    
    index_path = Path("index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Create backup
    backup_path = Path("index-backup-tab-fix.html")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f"✅ Backup created: {backup_path}")
    
    # Find the line with "<!-- Tab Content: Features -->"
    features_line_idx = None
    for i, line in enumerate(lines):
        if '<!-- Tab Content: Features -->' in line:
            features_line_idx = i
            break
    
    if features_line_idx is None:
        print("❌ Could not find Features tab comment")
        return False
    
    print(f"✅ Found Features tab at line {features_line_idx + 1}")
    
    # Insert closing div before the Features tab comment
    # Add it 2 lines before (after the empty lines)
    insert_idx = features_line_idx
    
    # Add the closing div
    lines.insert(insert_idx, '  </div>\n')
    lines.insert(insert_idx + 1, '\n')
    
    print("✅ Added closing </div> for Overview tab")
    
    # Write updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"\n✅ Updated: {index.html}")
    print("\n📋 Fix Applied:")
    print(f"  ✅ Inserted closing </div> at line {insert_idx + 1}")
    print("  ✅ Overview tab now properly closed")
    print("\n🧪 Test:")
    print("1. Refresh browser (Ctrl+F5)")
    print("2. Click Overview tab - should see screenshots")
    print("3. Click Features tab - should NOT see screenshots")
    print("4. All other tabs should work")
    
    return True

if __name__ == "__main__":
    print("🚀 Fixing Overview Tab...\n")
    success = fix_overview_tab()
    
    if success:
        print("\n✅ Overview tab fixed!")
    else:
        print("\n❌ Failed to fix.")
