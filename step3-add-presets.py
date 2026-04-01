#!/usr/bin/env python3
"""
Step 3: Add pricing presets (Starter, Professional, Enterprise)
"""

import re
from pathlib import Path

# Read current version
with open("index.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Create backup
with open("index-backup-step3.html", 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Backup created: index-backup-step3.html")

# Step 1: Add preset CSS
preset_css = """
/* Pricing Presets */
.pricing-presets {
  display: flex;
  gap: 16px;
  margin-bottom: 32px;
  justify-content: center;
  flex-wrap: wrap;
}

.preset-btn {
  padding: 16px 32px;
  background: var(--surface);
  border: 2px solid var(--border);
  color: var(--text);
  font-family: 'Syne', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
  border-radius: 4px;
  min-width: 180px;
  text-align: center;
}

.preset-btn:hover {
  border-color: var(--accent);
  background: rgba(0, 212, 255, 0.05);
}

.preset-btn.active {
  border-color: var(--accent);
  background: rgba(0, 212, 255, 0.1);
  color: var(--accent);
}

.preset-label {
  display: block;
  font-size: 1.1rem;
  margin-bottom: 4px;
}

.preset-desc {
  display: block;
  font-size: 0.75rem;
  color: var(--text-dim);
  font-family: 'DM Mono', monospace;
}
"""

# Find last </style> in head
head_end = content.find('</head>')
head_content = content[:head_end]
last_style_pos = head_content.rfind('</style>')

content = content[:last_style_pos] + "\n" + preset_css + "\n" + content[last_style_pos:]
print("✅ Added preset CSS")

# Step 2: Add preset buttons HTML before the calculator
presets_html = """
  <!-- Pricing Presets -->
  <div class="pricing-presets">
    <button class="preset-btn" onclick="applyPreset('starter')">
      <span class="preset-label" data-en="Starter" data-es="Inicial">Starter</span>
      <span class="preset-desc" data-en="5 seats · Core only" data-es="5 seats · Solo Core">5 seats · Core only</span>
    </button>
    <button class="preset-btn" onclick="applyPreset('professional')">
      <span class="preset-label" data-en="Professional" data-es="Profesional">Professional</span>
      <span class="preset-desc" data-en="10 seats · Core + 3 modules" data-es="10 seats · Core + 3 módulos">10 seats · Core + 3 modules</span>
    </button>
    <button class="preset-btn" onclick="applyPreset('enterprise')">
      <span class="preset-label" data-en="Enterprise" data-es="Empresa">Enterprise</span>
      <span class="preset-desc" data-en="25 seats · All modules" data-es="25 seats · Todos los módulos">25 seats · All modules</span>
    </button>
  </div>

"""

# Find the pricing calculator and insert presets before it
calc_pattern = r'(  <!-- Interactive pricing calculator -->)'
content = re.sub(calc_pattern, presets_html + r'\1', content)
print("✅ Added preset buttons HTML")

# Step 3: Add preset JavaScript
preset_js = """
// Pricing Presets
function applyPreset(preset) {
  // Clear all selections first
  selected.clear();
  document.querySelectorAll('.calc-module-toggle').forEach(el => {
    el.classList.remove('selected');
    const chk = el.querySelector('.calc-mod-check');
    if (chk && chk.id) chk.textContent = '';
  });
  
  // Remove active class from all preset buttons
  document.querySelectorAll('.preset-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  
  // Add active class to clicked preset
  event.target.closest('.preset-btn').classList.add('active');
  
  if (preset === 'starter') {
    // 5 seats, Core only
    document.getElementById('seatsInput').value = 5;
  } else if (preset === 'professional') {
    // 10 seats, Core + Operations + Excel + Wiki
    document.getElementById('seatsInput').value = 10;
    toggleMod('ops');
    toggleMod('excel');
    toggleMod('wiki');
  } else if (preset === 'enterprise') {
    // 25 seats, All modules
    document.getElementById('seatsInput').value = 25;
    toggleMod('ops');
    toggleMod('excel');
    toggleMod('wiki');
    toggleMod('incidents');
    toggleMod('agent');
    toggleMod('analytics');
  }
  
  calcPrice();
}
"""

# Find the closing </script> before </body>
body_end = content.rfind('</body>')
last_script_end = content[:body_end].rfind('</script>')

if last_script_end == -1:
    print("❌ Could not find </script>")
    exit(1)

# Insert before the closing </script>
content = content[:last_script_end] + "\n" + preset_js + "\n" + content[last_script_end:]
print("✅ Added preset JavaScript")

# Write updated content
with open("index.html", 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Step 3 Complete: Pricing presets added")
print("📋 Test: Go to Pricing tab and click preset buttons")
