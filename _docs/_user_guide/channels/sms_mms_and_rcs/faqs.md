---
nav_title: FAQ
article_title: SMS, MMS, and RCS FAQ
page_order: 20
description: "This article addresses frequently asked questions about SMS, MMS, and RCS messaging."
page_type: FAQ
alias: /sms_mms_rcs_faq/
channel:
  - SMS
  - MMS
  - RCS
---

# Frequently asked questions

> This article addresses frequently asked questions about SMS, MMS, and RCS messaging.

## General

### What is an `app_id` in the SMS API object?

The app identifier API key or `app_id` is a parameter associating activity with a specific app in your workspace. It designates which app within the workspace you are interacting with. For example, you will find that you will have an `app_id` for your iOS app, an `app_id` for your android app, and an `app_id` for your web integration.

You can find your `app_id` by navigating to **Settings** > **App Settings** and locating the **Identification** section.

### What happens if multiple users have the same phone number?

When multiple user profiles that share one phone number (enabled for SMS) are eligible for an action-based campaign or Canvas component at the same time, triggered by the event of an inbound SMS, Braze will dedupe users on the Canvas component level. This will prevent users from receiving more than one SMS text for a Canvas component, even if multiple users share the same phone number.

{% alert note %}
Braze doesn't dedupe by phone number for scheduled Canvases.
{% endalert %}

Braze will use the following flow to determine the recipient profile:
- Check which profile received SMS most recently (up to 7 days ago); if one exists, send it to that user.
- If neither had received SMS up to 7 days ago, send to the user who has a user alias of "phone" that matches the phone number.
- If neither exists, send to a random profile between the ones available.

If you receive a "START" or "STOP" keyword from the shared phone number, all user profiles will be subscribed and enabled for SMS or unsubscribed. This also applies to API state changes. For example, if multiple profiles with different external IDs have the same phone numbers, a subscription group state change through the API will update all profiles with that phone number, even if only one external ID is specified.

{% alert important %}
If you stagger your users into a Canvas and have different schedule times for each Canvas component, you can send a user with the same email or phone duplicate messages.
{% endalert %}

To prevent unnecessarily large updates, Braze will update a maximum of 100 user profiles that share an identifier when a subscription update is made. If more than 100 user profiles share the same phone number, not all profiles will be updated.

### What are shared short codes?

With a shared short code, all text messages, no matter what business or organization sends them, arrive on a consumer's mobile device from the same 5-6 digit phone number. While shared short codes are relatively low-cost and immediately available, this means that your business will not have a dedicated short code.

Some downsides to this approach include:

- If your customers opts-out of another business's messages that have a shared short code with you, they will have opted out of your messages as well.
- If one business violates the rules, all businesses' messages are suspended.
- Security issues

## Billing and pricing

### How will I be billed for SMS?

Besides the charges for short and long codes, Braze provides an allotment of SMS messages for different countries. That is, we work with you to set a certain number of message segments for different countries, which you'll use to send SMS campaigns. Billing is done by the number of message segments sent per country. To read more about how message segments are calculated see our [Message Segments and Copy Limits]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/) guide. Your account manager will contact you to let you know if you are close to reaching your maximum, providing relevant reports to help keep you informed. For further questions regarding overages, contact your Braze representative.

### Does MMS and SMS pricing differ?

MMS and SMS have different costs and are charged separately based on volume. Contact the Braze Onboarding team for pricing information.

### How can I avoid overages?

While we can't promise that you won't occasionally have an overage, you could follow these precautions to decrease the chances of going over your allotted limits:

- Pay attention to the number of characters in your SMS. Unintentionally sending more than one segment could cause overages. For more details, refer to our [segment breakdown]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/).
- Carefully calculate your SMS characters to account for Liquid or Connected Content. The Braze SMS composer in your dashboard does not estimate or factor in the usage of either of these features.
- Consider the type of encoding your message uses - if your message uses GSM-7 encoding, you can usually estimate that you can send a message with 128 characters per message segment. If your message uses [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) encoding, you can usually estimate that you can send a message with 67 characters per message segment.
- Test, test, and test! Always test your SMS messages before launch, especially when using Liquid and Connected Content.

### If a message is sent to a landline, will the message still count toward my SMS send count?

In the US, Canada, and UK:
- If an SMS is sent to a landline, it will be marked as **Undelivered**. Note that Twilio will still charge for attempted delivery, so messages marked as **Sent**, **Delivered**, or **Undelivered** in your message logs will be billed.
- In the UK, some carriers will convert the SMS into a voicemail, delivering the message.

In other countries:
- Twilio will throw an error, and you will not be billed for the attempted SMS message.

### Why is the Braze dashboard warning me I may be charged for additional message segments when my message is under 160 (GSM-7) or 70 (UCS-2) characters?

You might be charged additional message segments if you have Liquid personalization included in your message. Content Block templating does not occur until the message is preparing to be sent. When you are editing an SMS with a Content Block, Braze does not know what the Content Block will contain but provides a rough estimate. We recommend that users use the test pane to preview the message to better understand what to expect.

## Sending and deliverability

### Can you include links in an SMS?

You can include any link in any SMS campaign you would like. However, there are a few concerns to consider:

- Links may take up much of the 160 character limit for SMS. If you include a link and text, it may result in two SMS messages instead of just one.
- Companies often use link shorteners to limit the character count impact of a link. However, if sending a shortened link through a long code, carriers may block or deny the message, as they may be suspicious of the link redirect.
- Using a [short code]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/short_and_long_codes/) would be the most reliable number type for including links.

Braze also has its own link-shortening feature that will shorten links and provide click-through analytics automatically. Refer to [Link Shortening]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/link_shortening/) for more information.

### Do you need to rate-limit how fast you send SMS messages?

The default concurrency rate and throughput enable about 360,000 messages an hour per short code. Additional throughput requires additional short codes.

### How do you allowlist URLs for SMS?

Before sending SMS messages containing URLs to users in certain countries (for example, Sweden or Nordic countries), you must get these URLs registered with the carrier. Contact your Braze customer service manager to help. This process will take around five days.

### What are the best sending practices to avoid spam detection for SMS?

1. Make sure opt-in and opt-out instructions are clear.
2. Ensure you (the brand) have a relationship with the customer.
3. Make sure the content is relevant to the relationship and what the user has opted-in to receive.

For more guidelines on avoiding spam detection, visit [SMS laws and regulations guidelines]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/laws_and_regulations/).

### How many characters does an emoji use?

Emojis can be tricky, as there is no standard character count across all emojis. There is the risk the emoji will exceed the character limit and break the SMS into multiple messages, despite it showing as one message in the Braze composer. When testing your messages, you can better verify if a message will be split using our [segment calculator]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator).

## Subscription groups and opt-in/opt-out

### How do you create logic for selective opt-ins to SMS so users are in the right subscription group?

Custom keywords would be written as custom events, so you would want to create segments based on the keywords customers can text in. For example, if a user opts in to SMS for VIP messages but not alerts, you can create a VIP segment and an alerts segment, then assign the user to the appropriate segment.

### If a user texts "Stop" to our short code, are they unsubscribed from the subscription group?

What does that look like on the user profile? The subscription group will revert to 2 dashes (- -), and there will be custom events for subscribe and unsubscribe.

### If a user is opted out and sends a keyword to our short and long code, do they receive the response we configured for that keyword in Braze?

If a user is opted out and sends a keyword from one of the [default keyword categories]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/keywords/optin_optout/), they will receive the response for that keyword. If a user is opted out and sends a [custom keyword]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/keywords/keyword_handling/), they will not receive the response for that keyword.

### Will SMS event properties capture keywords in a sentence?

For a keyword to be recognized within a sentence, (for example, "please stop texting me"), you'll need to use a Liquid statement in the message to recognize the specific word. Event properties have a character limit of 256; otherwise, there is no character limit.

## Testing

### Do test text messages count toward limits?

Yes, they do. Keep this in mind when testing messages.

### Does a user need to be part of an SMS subscription group to receive SMS test messages?

Yes, they do. Users must have a valid phone number and be part of the SMS subscription group used for the test send.

### Is there a way to see if an alias exists on a user profile?

Aliases are not visible on the user profile. You would need to use the [Export User Data]({{site.baseurl}}/api/endpoints/export/) endpoints to confirm aliases being set.

## MMS

### Are there any changes to Currents data when sending an MMS?

No, the same level of insight will be provided when sending an MMS message.

### Can I control the order in which the image and message body of an MMS are delivered?

Braze has no control over the display order for when both a message-body and images are included in an MMS message. This is dependent on several factors including but not limited to:

- The carrier receiving the message
- The device receiving the message
- The overall size of the message

### Does MMS require a separate onboarding process?

No. MMS is now included in our SMS onboarding process. Existing customers who already went through onboarding can start sending MMS campaigns after completing the following steps:

1. Purchase MMS.
2. Contact the Braze Onboarding team to request the MMS feature to be flipped on. This will enable MMS and an SMS/MMS Subscription group will be created or updated for you.

Next, the Braze onboarding team will make sure your short and long codes are enabled (in the US and Canada) for MMS. They will also update your subscription groups to show your current numbers that were added or enabled for MMS. After these steps are complete, you can send MMS messages right away from our native SMS composer.

### Why can't I find MMS on my dashboard even though the feature is enabled?

MMS is only displayed on the Braze dashboard when a subscription group is considered "MMS enabled". This is reflected by an MMS tag when selecting the subscription group on the composer of an SMS/MMS message. This means that at least one number in the subscription group is capable of sending an MMS message.

Additionally, certain situations will require Twilio to re-approve the enablement of short codes that originally didn't have MMS enabled. This approval process could take weeks.

## RCS

### Can I send pre-recorded voicemails with RCS?

Yes, you can use media messages to support audio files.
