#!/usr/bin/env python3
"""
Step 2: Add tooltips to pricing modules
"""

import re
from pathlib import Path

# Read current version
with open("index.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Create backup
with open("index-backup-step2.html", 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Backup created: index-backup-step2.html")

# Step 1: Add tooltip CSS before closing </style>
tooltip_css = """
/* Tooltip System */
.info-tooltip {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--border);
  color: var(--text-dim);
  font-size: 0.7rem;
  font-family: 'DM Mono', monospace;
  cursor: help;
  margin-left: 6px;
  position: relative;
  transition: all 0.2s;
}

.info-tooltip:hover {
  background: var(--accent);
  color: var(--bg);
}

.info-tooltip::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: var(--surface2);
  color: var(--text);
  padding: 8px 12px;
  border-radius: 4px;
  font-size: 0.75rem;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
  border: 1px solid var(--border);
  z-index: 1000;
  font-family: 'DM Sans', sans-serif;
  max-width: 250px;
  white-space: normal;
  text-align: center;
}

.info-tooltip:hover::after {
  opacity: 1;
}

@media (max-width: 768px) {
  .info-tooltip::after {
    left: auto;
    right: 0;
    transform: none;
  }
}
"""

# Find last </style> in head
head_end = content.find('</head>')
if head_end == -1:
    print("❌ Could not find </head>")
    exit(1)

head_content = content[:head_end]
last_style_pos = head_content.rfind('</style>')

if last_style_pos == -1:
    print("❌ Could not find </style>")
    exit(1)

content = content[:last_style_pos] + "\n" + tooltip_css + "\n" + content[last_style_pos:]
print("✅ Added tooltip CSS")

# Step 2: Add tooltips to each module
# Define tooltips for each module
tooltips = {
    'Core (RAG)': 'AI document search with page-level citations',
    'Operations': 'Task management, projects, workflow automation',
    'Excel Copilot': 'Query Excel in natural language, generate charts',
    'Wiki': 'Knowledge base with markdown and version control',
    'Incidents': 'Generate incident reports with AI assistance',
    'AI Agent': 'Autonomous AI agents for multi-step tasks',
    'Analytics': 'Usage tracking and productivity metrics'
}

# Add tooltip to Core module
core_pattern = r'(<span class="calc-mod-name" data-en="Core \(RAG\)" data-es="Core \(RAG\)">Core \(RAG\)</span>)'
core_replacement = r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Core (RAG)'] + '">ⓘ</span>'
content = re.sub(core_pattern, core_replacement, content)
print("✅ Added tooltip to Core (RAG)")

# Add tooltip to Operations
ops_pattern = r'(<span class="calc-mod-name" data-en="Operations" data-es="Operaciones">Operations</span>)'
ops_replacement = r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Operations'] + '">ⓘ</span>'
content = re.sub(ops_pattern, ops_replacement, content)
print("✅ Added tooltip to Operations")

# Add tooltip to Excel Copilot
excel_pattern = r'(<span class="calc-mod-name" data-en="Excel Copilot" data-es="Copiloto Excel">Excel Copilot</span>)'
excel_replacement = r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Excel Copilot'] + '">ⓘ</span>'
content = re.sub(excel_pattern, excel_replacement, content)
print("✅ Added tooltip to Excel Copilot")

# Add tooltip to Wiki
wiki_pattern = r'(<span class="calc-mod-name" data-en="Wiki" data-es="Wiki">Wiki</span>)'
wiki_replacement = r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Wiki'] + '">ⓘ</span>'
content = re.sub(wiki_pattern, wiki_replacement, content)
print("✅ Added tooltip to Wiki")

# Add tooltip to Incidents
incidents_pattern = r'(<span class="calc-mod-name" data-en="Incidents" data-es="Incidencias">Incidents</span>)'
incidents_replacement = r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Incidents'] + '">ⓘ</span>'
content = re.sub(incidents_pattern, incidents_replacement, content)
print("✅ Added tooltip to Incidents")

# Add tooltip to AI Agent
agent_pattern = r'(<span class="calc-mod-name" data-en="AI Agent" data-es="Agente IA">AI Agent</span>)'
agent_replacement = r'\1<span class="info-tooltip" data-tooltip="' + tooltips['AI Agent'] + '">ⓘ</span>'
content = re.sub(agent_pattern, agent_replacement, content)
print("✅ Added tooltip to AI Agent")

# Add tooltip to Analytics
analytics_pattern = r'(<span class="calc-mod-name" data-en="Analytics" data-es="Analítica">Analytics</span>)'
analytics_replacement = r'\1<span class="info-tooltip" data-tooltip="' + tooltips['Analytics'] + '">ⓘ</span>'
content = re.sub(analytics_pattern, analytics_replacement, content)
print("✅ Added tooltip to Analytics")

# Write updated content
with open("index.html", 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Step 2 Complete: Tooltips added to all pricing modules")
print("📋 Test: Go to Pricing tab and hover over ⓘ icons")
