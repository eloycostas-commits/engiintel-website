#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the form submission handler to use Resend API directly
old_handler = '''      try {
        const webhookUrl = window.location.hostname === 'localhost' 
          ? 'http://localhost:5678/webhook/contact-form'
          : 'https://n8n.engiintel.com/webhook/contact-form';
        
        const response = await fetch(webhookUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        });'''

new_handler = '''      try {
        // Send directly to Resend API
        const response = await fetch('https://api.resend.com/emails', {
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
        });'''

if old_handler in content:
    content = content.replace(old_handler, new_handler)
    print("✓ Updated form to send directly to Resend API")
else:
    print("✗ Could not find form handler to update")

# Write back
with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("✓ Form will now send emails to: eloycostas@engiintel.com")
