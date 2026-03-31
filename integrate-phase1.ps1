# Phase 1 Integration Script - PowerShell
# This script integrates the new tabs into index.html

Write-Host "Starting Phase 1 Integration..." -ForegroundColor Cyan

# 1. Backup current index.html
Write-Host "Creating backup..." -ForegroundColor Yellow
Copy-Item "index.html" "index-backup-$(Get-Date -Format 'yyyyMMdd-HHmmss').html"

# 2. Read current index.html
$content = Get-Content "index.html" -Raw

# 3. Read tab content files
$overviewContent = Get-Content "tabs/overview.html" -Raw
$featuresContent = Get-Content "tabs/features.html" -Raw
$industriesContent = Get-Content "tabs/industries.html" -Raw
$resourcesContent = Get-Content "tabs/resources.html" -Raw

# 4. Update tabs navigation - add new tabs and reorder
$oldTabsNav = @'
<div class="tabs-container">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('document-intelligence')" data-en="Document Intelligence" data-es="Inteligencia Documental">Document Intelligence</button>
    <button class="tab-btn" onclick="switchTab('excel-copilot')" data-en="Excel Copilot" data-es="Excel Copilot">Excel Copilot</button>
    <button class="tab-btn" onclick="switchTab('wiki')" data-en="Wiki" data-es="Wiki">Wiki</button>
    <button class="tab-btn" onclick="switchTab('assets')" data-en="Assets" data-es="Activos">Assets</button>
    <button class="tab-btn" onclick="switchTab('incidents')" data-en="Incidents" data-es="Incidencias">Incidents</button>
    <button class="tab-btn" onclick="switchTab('ai-agent')" data-en="AI Agent" data-es="Agente IA">AI Agent</button>
    <button class="tab-btn" onclick="switchTab('pricing')" data-en="Pricing" data-es="Precios">Pricing</button>
  </div>
</div>
'@

$newTabsNav = @'
<div class="tabs-container">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('overview')" data-en="Overview" data-es="Resumen">Overview</button>
    <button class="tab-btn" onclick="switchTab('features')" data-en="Features" data-es="Características">Features</button>
    <button class="tab-btn" onclick="switchTab('document-intelligence')" data-en="Document Intelligence" data-es="Inteligencia Documental">Document Intelligence</button>
    <button class="tab-btn" onclick="switchTab('excel-copilot')" data-en="Excel Copilot" data-es="Excel Copilot">Excel Copilot</button>
    <button class="tab-btn" onclick="switchTab('wiki')" data-en="Wiki" data-es="Wiki">Wiki</button>
    <button class="tab-btn" onclick="switchTab('assets')" data-en="Assets" data-es="Activos">Assets</button>
    <button class="tab-btn" onclick="switchTab('incidents')" data-en="Incidents" data-es="Incidencias">Incidents</button>
    <button class="tab-btn" onclick="switchTab('ai-agent')" data-en="AI Agent" data-es="Agente IA">AI Agent</button>
    <button class="tab-btn" onclick="switchTab('industries')" data-en="Industries" data-es="Industrias">Industries</button>
    <button class="tab-btn" onclick="switchTab('pricing')" data-en="Pricing" data-es="Precios">Pricing</button>
    <button class="tab-btn" onclick="switchTab('resources')" data-en="Resources" data-es="Recursos">Resources</button>
  </div>
</div>
'@

Write-Host "Updating tabs navigation..." -ForegroundColor Yellow
$content = $content -replace [regex]::Escape($oldTabsNav), $newTabsNav

# 5. Update document-intelligence tab to remove active class
$content = $content -replace 'id="document-intelligence" class="tab-content active"', 'id="document-intelligence" class="tab-content"'

# 6. Insert new tab content sections BEFORE document-intelligence tab
$insertMarker = '<!-- Tab Content: Document Intelligence -->'
$newTabsSections = @"
<!-- Tab Content: Overview -->
$overviewContent

<!-- Tab Content: Features -->
$featuresContent

<!-- Tab Content: Document Intelligence -->
"@

Write-Host "Inserting new tab content..." -ForegroundColor Yellow
$content = $content -replace [regex]::Escape($insertMarker), $newTabsSections

# 7. Insert Industries and Resources tabs BEFORE Pricing tab
$pricingMarker = '<!-- Tab Content: Pricing -->'
$industriesResourcesSections = @"
<!-- Tab Content: Industries -->
$industriesContent

<!-- Tab Content: Resources -->
$resourcesContent

<!-- Tab Content: Pricing -->
"@

$content = $content -replace [regex]::Escape($pricingMarker), $industriesResourcesSections

# 8. Save the updated content
Write-Host "Saving updated index.html..." -ForegroundColor Yellow
$content | Set-Content "index.html" -NoNewline

Write-Host "`nPhase 1 Integration Complete!" -ForegroundColor Green
Write-Host "Changes made:" -ForegroundColor Cyan
Write-Host "  - Added 4 new tabs: Overview, Features, Industries, Resources" -ForegroundColor White
Write-Host "  - Overview is now the default active tab" -ForegroundColor White
Write-Host "  - Total tabs: 11" -ForegroundColor White
Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "  1. Test locally: Open index.html in browser" -ForegroundColor White
Write-Host "  2. Commit: git add index.html" -ForegroundColor White
Write-Host "  3. Commit: git commit -m 'Phase 1: Integrate new tabs into index.html'" -ForegroundColor White
Write-Host "  4. Deploy: git push origin main" -ForegroundColor White
