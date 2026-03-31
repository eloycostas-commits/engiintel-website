# Website Update Complete

## What's Been Done

### Pricing Calculator ✓
- Interactive calculator with seat counter (1-500 users)
- Module selection toggles (Operations, Excel Copilot, Wiki, Incidents, AI Agent, Analytics)
- Real-time price calculation
- Volume discounts: 15+ seats (-10%), 25+ seats (-15%), 50+ seats (-20%)
- Pricing: Core €8/seat + €4/seat per module
- Bilingual support (EN/ES)
- "Request this plan" button navigates to Resources tab

### Contact Form Email Integration ✓
- Form sends directly to Resend API (simpler than n8n flow)
- Emails sent to: **eloycostas@engiintel.com**
- From: EngiIntel Website <onboarding@resend.dev>
- Subject: "New Contact Form Submission from [Name]"
- Includes all form data: name, email, company, industry, interests, message, language, timestamp
- Success/error messages in user's language (EN/ES)
- Error message includes fallback email: eloycostas@engiintel.com

### Hero CTA Buttons ✓
- "Request Beta Access" → navigates to Resources tab
- "Book a Demo" → navigates to Resources tab
- Both buttons properly trigger switchTab('resources')

## Testing

To test the form submission:
1. Open index.html in browser
2. Navigate to Resources tab
3. Fill out the contact form
4. Submit
5. Check eloycostas@engiintel.com for the email

## Technical Details

- **Resend API Key**: re_43jiWP48_3vxjr9PnCFKBaQCrY4UvdJNJ
- **API Endpoint**: https://api.resend.com/emails
- **Recipient**: eloycostas@engiintel.com
- **From Address**: onboarding@resend.dev

## Deployment

Changes committed to git:
- Commit: 4efe3b6
- Message: "Add pricing calculator and direct Resend API integration for contact form"

Ready to push to production.
