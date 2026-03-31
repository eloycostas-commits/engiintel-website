#!/usr/bin/env python3
"""
Day 1: Layout Redesign Implementation
- Expand content width to 1200px
- Add CSS for two-column benefits layout
- Prepare for accordion integration
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def expand_content_width(html):
    """Task 1: Expand content width from 800px to 1200px"""
    print("✓ Expanding content width to 1200px...")
    
    # Update tab-content max-width (already at 1400px, keep it)
    # Update section-sub max-width
    html = re.sub(
        r'\.section-sub \{ color: var\(--text-mid\); font-size: 1rem; line-height: 1\.75; max-width: 600px;',
        r'.section-sub { color: var(--text-mid); font-size: 1rem; line-height: 1.75; max-width: 800px;',
        html
    )
    
    # Update hero-sub max-width
    html = re.sub(
        r'\.hero-sub \{ font-size: 1\.1rem; color: var\(--text-mid\); line-height: 1\.7; margin-bottom: 36px; max-width: 600px;',
        r'.hero-sub { font-size: 1.1rem; color: var(--text-mid); line-height: 1.7; margin-bottom: 36px; max-width: 800px;',
        html
    )
    
    # Update p max-width
    html = re.sub(
        r'p \{\s*max-width: 800px;',
        r'p { max-width: 900px;',
        html
    )
    
    return html

def add_two_column_css(html):
    """Task 2: Add CSS for two-column benefits layout"""
    print("✓ Adding two-column benefits CSS...")
    
    two_column_css = '''
/* Two-Column Benefits Layout */
.benefits-section {
  max-width: 1200px;
  margin: 60px auto;
  padding: 0 60px;
}

.benefits-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.benefits-text {
  text-align: left;
}

.benefits-text h2 {
  margin-bottom: 24px;
}

.benefits-text ul {
  list-style: none;
  margin-top: 24px;
}

.benefits-text li {
  padding: 12px 0;
  padding-left: 32px;
  position: relative;
  font-size: 1rem;
  color: var(--text-mid);
  line-height: 1.6;
}

.benefits-text li::before {
  content: '●';
  position: absolute;
  left: 0;
  color: var(--accent);
  font-size: 1.2rem;
}

.benefits-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.roi-card {
  background: var(--surface);
  border: 2px solid var(--accent);
  padding: 48px 40px;
  text-align: center;
  border-radius: 8px;
  box-shadow: 0 8px 32px rgba(0, 212, 255, 0.15);
}

.roi-value {
  font-family: 'Syne', sans-serif;
  font-size: 4rem;
  font-weight: 800;
  color: var(--accent);
  line-height: 1;
  margin-bottom: 12px;
}

.roi-label {
  font-family: 'DM Mono', monospace;
  font-size: 0.9rem;
  color: var(--text-dim);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 24px;
}

.roi-breakdown {
  font-size: 0.85rem;
  color: var(--text-mid);
  line-height: 1.8;
  text-align: left;
  padding-top: 24px;
  border-top: 1px solid var(--border);
}

/* Responsive: Stack on mobile */
@media (max-width: 900px) {
  .benefits-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  
  .benefits-section {
    padding: 0 30px;
  }
  
  .roi-card {
    padding: 36px 28px;
  }
  
  .roi-value {
    font-size: 3rem;
  }
}
'''
    
    # Insert before the closing </style> tag
    html = html.replace('</style>', two_column_css + '\n</style>')
    
    return html

def add_full_width_hero_css(html):
    """Task 3: Add full-width hero background"""
    print("✓ Adding full-width hero background...")
    
    hero_css = '''
/* Full-Width Hero Background */
.hero {
  background: radial-gradient(ellipse at top, rgba(0, 212, 255, 0.08) 0%, transparent 50%);
  position: relative;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
  opacity: 0.3;
}
'''
    
    # Insert before the closing </style> tag
    html = html.replace('</style>', hero_css + '\n</style>')
    
    return html

def add_content_section_css(html):
    """Task 4: Add content-section class for consistent width"""
    print("✓ Adding content-section CSS...")
    
    content_css = '''
/* Content Section Container */
.content-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 60px;
}

.content-section-wide {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 60px;
}

@media (max-width: 900px) {
  .content-section,
  .content-section-wide {
    padding: 0 30px;
  }
}
'''
    
    # Insert before the closing </style> tag
    html = html.replace('</style>', content_css + '\n</style>')
    
    return html

def main():
    print("=" * 60)
    print("DAY 1: LAYOUT REDESIGN IMPLEMENTATION")
    print("=" * 60)
    print()
    
    # Read index.html
    html = read_file('index.html')
    
    # Task 1: Expand content width
    html = expand_content_width(html)
    
    # Task 2: Add two-column benefits CSS
    html = add_two_column_css(html)
    
    # Task 3: Add full-width hero background
    html = add_full_width_hero_css(html)
    
    # Task 4: Add content-section CSS
    html = add_content_section_css(html)
    
    # Write updated index.html
    write_file('index.html', html)
    
    print()
    print("=" * 60)
    print("CSS UPDATES COMPLETE!")
    print("=" * 60)
    print()
    print("Changes made:")
    print("  ✓ Expanded content width (600px → 800-900px)")
    print("  ✓ Added two-column benefits grid CSS")
    print("  ✓ Added full-width hero background")
    print("  ✓ Added content-section containers")
    print()
    print("Next steps:")
    print("  1. Integrate accordion system (replace Features tab)")
    print("  2. Add two-column benefits HTML to Overview tab")
    print("  3. Test responsive behavior")
    print()
    print("Files ready:")
    print("  - capabilities-accordion.html (ready to integrate)")
    print("  - Updated index.html (CSS ready)")

if __name__ == '__main__':
    main()
