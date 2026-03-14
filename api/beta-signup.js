export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'method not allowed' });

  const { name, email, company, industry, message } = req.body ?? {};
  const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!name || !email || !emailRe.test(email)) {
    return res.status(400).json({ error: 'name and valid email are required' });
  }

  const resendKey = process.env.RESEND_API_KEY;
  if (!resendKey) return res.status(500).json({ error: 'email service not configured' });

  const founderEmail = process.env.BETA_FOUNDER_EMAIL || 'eloycostas@outlook.com';
  const safe = (s) => String(s || '—').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  try {
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${resendKey}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: 'onboarding@resend.dev',
        to: [founderEmail],
        subject: `New EngiIntel Beta Signup – ${safe(email)}`,
        html: `<p><strong>New beta signup received:</strong></p>
<ul>
  <li><strong>Name:</strong> ${safe(name)}</li>
  <li><strong>Email:</strong> ${safe(email)}</li>
  <li><strong>Company:</strong> ${safe(company)}</li>
  <li><strong>Industry:</strong> ${safe(industry)}</li>
  <li><strong>Message:</strong> ${safe(message)}</li>
</ul>`,
      }),
    });
  } catch (err) {
    console.error('Resend error:', err);
  }

  return res.status(200).json({ ok: true });
}
