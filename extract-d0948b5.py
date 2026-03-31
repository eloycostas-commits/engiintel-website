#!/usr/bin/env python3
import subprocess

print("Extracting d0948b5...")
result = subprocess.run(
    ["git", "show", "d0948b5:index.html"],
    capture_output=True
)

content = result.stdout
print(f"Read {len(content)} bytes")

# Fix corrupted characters using byte patterns
content = content.replace(b'\xc3\x94\xc3\xa5\xc3\x86', b'\xe2\x80\xa2')  # bullet
content = content.replace(b'\xc3\x94\xc2\xa3\xc3\xb4', b'\xe2\x9c\x93')  # checkmark
content = content.replace(b'\xc3\x94\xc3\x87\xc3\xb6', b'\xe2\x80\x94')  # em dash

print("Writing...")
with open("index.html", "wb") as f:
    f.write(content)

print(f"Done! {len(content)} bytes")
