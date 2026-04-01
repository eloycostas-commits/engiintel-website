#!/usr/bin/env python3
"""
Integrate Accordion System into index.html
Replaces the old module listing with the new accordion-based capabilities system
"""

import re
from pathlib import Path

def integrate_accordion():
    """Integrate the accordion system from capabilities-accordion.html into index.html"""
    
    # Read the files
    index_path = Path("index.html")
    accordion_path = Path("capabilities-accordion.html")
    
    if not index_path.exists():
        print(f"❌ Error: {index_path} not found")
        return False
    
    if not accordion_path.exists():
        print(f"❌ Error: {accordion_path} not found")
        return False
    
    # Read index.html
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Read accordion HTML
    with open(accordion_path, 'r', encoding='utf-8') as f:
        accordion_content = f.read()
    
    # Create backup
    backup_path = Path("index-backup-before-accordion.html")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"✅ Backup created: {backup_path}")
    
    # The accordion file contains everything we need - just use it as is
    # It includes the tab-content div, styles, and script
    new_features_content = accordion_content.strip()
    
    # Find and replace the old features tab content in index.html
    # Look for the pattern: <!-- Tab Content: Core --> ... <!-- Tab Content: Excel Copilot -->
    old_features_pattern = r'<!-- Tab Content: Core -->.*?(?=<!-- Tab Content: Excel Copilot -->)'
    
    if not re.search(old_features_pattern, index_content, re.DOTALL):
        print("❌ Error: Could not find old features tab content in index.html")
        print("Looking for alternative patterns...")
        
        # Try alternative pattern - look for any tab content before Excel Copilot
        alt_pattern = r'<div id="[^"]*" class="tab-content">.*?(?=<!-- Tab Content: Excel Copilot -->)'
        matches = list(re.finditer(alt_pattern, index_content, re.DOTALL))
        
        if matches:
            print(f"Found {len(matches)} tab content sections before Excel Copilot")
            # We want to replace the first one (likely the features/core tab)
            first_match = matches[0]
            print(f"Replacing content starting at position {first_match.start()}")
            
            # Replace the first tab content
            index_content = (
                index_content[:first_match.start()] +
                new_features_content +
                index_content[first_match.end():]
            )
        else:
            print("❌ Error: Could not find any tab content to replace")
            return False
    else:
        # Replace using the original pattern
        index_content = re.sub(
            old_features_pattern,
            new_features_content,
            index_content,
            flags=re.DOTALL
        )
    
    # Write the updated index.html
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print("✅ Accordion system integrated successfully!")
    print(f"✅ Updated: {index_path}")
    print("\n📋 Next steps:")
    print("1. Open index.html in your browser")
    print("2. Test the accordion expand/collapse functionality")
    print("3. Test the language switcher (EN/ES)")
    print("4. Test responsive behavior on mobile")
    print("5. Verify all 22 modules are present in the 4 pillars")
    
    return True

if __name__ == "__main__":
    print("🚀 Starting accordion integration...\n")
    success = integrate_accordion()
    
    if success:
        print("\n✅ Integration complete!")
    else:
        print("\n❌ Integration failed. Check errors above.")
