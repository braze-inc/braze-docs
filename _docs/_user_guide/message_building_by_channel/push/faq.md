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

### What is the difference between "Send to Production" and "Send to Development" for iOS push certificates?

When adding an Apple Push Certificate in Braze, the **Send to Production** and **Send to Development** options determine which APNs (Apple Push Notification service) gateway Braze uses to deliver push notifications:

- **Send to Development:** Select this if the app was built in development mode in Xcode and signed with a development provisioning profile. Push notifications are routed through Apple's development (sandbox) gateway.
- **Send to Production:** Select this if the app is distributed via Apple's TestFlight, App Store, or enterprise distribution. Push notifications are routed through Apple's production gateway.

If the wrong option is selected, push notifications will silently fail because the push token type won't match the gateway. When in doubt, apps distributed through TestFlight or the App Store should use **Send to Production**.
