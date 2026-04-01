# Contact Form Troubleshooting Guide

## Current Status
The form now has graceful error handling - it will always show success to the user, but logs all submissions in Vercel for manual follow-up.

## How to Check Form Submissions

### Option 1: Check Vercel Function Logs
1. Go to https://vercel.com/your-project
2. Click on "Deployments"
3. Click on your latest deployment
4. Click on "Functions" tab
5. Click on `/api/contact-form`
6. View the logs - all form submissions are logged here

Look for lines like:
```
=== CONTACT FORM SUBMISSION ===
Name: John Doe
Email: john@example.com
...
```

### Option 2: Check if Resend is Working
The logs will show:
- `Resend API key found: re_43jiWP4...` (API key is loaded)
- `Sending email from: onboarding@resend.dev`
- `Sending email to: eloycostas@engiintel.com`
- `Resend API response status: 200` (success) or error code
- `Resend API response data: {...}` (details from Resend)

## Common Issues

### Issue 1: Resend Free Tier Limitations
Resend's free tier has restrictions:
- Can only send FROM: `onboarding@resend.dev` (or verified domain)
- Can only send TO: The email address you used to sign up for Resend

**Solution**: Verify that `eloycostas@engiintel.com` is the email you used to create your Resend account.

If not, either:
1. Change `BETA_FOUNDER_EMAIL` to match your Resend account email
2. Or verify your domain in Resend and update `RESEND_FROM`

### Issue 2: API Key Invalid
Check the logs for: `RESEND_API_KEY not configured`

**Solution**: 
1. Go to https://resend.com/api-keys
2. Verify your API key is active
3. Copy the key and update it in Vercel environment variables
4. Redeploy

### Issue 3: Environment Variables Not Set
**Solution**:
1. Go to Vercel → Settings → Environment Variables
2. Verify these are set:
   - `RESEND_API_KEY`
   - `RESEND_FROM`
   - `BETA_FOUNDER_EMAIL`
3. Make sure they're enabled for "Production" environment
4. Redeploy after adding/changing variables

## Current Behavior
With the updated code:
- ✅ User always sees success message (good UX)
- ✅ All submissions are logged in Vercel (you can manually follow up)
- ✅ If Resend works, email is sent automatically
- ✅ If Resend fails, you can still see the submission in logs

## Testing Steps
1. Deploy the updated code
2. Fill out the form on your live site
3. Check Vercel function logs immediately
4. Look for the submission data in the logs
5. Check your email (if Resend is working)

## Alternative: Use Formspree (Simpler)
If Resend continues to have issues, you can switch to Formspree:

1. Go to https://formspree.io
2. Create a free account
3. Create a new form
4. Get your form endpoint (e.g., `https://formspree.io/f/xanykorv`)
5. Update `js/app.js` to use that endpoint instead of `/api/contact-form`

Formspree is simpler and has no restrictions on the free tier (50 submissions/month).
