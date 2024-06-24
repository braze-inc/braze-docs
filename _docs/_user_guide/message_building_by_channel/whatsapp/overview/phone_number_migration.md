---
nav_title: WhatsApp Phone Number Migration
article_title: WhatsApp Phone Number Migration
page_order: 1
description: "This reference article covers how to migrate your WhatsApp phone number."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp phone number migration

> Migrate your WhatsApp phone number between WhatsApp Business Accounts by using Meta's Embedded Signup.

## Prerequisites

Your phone number must meet Meta's requirements to be eligible for migration:

- Your Meta Business Account is verified.
- Your existing WhatsApp Business Account is approved.
- Your existing WhatsApp Business Account has a valid payment method in **Payment Settings**.
- Your business phone number has two-step verification turned off. If you own your WhatsApp Business Account, you can turn off two-step verification on their number in the WhatsApp Manager. Otherwise, you must ask your Solution Provider to turn it off for you.

For information on migrating your WhatsApp phone number, see Meta's documentation for [Migrating phone numbers between WhatsApp Business Accounts via embedded signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/).

## Migrating your WhatsApp phone number

Follow the [migration steps](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/#migration-steps) provided by Meta's embedded sign-up experience.

{% alert note %}
If you’re migrating a phone number to a different WhatsApp Business Group and Meta’s Embedded Signup (Step 2) requires the display name to match, take note of the existing display name on your WhatsApp Business Manager's **Phone Numbers** page. Enter that name during the Embedded Signup step.<br><br>![The WhatsApp Business Manager's Phone Numbers page with a display name of "Braze" listed next to a phone number.]({% image_buster /assets/img/whatsapp/phone_numbers.png %})
{% endalert %}