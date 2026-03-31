#!/usr/bin/env python3
"""
Complete Integration Script for Phase 1
Integrates all new tabs and replaces screenshot placeholders
"""

import re

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("Starting Phase 1 complete integration...")
    
    # Read all files
    print("Reading files...")
    html = read_file('index.html')
    overview = read_file('tabs/overview.html')
    features = read_file('tabs/features.html')
    industries = read_file('tabs/industries.html')
    resources = read_file('tabs/resources.html')
    
    # Screenshot replacements
    screenshot_map = {
        r'<div class="screenshot-placeholder"[^>]*>\[Screenshot: Query \+ Results\]</div>': 
            '<img src="screenshots/comparar documentos.jpg" alt="Natural Language Query" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">',
        r'<div class="screenshot-placeholder"[^>]*>\[Screenshot: Architecture Diagram\]</div>':
            '<img src="screenshots/panel principal.jpg" alt="Architecture" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">',
        r'<div class="screenshot-placeholder"[^>]*>\[Screenshot: OCR Processing\]</div>':
            '<img src="screenshots/panel principal.jpg" alt="OCR Processing" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">',
        r'<div class="screenshot-placeholder"[^>]*>\[Screenshot: Chart Generation\]</div>':
            '<img src="screenshots/are de analisis.jpg" alt="Chart Generation" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">',
        r'<div class="screenshot-placeholder"[^>]*>\[Screenshot: Connectors\]</div>':
            '<img src="screenshots/panel principal.jpg" alt="Connectors" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">',
        r'<div class="screenshot-placeholder"[^>]*>\[Screenshot: Audit Log\]</div>':
            '<img src="screenshots/Paneld e Administración.jpg" alt="Audit Log" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">',
        r'<div class="screenshot-placeholder"[^>]*>\[Screenshot: Docker Deploy\]</div>':
            '<img src="screenshots/panel principal.jpg" alt="Docker Deploy" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">',
        r'<div class="screenshot-placeholder"[^>]*>\[Screenshot: Upload Interface\]</div>':
            '<img src="screenshots/panel principal.jpg" alt="Upload Interface" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">',
    }
    
    # Replace screenshots in overview tab
    print("Replacing screenshots in overview...")
    for pattern, replacement in screenshot_map.items():
        overview = re.sub(pattern, replacement, overview)
    
    # Step 1: Insert Overview and Features tabs after tabs-container
    print("Inserting Overview and Features tabs...")
    marker1 = '</div>\n</div>\n\n\n<!-- Tab Content: Document Intelligence -->'
    replacement1 = f'</div>\n</div>\n\n\n{overview}\n\n{features}\n\n<!-- Tab Content: Document Intelligence -->'
    html = html.replace(marker1, replacement1)
    
    # Step 2: Change document-intelligence from active to inactive
    print("Updating active tab...")
    html = html.replace(
        '<div id="document-intelligence" class="tab-content active">',
        '<div id="document-intelligence" class="tab-content">'
    )
    
    # Step 3: Insert Industries tab before Pricing
    print("Inserting Industries tab...")
    marker2 = '<!-- Tab Content: Pricing -->'
    replacement2 = f'{industries}\n\n\n{marker2}'
    html = html.replace(marker2, replacement2)
    
    # Step 4: Insert Resources tab before Footer
    print("Inserting Resources tab...")
    marker3 = '<!-- Footer (Always Visible) -->'
    replacement3 = f'{resources}\n\n\n{marker3}'
    html = html.replace(marker3, replacement3)
    
    # Write final file
    print("Writing final file...")
    write_file('index-complete.html', html)
    
    print("\n✓ Integration complete!")
    print("\nCreated: index-complete.html")
    print("\nNext steps:")
    print("  1. Open index-complete.html in your browser")
    print("  2. Test all tabs and screenshots")
    print("  3. If everything works:")
    print("     - Backup: mv index.html index-old.html")
    print("     - Deploy: mv index-complete.html index.html")
    print("  4. Push to Vercel")

if __name__ == '__main__':
    main()
