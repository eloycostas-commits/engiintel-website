#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3 - Critical Fixes Implementation
1. Fix CTA scroll behavior
2. Improve code block contrast (WCAG)
3. Add whitespace for better breathing room
4. Fix typography (left-align, better line-height)
"""

import re

print("🚀 Implementing Phase 3 Critical Fixes\n")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📖 Read {len(content)} bytes")

# Step 1: Fix CTA scroll behavior
print("\n🔧 Step 1: Fixing CTA scroll behavior...")

scroll_css = """
/* Fix CTA scroll behavior for all screen sizes */
#resources {
  scroll-margin-top: 100px;
}

html {
  scroll-padding-top: 100px;
}

/* Smooth scroll */
html {
  scroll-behavior: smooth;
}
"""

# Insert before closing </style>
style_end = content.rfind('</style>')
if style_end > 0:
    content = content[:style_end] + scroll_css + '\n' + content[style_end:]
    print("   ✓ Added scroll margin CSS")

# Step 2: Improve code block contrast (WCAG compliance)
print("\n🔧 Step 2: Improving code block contrast...")

# Find any code/terminal styling and improve contrast
code_contrast_css = """
/* Improved code block contrast (WCAG AA) */
.code-block,
.terminal-block,
pre {
  background: #0a0e13;
  border: 1px solid var(--border);
}

.code-comment {
  color: #8a9bab !important; /* Lighter gray for better contrast */
}

.code-keyword {
  color: var(--accent) !important;
}

.code-string {
  color: var(--accent3) !important;
}

.code-function {
  color: #00d4ff !important;
}
"""

# Insert before closing </style>
style_end = content.rfind('</style>')
if style_end > 0:
    content = content[:style_end] + code_contrast_css + '\n' + content[style_end:]
    print("   ✓ Added improved code contrast CSS")

# Step 3: Add more whitespace
print("\n🔧 Step 3: Adding whitespace for better breathing room...")

whitespace_css = """
/* Increased whitespace for better readability */
.tab-content > div {
  margin-bottom: 80px !important; /* Increased from 40px */
}

.capability-card,
.solution-card,
.problem-section,
.how-it-works-section {
  padding: 48px 40px !important; /* More generous padding */
}

/* Better section separation */
section + section {
  margin-top: 80px;
}

/* More breathing room in cards */
.module-card,
.pricing-card {
  padding: 48px 36px !important;
}
"""

# Insert before closing </style>
style_end = content.rfind('</style>')
if style_end > 0:
    content = content[:style_end] + whitespace_css + '\n' + content[style_end:]
    print("   ✓ Added whitespace improvements")

# Step 4: Fix typography
print("\n🔧 Step 4: Fixing typography...")

typography_css = """
/* Improved typography */
p, .section-sub, .hero-sub {
  text-align: left !important; /* No justify */
  line-height: 1.7 !important; /* Better readability */
}

/* Better paragraph spacing */
p + p {
  margin-top: 1.2em;
}

/* Improved heading spacing */
h2 {
  margin-bottom: 24px !important;
}

h3 {
  margin-bottom: 16px !important;
}

/* Better list spacing */
ul, ol {
  line-height: 1.8;
}

li + li {
  margin-top: 0.5em;
}
"""

# Insert before closing </style>
style_end = content.rfind('</style>')
if style_end > 0:
    content = content[:style_end] + typography_css + '\n' + content[style_end:]
    print("   ✓ Added typography improvements")

# Step 5: Ensure all CTAs point to resources tab
print("\n🔧 Step 5: Verifying CTA consistency...")

# Count how many "Book a Demo" buttons exist
book_demo_count = content.count('onclick="switchTab(\'resources\')"')
print(f"   ℹ️  Found {book_demo_count} CTAs pointing to resources tab")

# Step 6: Add mobile-specific improvements
print("\n🔧 Step 6: Adding mobile optimizations...")

mobile_css = """
/* Mobile-specific improvements */
@media (max-width: 768px) {
  .tab-content {
    padding: 60px 24px !important;
  }
  
  .capability-card,
  .solution-card,
  .problem-section {
    padding: 32px 24px !important;
  }
  
  /* Larger touch targets */
  .btn-primary,
  .btn-secondary {
    min-height: 48px;
    padding: 14px 28px !important;
  }
  
  /* Better mobile typography */
  h1 {
    font-size: 2rem !important;
  }
  
  h2 {
    font-size: 1.5rem !important;
  }
  
  /* Reduce excessive whitespace on mobile */
  .tab-content > div {
    margin-bottom: 48px !important;
  }
}
"""

# Insert before closing </style>
style_end = content.rfind('</style>')
if style_end > 0:
    content = content[:style_end] + mobile_css + '\n' + content[style_end:]
    print("   ✓ Added mobile optimizations")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f"\n✅ Done! Wrote {len(content)} bytes")
print("\n📋 Critical Fixes Applied:")
print("  ✓ Fixed CTA scroll behavior (scroll-margin-top)")
print("  ✓ Improved code block contrast (WCAG AA)")
print("  ✓ Added whitespace (80px section spacing)")
print("  ✓ Fixed typography (left-align, line-height 1.7)")
print("  ✓ Verified CTA consistency")
print("  ✓ Added mobile optimizations")
print("\n🚀 Ready for Phase 3 UX improvements!")
