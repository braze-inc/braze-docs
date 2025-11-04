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

Your SPF record will be set up when Braze configures your IPs and domains - beyond adding the DNS records we give you, no further action is required.

### Domain Keys Identified Mail (DKIM)

This method confirms that your Braze email-sending domain is authorized to send mail on your behalf. This method is designed to validate the sender's authenticity and validates the integrity of the message is preserved. It also uses individual cryptographic digital signatures so ISPs can be sure the mail they're delivering is the same as the mail you sent.

Braze signs the mail with your secret private key. The ISPs verify the signature against your public key, which is stored in your custom DNS record. No two signatures are exactly alike, and only your public key can successfully verify your private key signature.

Your DKIM record will be set up when Braze configures your IPs and domains-beyond adding the DNS records we give you, no further action is required.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC)

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) is an email authentication protocol for email senders to prove the legitimacy of their mail, which enables mailbox receiver confidence and encourages mail acceptance. DMARC allows email senders to specify how to handle emails that were not authenticated using Sender Policy Framework (SPF) or Domain Keys Identified Mail (DKIM). This is achieved by verifying that both SPF and DKIM checks are passed. 

Senders can instruct mailbox providers on how they should handle mail that failed their signature or authentication checks. Failures could indicate that others are trying to imitate you or your email. Senders can tell mailbox providers to reject or quarantine mail and even send automated reports about mail that fails checks. By doing so, mailbox providers can better identify spammers and prevent malicious email from invading inboxes while minimizing false positives and providing better authentication reporting for greater transparency in the marketplace.

#### How it works

To deploy DMARC, you need to publish a DMARC Record to your Domain Naming System (DNS). This is a TXT record that publicly expresses your email domain’s policy after checking SPF and DKIM status. DMARC authenticates if either SPF or DKIM, or both pass. This is referred to as DMARC Alignment.

A DMARC record also tells email servers to send XML reports back to the reporting email address listed in the DMARC record. These reports provide insight into how your email is moving through the ecosystem and allow you to identify everything that is attempting to use your email domain to send email communications.

The policy you have in your DMARC record will tell the participating recipient email server what to do with mail that doesn’t pass SPF and DKIM but claims to be from your domain. Braze recommends setting a DMARC policy on the root domain, which will be applied to all subdomains. This means no additional setup will be necessary on any current and new subdomains in the future. There are three types of policies you can set:

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

