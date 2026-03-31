#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuild the corrupted CSS section
"""

# Read file with latin-1 to handle any encoding
with open("index.html", "r", encoding="latin-1") as f:
    lines = f.readlines()

print(f"📖 Read {len(lines)} lines")

# Find the corrupted section (around line 67-84)
# Replace lines 67-84 with clean CSS
clean_css = """.lang-switch {
  display: flex;
  gap: 4px;
  margin-left: 20px;
}
.lang-btn {
  background: none;
  border: 1px solid var(--border);
  color: var(--text-dim);
  padding: 6px 12px;
  font-family: 'DM Mono', monospace;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;
}
.lang-btn.active, .lang-btn:hover {
"""

# Find where corruption starts (line with ".lang-switch {")
start_idx = None
for i, line in enumerate(lines):
    if ".lang-switch {" in line:
        start_idx = i
        break

if start_idx is None:
    print("❌ Could not find .lang-switch")
    exit(1)

print(f"✓ Found .lang-switch at line {start_idx + 1}")

# Find where clean CSS resumes (line with "border-color: var(--accent);")
end_idx = None
for i in range(start_idx, min(start_idx + 30, len(lines))):
    if "border-color: var(--accent);" in lines[i]:
        end_idx = i - 1  # The line before "border-color"
        break

if end_idx is None:
    print("❌ Could not find end of corruption")
    exit(1)

print(f"✓ Found end at line {end_idx + 1}")
print(f"🔧 Replacing lines {start_idx + 1} to {end_idx + 1}")

# Replace the corrupted section
new_lines = lines[:start_idx] + [clean_css + "\n"] + lines[end_idx + 1:]

# Write back with UTF-8
with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.writelines(new_lines)

print(f"✅ Fixed! Wrote {len(new_lines)} lines")
