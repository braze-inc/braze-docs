---
nav_title: FAQ
article_title: In-App Message FAQ
page_order: 8
description: "This article provides answers to frequently asked questions about In-App Messages."
tool: in-app messages

---

# Frequently asked questions

> This article provides answers to some frequently asked questions about in-app messages.

### What is an in-browser message and how does it differ from an in-app message?

In-browser messages are in-app messages sent to web browsers. To create an in-browser message, make sure to select **Web Browser** under the **Send To** field when creating your in-app message campaign or Canvas. 

### Will an in-app message display if a device is offline?

It depends. Because in-app messages are delivered at session start, the device is able to download the payload prior to going offline, the in-app message can still be displayed while offline. If the payload is not downloaded, then the in-app message will not display.

### If a user already has an in-app message payload on their device and the message expiration is changed, will the expiration be updated on their device?

When a user starts a session, Braze checks if changes have been made to any in-app messages that they are eligible for and updates them accordingly. So if the expiration has changed and they log a session, then the in-app message is sent to the device with the updated information.

### How do I set up Quiet Hours for an in-app message campaign?

The Quiet Hours feature isn't available for use with in-app message campaigns. This feature is used to prevent messages from being sent to your users during specific hours. For in-app message campaigns, your users will only receive in-app messages if they are active within the app. 

As a workaround to send in-app messages during a specific time, use the following sample Liquid code. This allows the message to be aborted if the in-app message is displayed after 7:59 pm or before 8 am at the specified time zone.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### When is eligibility for an in-app message calculated?

Eligibility for an in-app message is calculated at the time of delivery. If an in-app message is scheduled to send at 7 am, then eligibility is checked for this in-app message at 7 am.

Once the in-app message is displayed, the eligibility will depend on when the in-app message is downloaded and triggered.

### Why is my archived in-app message campaign still delivering in-app message impressions?

This can occur for users who met the segment criteria when the in-app message campaign was active.

To prevent this, during your campaign setup, select **Re-evaluate campaign eligibility before displaying**. 

### How does Braze calculate an in-app message expiration set to "after 1 day(s)"?

Braze calculates an expiration time of one day as 24 hours after users are eligible to receive a message.

### What are templated in-app messages?

In-app messages are delivered as templated in-app messages when **Re-evaluate campaign eligibility before displaying** is selected or if any of the following Liquid tags exist in the message:

- `canvas_entry_properties`
- `connected_content`
- SMS variables such as {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

This means that during session start, the device receives the trigger of that in-app message instead of the entire message. When the user triggers the in-app message, the user's device makes a network request to fetch the actual message.

{% alert note %}
The message is not delivered if the device doesn't have access to the internet. The message might not be delivered if the Liquid logic takes too long to resolve.
{% endalert %}

### How does abort behavior work for in-app messages?

At Braze, an abort occurs when a user takes an action that makes them eligible to receive a message, but they don't receive the message because its Liquid logic marks them as ineligible. For example:

1. Sam performs an action which should trigger an email campaign.
2. The email's body contains Liquid logic that says if a custom attribute score is less than 50, do not send this email.
3. Sam's custom attribute score is 20.
4. Braze recognizes that Sam shouldn't receive this email, and the email is aborted.
5. An abort event is logged.

However, because in-app messages are a pull channel, aborts work a little differently for them.

#### Standard in-app message abort behavior

In-app messages are pulled in by the device at session start and cached on the device, so regardless of Internet connection quality, the message can be delivered instantly to the user. For example, if a user receives five in-app messages within their session, they receive all five on session start. The messages are cached locally and appear when their defined trigger events occur (session start, user clicks a button which logs a custom event, or other).

In other words, the logic that determines if an in-app message should be aborted occurs **before** the trigger has occurred. To demonstrate this, let's say Sam from the email example is subscribed to push notifications.

1. Sam starts a session by launching a Braze-powered app on their phone.
2. Based on the audience criteria of the active campaigns in the workspace, Sam could be eligible for five different campaigns. All five are pulled into their phone and cached.
3. Sam **has not** performed any actions that would trigger these messages, but they could receive those messages in the session.
4. The Liquid in two of the in-app messages has rules that exclude Sam from receiving the message (such as their score custom attribute not being high enough).
5. Sam is not sent the two in-app messages that exclude them, but they are sent the other three messages.
6. No abort events are logged.

Braze doesn't log any abort events in Sam's case because this doesn't fulfill the definition of an abort; Sam **did not** perform any actions that would trigger the messages. For in-app messages, users never actually perform the trigger before Braze determines they shouldn't see the message.

#### Templated in-app message abort behavior

[Templated in-app messages](#what-are-templated-in-app-messages) force the SDK to reevaluate if a message should display when the trigger event occurs. This has a different abort behavior. To demonstrate, consider this example:

1. Sam starts a Braze session by launching a Braze-powered app on their phone.
2. The audience criteria of the active campaigns say Sam could be eligible for a templated in-app message, so the trigger information is sent to their device without the message payload.
3. Sam selects a button that logs a custom event, triggering the templated in-app message.
4. Sam's device makes a network request to fetch the in-app message.
5. The message's Liquid logic leads to an abort, so Braze logs this as an abort; Sam performed the trigger action prior to this evaluation.

#### Comparing in-app message abort behavior

This table compares the in-app message flows that Sam experienced:

| In-app message | Abort behavior |
| --- | --- |
| Standard | An abort event was not logged because Sam didn't perform any actions that would trigger a message.<br><br>Standard in-app messages don't log aborts because the definition of an abort is "didn't see the message despite performing the trigger action." Because in-app messages are delivered to the device before the trigger actions occur, it doesn't make sense to consider in-app messages omitted because of Liquid logic. |
| Templated | An abort event was logged because Sam performed the trigger action to trigger the templated in-app message, but received an abort in the Liquid templating. <br><br>Templated in-app messages log aborts because the Liquid evaluation occurs after the trigger action has been performed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }