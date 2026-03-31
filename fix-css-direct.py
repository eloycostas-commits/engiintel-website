#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Direct string replacement - find the exact corrupted section and replace it
corrupted = '''.lang-btn {
  background: none;
  border: 1px solid var(--border);
  color: var(--text-dim);
  padding: 6px 12px;
  font-family: 'DM Mono', monospace;
  font-size: 0.75rem;
        // Send to n8n webhook (update this URL to your production n8n instance)
        const webhookUrl = window.location.hostname === 'localhost' 
          ? 'http://localhost:5678/webhook/contact-form'
          : 'https://n8n.engiintel.com/webhook/contact-form'; // Update with your n8n production URL
        
        const response = await fetch(webhookUrl, {
}'''

fixed = '''.lang-btn {
  background: none;
  border: 1px solid var(--border);
  color: var(--text-dim);
  padding: 6px 12px;
  font-family: 'DM Mono', monospace;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;
}'''

if corrupted in content:
    content = content.replace(corrupted, fixed)
    print("✓ Fixed CSS corruption")
else:
    print("✗ Corrupted section not found - checking for variations")
    # Try to find it with different whitespace
    import re
    # Remove extra whitespace for matching
    corrupted_normalized = re.sub(r'\s+', ' ', corrupted)
    content_normalized = re.sub(r'\s+', ' ', content)
    if corrupted_normalized in content_normalized:
        print("  Found with different whitespace - attempting fix")
        # Find the position in the original
        start = content.find('.lang-btn {')
        if start != -1:
            # Find the next .lang-btn.active
            end = content.find('.lang-btn.active', start)
            if end != -1:
                # Replace everything between
                content = content[:start] + fixed + '\n' + content[end:]
                print("✓ Fixed with position-based replacement")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
