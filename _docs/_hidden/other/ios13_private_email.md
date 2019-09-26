---
nav_title: Sending Emails to Apple Private Relay
permalink: /email_relay/
---

# Sending Emails to Apple Private Relay

Braze customers who use Sendgrid as an email provider can now, essentially, "whitelist" with Apple without having to make DNS changes.

Go to your APple Certificate page and whitelist an individual email address. It should be formatted as:

`bounces+<YOUR_UID>@<YOUR_WHITELABEL_SUBDOMAIN_AND_DOMAIN>`

And could look like:

`bounces+1234567@braze.online.docs.com`

| Value | Description |
|---|---|
| UID | This value is provided by Sendgrid in your DNS records. Do not include the "U" character in your UID in the email address you whitelabel. For example, if your UID is presented in Sendgrid as `u1234567.wl134.sendgrid.net`, then `1234567` is the UID value. <br> _You can also ask your Braze representative to provide your UID if you had previously provided it._ |
| Whitelabel Subdomain and Domain | This is the initial domain and subdomain you entered into Sendgrid Sendgrid. You can also use the HOST value in your DNS records in Sendgrid. |

Once added to your Apple Certificate page, emails from this address will be delivered to the Apple Private Relay system.

This means that you must use that email address to send emails from Braze.

## What is the Apple Private Relay System?

With the recent iOS 13 release, Apple has introduced new functionality for Apple customers, which impacts how email is sent to them. The new Apple single sign-on feature allows Apple customers to share their email address (example@icloud.com) or to hide their email address, in which case a ‘masked’ email address (e.g., tq1234snin@privaterelay.appleid.com) will be provided to brands (as opposed to the user's personal email address).
