#!/usr/bin/env python3
"""
Script to insert new tab content into index.html
This helps avoid file size limitations when using strReplace
"""

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def insert_after_marker(content, marker, new_content):
    """Insert new_content after the marker string"""
    parts = content.split(marker, 1)
    if len(parts) == 2:
        return parts[0] + marker + '\n' + new_content + parts[1]
    else:
        print(f"Warning: Marker not found: {marker}")
        return content

def main():
    # Read current index.html
    html = read_file('index.html')
    
    # Read new tab contents
    overview_tab = read_file('tabs/overview.html')
    features_tab = read_file('tabs/features.html')
    industries_tab = read_file('tabs/industries.html')
    resources_tab = read_file('tabs/resources.html')
    
    # Find insertion point (after tabs-container, before first tab-content)
    marker = '</div>\n</div>\n\n\n<!-- Tab Content: Document Intelligence -->'
    
    # Build new tabs content
    new_tabs = f"""

{overview_tab}

{features_tab}
"""
    
    # Insert new tabs
    html = insert_after_marker(html, marker, new_tabs)
    
    # Change document-intelligence from active to inactive
    html = html.replace(
        '<div id="document-intelligence" class="tab-content active">',
        '<div id="document-intelligence" class="tab-content">'
    )
    
    # Find where to insert industries tab (after ai-agent, before pricing)
    industries_marker = '<!-- Tab Content: Pricing -->'
    html = insert_after_marker(html, industries_marker, f'\n{industries_tab}\n')
    
    # Find where to insert resources tab (after pricing, before footer)
    resources_marker = '</div>\n\n\n<!-- Footer (Always Visible) -->'
    html = insert_after_marker(html, resources_marker, f'\n{resources_tab}\n')
    
    # Write updated file
    write_file('index-phase1.html', html)
    print("✅ Created index-phase1.html with new tabs")
    print("📝 Review the file, then rename to index.html when ready")

if __name__ == '__main__':
    main()
