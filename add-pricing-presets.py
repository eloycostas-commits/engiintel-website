#!/usr/bin/env python3
"""
Add pricing presets to the calculator
Allows users to quickly select common configurations
"""

import re
from pathlib import Path

def add_pricing_presets():
    """Add preset buttons to pricing calculator"""
    
    index_path = Path("index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    backup_path = Path("index-backup-before-presets.html")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_path}")
    
    # Define presets
    presets_html = """
          <!-- Pricing Presets -->
          <div style="margin-bottom: 32px;">
            <div class="calc-section-label" data-en="Quick presets" data-es="Preajustes rápidos">Quick presets</div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 24px;">
              
              <!-- Preset 1: Starter -->
              <button onclick="applyPreset('starter')" style="background: var(--surface); border: 1px solid var(--border); padding: 16px; cursor: pointer; transition: all 0.2s; text-align: left;" onmouseover="this.style.borderColor='rgba(0,212,255,0.3)'" onmouseout="this.style.borderColor='var(--border)'">
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.9rem; color: var(--text); margin-bottom: 4px;" data-en="Starter" data-es="Inicial">Starter</div>
                <div style="font-size: 0.75rem; color: var(--text-dim); margin-bottom: 8px;" data-en="Core + Wiki" data-es="Core + Wiki">Core + Wiki</div>
                <div style="font-family: 'DM Mono', monospace; font-size: 0.85rem; color: var(--accent);" data-en="~€12/seat" data-es="~€12/usuario">~€12/seat</div>
              </button>
              
              <!-- Preset 2: Professional -->
              <button onclick="applyPreset('professional')" style="background: var(--surface2); border: 2px solid var(--accent); padding: 16px; cursor: pointer; transition: all 0.2s; text-align: left; position: relative;" onmouseover="this.style.boxShadow='0 4px 20px rgba(0,212,255,0.2)'" onmouseout="this.style.boxShadow='none'">
                <div style="position: absolute; top: 8px; right: 8px; background: var(--accent); color: var(--bg); padding: 2px 8px; font-size: 0.65rem; font-family: 'DM Mono', monospace; font-weight: 700;" data-en="POPULAR" data-es="POPULAR">POPULAR</div>
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.9rem; color: var(--text); margin-bottom: 4px;" data-en="Professional" data-es="Profesional">Professional</div>
                <div style="font-size: 0.75rem; color: var(--text-dim); margin-bottom: 8px;" data-en="Core + Excel + Wiki + Assets" data-es="Core + Excel + Wiki + Activos">Core + Excel + Wiki + Assets</div>
                <div style="font-family: 'DM Mono', monospace; font-size: 0.85rem; color: var(--accent);" data-en="~€20/seat" data-es="~€20/usuario">~€20/seat</div>
              </button>
              
              <!-- Preset 3: Enterprise -->
              <button onclick="applyPreset('enterprise')" style="background: var(--surface); border: 1px solid var(--border); padding: 16px; cursor: pointer; transition: all 0.2s; text-align: left;" onmouseover="this.style.borderColor='rgba(0,212,255,0.3)'" onmouseout="this.style.borderColor='var(--border)'">
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.9rem; color: var(--text); margin-bottom: 4px;" data-en="Enterprise" data-es="Empresa">Enterprise</div>
                <div style="font-size: 0.75rem; color: var(--text-dim); margin-bottom: 8px;" data-en="All modules included" data-es="Todos los módulos incluidos">All modules included</div>
                <div style="font-family: 'DM Mono', monospace; font-size: 0.85rem; color: var(--accent);" data-en="~€32/seat" data-es="~€32/usuario">~€32/seat</div>
              </button>
              
            </div>
          </div>
"""
    
    # Find the pricing calculator section and add presets before "Select modules"
    pattern = r'(<div class="calc-section-label" data-en="Select modules")'
    
    if re.search(pattern, content):
        content = re.sub(pattern, presets_html + r'\1', content)
        print("✅ Added pricing presets HTML")
    else:
        print("⚠️  Could not find 'Select modules' section")
        return False
    
    # Add JavaScript for preset functionality
    preset_script = """
// Pricing Presets
function applyPreset(presetName) {
  // Clear all selections first
  selected.clear();
  document.querySelectorAll('.calc-module-toggle').forEach(el => {
    el.classList.remove('selected');
    const checkId = el.id ? el.id.replace('mod-', 'chk-') : null;
    if (checkId) {
      const check = document.getElementById(checkId);
      if (check) check.textContent = '';
    }
  });
  
  // Apply preset selections
  const presets = {
    'starter': ['wiki'],
    'professional': ['excel', 'wiki', 'ops'],
    'enterprise': ['ops', 'excel', 'wiki', 'incidents', 'agent', 'analytics']
  };
  
  const modules = presets[presetName] || [];
  modules.forEach(modId => {
    selected.add(modId);
    const el = document.getElementById('mod-' + modId);
    const chk = document.getElementById('chk-' + modId);
    if (el) el.classList.add('selected');
    if (chk) chk.textContent = '✓';
  });
  
  // Set default seats based on preset
  const defaultSeats = {
    'starter': 5,
    'professional': 15,
    'enterprise': 50
  };
  
  const seats = defaultSeats[presetName] || 10;
  document.getElementById('seatsInput').value = seats;
  
  // Recalculate price
  calcPrice();
  
  // Visual feedback
  const buttons = document.querySelectorAll('[onclick^="applyPreset"]');
  buttons.forEach(btn => {
    btn.style.transform = '';
  });
  event.target.closest('button').style.transform = 'scale(0.95)';
  setTimeout(() => {
    event.target.closest('button').style.transform = '';
  }, 150);
}
"""
    
    # Add preset script before closing </script> tag (before the last one)
    # Find the last script tag before </body>
    body_end = content.rfind('</body>')
    last_script_end = content.rfind('</script>', 0, body_end)
    
    if last_script_end > 0:
        content = content[:last_script_end] + "\n" + preset_script + "\n" + content[last_script_end:]
        print("✅ Added preset JavaScript")
    else:
        print("⚠️  Could not find script section")
        return False
    
    # Write updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Updated: {index_path}")
    print("\n📋 Presets Added:")
    print("  ✅ Starter - Core + Wiki (~€12/seat)")
    print("  ✅ Professional - Core + Excel + Wiki + Assets (~€20/seat)")
    print("  ✅ Enterprise - All modules (~€32/seat)")
    print("\n🧪 Test:")
    print("1. Open index.html")
    print("2. Go to Pricing tab")
    print("3. Click on preset buttons")
    print("4. Modules should auto-select")
    print("5. Price should update automatically")
    
    return True

if __name__ == "__main__":
    print("🚀 Adding Pricing Presets...\n")
    success = add_pricing_presets()
    
    if success:
        print("\n✅ Presets added successfully!")
    else:
        print("\n❌ Failed to add presets.")
