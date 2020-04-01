---
nav_title: Authentication
page_order: 1
page_type: reference
description: "Email authentication, or validation, is a collection of techniques aimed at equipping your email with verifiable information about its origin."
---

# Authentication

> Email authentication, or validation, is a collection of techniques aimed at equipping your email with verifiable information about its origin.

Proper authentication is crucial for ISPs to recognize you as a sender of desirable email. It's how the ISPs know it's you, and how they know to deliver your mail immediately. Without authentication, your outreach is presumed to be fraudulent.

## Methods of Authentication

### Sender Policy Framework (SPF)

This method confirms that your Braze e-mail sending IP address is authorized to send mail on your behalf. This is your basic authentication and is accomplished by publishing the text records in DNS settings. The receiving server will check the DNS records and determine whether it is authentic or not. This method is designed to validate the email sender.

Your SPF record will be set up when Braze configures your IPs and domains - beyond adding the DNS records we give to you, no further action is required on your end.

### Domain Keys Identified Mail (DKIM)

This method confirms that your Braze e-mail sending domain is authorized to send mail on your behalf. This method is designed to validate the authenticity of the sender AND ensure the integrity of the message is preserved. It also uses individual cryptographic digital signatures so ISPs can be sure the mail they're delivering is the same as the mail you sent.

Braze signs the mail with your secret private key.  The ISPs verify the signature against your public key, which is stored in your custom DNS record.  No two signatures are exactly alike, and only your public key can successfully verify your private key signature.

Your DKIM record will be set up when Braze configures your IPs and domains - beyond adding the DNS records we give to you, no further action is required on your end.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC)

This method takes the SPF and DKIM authentication protocols one step further.

If you decide to use DMARC, you can instruct ISPs how they should handle mail that failed your signature or authentication checks. Failures could be a sign that others are trying to imitate you or your email. You can tell the ISPs to reject or quarantine the mail, and even send you automated reports about the bad mail.

#### Create a DMARC Record

1. Visit the [DMARC Record Wizard](https://dmarcian.com/dmarc-record-wizard/)
2. Using this wizard, specify the DMARC settings you would like. (e.g Reporting address, what data to collect)
3. From these settings, you will get an output like this:<br>![DMARC1][1]{:height="280px"}
4. Navigate to your hosting provider, and insert the Wizard output as a TXT record. <br>![DMARC2][2]{:height="75px"}

Note: You may need to do external validation if you're sending to an e-mail address with a different domain (e.g The target/host `hello.brazetest.info` differs from the reporting address `example.email@braze.com`) A workaround for this would involve having a record on Braze's DNS hosting provider to allow the reports to be sent to the correct reporting address. Information on this can be found in the in the DMARCAnalyzer [docs][4] and here in the MXTOOLBOX [docs][5].

#### Verify that DMARC is Working

1. Test with one of the following tools:
  - [DMARCAnalyzer](https://www.dmarcanalyzer.com)
  - [MXTOOLBOX](https://mxtoolbox.com)
2. Send yourself an email through Gmail.
3. From the received email, look for and select 'Show Original E-Mail'.
4. Here, you can see your DMARC status. If you see a `PASS` under the DMARC field, your DMARC is working.<br>![DMARC3][3]{:height="200px"}


{% alert important %}
DMARC will need to be set up and implemented by __you__ directly. This is due to certain required fields, such as Reporting Address, needing information only you can provide. (e.g Where you want your report sent) For more information on DMARC, read more [here](https://dmarc.org/).
{% endalert %}

[1]:{% image_buster /assets/img/DMARC1.png %}
[2]:{% image_buster /assets/img/DMARC2.png %}
[3]:{% image_buster /assets/img/DMARC3.png %}
[4]: https://www.dmarcanalyzer.com/how-does-external-domain-verification-work/
[5]: https://mxtoolbox.com/problem/dmarc/dmarc-external-validation
