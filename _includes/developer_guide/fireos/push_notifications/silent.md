{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Setting up silent push notifications

Silent notifications are available through the Braze [Messaging API]({{site.baseurl}}/api/endpoints/messaging/). To take advantage of them, you need to set the `send_to_sync` flag to `true` within the [Android push object]({{site.baseurl}}/api/objects_filters/messaging/android_object/) and ensure there are no `title` or `alert` fields set as it will cause errors when used alongside `send_to_sync`. You can, however, include data `extras` within the object.

Silent notifications are also available within the dashboard. To send a silent notification, ensure the title and body fields of the notification are blank, as pictured:

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Silent Push Notification Example -- Android")
