---
nav_title: Silent Push Notifications
article_title: Silent Push Notifications for Android
platform: Android
page_order: 3
description: "This article covers how to implement silent push notifications in your Android application."
channel:
  - push

---

# Silent push notifications for Android

> Silent notifications allow you to notify your app in the background when important events occur. You might have new instant messages to deliver, new issues of a magazine to publish, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. Silent notifications are great for sporadic but immediately important content, where the delay between background fetches might not be acceptable.

## Setting up silent push notifications

{% alert tip %}
When you [compose your push notification message]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message//?tab=android#step-4-compose-your-push-message), you can send a silent Android push notification by sending a message with only a single space. Keep in mind, this is **not** the recommended method for sending push notifications, but can be helpful in some cases.
{% endalert %}

Silent notifications are available through the Braze [Messaging API][2]. To take advantage of them, you need to set the `send_to_sync` flag to `true` within the [Android push object][3] and ensure there are no `title` or `alert` fields set as it will cause errors when used alongside `send_to_sync`. You can, however, include data `extras` within the object.

Silent notifications are also available within the dashboard. To send a silent notification, ensure the title and body fields of the notification are blank as pictured:

![][6]

[2]: {{site.baseurl}}/api/endpoints/messaging/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[6]: {% image_buster /assets/img_archive/SilentPushExample.png %} "Silent Push Notification Example -- Android"
