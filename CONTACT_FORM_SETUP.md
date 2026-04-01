# Contact Form Setup Guide

## Overview
The contact form now uses a Vercel serverless function (`/api/contact-form`) that sends emails via Resend API.

## Architecture
```
User fills form → Frontend JS → /api/contact-form → Resend API → Email to you
```

## Vercel Environment Variables Required

You need to add these environment variables in your Vercel project settings:

1. Go to: https://vercel.com/your-project/settings/environment-variables

2. Add these variables:

```
RESEND_API_KEY=re_43jiWP48_3vxjr9PnCFKBaQCrY4UvdJNJ
RESEND_FROM=onboarding@resend.dev
BETA_FOUNDER_EMAIL=eloycostas@engiintel.com
```

## How to Add Environment Variables in Vercel

1. Open your Vercel dashboard
2. Select your project (engiintel-website)
3. Go to Settings → Environment Variables
4. Add each variable:
   - Name: `RESEND_API_KEY`
   - Value: `re_43jiWP48_3vxjr9PnCFKBaQCrY4UvdJNJ`
   - Environment: Production, Preview, Development (select all)
   - Click "Save"

5. Repeat for `RESEND_FROM` and `BETA_FOUNDER_EMAIL`

6. Redeploy your site (or push a new commit)

## Testing

After deployment:
1. Visit your live site
2. Fill out the contact form
3. Submit
4. Check your email at eloycostas@engiintel.com

## Files Changed
- ✅ Created: `/api/contact-form.js` (Vercel serverless function)
- ✅ Updated: `/js/app.js` (form handler now calls `/api/contact-form`)
- ✅ Rebuilt: `/public/index.html` (ready for deployment)

## Security Note
The Resend API key is now safely stored in Vercel environment variables (server-side), not exposed in frontend code.
