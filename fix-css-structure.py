#!/usr/bin/env python3

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Find and fix line 68 (index 67)
if len(lines) > 67:
    line68 = lines[67]
    if "module-features li::before" in line68:
        lines[67] = line68.replace("'ÔåÆ'", "'•'").replace("'Ã"Ã¥Ã†'", "'•'")
        print(f"Fixed line 68")

# Find and fix line 78 (index 77)
if len(lines) > 77:
    line78 = lines[77]
    if "pricing-features li::before" in line78:
        lines[77] = line78.replace("'Ô£ô'", "'✓'").replace("'Ã"Â£Ã´'", "'✓'")
        print(f"Fixed line 78")

with open("index.html", "w", encoding="utf-8", newline='') as f:
    f.writelines(lines)

print("Done!")
