# EngiIntel Website - Modular Component Architecture

## Overview

The landing page uses a modular component system where you edit small files (under 300 lines) and build them into a single HTML file for deployment.

## Structure

```
/
├── index.html                 # Built file (deployed to Vercel)
├── build-landing.js           # Build script
├── package.json               # Build commands
├── components/                # Edit these files ✏️
│   ├── header.html           (7 lines)
│   ├── hero.html             (136 lines)
│   ├── tabs.html             (15 lines)
│   ├── overview-tab.html     (148 lines)
│   ├── features-tab.html     (120 lines)
│   ├── document-intelligence-tab.html (43 lines)
│   ├── excel-copilot-tab.html (42 lines)
│   ├── wiki-tab.html         (42 lines)
│   ├── assets-tab.html       (42 lines)
│   ├── incidents-tab.html    (42 lines)
│   ├── ai-agent-tab.html     (43 lines)
│   ├── industries-tab.html   (135 lines)
│   ├── pricing-tab.html      (139 lines)
│   ├── resources-tab.html    (220 lines)
│   └── footer.html           (40 lines)
├── css/
│   └── styles.css            # Edit styles here ✏️
└── js/
    └── app.js                # Edit JavaScript here ✏️
```

## Workflow

### 1. Edit a component
```bash
# Open and edit any component file
code components/pricing-tab.html
```

### 2. Build
```bash
npm run build
```

### 3. Deploy
```bash
git add -A
git commit -m "Update: [description]"
git push origin main
```

Vercel automatically deploys when you push to main.

## Benefits

✅ Edit small files (7-220 lines) instead of 2,200-line monolith
✅ No corruption risk - each component is isolated
✅ Clear version control - see exactly what changed
✅ Fast builds - combines in <1 second
✅ No dependencies - uses Node.js built-in fs module

## Safety

- **Clean backup**: `index-clean-backup.html` (verified working)
- **Recovery**: If something breaks, run `npm run build` to regenerate

## Component Guidelines

- Keep each component under 300 lines
- Use `data-en` and `data-es` attributes for translations
- No inline styles (use css/styles.css)
- No inline scripts (use js/app.js)
- Pure HTML fragments (no `<html>`, `<head>`, `<body>` tags)

## Build Script

The `build-landing.js` script:
1. Reads all component HTML files
2. Reads CSS and JavaScript
3. Combines them into a single `index.html`
4. Inlines CSS in `<style>` tag
5. Inlines JS in `<script>` tag

This gives you the best of both worlds:
- Modular development (easy editing)
- Single-file deployment (works on Vercel)
