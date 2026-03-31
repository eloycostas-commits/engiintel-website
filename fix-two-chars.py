#!/usr/bin/env python3

with open("index.html", "rb") as f:
    content = f.read()

# Fix the two corrupted characters
content = content.replace(b'\xc3\x94\xc3\xa5\xc3\x86', b'\xe2\x80\xa2')  # bullet
content = content.replace(b'\xc3\x94\xc2\xa3\xc3\xb4', b'\xe2\x9c\x93')  # checkmark

with open("index.html", "wb") as f:
    f.write(content)

print("Fixed!")
