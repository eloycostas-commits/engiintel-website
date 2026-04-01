# Deploy Contact Form Fix

## What Changed
✅ Updated `vercel.json` to properly configure serverless functions
✅ API endpoint will now be recognized by Vercel

## Deploy Commands

```bash
git add .
git commit -m "Fix API endpoint configuration for Vercel"
git push
```

## After Deployment

1. Wait for Vercel to finish deploying (1-2 minutes)
2. Test the form on your live site
3. Check Vercel function logs if there are still issues

## Vercel Function Logs

To check if the API is working:
1. Go to https://vercel.com/your-project
2. Click "Deployments" → Latest deployment
3. Click "Functions" tab
4. Click `/api/contact-form`
5. View real-time logs

## What to Look For in Logs

Success:
```
=== CONTACT FORM SUBMISSION ===
Name: Test User
Email: test@example.com
...
Resend API response status: 200
Email sent successfully
```

If you see this, emails are working!

## Important: Resend Free Tier Limitation

Resend free tier can ONLY send emails TO the email address you used to sign up for Resend.

If `eloycostas@engiintel.com` is NOT your Resend account email:
1. Go to Vercel → Settings → Environment Variables
2. Change `BETA_FOUNDER_EMAIL` to match your Resend signup email
3. Redeploy

Or verify your domain in Resend to send to any email.
