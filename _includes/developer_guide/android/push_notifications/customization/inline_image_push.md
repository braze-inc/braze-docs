# Inline image push

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> Showcase a larger image within your Android push notification using inline image push. With this design, users won't have to manually expand the push to enlarge the image. 

## Platform availability

This feature is only available for Android&#8212;not FireOS.

## Prerequisites

No additional integration or SDK changes are required to use this feature. Devices or SDKs that do not meet the following minimum version requirements will instead show a standard big image push notification.

- This notification type requires the Braze Android SDK v10.0.0+ and Android M+ devices. 
- Unsupported devices or SDKs will fall back to the standard big image push notification.
- Unlike regular Android push notifications, inline image push images are in a 3:2 aspect ratio.

{% alert note %}
Devices running Android 12 will render differently due to changes in custom push notification styles.
{% endalert %}

## Setting up the dashboard

When creating an Android push message, this feature is available in the **Notification Type** dropdown.

![The push campaign editor showing the location of the "Notification Type" dropdown (above the standard push preview).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})
