---
nav_title: FAQ
article_title: MMS FAQ
page_order: 4
description: "This article covers some of the most frequently asked questions about MMS."
page_type: FAQ
alias: /mms_faq/
channel:
  - MMS
  
---

# Frequently asked questions

> On this page, we'll attempt to answer your most stringent questions about MMS.

### Are there any changes to Currents data when sending an MMS?

No, the same level of insight will be provided when sending an MMS message.

### Can I control the order in which the image and message body of an MMS are delivered?

Braze has no control over the display order for when both a message-body and images are included in an MMS message. This is dependent on several factors including but not limited to:

- The carrier receiving the message
- The device receiving the message
- The overall size of the message

### Does MMS and SMS pricing differ?

MMS and SMS have different costs and are charged separately based on volume. Contact the Braze Onboarding team for pricing information.

### Does MMS require a separate onboarding process?

Nope! MMS is now included in our SMS onboarding process. Existing customers who already went through onboarding can start sending MMS campaigns after completing the following steps:

1. Purchase MMS.
2. Contact the Braze Onboarding team to request the MMS feature to be flipped on. This will enable MMS and an SMS/MMS Subscription group will be created or updated for you.

Next, the Braze onboarding team will make sure your short and long codes are enabled (in the US and Canada) for MMS. They will also update your subscription groups to show your current numbers that were added or enabled for MMS. After these steps are complete, you can send MMS messages right away from our native SMS composer.

### Why can't I find MMS on my dashboard even though the feature is enabled?

MMS is only displayed on the Braze dashboard when a subscription group is considered "MMS enabled". This is reflected by an MMS tag when selecting the subscription group on the composer of an SMS/MMS message. This means that at least one number in the subscription group is capable of sending an MMS message.

Additionally, certain situations will require Twilio to re-approve the enablement of short codes that originally didn't have MMS enabled. This approval process could take weeks.
