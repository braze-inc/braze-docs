---
nav_title: WhatsApp phone number migration
article_title: WhatsApp Phone Number Migration
page_order: 3
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

For information on migrating your WhatsApp phone number, see Meta's documentation for [Migrating phone numbers between WhatsApp Business Accounts via Embedded Signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/).

## Migrating your WhatsApp phone number

1. In the WhatsApp Manager, select the WhatsApp Business Account (WABA) associated with your phone number, then go to **Account tools** > **Phone numbers**.
2. Select **Turn off two-step verification** and complete the steps that follow.<br><br>![WhatsApp Business Manager opened to the "Phone numbers" page.]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> If you’re migrating a phone number to a different WhatsApp Business Group and Meta’s embedded signup requires the display name to match, take note of the existing display name on the **Phone Numbers** page. You'll enter that name during the next step.<br><br>![The WhatsApp Business Manager's Phone Numbers page with a display name of "Braze" listed next to a phone number.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Continue Meta’s embedded signup workflow to completion with these considerations:
- You can't select the same business portfolio that is used by a different Business Solution Provider.
- You can't select a phone number that's used by another Business Solution Provider.
- You must create a new WABA, not select an existing one.