# Backup & Recovery Instructions

## Clean Backup File

**File**: `index-clean-backup.html`  
**Size**: 128,719 bytes  
**Status**: ✅ VERIFIED WORKING  
**Date**: April 1, 2026

This is your safety net. If anything goes wrong with `index.html`, restore from this backup.

## Quick Recovery Command

If `index.html` gets corrupted:

```bash
# Windows PowerShell
Copy-Item index-clean-backup.html index.html -Force

# Verify it worked
(Get-Item index.html).Length  # Should show 128719
```

## What's in the Clean Backup

✅ All 10 tabs working
✅ Pricing calculator functional
✅ Bilingual support (EN/ES)
✅ Mobile responsive
✅ Contact form + GDPR banner
✅ No corruption

## Working Files

- `index.html` - Active working file (edit this)
- `index-clean-backup.html` - Clean backup (DON'T edit this)
- `index-backup-before-accordion.html` - Original backup (can delete)

## Safe Editing Guidelines

### ✅ SAFE to Edit:
- Text content (headings, paragraphs)
- CSS values (colors, sizes, spacing)
- Adding new CSS classes
- Adding new HTML sections at the end of tabs
- Changing data-en/data-es attributes

### ⚠️ RISKY to Edit:
- JavaScript functions (switchTab, calcPrice, etc.)
- Inline `<script>` tags
- Tab structure (div ids, classes)
- Closing tags

### ❌ NEVER Do:
- Use Python regex scripts on HTML
- Use BeautifulSoup prettify()
- Delete closing tags
- Mix JavaScript into HTML body
- Modify without testing

## Recommended Workflow

1. **Make small changes**: Edit one thing at a time
2. **Test immediately**: Open in browser after each change
3. **Commit often**: Git commit after each working change
4. **Keep backup**: Never delete `index-clean-backup.html`

## If Something Goes Wrong

1. **Don't panic**: You have a backup
2. **Restore backup**: `Copy-Item index-clean-backup.html index.html -Force`
3. **Test restored file**: Open in browser
4. **Try again**: Make smaller changes

## Backup Verification

To verify your backup is intact:

```powershell
# Check file size
(Get-Item index-clean-backup.html).Length  # Should be 128719

# Check for switchTab function
Select-String -Path index-clean-backup.html -Pattern "function switchTab" -Quiet  # Should be True

# Check for closing tag
Select-String -Path index-clean-backup.html -Pattern "</html>" -Quiet  # Should be True

# Count tabs
(Select-String -Path index-clean-backup.html -Pattern 'class="tab-btn"').Count  # Should be 10
```

## Recovery Test

Test the recovery process now:

```powershell
# 1. Corrupt the file (for testing)
"CORRUPTED" | Out-File index.html

# 2. Restore from backup
Copy-Item index-clean-backup.html index.html -Force

# 3. Verify restoration
(Get-Item index.html).Length  # Should be 128719
```

---

**Remember**: `index-clean-backup.html` is your lifeline. Keep it safe!

