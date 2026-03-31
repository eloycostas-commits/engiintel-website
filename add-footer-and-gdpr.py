#!/usr/bin/env python3
"""
Add footer with legal links and GDPR cookie consent banner
"""

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def add_footer_and_gdpr(html):
    """Add footer with legal links and GDPR banner"""
    
    # Footer HTML
    footer_html = '''
<!-- Footer -->
<footer style="border-top: 1px solid var(--border); padding: 48px 60px; background: var(--surface);">
  <div style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 48px;">
    
    <!-- Column 1: Brand -->
    <div>
      <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.3rem; margin-bottom: 16px;">
        Engi<span style="color: var(--accent);">Intel</span>
      </div>
      <p style="font-size: 0.9rem; color: var(--text-dim); line-height: 1.7;" data-en="100% on-premise AI platform for regulated industries. Your data never leaves your server." data-es="Plataforma de IA 100% on-premise para industrias reguladas. Tus datos nunca salen de tu servidor.">
        100% on-premise AI platform for regulated industries. Your data never leaves your server.
      </p>
    </div>
    
    <!-- Column 2: Legal -->
    <div>
      <h4 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1rem; margin-bottom: 16px;" data-en="Legal" data-es="Legal">Legal</h4>
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <a href="privacy-policy.html" style="color: var(--text-mid); text-decoration: none; font-size: 0.9rem; transition: color 0.2s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--text-mid)'" data-en="Privacy Policy" data-es="Política de Privacidad">Privacy Policy</a>
        <a href="terms-of-service.html" style="color: var(--text-mid); text-decoration: none; font-size: 0.9rem; transition: color 0.2s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--text-mid)'" data-en="Terms of Service" data-es="Términos de Servicio">Terms of Service</a>
      </div>
    </div>
    
    <!-- Column 3: Contact -->
    <div>
      <h4 style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1rem; margin-bottom: 16px;" data-en="Contact" data-es="Contacto">Contact</h4>
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <a href="mailto:eloycostas@engiintel.com" style="color: var(--text-mid); text-decoration: none; font-size: 0.9rem; transition: color 0.2s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--text-mid)'">eloycostas@engiintel.com</a>
        <p style="font-size: 0.85rem; color: var(--text-dim); margin: 0;" data-en="Built by engineers, for engineers" data-es="Construido por ingenieros, para ingenieros">Built by engineers, for engineers</p>
      </div>
    </div>
    
  </div>
  
  <!-- Copyright -->
  <div style="max-width: 1400px; margin: 32px auto 0; padding-top: 32px; border-top: 1px solid var(--border); text-align: center;">
    <p style="font-family: 'DM Mono', monospace; font-size: 0.75rem; color: var(--text-dim);">
      © 2026 EngiIntel. <span data-en="All rights reserved." data-es="Todos los derechos reservados.">All rights reserved.</span>
    </p>
  </div>
</footer>

<!-- GDPR Cookie Consent Banner -->
<div id="gdpr-banner" style="position: fixed; bottom: 0; left: 0; right: 0; background: var(--surface2); border-top: 2px solid var(--accent); padding: 24px; z-index: 1000; display: none;">
  <div style="max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 300px;">
      <p style="font-size: 0.9rem; color: var(--text); margin: 0;" data-en="We use cookies to improve your experience and analyze site usage. By continuing to use this site, you consent to our use of cookies." data-es="Usamos cookies para mejorar tu experiencia y analizar el uso del sitio. Al continuar usando este sitio, consientes nuestro uso de cookies.">
        We use cookies to improve your experience and analyze site usage. By continuing to use this site, you consent to our use of cookies.
      </p>
      <a href="privacy-policy.html" style="color: var(--accent); font-size: 0.85rem; text-decoration: none;" data-en="Learn more" data-es="Más información">Learn more</a>
    </div>
    <div style="display: flex; gap: 12px;">
      <button onclick="acceptCookies()" style="background: var(--accent); color: var(--bg); border: none; padding: 12px 24px; font-family: 'Syne', sans-serif; font-weight: 600; font-size: 0.85rem; cursor: pointer; transition: all 0.2s;" data-en="Accept" data-es="Aceptar">Accept</button>
      <button onclick="declineCookies()" style="background: transparent; color: var(--text-mid); border: 1px solid var(--border); padding: 12px 24px; font-family: 'Syne', sans-serif; font-weight: 600; font-size: 0.85rem; cursor: pointer; transition: all 0.2s;" data-en="Decline" data-es="Rechazar">Decline</button>
    </div>
  </div>
</div>

<script>
// GDPR Cookie Consent
function showGDPRBanner() {
  const consent = localStorage.getItem('gdpr-consent');
  if (!consent) {
    document.getElementById('gdpr-banner').style.display = 'block';
  }
}

function acceptCookies() {
  localStorage.setItem('gdpr-consent', 'accepted');
  document.getElementById('gdpr-banner').style.display = 'none';
}

function declineCookies() {
  localStorage.setItem('gdpr-consent', 'declined');
  document.getElementById('gdpr-banner').style.display = 'none';
  // Disable Google Analytics if declined
  window['ga-disable-G-5P3VL8DTRG'] = true;
}

// Show banner on page load
window.addEventListener('DOMContentLoaded', showGDPRBanner);
</script>

</body>
</html>'''
    
    # Find </body></html> and replace with footer
    if '</body>' in html:
        html = html.replace('</body>\n</html>', footer_html)
    elif '</body></html>' in html:
        html = html.replace('</body></html>', footer_html)
    else:
        # Just append before the end
        html = html.rstrip() + '\n' + footer_html
    
    return html

def main():
    print("Adding footer and GDPR banner...")
    
    html = read_file('index.html')
    html = add_footer_and_gdpr(html)
    write_file('index.html', html)
    
    print("✓ Footer with legal links added")
    print("✓ GDPR cookie consent banner added")
    print()
    print("Footer includes:")
    print("  - Link to Privacy Policy")
    print("  - Link to Terms of Service")
    print("  - Contact email")
    print("  - Copyright notice")
    print()
    print("GDPR banner:")
    print("  - Shows on first visit")
    print("  - Accept/Decline options")
    print("  - Stores consent in localStorage")
    print("  - Disables GA if declined")

if __name__ == '__main__':
    main()
