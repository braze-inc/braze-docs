---
nav_title: FAQs
article_title: Push FAQs
page_order: 25
description: "This article addresses some of the most frequently asked questions that arise when setting up push campaigns."
page_type: FAQ
channel:
  - Push
---

# Frequently asked questions

> This article provides answers to some frequently asked questions about the push channel.

### What happens when multiple users log into a single device?

When a user logs out of a device or website, they will remain reachable by push until another user logs in. At that point, the push token is reassigned to the new user. This is because each device can only have one active push subscription per app or website.

When a push token is reassigned, the change is reflected in the user profile's **Push Changelog**. You can find this by going to the **Engagement** tab in the user profile.

![The "Push Changelog" in the "Contact Settings" section.]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### What does “Error sending push because the payload was invalid” mean?

This message indicates that APNs rejected the push request due to an invalid payload (for example, an empty payload or a payload that’s too large).

For details and next steps, see [Common Push Error Messages]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

### Why doesn't an opted-in user have a push token?

This can happen if the user’s push token was reassigned to someone else who used the same device.

1. Go to the **Push Changelog** in the **Engagement** tab of the affected user's profile.
2. Look for a message that says the push token was moved to another user.
3. Copy the push token and paste into the user search bar. 
4. If the push token still exists, you'll be directed to the user who most recently logged in on the device.

If you want the push token reassigned to the original user:

1. Have the original user log into the profile with the missing push token.
2. Trigger a new push send. This will move the token back to the account if they still have push enabled on the device level.

### How does Braze determine when a push message is sent successfully?

A message is logged as sent as soon as the message is received by the push service provider. This does not necessarily mean the user has received or viewed the message.

For iOS, the push service provider is Apple Push Notification Service (APNs), and for Android, it is typically Firebase Cloud Messaging (FCM). The push service provider will immediately respond with success or failure. A failure could include a bounce or a retry for network failure.

If a success message is returned, the send will be logged by Braze and the push service will then attempt to deliver to the device. If the device cannot immediately be reached, the service will retry up to its expiration option set in Braze (**TTL** for Android, **Expiry** for iOS). If the message times out, the push service will discard the push, but it will not be considered a bounce.

- For action-based delivery push campaigns, the message send is logged as soon as the user has performed the action that triggers the campaign.
- For scheduled campaigns, the send time is the time the message was enqueued and passed to the push service provider.
- For both delivery types, the message will be marked as "sent" in Braze and in the user profile under **Campaigns Received**, even though the user may not have seen or received the push yet.

The "deliveries" metric for push in the dashboard is calculated on page load as the number of sends minus bounces.

