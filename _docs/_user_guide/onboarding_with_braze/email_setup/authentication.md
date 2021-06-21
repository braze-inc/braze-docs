---
nav_title: Authentication
page_order: 1

page_type: reference
description: "This reference article covers email authentication, a collection of techniques aimed at equipping your email with verifiable information about its origin."
channel: email
---

# Authentication

> Email authentication, or validation, is a collection of techniques aimed at equipping your email with verifiable information about its origin.

Proper authentication is crucial for ISPs to recognize you as a sender of desirable email. It's how the ISPs know it's you, and how they know to deliver your mail immediately. Without authentication, your outreach is presumed to be fraudulent.

## Methods of Authentication

### Sender Policy Framework (SPF)

This method confirms that your Braze email sending IP address is authorized to send mail on your behalf. This is your basic authentication and is accomplished by publishing the text records in DNS settings. The receiving server will check the DNS records and determine whether it is authentic or not. This method is designed to validate the email sender.

Your SPF record will be set up when Braze configures your IPs and domains - beyond adding the DNS records we give to you, no further action is required on your end.

### Domain Keys Identified Mail (DKIM)

This method confirms that your Braze email sending domain is authorized to send mail on your behalf. This method is designed to validate the authenticity of the sender AND ensure the integrity of the message is preserved. It also uses individual cryptographic digital signatures so ISPs can be sure the mail they're delivering is the same as the mail you sent.

Braze signs the mail with your secret private key.  The ISPs verify the signature against your public key, which is stored in your custom DNS record.  No two signatures are exactly alike, and only your public key can successfully verify your private key signature.

Your DKIM record will be set up when Braze configures your IPs and domains - beyond adding the DNS records we give to you, no further action is required on your end.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC)

This method takes the SPF and DKIM authentication protocols one step further.

If you decide to use DMARC, you can instruct ISPs how they should handle mail that failed your signature or authentication checks. Failures could be a sign that others are trying to imitate you or your email. You can tell the ISPs to reject or quarantine the mail, and even send you automated reports about the bad mail.
