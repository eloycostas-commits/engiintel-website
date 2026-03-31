#!/usr/bin/env python3
import subprocess
import sys

print("🔧 Comprehensive Website Fix\n")
print("=" * 60)

# Step 1: Get clean tab-based version from git
print("\n📥 Step 1: Extracting clean tab-based version from git...")
result = subprocess.run(
    ["git", "show", "2065634:index.html"],
    capture_output=True,
    text=True,
    encoding='latin-1'  # Use latin-1 to preserve bytes
)

if result.returncode != 0:
    print(f"❌ Git extraction failed: {result.stderr}")
    sys.exit(1)

content = result.stdout
print(f"✓ Extracted {len(content)} bytes")

# Step 2: Fix CSS corruption
print("\n🔧 Step 2: Fixing CSS corruption...")
fixes = [
    ("content: 'ÔåÆ'", "content: '•'"),
    ("content: 'Ô£ô'", "content: '✓'"),
    ("content: 'Ã"Ã¥Ã†'", "content: '•'"),
    ("content: 'Ã"Â£Ã´'", "content: '✓'"),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print(f"✓ Fixed: {old[:20]}... → {new}")

# Step 3: Write clean version
print("\n💾 Step 3: Writing clean version...")
with open("index.html", "w", encoding="utf-8", newline='\n') as f:
    f.write(content)

print(f"✓ Wrote {len(content)} bytes with UTF-8 encoding")

print("\n✅ Base file is now clean!")
print("📋 Next steps:")
print("   1. Run add-phase1-tabs.py to add Overview, Features, Industries, Resources tabs")
print("   2. Run complete-pricing-restore.py to add the pricing calculator")
print("   3. Test in browser")
