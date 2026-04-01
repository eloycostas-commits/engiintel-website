#!/usr/bin/env python3
"""
Replace the Features tab content with the new accordion system
"""

from pathlib import Path
import re

def replace_features_tab():
    """Replace the features tab with accordion system"""
    
    # Read files
    index_path = Path("index.html")
    accordion_path = Path("capabilities-accordion.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    with open(accordion_path, 'r', encoding='utf-8') as f:
        accordion_content = f.read()
    
    # Create backup
    backup_path = Path("index-backup-before-accordion.html")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"✅ Backup created: {backup_path}")
    
    # Find the features tab content
    # Pattern: <div id="features" class="tab-content"> ... </div> (before next tab)
    pattern = r'(<div id="features" class="tab-content">)(.*?)(<!-- Tab Content:)'
    
    match = re.search(pattern, index_content, re.DOTALL)
    
    if not match:
        print("❌ Error: Could not find features tab in index.html")
        return False
    
    print(f"✅ Found features tab at position {match.start()}")
    
    # Extract just the HTML content (without style and script tags) from accordion
    # We only want the div content, not the styles/scripts (those go in head)
    accordion_html = re.sub(r'<style>.*?</style>', '', accordion_content, flags=re.DOTALL)
    accordion_html = re.sub(r'<script>.*?</script>', '', accordion_html, flags=re.DOTALL)
    accordion_html = accordion_html.strip()
    
    # Extract the styles and script separately
    style_match = re.search(r'<style>(.*?)</style>', accordion_content, re.DOTALL)
    script_match = re.search(r'<script>(.*?)</script>', accordion_content, re.DOTALL)
    
    accordion_styles = style_match.group(1) if style_match else ""
    accordion_script = script_match.group(1) if script_match else ""
    
    # Replace the features tab content
    # Keep the opening div tag, replace the content, keep the comment for next tab
    new_content = match.group(1) + "\n" + accordion_html.replace('<div id="features" class="tab-content">', '').replace('</div>\n\n', '\n') + "\n</div>\n\n" + match.group(3)
    
    index_content = index_content[:match.start()] + new_content + index_content[match.end():]
    
    # Add the accordion styles to the existing <style> section
    style_section_end = index_content.find('</style>')
    if style_section_end > 0:
        index_content = (
            index_content[:style_section_end] +
            "\n\n/* Accordion System Styles */\n" +
            accordion_styles +
            "\n" +
            index_content[style_section_end:]
        )
        print("✅ Added accordion styles to <style> section")
    
    # Add the accordion script before the closing </body> tag
    body_end = index_content.rfind('</body>')
    if body_end > 0:
        index_content = (
            index_content[:body_end] +
            "\n<script>\n" +
            accordion_script +
            "\n</script>\n\n" +
            index_content[body_end:]
        )
        print("✅ Added accordion script before </body>")
    
    # Write the updated file
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"✅ Updated: {index_path}")
    print("\n📋 Changes made:")
    print("1. Replaced features tab content with accordion system")
    print("2. Added accordion CSS styles")
    print("3. Added accordion JavaScript")
    print("\n🧪 Next steps:")
    print("1. Open index.html in browser")
    print("2. Click on 'Features' tab")
    print("3. Test accordion expand/collapse")
    print("4. Test language switcher")
    print("5. Test on mobile (resize browser)")
    
    return True

if __name__ == "__main__":
    print("🚀 Replacing Features tab with Accordion system...\n")
    success = replace_features_tab()
    
    if success:
        print("\n✅ Replacement complete!")
    else:
        print("\n❌ Replacement failed.")
