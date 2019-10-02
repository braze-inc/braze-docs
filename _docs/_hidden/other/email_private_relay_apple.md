---
nav_title: Sending Emails to Apple Private Relay
permalink: /email_relay/
---

# Sending Emails to Apple Private Relay

Braze customers who use Sendgrid as an email provider can now, essentially, "[whitelist](https://help.apple.com/developer-account/?lang=en#/devf822fb8fc)" with Apple without having to make DNS changes.

Go to your [Apple Certificate](https://help.apple.com/developer-account/?lang=en#/devf822fb8fc) page and whitelist the email address you wish to use for sending via Apple's Email Relay Service.

![Whitelabel the Address]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

The address should be formatted as:

`bounces+<YOUR_UID>@<YOUR_WHITELABEL_SUBDOMAIN_AND_DOMAIN>`

For example: `bounces+1234567@braze.online.docs.com`.


| Value | Description |
|---|---|
| UID | This value is provided by Sendgrid in your DNS records. Do not include the "U" character in your UID in the email address you whitelabel. For example, if your UID is presented in Sendgrid as `u1234567.wl134.sendgrid.net`, then `1234567` is the UID value. <br> <br> _You can also ask your Braze representative to provide your UID, if you do not have access to your DNS records._ |
| Whitelabel Subdomain and Domain | This is the initial domain and subdomain you entered into Sendgrid. You can also use the HOST value in your DNS Records in Sendgrid. <br> <br> ![HOST Value DNS Records]({% image_buster /assets/img/email-relay-dns-records.png %}) |


Once added to your Apple Certificate page, emails from this from-address domain will be delivered to the Apple Private Relay system.

If you have any further questions, please [submit a support ticket]({{ site.baseurl }}/support_contact/).


## What is the Apple Private Relay System?

With the recent iOS 13 release, Apple has introduced new functionality for Apple customers, which impacts how email is sent to them. The new Apple single sign-on (SSO) feature allows Apple customers to share their email address (`example@icloud.com`) or to hide their email address, in which case a "masked" email address (`tq1234snin@privaterelay.appleid.com`) will be provided to brands (as opposed to the user's personal email address).
