# Quick Reference Card

## Your Files

| File | Purpose | Edit? |
|------|---------|-------|
| `index.html` | Active website | ✅ YES - Work here |
| `index-clean-backup.html` | Safety backup | ❌ NO - Keep pristine |
| `index-backup-before-accordion.html` | Old backup | ⏭️ Can delete |

## Emergency Recovery

```powershell
Copy-Item index-clean-backup.html index.html -Force
```

## Current Status

✅ **Deployed**: Live on Vercel  
✅ **Backup**: Saved as `index-clean-backup.html`  
✅ **Score**: 9.0/10  
✅ **All tabs working**: 10 tabs functional  

## What's Working

- All 10 tabs (Overview, Features, Document Intelligence, Excel Copilot, Wiki, Assets, Incidents, AI Agent, Industries, Pricing, Resources)
- Interactive pricing calculator
- Bilingual support (EN/ES)
- Mobile responsive
- Contact form
- GDPR banner

## Next Steps

1. Test the live site on Vercel
2. Get user feedback
3. Make small improvements based on feedback
4. Always test locally before pushing

## Safe Editing Tips

✅ **DO**:
- Edit text content
- Change colors/spacing in CSS
- Add new sections at end of tabs
- Test after each change
- Commit often

❌ **DON'T**:
- Use Python scripts on HTML
- Delete closing tags
- Edit JavaScript functions without testing
- Make multiple changes at once

## Deployment

```bash
git add index.html
git commit -m "your change description"
git push origin main
```

Vercel auto-deploys in 1-2 minutes.

---

**Remember**: You have a backup. Don't be afraid to experiment!

