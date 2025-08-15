---
nav_title: Sending emails to apple private relay
article_title: Sending Emails to Apple Private Relay
alias: /email_relay/
page_order: 0
description: "This article covers the process of sending emails to Apple Private Relay."
channel:
  - email
  
---

# Sending emails to Apple Private Relay

> Apple's single sign-on (SSO) feature allows their users to share their email addresses (`example@icloud.com`) or to hide their email addresses by masking what's provided to brands (`tq1234snin@privaterelay.appleid.com`) instead of their personal email address. Apple will then forward messages sent to the relay addresses to the user's actual email address. 

To send emails to Apple's private email relay, register your sending domains with Apple. If you don't configure your domains with Apple, emails sent to relay addresses will result in bounces.

If a user decides to disable the email forwarding to your app's relay email, Braze will receive email bounce information as usual. These users can manage apps that use sign-in with Apple from their Apple ID settings page (see [Apple's documentation](https://support.apple.com/en-us/HT210426)).

## Sending emails for SendGrid

If you use SendGrid as an email provider, you can send emails to Apple without making DNS changes. 

1. Log into the [Apple Developer Portal](https://developer.apple.com/)
2. Go to the **Certificates, Identifiers & Profiles** page.
3. Select **Services** > **Sign in with Apple for Email Communication**.
4. In the **Email Sources** section, add the domains and subdomains.
- The address should be formatted as: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (an example is: `bounces+1234567@braze.online.docs.com`). 

If your desired "From" address is an `abmail` address, include that in your subdomain. For example, use `abmail.docs.braze.com` instead of `docs.braze.com`.

## Sending emails for SparkPost

To set up Apple Private Relay for SparkPost, follow these steps: 

1. Sign in with Apple.
2. Follow [Apple's documentation](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) to register the email domains.
3. Apple will automatically check the domains, show which ones are verified, and provide the option to reverify or delete the domains.

### Considerations

If a sending domain is also used as a bounce domain, you won't be able to store any records and will need to follow these additional steps:

1. If the domain has already been verified on SparkPost, you **must** create MX and TXT records: 

| Instance | MX record                   | TXT record                                    |
|----------|-----------------------------|-----------------------------------------------|
| US       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
To avoid SPF failures, you must create the MX and TXT records and have them propagated in the DNS **before** deleting the CNAME record.
{% endalert %}

{:start="2"}
2. Delete the CNAME record.
3. Replace it with the MX and TXT records for proper routing.
4. Create your A record to point to your CDN or file hosting.

If you have any further questions, open a [support ticket]({{site.baseurl}}/braze_support/).
