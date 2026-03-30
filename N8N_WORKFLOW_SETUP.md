# N8N Workflow Setup for Contact Form

## Overview
The website contact form now sends data to an n8n webhook that needs to be created.

## What Was Fixed

### 1. Button Navigation
- Fixed `switchTab()` function to properly navigate to Resources tab
- CTA buttons ("Request Beta Access", "Book a Demo") now correctly switch to Resources tab and scroll to form

### 2. Form Submission
- Added JavaScript form submission handler
- Form prevents default submission and sends data via fetch API
- Shows loading state while sending
- Displays success/error messages in user's language (EN/ES)

### 3. Webhook URL
- Development: `http://localhost:5678/webhook/contact-form`
- Production: `https://n8n.engiintel.com/webhook/contact-form` (needs to be configured)

## N8N Workflow Required

You need to create an n8n workflow with the following structure:

### Nodes:

1. **Webhook Trigger**
   - Path: `/webhook/contact-form`
   - Method: POST
   - Response Mode: Respond Immediately
   - Response Code: 200

2. **Resend Email Node**
   - From: `onboarding@resend.dev` (or your verified domain)
   - To: `eloycostas@engiintel.com`
   - Subject: `New Contact Form Submission - {{$json.name}}`
   - Email Body (HTML):
   ```html
   <h2>New Contact Form Submission</h2>
   <p><strong>Name:</strong> {{$json.name}}</p>
   <p><strong>Email:</strong> {{$json.email}}</p>
   <p><strong>Company:</strong> {{$json.company}}</p>
   <p><strong>Industry:</strong> {{$json.industry}}</p>
   <p><strong>Interests:</strong> {{$json.interests}}</p>
   <p><strong>Message:</strong></p>
   <p>{{$json.message}}</p>
   <p><strong>Language:</strong> {{$json.language}}</p>
   <p><strong>Submitted:</strong> {{$json.timestamp}}</p>
   ```

### Form Data Structure:
```json
{
  "name": "John Doe",
  "email": "john@company.com",
  "company": "Acme Corp",
  "industry": "elevator",
  "interests": ["demo", "pricing"],
  "message": "I'm interested in learning more...",
  "language": "en",
  "timestamp": "2026-03-30T12:00:00.000Z"
}
```

## Steps to Create Workflow

### Using n8n MCP (Recommended):

The n8n MCP is now configured in `.vscode/mcp.json`. You can use it to create the workflow programmatically.

### Manual Setup:

1. Open n8n at `http://localhost:5678`
2. Create new workflow
3. Add Webhook node:
   - Set path to `contact-form`
   - Set method to POST
   - Enable "Respond Immediately"
4. Add Resend node:
   - Configure with API key from `.env`: `re_43jiWP48_3vxjr9PnCFKBaQCrY4UvdJNJ`
   - Set from email: `onboarding@resend.dev`
   - Set to email: `eloycostas@engiintel.com`
   - Configure email template as shown above
5. Connect Webhook → Resend
6. Activate workflow
7. Test with form submission

## Production Deployment

For production, you need to:

1. Deploy n8n to a production server (e.g., `n8n.engiintel.com`)
2. Update the webhook URL in `index.html` (line with `https://n8n.engiintel.com/webhook/contact-form`)
3. Configure Resend with a verified domain email (not `onboarding@resend.dev`)
4. Enable CORS in n8n for `engiintel.com` domain
5. Use HTTPS for the webhook URL

## Testing

1. Open website locally or on Vercel
2. Click "Request Beta Access" or "Book a Demo"
3. Should navigate to Resources tab
4. Fill out the form
5. Submit
6. Should see success message
7. Check `eloycostas@engiintel.com` for email

## Current Status

- ✅ Website form fixed
- ✅ JavaScript handler added
- ✅ n8n MCP configured
- ⏳ N8N workflow needs to be created
- ⏳ Production n8n URL needs to be configured
