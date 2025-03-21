---
nav_title: FAQ
article_title: Push FAQ
page_order: 80
description: "This article addresses some of the most frequently asked questions that arise when setting up push campaigns."
page_type: FAQ
channel:
  - Push
---

# Frequently asked questions

> This article provides answers to some frequently asked questions about the push channel.

### What happens when multiple users log into a single device?

When a user logs out of an device or website, they will remain reachable by push until another user logs in and their push token is reassigned to the new user of the device. This is because a given app or website can only have one push subscription per device.

When a push token is reassigned, the change is reflected in the user profile's **Push Changelog**. You can find this by going to the **Engagement** tab in the user profile.

![The "Push Changelog" in the "Contact Settings" section.][1]{: style="max-width:50%;"}

### Why doesn't an opted-in user have a push token?

The user's push token may have been moved to another user.

1. Go to the **Push Changelog** in the **Engagement** tab of the affected user's profile, and look for the relevant push token. It will have a message that says the push token was moved to another user.
2. Copy and paste the affected push token into the user search bar. If the token still exists, it will lead to a user that has more recently logged into the device.
3. Have the user log into the profile with the missing token.
4. Trigger a new push send. This will move the token back to the account if they still have push enabled on the device level.

If the push token doesn't exist, check the user docs for other accounts using the same device. The push token should be in one of those, and the associated account should have a more recent session time than the original.

[1]: {% image_buster /assets/img/push_changelog_faq.png %}