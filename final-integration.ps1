# Final Integration Script - Phase 1
# This script integrates all new tabs and screenshots

Write-Host "Starting Phase 1 Final Integration..." -ForegroundColor Cyan
Write-Host ""

# Read files
Write-Host "Reading files..." -ForegroundColor Yellow
$html = Get-Content -Path "index.html" -Raw -Encoding UTF8
$overview = Get-Content -Path "tabs/overview.html" -Raw -Encoding UTF8
$features = Get-Content -Path "tabs/features.html" -Raw -Encoding UTF8
$industries = Get-Content -Path "tabs/industries.html" -Raw -Encoding UTF8
$resources = Get-Content -Path "tabs/resources.html" -Raw -Encoding UTF8

# Screenshot mapping
$screenshotMap = @{
    '[Screenshot: Query + Results]' = 'screenshots/comparar documen...';
    '[Screenshot: Architecture Diagram]' = 'screenshots/panel principal.jpg';
    '[Screenshot: OCR Processing]' = 'screenshots/panel principal.jpg';
    '[Screenshot: Chart Generation]' = 'screenshots/are de analisis.jpg';
    '[Screenshot: Connectors]' = 'screenshots/panel principal.jpg';
    '[Screenshot: Audit Log]' = 'screenshots/Paneld e Adminis...';
    '[Screenshot: Docker Deploy]' = 'screenshots/panel principal.jpg';
    '[Screenshot: Upload Interface]' = 'screenshots/panel principal.jpg';
}

# Replace screenshot placeholders in overview tab
Write-Host "Replacing screenshot placeholders..." -ForegroundColor Yellow
foreach ($placeholder in $screenshotMap.Keys) {
    $imagePath = $screenshotMap[$placeholder]
    $styleAttr = 'width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;'
    $imgTag = "<img src=`"$imagePath`" alt=`"EngiIntel Screenshot`" style=`"$styleAttr`">"
    $placeholderDiv = "<div class=`"screenshot-placeholder`" data-en=`"$placeholder`" data-es=`"[Captura: *]`">$placeholder</div>"
    $overview = $overview -replace [regex]::Escape($placeholderDiv), $imgTag
    
    # Also try simpler pattern
    $overview = $overview -replace "<div class=`"screenshot-placeholder`"[^>]*>.*?$placeholder.*?</div>", $imgTag
}

# Step 1: Insert Overview and Features tabs
Write-Host "Inserting Overview and Features tabs..." -ForegroundColor Yellow
$marker1 = "</div>`r`n</div>`r`n`r`n`r`n<!-- Tab Content: Document Intelligence -->"
$replacement1 = "</div>`r`n</div>`r`n`r`n`r`n$overview`r`n`r`n$features`r`n`r`n<!-- Tab Content: Document Intelligence -->"
$html = $html -replace [regex]::Escape($marker1), $replacement1

# Step 2: Change document-intelligence from active to inactive
Write-Host "Updating active tab..." -ForegroundColor Yellow
$html = $html -replace '<div id="document-intelligence" class="tab-content active">', '<div id="document-intelligence" class="tab-content">'

# Step 3: Insert Industries tab before Pricing
Write-Host "Inserting Industries tab..." -ForegroundColor Yellow
$marker2 = "<!-- Tab Content: Pricing -->"
$replacement2 = "$industries`r`n`r`n`r`n$marker2"
$html = $html -replace [regex]::Escape($marker2), $replacement2

# Step 4: Insert Resources tab before Footer
Write-Host "Inserting Resources tab..." -ForegroundColor Yellow
$footerComment = '<!-- Footer (Always Visible) -->'
$beforeFooter = "</div>`r`n`r`n`r`n"
$marker3 = $beforeFooter + $footerComment
$replacement3 = $beforeFooter + $resources + "`r`n`r`n`r`n" + $footerComment
$html = $html -replace [regex]::Escape($marker3), $replacement3

# Write output
Write-Host "Writing integrated file..." -ForegroundColor Yellow
$html | Out-File -FilePath "index-integrated.html" -Encoding UTF8 -NoNewline

Write-Host ""
Write-Host "Integration complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  - Created: index-integrated.html" -ForegroundColor White
Write-Host "  - Added: 4 new tabs (Overview, Features, Industries, Resources)" -ForegroundColor White
Write-Host "  - Replaced: Screenshot placeholders with actual images" -ForegroundColor White
Write-Host "  - Updated: Active tab to Overview" -ForegroundColor White
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Open index-integrated.html in your browser" -ForegroundColor White
Write-Host "  2. Test all tabs and language switching" -ForegroundColor White
Write-Host "  3. If everything works, rename:" -ForegroundColor White
Write-Host "     mv index.html index-old.html" -ForegroundColor Gray
Write-Host "     mv index-integrated.html index.html" -ForegroundColor Gray
Write-Host "  4. Deploy to Vercel" -ForegroundColor White
Write-Host ""
