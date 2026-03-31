# Quick Integration Guide - Phase 1

## 🚀 Fast Track (15 Minutes)

### Step 1: Open Files (2 min)
Open in your code editor:
- `index.html` (main file to edit)
- `tabs/overview.html` (copy from here)
- `tabs/features.html` (copy from here)
- `tabs/industries.html` (copy from here)
- `tabs/resources.html` (copy from here)

### Step 2: Insert Overview & Features (5 min)
1. In `index.html`, find line ~511:
   ```html
   </div>
   </div>


   <!-- Tab Content: Document Intelligence -->
   ```

2. Place cursor AFTER `</div></div>` and BEFORE `<!-- Tab Content: Document Intelligence -->`

3. Paste:
   - Entire content of `tabs/overview.html`
   - 2 blank lines
   - Entire content of `tabs/features.html`
   - 2 blank lines

### Step 3: Fix Active Tab (1 min)
1. Find line ~515:
   ```html
   <div id="document-intelligence" class="tab-content active">
   ```

2. Remove `active`:
   ```html
   <div id="document-intelligence" class="tab-content">
   ```

### Step 4: Insert Industries (3 min)
1. Find line ~897:
   ```html
   <!-- Tab Content: Pricing -->
   ```

2. Place cursor BEFORE this comment

3. Paste:
   - Entire content of `tabs/industries.html`
   - 3 blank lines

### Step 5: Insert Resources (3 min)
1. Find line ~1050 (near end):
   ```html
   <!-- Footer (Always Visible) -->
   ```

2. Place cursor BEFORE this comment

3. Paste:
   - Entire content of `tabs/resources.html`
   - 3 blank lines

### Step 6: Save & Test (1 min)
1. Save `index.html`
2. Open in browser
3. Click through all 11 tabs
4. Test EN/ES language switch

## ✅ Verification Checklist

- [ ] Overview tab loads first (active by default)
- [ ] All 11 tabs visible in navigation
- [ ] Stats strip shows: 0ms, 100%, ∞, 13×
- [ ] Problem section shows 4 stats
- [ ] Feature comparison table displays
- [ ] 6 industry cards visible
- [ ] FAQ has 15 questions
- [ ] Contact form displays
- [ ] Language switching works
- [ ] Mobile view works

## 🐛 Troubleshooting

**Tabs don't switch?**
- Check browser console for errors
- Verify JavaScript at bottom of file is intact

**Content looks broken?**
- Check for missing closing tags
- Verify CSS styles section is complete

**Language switching doesn't work?**
- Verify `setLang()` function exists
- Check data-en and data-es attributes

## 📸 Screenshot Replacement

Find and replace these 8 placeholders:

```html
<!-- Find this: -->
<div class="screenshot-placeholder">[Screenshot: Query + Results]</div>

<!-- Replace with: -->
<img src="screenshots/query-results.png" alt="Query Results" style="width: 100%; border: 1px solid var(--border); margin-top: 16px;">
```

Repeat for all 8 placeholders.

## 🚀 Deploy

```bash
git add .
git commit -m "Phase 1: Add Overview, Features, Industries, Resources tabs"
git push origin main
```

Vercel auto-deploys in ~2 minutes.

## 📊 Result

You'll have:
- 11 tabs (was 7)
- Feature comparison table
- 6 industry solutions
- 15 FAQ items
- Contact form
- Trust indicators
- All bilingual

**Done! 🎉**

