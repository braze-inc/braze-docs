---
nav_title: FAQ
article_title: WhatsApp FAQ
page_order: 80
description: "This article addresses some of the most frequently asked questions that arise when setting up WhatsApp campaigns."
page_type: FAQ
channel:
  - WhatsApp

---

# Frequently asked questions

> On this page, we'll attempt to answer your most stringent questions about WhatsApp!<br><br>This FAQ is not intended to provide, nor may it be relied upon as providing legal advice. The use of the WhatsApp channel is subject to specific Meta Platforms, Inc. requirements. To ensure that you are using the WhatsApp channel in compliance with all applicable requirements and any laws to which you may specifically be subject, you should seek the advice of your legal counsel.

## FAQ topics
- [WhatsApp business accounts](#whatsapp-business-accounts)
- [WhatsApp business account phone number](#whatsapp-business-account-phone-numbers)
- [Opt-in and subscription management](#opt-in-and-subscription-management) 
- [Messaging limits](#messaging-limits) 
- [WhatsApp templates](#whatsapp-templates)
- [Deliverability](#deliverability) 
- [Miscellaneous](#miscellaneous)

### WhatsApp business accounts 

#### How do I create a WhatsApp business account? 
We recommend creating your WhatsApp business account (WABA) through the embedded sign-up flow in the Braze dashboard. 

#### I already have a Meta business account. Do I still need a WhatsApp business account? 
Yes, you still need to create a WhatsApp business account. We recommend you [nest your WABA underneath your main Meta business account](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/overview/). 

#### How do I access my WhatsApp business account? 
After completing the embedded sign-up flow, you can access your account at business.facebook.com by navigating to the [WhatsApp section](https://business.facebook.com/wa/manage/home). 

#### If I already have a WhatsApp business account, how do I connect it to Braze? 
You may be able to migrate your existing WABA depending on the type of WABA you currently have (see details below). Note that WhatsApp business accounts can only be connected to **one** business solution provider simultaneously.

**If your account was set up on the On-Behalf-Of (OBO) model:**
- Your WABA is owned by the business service provider who set up the account and sends messages on your behalf. For customers with existing OBO accounts, Braze recommends that you create a new WhatsApp business account with a new phone number via the embedded sign-up flow. Note that templates, business verification (if applicable), and current messaging limit will be lost when you do this, meaning you will need to resubmit templates for approval and build up your messaging limit again. Braze recommends copying over your templates or saving them before shutting down your existing OBO account so that you can more easily rebuild templates.<br>

**If your account was set up on the WhatsApp business account sharing model (via an embedded sign-up flow with a different business service provider):**
- You own your WABA. For sharing accounts, Braze recommends that you create a new WhatsApp business account but [migrate your existing phone number](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/). This will ensure that your templates, business verification (if applicable), and current messaging limit will remain as is and "port" over to Braze.

If you’d like to migrate an existing phone number, notify your Braze contact and they can help with the process.

#### If I have an existing phone number that I am migrating, how long will it take for my new WABA to be set up? 
Your new WABA will be set up immediately after completing the embedded sign-up flow, which should only take a few minutes. 

#### Can I connect multiple WABAs to Braze? 
Yes, you can connect one WABAs per workspace. Therefore you can have multiple WABAs connected to multiple of your Braze workspaces. For example, if you have different workspaces for different brands, or different workspaces for different countries, each can have it's own WABA connected.

### WhatsApp business account phone numbers 

#### Do I need a phone number for my WhatsApp business account? 
Yes, you need a number that you have access to. You will be asked to verify your phone number with 2-factor authentication when you go through the embedded sign-up flow. The phone number cannot be used for other WhatsApp accounts (business or personal).

#### What types of phone numbers are supported with WhatsApp? 
Refer to Meta's requirements for [phone numbers](https://developers.facebook.com/docs/whatsapp/phone-numbers) for more information. 

#### Can I use one phone number across multiple WABAs? 
No. A phone number cannot be shared across multiple WABAs. 

#### Do I need a specific type of phone number to send messages to specific countries? 
No. WhatsApp allows you to send messages to end-users from any supported phone number in any country. Refer to Meta's requirements for [phone numbers](https://developers.facebook.com/docs/whatsapp/phone-numbers) for more information. 

#### Do I need to use a country-specific phone number to send to certain countries?
No. With WhatsApp, any supported phone number can send to end-users in any supported country.

### Opt-in and subscription management 

#### Do I need to collect opt-in to send marketing messages to end-users on WhatsApp? 
Yes, WhatsApp requires businesses to [collect opt-in consent](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) to send marketing messages to end-users.

#### Can I proactively message end-users on WhatsApp to collect opt-in consent? 
If you choose to proactively message end-users, your first business-initiated message should ask the user if the user wants to receive marketing messages from your business and should comply with Meta's requirements for [getting opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Keep in mind that WhatsApp will monitor your business reputation on the channel, so the recommended best practice is to be explicit with end-users and only send messages they have indicated they want to receive.
 
#### Do I need to collect the end user's phone number when I collect opt-in? 
You need to have the end-users phone number on the Braze profile to message them. 
- If you already have their number, you do not need to collect it during opt-in. 
- If you do not have the end-users number, your opt-in method should include phone number capture. 

#### How do I update the subscription status of end-users who opt-in? 
Subscription management of the WhatsApp Channel functions similarly to how it functions in other Braze channels. Refer to [Managing user subscriptions](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more information.  

#### If I already have a list of users who have opted-in to receive marketing messages on WhatsApp, how do I update their subscription status in Braze? 
You can update their subscription status via [user import](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import#importing-custom-data). 

#### What methods should I use to collect opt-ins? 
Braze recommends referring to [Meta's guidelines for opt-in methods](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) to maintain compliance. Refer to the following resource for Braze [channel and opt-in ideas and suggestions](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit).

#### Is double opt-in required for WhatsApp? 
No, double opt-in is not required. 

#### How do end users opt out of WhatsApp messages? 
End-users can opt out in two ways:
1. Set up an inbound WhatsApp message with a specific opt-out word and use a webhook to update the user subscription status.
2. Add an opt-out quick reply within the WhatsApp template, with a corresponding webhook to update. 

### Messaging limits 

#### What are messaging limits? 
Messaging limits are a WhatsApp integrity building concept. They determine the maximum number of business-initiated conversations each phone number can start in a rolling 24-hour period. There are four messaging limit levels: 1k, 10k, 100k, and unlimited.

#### How do I increase my messaging limit? 
WhatsApp will increase your messaging limit if you meet the following conditions:
1. [Phone number status](https://www.facebook.com/business/help/896873687365001) is **Connected** 
2. [Phone number quality rating](https://www.facebook.com/business/help/896873687365001) is **Medium** or **High**
3. In the last seven days, you have initiated X or more conversations with unique users, where X is your current messaging limit divided by 2 

So, to go from 100k to unlimited, you must send at least 50,000 business-initiated conversations in a 7-day period. 

#### How long does it take to increase my messaging limits? 
If all of the previous conditions are met, you can increase your messaging limit from 1k to unlimited in 4 days. 

#### Where can I see my current messaging limit? 
You can check your current messaging limits in the **WhatsApp Manager > Overview Dashboard > Insights** tab. 

#### What happens if I attempt to send messages when I have already reached my messaging limit?
If you try to send a campaign or Canvas to more unique users than your current limit allows, the messages will fail to send. Braze will continue to attempt to resend the messages if/when your messaging limit increases for up to one day. 

#### Can my messaging limit decrease?
Yes, if your phone number quality rating drops too low, you are at risk of WhatsApp decreasing your messaging limit. Braze recommends you subscribe and be notified of quality-related updates from WhatsApp, including updates to your phone number status and messaging limit level. You can subscribe to notifications directly in the WhatsApp Manager dashboard. 

### WhatsApp templates 

#### What is a WhatsApp Template? 
WhatsApp requires that all business-initiated messages start using an approved template. The template includes the copy of the message, along with optional rich media like images, calls-to-action, and quick reply buttons. Once WhatsApp approves templates, they can be used to compose a WhatsApp message in Braze. 

#### Where do I create, edit, and manage my WhatsApp templates? 
You will create, edit, manage, and submit templates for approval directly in the WhatsApp Manager. Once your WABA is connected to Braze, you will see all your templates in the dashboard with a status indicator. If a template is rejected, you will resubmit directly through the WhatsApp manager. **Templates cannot be created or edited directly in Braze.**

#### How long does it take WhatsApp to review a template submission? 
The approval process can take up to 24 hours, but often templates get processed in a matter of hours or minutes. 

#### How many templates can I have at a given time? 
Your message template limit depends on your business verification status. You can check your limit on the **WhatsApp Manager > Message Templates** page. 

#### How do I personalize Braze's template copy and rich media? 
WhatsApp allows for variable parameters to be inserted into message templates. Messages cannot start or end with a variable parameter. Variable parameters can be populated with liquid logic in the Braze platform. Refer to [composing a WhatsApp message in Braze](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/create/#step-2-compose-your-whatsapp-message) to learn more about variable parameters. 

#### My template got rejected. Can Braze help me get it approved? 
The Braze team does not have visibility into template rejections. You should work directly with your WhatsApp Business manager to edit and resubmit the template. Make sure to provide a sample template where necessary. Double-check that your template follows Meta's [business](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) or [commerce](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) policies.

#### Can the rich media be targeted or personalized in Braze? 
Images can be uploaded from the Media Library but cannot be dynamically targeted. For URLs, the last part of the link can be dynamically populated using Liquid. 

### Deliverability 

#### Why would a message not be delivered? 
There are various reasons a message would fail to be delivered, including network issues and the device being turned off. 

#### If a message is not delivered, will I be billed? 
No. If a message is not delivered, you will not be billed. 

#### What happens if an end-user blocks my business? 
If an end-user blocks your business, subsequent messages you attempt to send will not be delivered, and you will not be billed. 

#### What happens if an end-user reports a message? 
If an end-user reports a message, you can still send subsequent messages to this user. However, reporting may affect your quality rating on the channel. 

#### If an end-user blocks or reports my business, will their subscription status be updated in Braze? 
No. Their Braze subscription status will not be updated. 

### Miscellaneous

#### Does Braze support customer support use cases like chatbots and human-assisted chat for WhatsApp? 
We do not support chatbots or human-assisted chat within Braze or through direct integrations. 

If you already use WhatsApp as a customer support channel, we recommend you keep your current setup and create a new WABA via Braze for marketing messaging. This WABA will require a new phone number. 

#### What kind of rich media is supported in WhatsApp templates? 
You can add images, calls to action (URL or phone number), and quick reply buttons to WhatsApp templates. You can add these elements when you build templates directly in WhatsApp. 

#### Can I import user phone numbers? 
Yes. You can [import user phone numbers](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers). 

#### What is business verification? 
Business verification is a WhatsApp concept used to ensure that the brand is a legitimate business. It can be completed in the WhatsApp Manager. Business verification is also required to scale messaging. Without business verification, customers can only send up to 250 unique end-users in a rolling 24-hour period. 

#### What is an official business account? 
OBA gives you the green check mark next to your display name and is optional. You can apply for an official business account after completing business verification. Note that business verification and an official business account are different WhatsApp concepts. 

#### What metrics are available in the Braze dashboard? 
You can see unique recipients, sends, deliveries, reads, and failures in the Braze dashboard. Note that the end-users read receipts must be "On" for Braze to track reads. You can also set up conversion events to monitor campaign performance, similar to other channels. 

#### What is a WhatsApp conversation? 
WhatsApp is a channel focused on 2-way messaging and thus anchors on conversations (instead of the number of individual messages). A conversation is a 24-hour thread between a business and an end-user.

- **Business-initiated conversation**: A conversation where the business starts by sending an approved template message to the end user. As soon as the business sends a message, it begins the 24-hour window.
- **User-initiated conversation**: A conversation where the end-user sends a message to the business. When the business sends a message in response, this begins the 24-hour window.

#### What factors affect phone number quality rating, and what happens when my quality rating drops too low? 
Factors that affect phone number quality rating include an end-user blocking a business (and the reasons they provide when they block a business) and an end-user reporting a business. 

When a quality rating is low, the phone number status changes from **Connected** to **Flagged**. If the quality doesn't improve over seven days, the status returns to **Connected**. However, the messaging limit will decrease to the next level. For example, a phone number that used to have a 100,000 messaging limit now has a 10,000 messaging limit.
