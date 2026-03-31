#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read with UTF-8-sig to strip BOM
with open("index.html", "r", encoding="utf-8-sig") as f:
    content = f.read()

# Write back without BOM
with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.write(content)

print(f"✅ Removed BOM, wrote {len(content)} bytes")
