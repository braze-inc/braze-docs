---
nav_title: Inline Image Push
platform: Android
page_order: 14

---

# Android Inline Image Push

![Android Inline Image Push example]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: width="55%"}

Inline Image push notifications are custom push notifications by Braze that show images inline without the need to manually expand like standard push notifications.

# Usage Overview

No extra integration is required for Android Inline Image Push after upgrading to Braze Android SDK 10.0.0. Inline Image push notifications require Android M+ devices. Devices lower than Android M will see standard big image push notifications instead of inline images. Additionally, push action buttons are not supported when using this notification type.

# Inline Image Aspect Ratio

Unlike regular Android push notifications, Inline Image push images are in a 3:2 aspect ratio.
