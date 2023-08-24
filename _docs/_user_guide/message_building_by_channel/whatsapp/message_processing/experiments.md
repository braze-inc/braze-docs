---
nav_title: WhatsApp Marketing Experiment
article_title: WhatsApp Marketing Experiment
description: "This article describes the potential impacts of Meta's marketing experiment in WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 200

---

# WhatsApp marketing experiment

Meta recently introduced new experimentation to the WhatsApp Business Platform in order to assess how marketing messages impact consumer experience and engagement. This experiment may affect your marketing messages sent on the WhatsApp Business API with Braze and other providers.

Meta intends to continue such experimentation on the WhatsApp platform. Please see [Meta’s documentation](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) for more information.

## Meta experimentation affects marketing messages only

This experiment has the potential to impact the delivery of marketing template messages. Utility and authentication templates will continue to be delivered without any experimentation impact.

In the experiment, Meta randomly chooses approximately 1% of WhatsApp consumers as participants. If chosen, Meta will not deliver marketing message templates to these consumers unless one of the following is true:

- If a consumer has replied to you in the last 24 hours;
- If an existing marketing conversation is open; or
- If a WhatsApp Ad was clicked on by the consumer in the last 72 hours.

## Frequently asked questions

### How will I know if my marketing message was impacted by Meta's experiment?

If a message isn’t delivered due to the experiment, a specific error code will be surfaced under Activity Log and within Currents. The message will also be counted as a failure and incorporated into your WhatsApp Failures metrics across all reporting within the Braze dashboard. You will not be charged for these messages.

This 130472 error code will state “User’s number is part of an experiment.” Please see [Meta’s documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) for more information on WhatsApp Cloud API error codes.

### Can I opt out of Meta's experiment?

No, Meta does not permit any experiment opt-outs. All WhatsApp Business API providers and users are subject to this Meta experiment.

### Can I try to resend a template later?

There is no fixed time for this experiment. As such, a consumer may continue to be subject to the experiment.

### What can I do if my marketing messages are not delivered due to Meta's experiment?

We recommend using other Braze channels, such as email, SMS, push notifications, or in-app messages to send a message with similar content to your intended users.

