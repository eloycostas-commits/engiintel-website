/**
 * Vercel Serverless Function - Contact Form Handler
 * Sends contact form submissions via Resend API
 */

module.exports = async function handler(req, res) {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Extract form data
  const { name, email, company, industry, interests, message, language, timestamp } = req.body || {};

  // Log the submission (visible in Vercel function logs)
  console.log('=== CONTACT FORM SUBMISSION ===');
  console.log('Name:', name);
  console.log('Email:', email);
  console.log('Company:', company);
  console.log('Industry:', industry);
  console.log('Interests:', interests);
  console.log('Message:', message);
  console.log('Language:', language);
  console.log('Timestamp:', timestamp);
  console.log('================================');

  // Validate required fields
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!name || !email || !emailRegex.test(email)) {
    return res.status(400).json({ error: 'Name and valid email are required' });
  }

  // Get Resend API key from environment
  const resendKey = process.env.RESEND_API_KEY;
  if (!resendKey) {
    console.error('RESEND_API_KEY not configured in environment variables');
    // Still return success so user doesn't see error
    return res.status(200).json({ 
      success: true,
      message: 'Form received. Check Vercel logs.',
      warning: 'Email service not configured'
    });
  }

  console.log('Resend API key found:', resendKey.substring(0, 10) + '...');

  // Sanitize HTML
  const safe = (s) => String(s || '—').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  // Prepare email payload
  const founderEmail = process.env.BETA_FOUNDER_EMAIL || 'eloycostas@outlook.com';
  const fromAddress = process.env.RESEND_FROM || 'onboarding@resend.dev';

  console.log('Sending email from:', fromAddress);
  console.log('Sending email to:', founderEmail);

  const emailPayload = {
    from: fromAddress,
    to: [founderEmail],
    reply_to: email,
    subject: `New Contact Form - ${safe(name)} (${safe(company || 'No company')})`,
    html: `
      <h2>New Contact Form Submission</h2>
      <table style="border-collapse: collapse; width: 100%; max-width: 600px;">
        <tr style="border-bottom: 1px solid #ddd;">
          <td style="padding: 12px; font-weight: bold;">Name:</td>
          <td style="padding: 12px;">${safe(name)}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
          <td style="padding: 12px; font-weight: bold;">Email:</td>
          <td style="padding: 12px;"><a href="mailto:${safe(email)}">${safe(email)}</a></td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
          <td style="padding: 12px; font-weight: bold;">Company:</td>
          <td style="padding: 12px;">${safe(company)}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
          <td style="padding: 12px; font-weight: bold;">Industry:</td>
          <td style="padding: 12px;">${safe(industry)}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
          <td style="padding: 12px; font-weight: bold;">Interests:</td>
          <td style="padding: 12px;">${Array.isArray(interests) ? interests.map(safe).join(', ') : safe(interests)}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
          <td style="padding: 12px; font-weight: bold;">Message:</td>
          <td style="padding: 12px;">${safe(message)}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
          <td style="padding: 12px; font-weight: bold;">Language:</td>
          <td style="padding: 12px;">${safe(language)}</td>
        </tr>
        <tr>
          <td style="padding: 12px; font-weight: bold;">Timestamp:</td>
          <td style="padding: 12px;">${safe(timestamp)}</td>
        </tr>
      </table>
      <p style="margin-top: 24px; color: #666; font-size: 14px;">
        Reply directly to this email to respond to ${safe(name)}.
      </p>
    `
  };

  // Send email via Resend
  try {
    console.log('Calling Resend API...');
    const resendResponse = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${resendKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(emailPayload)
    });

    const data = await resendResponse.json();
    console.log('Resend API response status:', resendResponse.status);
    console.log('Resend API response data:', data);

    if (!resendResponse.ok) {
      console.error('Resend API error:', {
        status: resendResponse.status,
        data: data
      });
      
      // Return success to user even if email fails (graceful degradation)
      // The submission is logged in Vercel for manual follow-up
      return res.status(200).json({ 
        success: true,
        message: 'Form received. We will contact you soon.',
        warning: 'Email delivery pending'
      });
    }

    console.log('Email sent successfully:', data);
    return res.status(200).json({ 
      success: true,
      message: 'Email sent successfully',
      id: data.id 
    });

  } catch (error) {
    console.error('Error sending email:', error);
    
    // Return success to user even if email fails (graceful degradation)
    // The submission is logged in Vercel for manual follow-up
    return res.status(200).json({ 
      success: true,
      message: 'Form received. We will contact you soon.',
      warning: error.message
    });
  }
}
