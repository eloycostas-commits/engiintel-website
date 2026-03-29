# EngiIntel Website Redesign Plan

## Current Issues
1. **Google Analytics**: Wrong tracking code (GTM instead of GA4)
2. **User Experience**: Too much scrolling - single-page layout causes disengagement
3. **Missing Features**: Excel module and recent improvements not documented
4. **Navigation**: No clear path to specific information

## Proposed Solution: Multi-Page Architecture

### Structure Overview
```
Home (Landing)
├── Features (Separate page)
├── Modules (Separate page with sub-pages)
│   ├── Document Intelligence
│   ├── Excel Copilot ⭐ NEW
│   ├── Wiki & Knowledge Base
│   ├── Asset Registry
│   ├── Incident Reports
│   └── AI Agent Mode
├── Industries (Separate page)
├── Pricing (Separate page with calculator)
├── How It Works (Separate page)
└── Contact (Separate page)
```

### Page Breakdown

#### 1. **Home Page** (index.html)
**Purpose**: Hook visitors and guide them to relevant sections

**Content**:
- Hero section with value proposition
- 3-4 key benefits (cards with icons)
- Quick stats strip
- Featured module spotlight (rotating)
- Trust indicators (GDPR, offline, etc.)
- CTA buttons to Features, Modules, and Contact

**Length**: 2-3 screens max

---

#### 2. **Features Page** (features.html)
**Purpose**: Deep dive into capabilities

**Content**:
- Feature grid (current features section)
- Comparison table (EngiIntel vs Cloud AI vs Manual)
- Technical specifications
- Integration capabilities
- Security & compliance details

---

#### 3. **Modules Page** (modules.html)
**Purpose**: Module catalog with navigation to detailed pages

**Content**:
- Module cards grid (6 modules)
- Each card links to dedicated page
- Pricing calculator (current one)
- "Build Your Stack" configurator

**Sub-pages**:
- `modules/document-intelligence.html`
- `modules/excel-copilot.html` ⭐ NEW
- `modules/wiki.html`
- `modules/assets.html`
- `modules/incidents.html`
- `modules/ai-agent.html`

---

#### 4. **Excel Copilot Module Page** ⭐ NEW
**Purpose**: Showcase the new Excel functionality

**Content**:
- Hero: "AI-Powered Excel Analysis"
- Key features:
  - Natural language queries on Excel data
  - Chart generation with one command
  - Macro system for reusable queries
  - Workflow automation
  - Multi-sheet analysis
- Demo video/GIF
- Use cases:
  - Regulatory compliance tracking
  - Asset data analysis
  - Report generation
- Pricing: €15/month per seat
- CTA: "Try Excel Copilot"

---

#### 5. **Industries Page** (industries.html)
**Purpose**: Industry-specific use cases

**Content**:
- Industry cards (current section)
- Case studies (when available)
- Industry-specific features
- Testimonials (when available)

---

#### 6. **Pricing Page** (pricing.html)
**Purpose**: Clear pricing with calculator

**Content**:
- 3-tier pricing cards (Free, Pro, Enterprise)
- Module pricing calculator (current one)
- FAQ about pricing
- Volume discounts
- CTA: "Start Free Trial" / "Book Demo"

---

#### 7. **How It Works Page** (how-it-works.html)
**Purpose**: Technical overview and onboarding

**Content**:
- 4-step process (current section)
- Architecture diagram
- Deployment options
- System requirements
- Integration guide
- Roadmap

---

#### 8. **Contact Page** (contact.html)
**Purpose**: Lead generation

**Content**:
- Contact form (current one)
- Calendar booking widget (optional)
- Contact details
- Office locations (if applicable)
- FAQ

---

### Navigation Structure

**Main Navigation** (sticky header):
```
Logo | Features | Modules ▼ | Industries | Pricing | How It Works | Contact | [Book Demo CTA]
```

**Modules Dropdown**:
```
All Modules
─────────────
📄 Document Intelligence
📊 Excel Copilot ⭐ NEW
📚 Wiki & Knowledge Base
🏢 Asset Registry
⚠️ Incident Reports
🤖 AI Agent Mode
```

---

### Key Improvements

#### 1. **Reduced Cognitive Load**
- Each page focuses on ONE topic
- Clear navigation between related content
- Breadcrumbs for orientation

#### 2. **Better Conversion Path**
```
Home → Learn about specific module → See pricing → Book demo
```

#### 3. **SEO Benefits**
- More pages = more keywords
- Dedicated URLs for each module
- Better internal linking

#### 4. **Easier Updates**
- Add new modules without cluttering main page
- Update pricing independently
- A/B test individual pages

---

### Excel Module Content (NEW)

**Hero Section**:
```
"Turn Excel into Your AI Assistant"
Natural language queries. Instant charts. Automated workflows.
[Try Excel Copilot →]
```

**Features**:
1. **Natural Language Queries**
   - "Show me elevators with 1966 regulations by region"
   - Get instant tables with filtered data
   - No formulas needed

2. **One-Click Charts**
   - "Create a bar chart showing..."
   - AI generates the chart automatically
   - Download Excel with embedded chart

3. **Macro System**
   - Save frequent queries as macros
   - One-click reuse
   - Share with team

4. **Workflow Context**
   - Define custom workflows
   - AI follows your business logic
   - Consistent results every time

5. **Multi-Sheet Analysis**
   - Query across multiple sheets
   - Automatic data correlation
   - Complex analysis made simple

**Use Cases**:
- Regulatory compliance tracking
- Asset inventory analysis
- Maintenance schedule optimization
- Incident data reporting
- Cost analysis and forecasting

**Pricing**: €15/month per seat (add-on to Pro plan)

---

### Technical Implementation

#### Phase 1: Fix Current Issues (Immediate)
1. ✅ Update Google Analytics code
2. ✅ Add Excel module to current page
3. ✅ Update feature descriptions

#### Phase 2: Create New Pages (Week 1-2)
1. Create page templates
2. Split content into separate pages
3. Implement navigation
4. Add breadcrumbs

#### Phase 3: Excel Module Page (Week 2)
1. Design Excel module page
2. Add screenshots/demos
3. Write copy
4. Add to navigation

#### Phase 4: Polish & Launch (Week 3)
1. Test all links
2. Mobile optimization
3. SEO optimization
4. Analytics setup
5. Launch

---

### Files to Create

```
engiintel-website/
├── index.html (redesigned - shorter)
├── features.html (new)
├── modules.html (new)
├── modules/
│   ├── document-intelligence.html
│   ├── excel-copilot.html ⭐ NEW
│   ├── wiki.html
│   ├── assets.html
│   ├── incidents.html
│   └── ai-agent.html
├── industries.html (new)
├── pricing.html (new)
├── how-it-works.html (new)
├── contact.html (new)
├── css/
│   └── styles.css (shared styles)
└── js/
    └── main.js (shared scripts)
```

---

### Next Steps

**Option A: Quick Fix (1-2 hours)**
- Update Google Analytics
- Add Excel module section to current page
- Update feature list

**Option B: Full Redesign (2-3 weeks)**
- Implement multi-page architecture
- Create all new pages
- Better UX and conversion

**Recommendation**: Start with Option A (quick wins), then plan Option B for next sprint.

---

## Questions for Validation

1. **Priority**: Quick fix or full redesign?
2. **Excel Module**: Should it be a separate page or section on modules page?
3. **Navigation**: Dropdown menus or separate pages only?
4. **Content**: Do you have screenshots/demos of Excel module?
5. **Timeline**: When do you need this live?

Please review and let me know which approach you prefer!
