# Encoding Issue Resolution

## Problem
The website integration has been experiencing persistent UTF-16/UTF-8 encoding issues that cause:
- Blank tabs (Overview, Features, Industries, Resources)
- Strange characters in Spanish text
- Corrupted special characters (—, é, ñ, etc.)
- Non-functional buttons

## Root Cause
The git repository contains files with mixed encodings:
- Some commits have UTF-16LE encoded files
- Python's `Path().write_text()` was saving with wrong encoding
- PowerShell `Out-File` was using UTF-16 by default
- Special characters (—, ∞, €, etc.) were being corrupted

## Solution
We need to:
1. Start from a clean, working base (commit 8d935ec - old single-page version)
2. Manually rebuild the tab-based structure with proper UTF-8
3. Ensure all special characters are properly encoded
4. Test locally before deploying

## Current Status
- Restored to commit 8d935ec (March 2026 single-page version)
- This version works but doesn't have the new tabs
- Need to rebuild tab structure from scratch with proper encoding

## Next Steps
1. Use the working single-page version as base
2. Add tab navigation structure
3. Integrate tab content with proper UTF-8 encoding
4. Test locally in browser
5. Deploy to Vercel

## Files to Use
- Base: `index.html` (from commit 8d935ec - currently checked out)
- Tab content: `tabs/*.html` (these are clean)
- Integration: Manual or careful Python script with explicit UTF-8

## Recommendation
Given the persistent encoding issues, the safest approach is to:
1. Keep the current working version (8d935ec)
2. Manually add the Phase 1 enhancements in smaller increments
3. Test after each change
4. Or: Accept the current working version and plan Phase 1 enhancements for later with proper tooling
