# Pricing Calculator Restoration Status

## Completed Tasks

### 1. Pricing Calculator HTML ✓
- Added interactive calculator with seat counter
- Added module selection toggles (Operations, Excel Copilot, Wiki, Incidents, AI Agent, Analytics)
- Added price summary panel with real-time updates
- Added volume discount display
- Calculator button navigates to Resources tab

### 2. Pricing Calculator CSS ✓
- Added complete styling for calculator components
- Responsive design for mobile devices
- Hover effects and transitions
- Grid layout for modules

### 3. Pricing Calculator JavaScript ✓
- `toggleMod(id)` - Toggles module selection
- `adjustSeats(delta)` - Increments/decrements seat count
- `calcPrice()` - Calculates total price with volume discounts
- Pricing logic: Core €8/seat + €4/seat per module
- Volume discounts: 15+ seats (-10%), 25+ seats (-15%), 50+ seats (-20%)
- Bilingual support (EN/ES)

### 4. Hero CTA Buttons ✓
- Changed from `<a href="#">` to `<button onclick="switchTab('resources')">`
- Both "Request Beta Access" and "Book a Demo" now navigate to Resources tab

## Known Issues

### CSS Corruption
All recent commits have JavaScript code mixed into the CSS section around lines 79-84:
```css
.lang-btn {
  ...
  font-size: 0.75rem;
        // Send to n8n webhook
        const webhookUrl = window.location.hostname === 'localhost' 
          ? 'http://localhost:5678/webhook/contact-form'
          : 'https://n8n.engiintel.com/webhook/contact-form';
        const response = await fetch(webhookUrl, {
}
```

This needs to be manually fixed by:
1. Removing the JavaScript code from the CSS section
2. Adding proper closing for `.lang-btn` rule:
```css
.lang-btn {
  background: none;
  border: 1px solid var(--border);
  color: var(--text-dim);
  padding: 6px 12px;
  font-family: 'DM Mono', monospace;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;
}
```

## Next Steps

1. Manually fix CSS corruption in index.html
2. Add form submission handler for contact form (if not already present)
3. Test calculator functionality in browser
4. Test form submission to n8n webhook
5. Commit and deploy changes

## Files Modified

- `engiintel-website/index.html` - Added calculator HTML, CSS, and JavaScript
- `engiintel-website/complete-pricing-restore.py` - Script to restore calculator
- `engiintel-website/restore-pricing-calculator.py` - Original restore script

## Testing Checklist

- [ ] Calculator displays correctly on desktop
- [ ] Calculator displays correctly on mobile
- [ ] Seat counter increments/decrements properly
- [ ] Module toggles work correctly
- [ ] Price updates in real-time
- [ ] Volume discounts apply correctly (15/25/50 seats)
- [ ] Language switching works (EN/ES)
- [ ] CTA buttons navigate to Resources tab
- [ ] Contact form submits to n8n webhook
- [ ] Success/error messages display correctly
