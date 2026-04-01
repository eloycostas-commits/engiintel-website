/**
 * Convert all JPG screenshots to WebP for better performance.
 * Outputs to public/screenshots/ alongside the originals.
 * Run: node convert-webp.js
 */

const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const SCREENSHOTS_DIR = path.join(__dirname, 'public', 'screenshots');

async function convertAll() {
  const files = fs.readdirSync(SCREENSHOTS_DIR).filter(f => /\.(jpg|jpeg)$/i.test(f));

  console.log(`Found ${files.length} JPG files to convert...\n`);

  const results = [];

  for (const file of files) {
    const inputPath = path.join(SCREENSHOTS_DIR, file);
    const outputName = file.replace(/\.(jpg|jpeg)$/i, '.webp');
    const outputPath = path.join(SCREENSHOTS_DIR, outputName);

    try {
      const meta = await sharp(inputPath)
        .webp({ quality: 82, effort: 4 })
        .toFile(outputPath);

      const inputSize = fs.statSync(inputPath).size;
      const outputSize = fs.statSync(outputPath).size;
      const saving = Math.round((1 - outputSize / inputSize) * 100);

      results.push({ file, outputName, width: meta.width, height: meta.height, saving });
      console.log(`✅ ${file} → ${outputName}  (${saving}% smaller, ${meta.width}×${meta.height})`);
    } catch (err) {
      console.error(`❌ Failed: ${file} — ${err.message}`);
    }
  }

  console.log('\n--- Summary ---');
  console.log(`Converted: ${results.length}/${files.length}`);

  // Print the picture element template for each file
  console.log('\n--- Picture element map (for components) ---');
  for (const r of results) {
    const base = r.file.replace(/\.(jpg|jpeg)$/i, '');
    console.log(`${r.file}: ${r.width}×${r.height}`);
  }
}

convertAll().catch(console.error);
