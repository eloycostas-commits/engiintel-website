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

  const send = (payload) =>
    fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${resendKey}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

  // 1. Founder notification
  try {
    await send({
      from: 'onboarding@resend.dev',
      to: [founderEmail],
      reply_to: email,
      subject: `New EngiIntel Beta Signup – ${safe(email)}`,
      html: `<p><strong>New beta signup received:</strong></p>
<ul>
  <li><strong>Name:</strong> ${safe(name)}</li>
  <li><strong>Email:</strong> ${safe(email)}</li>
  <li><strong>Company:</strong> ${safe(company)}</li>
  <li><strong>Industry:</strong> ${safe(industry)}</li>
  <li><strong>Message:</strong> ${safe(message)}</li>
</ul>`,
    });
  } catch (err) {
    console.error('Resend founder email error:', err);
  }

  // 2. Welcome email to the person who signed up
  // NOTE: Resend free tier only delivers to the account owner's verified email.
  // To send to any address, verify a domain in Resend and set RESEND_FROM env var.
  const fromAddress = process.env.RESEND_FROM || 'onboarding@resend.dev';
  try {
    await send({
      from: fromAddress,
      to: [email],
      subject: `Welcome to EngiIntel Beta – ${safe(name)}, we'll be in touch`,
      html: `<p>Hi ${safe(name)},</p>
<p>Thanks for joining the EngiIntel beta.</p>
<p>You're one of 5 companies we're onboarding first.<br>
I'll be in touch within 24 hours to schedule a demo.</p>
<p>In the meantime, explore what EngiIntel does at <a href="https://engiintel.com">engiintel.com</a></p>
<p>— Eloy<br>Founder, EngiIntel</p>`,
    });
  } catch (err) {
    console.error('Resend welcome email error:', err);
  }

  return res.status(200).json({ ok: true });
}
