---
nav_title: Inline Image Push
platform: Android
page_order: 14

---

# Android Inline Image Push

{% alert important %}
This feature is in Early Access. Please ask your account manager if you'd like to preview this new push message type.
{% endalert %}

![Android Inline Image Push example]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> Use the Inline Image push type to showcase your push notification images so users won't have to manually expand the message as required with a standard push type.

# Usage Requirements

This new notification type requires the Braze Android SDK v10.0.0+, and Android M+ devices.

Devices or SDKs which don't support this feature will fallback to see the standard big image push notifications instead of the new inline image design. Additionally, push action buttons are not supported when using this notification type.

This feature is available in the **Notification Type** menu when creating an Android Push message.

![Android Inline Image Push example]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

# Inline Image Aspect Ratio

Unlike regular Android push notifications, Inline Image push images are in a 3:2 aspect ratio.
