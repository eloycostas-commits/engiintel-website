# PowerShell script to integrate new tabs into index.html

Write-Host "🔧 Integrating Phase 1 enhancements..." -ForegroundColor Cyan

# Read the current index.html
$html = Get-Content -Path "index.html" -Raw

# Read new tab contents
$overviewTab = Get-Content -Path "tabs/overview.html" -Raw
$featuresTab = Get-Content -Path "tabs/features.html" -Raw
$industriesTab = Get-Content -Path "tabs/industries.html" -Raw
$resourcesTab = Get-Content -Path "tabs/resources.html" -Raw

# Step 1: Insert Overview and Features tabs after tabs-container
$marker1 = "</div>`n</div>`n`n`n<!-- Tab Content: Document Intelligence -->"
$newContent1 = "</div>`n</div>`n`n`n$overviewTab`n`n$featuresTab`n`n<!-- Tab Content: Document Intelligence -->"
$html = $html -replace [regex]::Escape($marker1), $newContent1

# Step 2: Change document-intelligence from active to inactive
$html = $html -replace '<div id="document-intelligence" class="tab-content active">', '<div id="document-intelligence" class="tab-content">'

# Step 3: Insert Industries tab before Pricing
$marker2 = "<!-- Tab Content: Pricing -->"
$newContent2 = "$industriesTab`n`n`n$marker2"
$html = $html -replace [regex]::Escape($marker2), $newContent2

# Step 4: Insert Resources tab after Pricing, before Footer
$footerMarker = '<!-- Footer (Always Visible) -->'
$beforeFooter = "</div>`n`n`n"
$marker3 = $beforeFooter + $footerMarker
$newContent3 = $beforeFooter + $resourcesTab + "`n`n`n" + $footerMarker
$html = $html -replace [regex]::Escape($marker3), $newContent3

# Write the updated HTML to a new file
$html | Out-File -FilePath "index-phase1.html" -Encoding UTF8 -NoNewline

Write-Host "✅ Created index-phase1.html with all Phase 1 enhancements" -ForegroundColor Green
Write-Host "📝 Review the file, then rename to index.html when ready" -ForegroundColor Yellow
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Review index-phase1.html in your browser" -ForegroundColor White
Write-Host "2. Add your 8 screenshots to replace placeholders" -ForegroundColor White
Write-Host "3. Test all tabs and language switching" -ForegroundColor White
Write-Host "4. Rename index-phase1.html to index.html" -ForegroundColor White
Write-Host "5. Deploy to Vercel" -ForegroundColor White
