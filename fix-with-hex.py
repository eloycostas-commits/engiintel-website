#!/usr/bin/env python3
import subprocess

print("Extracting from git...")
result = subprocess.run(
    ["git", "show", "2065634:index.html"],
    capture_output=True
)

content = result.stdout

print(f"Read {len(content)} bytes")

# Replace using byte patterns
# Corrupted bullet: bytes for the corrupted sequence
content = content.replace(b"content: '\xc3\x94\xc3\xa5\xc3\x86'", b"content: '\xe2\x80\xa2'")  # bullet
content = content.replace(b"content: '\xc3\x94\xc2\xa3\xc3\xb4'", b"content: '\xe2\x9c\x93'")  # checkmark

print("Writing fixed version...")
with open("index.html", "wb") as f:
    f.write(content)

print(f"Done! Wrote {len(content)} bytes")
