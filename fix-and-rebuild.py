#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Start with the old backup which has clean CSS
with open('index-old-backup.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the .lang-btn CSS corruption
corrupted_lang_btn = '''.lang-btn {
  background: none;
  border: 1px solid var(--border);
  color: var(--text-dim);
  padding: 6px 12px;
  font-family: 'DM Mono', monospace;
  font-size: 0.75rem;
.pricing-features li::before { content: '✓'; color: var(--accent3); flex-shrink: 0; }
        const webhookUrl = window.location.hostname === 'localhost' 
          ? 'http://localhost:5678/webhook/contact-form'
          : 'https://n8n.engiintel.com/webhook/contact-form'; // Update with your n8n production URL
        
        const response = await fetch(webhookUrl, {
}'''

clean_lang_btn = '''.lang-btn {
  background: none;
  border: 1px solid var(--border);
  color: var(--text-dim);
  padding: 6px 12px;
  font-family: 'DM Mono', monospace;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;
}'''

if corrupted_lang_btn in content:
    content = content.replace(corrupted_lang_btn, clean_lang_btn)
    print("✓ Fixed .lang-btn CSS corruption")

# Replace hero buttons to use switchTab
content = content.replace(
    '<a href="#contact" class="btn-primary"',
    '<button class="btn-primary" onclick="switchTab(\'resources\')"'
)
content = content.replace(
    '<a href="#contact" class="btn-secondary"',
    '<button class="btn-secondary" onclick="switchTab(\'resources\')"'
)
content = content.replace('</a>', '</button>', 2)  # Replace first 2 occurrences
print("✓ Updated hero CTA buttons")

# Add form ID
content = content.replace(
    '<form class="contact-form" action="#" method="POST">',
    '<form id="contactForm" class="contact-form" action="#" method="POST">'
)
print("✓ Added form ID")

# Update form handler in JavaScript to use Resend API
old_fetch = '''const response = await fetch('http://localhost:5678/webhook/contact-form', {'''
new_fetch = '''const response = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer re_43jiWP48_3vxjr9PnCFKBaQCrY4UvdJNJ'
          },
          body: JSON.stringify({
            from: 'EngiIntel Website <onboarding@resend.dev>',
            to: ['eloycostas@engiintel.com'],
            subject: `New Contact Form Submission from ${formData.name}`,
            html: `
              <h2>New Contact Form Submission</h2>
              <p><strong>Name:</strong> ${formData.name}</p>
              <p><strong>Email:</strong> ${formData.email}</p>
              <p><strong>Company:</strong> ${formData.company}</p>
              <p><strong>Industry:</strong> ${formData.industry}</p>
              <p><strong>Interests:</strong> ${formData.interests.join(', ')}</p>
              <p><strong>Message:</strong></p>
              <p>${formData.message}</p>
              <p><strong>Language:</strong> ${formData.language}</p>
              <p><strong>Timestamp:</strong> ${formData.timestamp}</p>
            `
          })
        });
        
        if (response.ok) {'''

if old_fetch in content:
    # Find and replace the entire fetch block
    fetch_start = content.find(old_fetch)
    fetch_end = content.find('if (response.ok) {', fetch_start)
    if fetch_start != -1 and fetch_end != -1:
        content = content[:fetch_start] + new_fetch + content[fetch_end + len('if (response.ok) {'):]
        print("✓ Updated form to use Resend API")

# Write the fixed file
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Rebuilt index.html from clean backup")
print("✓ All fixes applied")
print("✓ Form sends to: eloycostas@engiintel.com")
