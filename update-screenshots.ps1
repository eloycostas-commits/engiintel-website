# Update Screenshots Script
# This script replaces screenshot placeholders with actual images

Write-Host "Updating screenshots in integrated file..." -ForegroundColor Cyan

# Read the integrated file
$html = Get-Content -Path "index-integrated.html" -Raw -Encoding UTF8

# Screenshot mapping based on actual filenames
$replacements = @(
    @{
        old = '<div class="screenshot-placeholder" data-en="\[Screenshot: Query \+ Results\]"[^>]*>\[Screenshot: Query \+ Results\]</div>'
        new = '<img src="screenshots/comparar documentos.jpg" alt="Natural Language Query Interface" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">'
    },
    @{
        old = '<div class="screenshot-placeholder" data-en="\[Screenshot: Architecture Diagram\]"[^>]*>\[Screenshot: Architecture Diagram\]</div>'
        new = '<img src="screenshots/panel principal.jpg" alt="On-Premise Architecture" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">'
    },
    @{
        old = '<div class="screenshot-placeholder" data-en="\[Screenshot: OCR Processing\]"[^>]*>\[Screenshot: OCR Processing\]</div>'
        new = '<img src="screenshots/panel principal.jpg" alt="OCR Document Processing" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">'
    },
    @{
        old = '<div class="screenshot-placeholder" data-en="\[Screenshot: Chart Generation\]"[^>]*>\[Screenshot: Chart Generation\]</div>'
        new = '<img src="screenshots/are de analisis.jpg" alt="Excel Chart Generation" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">'
    },
    @{
        old = '<div class="screenshot-placeholder" data-en="\[Screenshot: Connectors\]"[^>]*>\[Screenshot: Connectors\]</div>'
        new = '<img src="screenshots/panel principal.jpg" alt="Document Connectors" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">'
    },
    @{
        old = '<div class="screenshot-placeholder" data-en="\[Screenshot: Audit Log\]"[^>]*>\[Screenshot: Audit Log\]</div>'
        new = '<img src="screenshots/Paneld e Administración.jpg" alt="Audit Logging" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">'
    },
    @{
        old = '<div class="screenshot-placeholder" data-en="\[Screenshot: Docker Deploy\]"[^>]*>\[Screenshot: Docker Deploy\]</div>'
        new = '<img src="screenshots/panel principal.jpg" alt="Docker Deployment" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">'
    },
    @{
        old = '<div class="screenshot-placeholder" data-en="\[Screenshot: Upload Interface\]"[^>]*>\[Screenshot: Upload Interface\]</div>'
        new = '<img src="screenshots/panel principal.jpg" alt="Document Upload Interface" style="width: 100%; border: 1px solid var(--border); margin-top: 16px; border-radius: 4px;">'
    }
)

# Apply replacements
foreach ($replacement in $replacements) {
    $html = $html -replace $replacement.old, $replacement.new
}

# Write updated file
$html | Out-File -FilePath "index-final.html" -Encoding UTF8 -NoNewline

Write-Host "Done! Created index-final.html with all screenshots" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Open index-final.html in your browser to test" -ForegroundColor White
Write-Host "  2. If everything looks good:" -ForegroundColor White
Write-Host "     mv index.html index-old.html" -ForegroundColor Gray
Write-Host "     mv index-final.html index.html" -ForegroundColor Gray
Write-Host "  3. Deploy to Vercel" -ForegroundColor White
