---
nav_title: Conversation Push
article_title: Conversation Push for Android
platform: Android
page_order: 5.92
description: "This appication covers how to implement android conversation push in your Android application."
channel:
  - push
---

# Android conversation push

![Android Conversation Push example]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

The [people and conversations initiative][2] is a multi-year Android initiative that aims to elevate people and conversations in the system surfaces of the phone. This priority is based on the fact that communication and interaction with other people is still the most valued and important functional area for the majority of Android users across all demographics.

No additional integration or SDK changes are required to use this feature. Devices or SDKs which don't meet the minimum version requirements will instead show a standard push notification.

## Usage requirements

- This notification type requires the Braze Android SDK v15.0.0+ and Android 11+ devices.
- Unsupported devices or SDKs will fallback to a standard push notification.

This feature is only available over the Braze REST API. See the [Android Push Object Documentation][1] for more information.

[1]: {{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object
[2]: https://developer.android.com/guide/topics/ui/conversations
