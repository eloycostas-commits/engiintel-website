# EngiIntel Website - Modular Architecture

## Overview
The website has been refactored from a single 2,200-line HTML file into a modular component-based architecture to prevent code corruption during iterations.

## Structure

```
/
├── index.html                  # Main entry point (70 lines)
├── css/
│   └── styles.css             # All styles (23KB)
├── js/
│   └── app.js                 # Component loader + all JavaScript (240 lines)
└── components/                # HTML fragments (all under 300 lines)
    ├── header.html            # Navigation + language switcher (7 lines)
    ├── hero.html              # Hero section (136 lines)
    ├── tabs.html              # Tab navigation bar (15 lines)
    ├── overview-tab.html      # Overview content (148 lines)
    ├── features-tab.html      # Features comparison (120 lines)
    ├── document-intelligence-tab.html  (43 lines)
    ├── excel-copilot-tab.html          (42 lines)
    ├── wiki-tab.html                   (42 lines)
    ├── assets-tab.html                 (42 lines)
    ├── incidents-tab.html              (42 lines)
    ├── ai-agent-tab.html               (43 lines)
    ├── industries-tab.html             (135 lines)
    ├── pricing-tab.html                (139 lines)
    ├── resources-tab.html              (220 lines)
    └── footer.html                     (40 lines)
```

## How It Works

1. **index.html** - Minimal entry point that:
   - Loads CSS and JavaScript
   - Defines component containers
   - Shows loading indicator

2. **js/app.js** - Component loader that:
   - Fetches all HTML components in parallel
   - Injects them into containers
   - Initializes all functionality (tabs, language, pricing, forms, GDPR)

3. **components/*.html** - Pure HTML fragments with:
   - No `<html>`, `<head>`, or `<body>` tags
   - Just the content for that section
   - All under 300 lines for easy editing

## Benefits

✅ **No more corruption** - Small files are easy to edit safely
✅ **Easy maintenance** - Each component is isolated and focused
✅ **Fast development** - Edit one component without touching others
✅ **Version control** - Clear diffs show exactly what changed
✅ **No build tools** - Vanilla JavaScript, works directly in browser

## Editing Workflow

### To edit a component:
1. Open the component file (e.g., `components/pricing-tab.html`)
2. Make your changes
3. Save the file
4. Refresh browser to see changes
5. Commit to GitHub
6. Vercel auto-deploys

### To add a new component:
1. Create `components/new-component.html`
2. Add container in `index.html`: `<div id="new-component-container"></div>`
3. Add loader in `js/app.js` components array:
   ```javascript
   { path: 'components/new-component.html', container: 'new-component-container' }
   ```
4. Commit and deploy

## Safety Net

- **Clean backup**: `index-clean-backup.html` (verified working version)
- **Monolithic backup**: `index-monolithic-backup.html` (pre-refactor version)
- **Recovery command**: `Copy-Item index-clean-backup.html index.html -Force`

## Technical Details

- **No frameworks** - Vanilla JavaScript only
- **No build step** - Works with `file://` protocol
- **Parallel loading** - All components load simultaneously
- **Preserved functionality**:
  - Language switching (EN/ES)
  - Tab navigation with URL anchors
  - Pricing calculator with real-time updates
  - Contact form with n8n webhook
  - Google Analytics
  - GDPR cookie banner

## Deployment

Changes are automatically deployed to Vercel when pushed to GitHub main branch.

```bash
git add -A
git commit -m "Update: [description]"
git push origin main
```

Vercel URL: https://engiintel-website.vercel.app
