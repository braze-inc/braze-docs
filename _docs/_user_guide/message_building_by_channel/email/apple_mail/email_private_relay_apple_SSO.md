---
nav_title: Sending Emails to Apple Private Relay
article_title: Sending Emails to Apple Private Relay
alias: /email_relay/
page_order: 0
description: "This article covers the process of sending emails to Apple Private Relay."
channel:
  - email
  
---

# Sending emails to Apple Private Relay

> With the iOS 13 release, Apple has introduced functionality for Apple customers that impacts how emails are sent to them. Apple's single sign-on (SSO) feature allows their users to share their email addresses (`example@icloud.com`) or to hide their email addresses by masking what's provided to brands (`tq1234snin@privaterelay.appleid.com`) as opposed to their personal email address.

These users can manage apps that use sign-in with Apple from their Apple ID settings page (see [Apple's documentation](https://support.apple.com/en-us/HT210426)). If a user decides to disable the email forwarding to your app's relay email, Braze will receive email bounce information as usual. To send emails to Apple's private email relay, register your sending domains with Apple.

## Sending emails for SendGrid

If you use SendGrid as an email provider, you can send emails to Apple without making DNS changes. Go to your **Apple Certificate** page and allow the email address you wish to use for sending via Apple's Email Relay Service (your desired "From" address).  

![Option to allowlist individual email addresses on the Apple Certificate page.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

The address should be formatted as: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(e.g., `bounces+1234567@braze.online.docs.com`). After the address is added to your Apple Certificate page, emails from this domain will be delivered via the Apple Private Relay system.

{% alert important %}
If your desired "From" address is an `abmail` address, include that in your subdomain. For example, use `abmail.docs.braze.com` instead of `docs.braze.com`. This might not be the case for your address. Check your DNS records in SendGrid. 
{% endalert %}

### From address values

Refer to this table for the components used when adding email addresses with Apple Private Relay.

| Value | Description |
|---|---|
| UID | This value is provided in your DNS records that are provided by Braze (from SendGrid). Do not include the letter "u" in your UID in the email address. For example, if your UID is presented in SendGrid as `u1234567.wl134.sendgrid.net`, then `1234567` is the UID value. <br><br> If you don't have access to your DNS records, contact your Braze customer success manager to provide your UID. |
| Whitelabeled Subdomain and Domain | The initial domain and subdomain you entered into SendGrid. You can also use the **HOST Value** in your DNS records in SendGrid. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Sending emails for SparkPost

To set up Apple Private Relay for SparkPost, follow these steps: 

1. Sign in with Apple. 
2. Add the email domains. 
3. Apple will automatically check the domains and show which ones are verified, and provide the option to reverify or delete the domains.

{% alert important %}
Make sure you complete this process within 2 to 3 days of the verification files being created, or else they will expire. Apple does not disclose how long they're valid for.
{% endalert %}

If you have any further questions, open a [support ticket]({{site.baseurl}}/braze_support/).
