---
nav_title: SMS/MMS FAQs
article_title: SMS/MMS FAQs
page_order: 0
description: "This article provides answers to frequently asked questions about SMS and MMS"
---

# SMS FAQs

> This article provides answers to frequently asked questions about SMS and MMS.

### What is an `app_id` in the SMS API object?

The app identifier API key or `app_id` is a parameter associating activity with a specific app in your app group. It designates which app within the app group you are interacting with. For example, you will find that you will have an `app_id` for your iOS app, an `app_id` for your android app, and an `app_id` for your web integration. 

Your `app_id` can be found on the dashboard by navigating to **Developer Console -> API Settings -> Identification"**.

### Does a user need to be part of an SMS subscription group to receive SMS test messages?

No. However, SMS test messages can only be sent to valid phone numbers in the database.

### How do you whitelist URLs for SMS?

Before sending SMS messages containing URLs to users in certain countries (For example, Sweden/Nordic countries), you must get these URLs registered with the carrier. Reach out to your Braze customer service manager to help; this process will take around five days.  

### How does SMS sending work if multiple profiles share the same phone number and are enabled for SMS?

Enabled for SMS means the phone number shared by the profiles is part of an SMS subscription group. 
- If you receive an inbound message "STOP" from the shared phone number, all user profiles with that number will be unsubscribed from SMS. 
- If you receive an inbound message "START" from the shared phone number, all user profiles with that number will be subscribed and enabled for SMS.

When multiple user profiles sharing one phone number (enabled for SMS) are eligible for a campaign or Canvas step at the same time, triggered by the event of an inbound SMS, Braze will use the following flow to determine the recipient profile:
- Check which profile received SMS most recently (up to 7 days ago); if one exists, send it to that user.
- If neither had received SMS up to 7 days ago, send to the user who has a user alias of "phone" that matches the phone number.
- If neither exists, send to a random profile between the ones available. 

### What SMS use cases does Braze not support?

There are three common SMS use cases that Braze does not currently support:
- Two-factor authorization
- ChatBots
- Phone Calls

### What are the best sending practices to avoid Spam detection for SMS?

1. Make sure opt-in and opt-out instructions are clear.
2. Ensure you(the brand) have a relationship with the customer.
3. Make sure the content is relevant to the relationship and what the user has opted-in to receive.

For more guidelines on avoiding spam detection, visit [SMS laws and regulations guidelines](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

### Why is the Braze dashboard warning me I may be charged for additional message segments when my message is under 160(GCM-7) or 70(UCS-2) characters?

You might be charged additional message segments if you have Liquid personalization included in your message. Content block templating does not occur until the message is preparing to be sent. When you are editing an SMS with a content block, Braze does not know what the content block will contain but provides a rough estimate. We recommend that users use the test pane to preview the message to better understand what to expect.

### If a message is sent to a landline, will the message still count toward my SMS send count?

In the US, Canada, and UK:
- If an SMS is sent to a landline, it will be marked as **Undelivered**. Note that Twilio will still charge for attempted delivery, so messages marked as **Sent**, **Delivered**, or **Undelivered** in your message logs will be billed.
- In the UK, some carriers will convert the SMS into a voicemail, delivering the message.

In other countries:
- Twilio will throw an error, and you will not be billed for the attempted SMS message. 