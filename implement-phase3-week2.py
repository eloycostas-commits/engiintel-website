#!/usr/bin/env python3
"""
Phase 3 Week 2: UX Improvements Implementation
Tasks #5-8: Group capabilities, add screenshots, simplify pricing, add use cases
"""

import re
from pathlib import Path

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def task5_group_capabilities(html):
    """
    Task #5: Group capabilities into 3 strategic categories
    - Security & Compliance (primary differentiator)
    - Productivity & Automation (core value)
    - Integration & Scalability (technical strength)
    """
    print("✓ Task #5: Grouping capabilities into 3 categories...")
    
    # Find the Features tab content
    features_section = '''
<!-- FEATURES TAB - REDESIGNED WITH CATEGORIES -->
<div id="features" class="tab-content">
  <div class="section-label" data-en="Platform Capabilities" data-es="Capacidades de la Plataforma">Platform Capabilities</div>
  <h2 data-en="Everything You Need for Regulated Industries" data-es="Todo lo que Necesitas para Industrias Reguladas">Everything You Need for Regulated Industries</h2>
  <p class="section-sub" data-en="EngiIntel combines security, productivity, and integration in one powerful platform. Built specifically for engineering teams in regulated environments." data-es="EngiIntel combina seguridad, productividad e integración en una plataforma potente. Construido específicamente para equipos de ingeniería en entornos regulados.">
    EngiIntel combines security, productivity, and integration in one powerful platform. Built specifically for engineering teams in regulated environments.
  </p>

  <!-- Category 1: Security & Compliance -->
  <div style="margin-top: 60px;">
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">
      <span style="font-size: 2.5rem;">🔒</span>
      <div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.5rem; margin: 0; color: var(--accent);" data-en="Security & Compliance" data-es="Seguridad y Cumplimiento">Security & Compliance</h3>
        <p style="margin: 4px 0 0; color: var(--text-dim); font-size: 0.9rem;" data-en="Your primary differentiator - zero data risk" data-es="Tu diferenciador principal - cero riesgo de datos">Your primary differentiator - zero data risk</p>
      </div>
    </div>
    
    <div class="modules-grid">
      <div class="module-card">
        <span class="module-icon">🏢</span>
        <div class="module-name" data-en="100% On-Premise Deployment" data-es="Despliegue 100% On-Premise">100% On-Premise Deployment</div>
        <div class="module-desc" data-en="Your data never leaves your infrastructure. Complete air-gapped deployment with zero cloud dependencies." data-es="Tus datos nunca salen de tu infraestructura. Despliegue completamente aislado sin dependencias en la nube.">
          Your data never leaves your infrastructure. Complete air-gapped deployment with zero cloud dependencies.
        </div>
        <ul class="module-features">
          <li data-en="Air-gapped architecture" data-es="Arquitectura aislada">Air-gapped architecture</li>
          <li data-en="No external API calls" data-es="Sin llamadas API externas">No external API calls</li>
          <li data-en="Complete data sovereignty" data-es="Soberanía completa de datos">Complete data sovereignty</li>
        </ul>
      </div>

      <div class="module-card">
        <span class="module-icon">✅</span>
        <div class="module-name" data-en="GDPR & ISO Compliant" data-es="Cumplimiento GDPR e ISO">GDPR & ISO Compliant</div>
        <div class="module-desc" data-en="Built-in compliance with GDPR, ISO 27001, and industry-specific regulations. Audit trails and logging included." data-es="Cumplimiento integrado con GDPR, ISO 27001 y regulaciones específicas de la industria. Registros de auditoría incluidos.">
          Built-in compliance with GDPR, ISO 27001, and industry-specific regulations. Audit trails and logging included.
        </div>
        <ul class="module-features">
          <li data-en="GDPR compliant by design" data-es="Cumplimiento GDPR por diseño">GDPR compliant by design</li>
          <li data-en="Complete audit trails" data-es="Registros de auditoría completos">Complete audit trails</li>
          <li data-en="Data retention policies" data-es="Políticas de retención de datos">Data retention policies</li>
        </ul>
      </div>

      <div class="module-card">
        <span class="module-icon">🔐</span>
        <div class="module-name" data-en="Role-Based Access Control" data-es="Control de Acceso Basado en Roles">Role-Based Access Control</div>
        <div class="module-desc" data-en="Granular permissions and user management. Control who can access what data and perform which actions." data-es="Permisos granulares y gestión de usuarios. Controla quién puede acceder a qué datos y realizar qué acciones.">
          Granular permissions and user management. Control who can access what data and perform which actions.
        </div>
        <ul class="module-features">
          <li data-en="Custom user roles" data-es="Roles de usuario personalizados">Custom user roles</li>
          <li data-en="Document-level permissions" data-es="Permisos a nivel de documento">Document-level permissions</li>
          <li data-en="Activity logging" data-es="Registro de actividad">Activity logging</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Category 2: Productivity & Automation -->
  <div style="margin-top: 80px;">
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">
      <span style="font-size: 2.5rem;">⚡</span>
      <div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.5rem; margin: 0; color: var(--accent3);" data-en="Productivity & Automation" data-es="Productividad y Automatización">Productivity & Automation</h3>
        <p style="margin: 4px 0 0; color: var(--text-dim); font-size: 0.9rem;" data-en="Core value - save 15+ hours per week" data-es="Valor principal - ahorra 15+ horas por semana">Core value - save 15+ hours per week</p>
      </div>
    </div>
    
    <div class="modules-grid">
      <div class="module-card">
        <span class="module-icon">🔍</span>
        <div class="module-name" data-en="RAG Document Search" data-es="Búsqueda RAG de Documentos">RAG Document Search</div>
        <div class="module-desc" data-en="Query 10,000+ documents in seconds with page-level citations. Natural language queries in Spanish or English." data-es="Consulta 10,000+ documentos en segundos con citas a nivel de página. Consultas en lenguaje natural en español o inglés.">
          Query 10,000+ documents in seconds with page-level citations. Natural language queries in Spanish or English.
        </div>
        <ul class="module-features">
          <li data-en="Hybrid semantic + keyword search" data-es="Búsqueda híbrida semántica + palabras clave">Hybrid semantic + keyword search</li>
          <li data-en="Page-level citations" data-es="Citas a nivel de página">Page-level citations</li>
          <li data-en="Multi-document context" data-es="Contexto multi-documento">Multi-document context</li>
        </ul>
      </div>

      <div class="module-card">
        <span class="module-icon">📊</span>
        <div class="module-name" data-en="Automated Report Generation" data-es="Generación Automática de Informes">Automated Report Generation</div>
        <div class="module-desc" data-en="Generate incident reports, maintenance logs, and compliance documents in one click. Reduce 2+ hours to 10 minutes." data-es="Genera informes de incidencias, registros de mantenimiento y documentos de cumplimiento en un clic. Reduce 2+ horas a 10 minutos.">
          Generate incident reports, maintenance logs, and compliance documents in one click. Reduce 2+ hours to 10 minutes.
        </div>
        <ul class="module-features">
          <li data-en="Template-based generation" data-es="Generación basada en plantillas">Template-based generation</li>
          <li data-en="Auto-fill from data sources" data-es="Auto-completado desde fuentes de datos">Auto-fill from data sources</li>
          <li data-en="PDF/Word export" data-es="Exportación PDF/Word">PDF/Word export</li>
        </ul>
      </div>

      <div class="module-card">
        <span class="module-icon">🤖</span>
        <div class="module-name" data-en="AI Agent Mode" data-es="Modo Agente IA">AI Agent Mode</div>
        <div class="module-desc" data-en="Autonomous AI agents that execute multi-step tasks. From data extraction to workflow automation." data-es="Agentes IA autónomos que ejecutan tareas multi-paso. Desde extracción de datos hasta automatización de flujos.">
          Autonomous AI agents that execute multi-step tasks. From data extraction to workflow automation.
        </div>
        <ul class="module-features">
          <li data-en="Multi-step task execution" data-es="Ejecución de tareas multi-paso">Multi-step task execution</li>
          <li data-en="Tool integration" data-es="Integración de herramientas">Tool integration</li>
          <li data-en="Scheduled automation" data-es="Automatización programada">Scheduled automation</li>
        </ul>
      </div>

      <div class="module-card">
        <span class="module-icon">📚</span>
        <div class="module-name" data-en="Wiki Knowledge Base" data-es="Base de Conocimiento Wiki">Wiki Knowledge Base</div>
        <div class="module-desc" data-en="Centralized knowledge management with AI-powered search. Keep your team's expertise accessible and organized." data-es="Gestión centralizada del conocimiento con búsqueda potenciada por IA. Mantén la experiencia de tu equipo accesible y organizada.">
          Centralized knowledge management with AI-powered search. Keep your team's expertise accessible and organized.
        </div>
        <ul class="module-features">
          <li data-en="Markdown-based editing" data-es="Edición basada en Markdown">Markdown-based editing</li>
          <li data-en="Version control" data-es="Control de versiones">Version control</li>
          <li data-en="AI-powered search" data-es="Búsqueda potenciada por IA">AI-powered search</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Category 3: Integration & Scalability -->
  <div style="margin-top: 80px; margin-bottom: 60px;">
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">
      <span style="font-size: 2.5rem;">🔗</span>
      <div>
        <h3 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.5rem; margin: 0; color: var(--accent2);" data-en="Integration & Scalability" data-es="Integración y Escalabilidad">Integration & Scalability</h3>
        <p style="margin: 4px 0 0; color: var(--text-dim); font-size: 0.9rem;" data-en="Technical strength - works with your existing tools" data-es="Fortaleza técnica - funciona con tus herramientas existentes">Technical strength - works with your existing tools</p>
      </div>
    </div>
    
    <div class="modules-grid">
      <div class="module-card">
        <span class="module-icon">🐘</span>
        <div class="module-name" data-en="PostgreSQL Support" data-es="Soporte PostgreSQL">PostgreSQL Support</div>
        <div class="module-desc" data-en="Native PostgreSQL integration for structured data. Query databases alongside documents with natural language." data-es="Integración nativa con PostgreSQL para datos estructurados. Consulta bases de datos junto con documentos en lenguaje natural.">
          Native PostgreSQL integration for structured data. Query databases alongside documents with natural language.
        </div>
        <ul class="module-features">
          <li data-en="SQL query generation" data-es="Generación de consultas SQL">SQL query generation</li>
          <li data-en="Natural language to SQL" data-es="Lenguaje natural a SQL">Natural language to SQL</li>
          <li data-en="Multi-database support" data-es="Soporte multi-base de datos">Multi-database support</li>
        </ul>
      </div>

      <div class="module-card">
        <span class="module-icon">🐳</span>
        <div class="module-name" data-en="Docker Deployment" data-es="Despliegue Docker">Docker Deployment</div>
        <div class="module-desc" data-en="One-command deployment with Docker Compose. Production-ready in minutes, not days." data-es="Despliegue con un comando usando Docker Compose. Listo para producción en minutos, no días.">
          One-command deployment with Docker Compose. Production-ready in minutes, not days.
        </div>
        <ul class="module-features">
          <li data-en="Docker Compose included" data-es="Docker Compose incluido">Docker Compose included</li>
          <li data-en="Auto-scaling support" data-es="Soporte de auto-escalado">Auto-scaling support</li>
          <li data-en="Health monitoring" data-es="Monitoreo de salud">Health monitoring</li>
        </ul>
      </div>

      <div class="module-card">
        <span class="module-icon">🔄</span>
        <div class="module-name" data-en="n8n Workflow Automation" data-es="Automatización de Flujos n8n">n8n Workflow Automation</div>
        <div class="module-desc" data-en="Visual workflow builder with 300+ integrations. Connect EngiIntel to your existing tools without code." data-es="Constructor visual de flujos con 300+ integraciones. Conecta EngiIntel a tus herramientas existentes sin código.">
          Visual workflow builder with 300+ integrations. Connect EngiIntel to your existing tools without code.
        </div>
        <ul class="module-features">
          <li data-en="300+ pre-built integrations" data-es="300+ integraciones pre-construidas">300+ pre-built integrations</li>
          <li data-en="Visual workflow editor" data-es="Editor visual de flujos">Visual workflow editor</li>
          <li data-en="Webhook support" data-es="Soporte de webhooks">Webhook support</li>
        </ul>
      </div>

      <div class="module-card">
        <span class="module-icon">📡</span>
        <div class="module-name" data-en="REST API" data-es="API REST">REST API</div>
        <div class="module-desc" data-en="Complete REST API for custom integrations. Build your own tools on top of EngiIntel's AI capabilities." data-es="API REST completa para integraciones personalizadas. Construye tus propias herramientas sobre las capacidades de IA de EngiIntel.">
          Complete REST API for custom integrations. Build your own tools on top of EngiIntel's AI capabilities.
        </div>
        <ul class="module-features">
          <li data-en="OpenAPI documentation" data-es="Documentación OpenAPI">OpenAPI documentation</li>
          <li data-en="Authentication & rate limiting" data-es="Autenticación y límite de tasa">Authentication & rate limiting</li>
          <li data-en="Webhook callbacks" data-es="Callbacks de webhook">Webhook callbacks</li>
        </ul>
      </div>
    </div>
  </div>
</div>
'''
    
    return features_section

def main():
    print("=" * 60)
    print("PHASE 3 WEEK 2: UX IMPROVEMENTS IMPLEMENTATION")
    print("=" * 60)
    print()
    
    # Generate the new Features tab content
    features_html = task5_group_capabilities("")
    
    # Save to a separate file for manual integration
    write_file('features-tab-redesigned.html', features_html)
    print("✓ Created features-tab-redesigned.html")
    print()
    print("Next: Manually replace the Features tab in index.html")
    print("      with the content from features-tab-redesigned.html")

if __name__ == '__main__':
    main()
