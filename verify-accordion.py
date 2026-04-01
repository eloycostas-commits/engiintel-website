#!/usr/bin/env python3
"""
Verify that the accordion system is properly integrated
"""

from pathlib import Path
import re

def verify_accordion():
    """Verify accordion integration"""
    
    index_path = Path("index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔍 Verifying Accordion Integration...\n")
    
    checks = []
    
    # Check 1: Accordion HTML in Features tab
    if 'id="features"' in content and 'capabilities-accordion' in content:
        checks.append(("✅", "Accordion HTML found in Features tab"))
    else:
        checks.append(("❌", "Accordion HTML NOT found in Features tab"))
    
    # Check 2: All 4 pillars present
    pillars = ['accordion-core', 'accordion-security', 'accordion-connectivity', 'accordion-analysis']
    found_pillars = [p for p in pillars if p in content]
    if len(found_pillars) == 4:
        checks.append(("✅", f"All 4 accordion pillars found: {', '.join(found_pillars)}"))
    else:
        checks.append(("❌", f"Only {len(found_pillars)}/4 pillars found"))
    
    # Check 3: Accordion CSS styles
    if '.accordion-item' in content and '.accordion-header' in content:
        checks.append(("✅", "Accordion CSS styles found"))
    else:
        checks.append(("❌", "Accordion CSS styles NOT found"))
    
    # Check 4: toggleAccordion function
    if 'function toggleAccordion' in content:
        checks.append(("✅", "toggleAccordion JavaScript function found"))
    else:
        checks.append(("❌", "toggleAccordion function NOT found"))
    
    # Check 5: DOMContentLoaded listener for accordion
    if 'document.addEventListener(\'DOMContentLoaded\'' in content and 'firstAccordion' in content:
        checks.append(("✅", "Accordion initialization script found"))
    else:
        checks.append(("❌", "Accordion initialization script NOT found"))
    
    # Check 6: Module cards
    module_count = content.count('class="module-card"')
    if module_count >= 22:
        checks.append(("✅", f"Found {module_count} module cards (expected 22+)"))
    else:
        checks.append(("⚠️", f"Found only {module_count} module cards (expected 22+)"))
    
    # Print results
    for icon, message in checks:
        print(f"{icon} {message}")
    
    # Summary
    passed = sum(1 for icon, _ in checks if icon == "✅")
    total = len(checks)
    
    print(f"\n📊 Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n✅ Accordion integration verified successfully!")
        print("\n💡 If you still don't see the accordion:")
        print("1. Clear your browser cache (Ctrl+Shift+Delete)")
        print("2. Hard refresh (Ctrl+F5 or Ctrl+Shift+R)")
        print("3. Try opening in incognito/private mode")
        print("4. Check browser console for JavaScript errors (F12)")
        print("5. Make sure you're opening the correct index.html file")
    else:
        print("\n❌ Some checks failed. Review the errors above.")
    
    return passed == total

if __name__ == "__main__":
    verify_accordion()
