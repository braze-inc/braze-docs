---
nav_title: Email authentication
article_title: Email Authentication
page_order: 2
page_type: reference
description: "This reference article covers email authentication, a collection of techniques aimed at equipping your email with verifiable information about its origin."
channel: email

---

# Email authentication

> Email authentication is a collection of techniques that equip your emails with verifiable information about its origin.<br><br>Proper authentication is crucial for internet service providers (ISPs) to recognize you as a sender of desirable emails and deliver your mail immediately. Without authentication, your outreach is presumed to be fraudulent. 

## Methods of authentication

### Sender Policy Framework (SPF)

This method confirms that your Braze email-sending IP address is authorized to send mail on your behalf. SPF is your basic authentication and is accomplished by publishing the text records in DNS settings. The receiving server will check the DNS records and determine whether they are authentic. This method is designed to validate the email sender.

Braze sets up your SPF record when we configure your IPs and domains. Beyond adding the DNS records we provide, you don't need to take further action.

### Domain Keys Identified Mail (DKIM)

This method confirms that your Braze email-sending domain is authorized to send mail on your behalf. This method is designed to validate the sender's authenticity and validates the integrity of the message is preserved. It also uses individual cryptographic digital signatures so ISPs can be sure the mail they're delivering is the same as the mail you sent.

Braze signs the mail with your secret private key. The ISPs verify the signature against your public key, which is stored in your custom DNS record. No two signatures are exactly alike, and only your public key can successfully verify your private key signature.

Braze sets up your DKIM record when we configure your IPs and domains. Beyond adding the DNS records we provide, you don't need to take further action.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC)

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) is an email authentication protocol for email senders to prove the legitimacy of their mail, which enables mailbox receiver confidence and encourages mail acceptance. DMARC allows email senders to specify how to handle emails that were not authenticated using Sender Policy Framework (SPF) or Domain Keys Identified Mail (DKIM). This is achieved by verifying that both SPF and DKIM checks are passed. 

Senders instruct mailbox providers how to handle mail that fails signature or authentication checks. Failures can indicate spoofing. You can tell providers to reject or quarantine failing mail and to send automated reports. This helps providers identify spammers, block malicious email, minimize false positives, and improve authentication reporting transparency.

#### How it works

To deploy DMARC, you need to publish a DMARC Record to your Domain Naming System (DNS). This is a TXT record that publicly expresses your email domain’s policy after checking SPF and DKIM status. DMARC authenticates if either SPF or DKIM, or both pass. This is referred to as DMARC Alignment.

A DMARC record also tells email servers to send XML reports back to the reporting email address listed in the DMARC record. These reports provide insight into how your email is moving through the ecosystem and allow you to identify everything that is attempting to use your email domain to send email communications.

Set a DMARC policy on the root domain so it applies to all subdomains. This avoids additional setup on current and future subdomains. You can set one of the following policies:

| Policy | Impact |
| --- | --- |
| None | Tell the mailbox provider to perform no actions against messages that fail. |
| Quarantine | Tell the mailbox provider to send messages that fail to the spam folder. |
| Reject | Tell the mailbox provider that messages that fail will go to the spam folder and should be blocked. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### How to check your domain's DMARC authentication

There are two options to check your domain's DMARC authentication:

- **Option 1:** You can input your parent domain or subdomain into any third-party DMARC checker, such as [MXToolbox](https://mxtoolbox.com/dmarc.aspx), to audit whether you have a DMARC policy in place and what that policy is set to.
    - **MXToolbox**: If you set your DMARC as the root domain, enter that into MXToolbox. If you set the DMARC at the subdomain, enter the sub-domain into MXToolbox. Be aware that MXToolbox doesn't "look up or down" when performing lookups. This means if you set the DMARC at the root domain and enter the subdomain, MXToolbox will show a failure as it doesn't know the DMARC has been set at the root domain.
- **Option 2:** Open an email from your domain or subdomain in your mailbox, and find the original message to check whether DMARC is passing authentication on this email.

For example, if you’re using Gmail, follow these steps:

1. Click the **More** <i class="fa-solid fa-ellipsis"></i> in an email message.
2. Select **Show original**.
3. Check if you have a "PASS" status for **DMARC**.

![An email that has "PASS" as the DMARC value.]({% image_buster /assets/img_archive/dmarc_example.png %})

