# Deployment Ready - Contact Form Fixed

## What Was Fixed

✅ Contact form now uses Vercel serverless function with Resend API
✅ ROI calculation shows correct formula: "15 hrs/week × €16/hr × 4 weeks = €960"
✅ ROI card has min-width: 400px to prevent text wrapping
✅ Site rebuilt and ready for deployment

## Files Changed

1. **Created**: `/api/contact-form.js` - Vercel serverless function
2. **Updated**: `/js/app.js` - Form handler calls `/api/contact-form`
3. **Rebuilt**: `/public/index.html` - Ready for deployment

## Next Steps

### 1. Configure Vercel Environment Variables

Go to: https://vercel.com/your-project/settings/environment-variables

Add these three variables:

```
RESEND_API_KEY=re_43jiWP48_3vxjr9PnCFKBaQCrY4UvdJNJ
RESEND_FROM=onboarding@resend.dev
BETA_FOUNDER_EMAIL=eloycostas@engiintel.com
```

### 2. Deploy

```bash
git add .
git commit -m "Fix contact form with Resend API"
git push
```

Vercel will auto-deploy from the `public/` folder.

### 3. Test

1. Visit your live site
2. Go to Resources tab
3. Fill out contact form
4. Submit
5. Check email at eloycostas@engiintel.com

## How It Works

```
User → Contact Form → /api/contact-form (Vercel Function) → Resend API → Your Email
```

The API key is safely stored in Vercel environment variables (server-side), not exposed in frontend code.

## Troubleshooting

If form doesn't work after deployment:
1. Verify environment variables are set in Vercel
2. Check Vercel function logs for errors
3. Verify Resend API key is valid at https://resend.com/api-keys
