#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print(f"📖 Read {len(content)} bytes")

# Fix the specific corrupted characters
replacements = [
    ("'Ã"Ã¥Ã†'", "'•'"),  # Corrupted bullet
    ("'Ã"Â£Ã´'", "'✓'"),  # Corrupted checkmark
    ("'ÔåÆ'", "'•'"),
    ("'Ô£ô'", "'✓'"),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"✓ Replaced {old} with {new}")

if count == 0:
    print("⚠️  No replacements made - checking hex...")
    # Try to find the actual bytes
    import re
    matches = re.findall(r"content: '([^']+)'", content)
    unique = set(matches)
    print(f"Found {len(unique)} unique content values:")
    for m in sorted(unique):
        if len(m) < 10:  # Only show short ones
            print(f"  '{m}' = {m.encode('utf-8').hex()}")

with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.write(content)

print(f"✅ Wrote {len(content)} bytes")
