{% multi_lang_include developer_guide/prerequisites/android.md %} Additionally, you'll need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Setting up silent push notifications

Silent notifications are available through the Braze [Messaging API]({{site.baseurl}}/api/endpoints/messaging/). To take advantage of them, you need to set the `send_to_sync` flag to `true` within the [Android push object]({{site.baseurl}}/api/objects_filters/messaging/android_object/) and ensure there are no `title` or `alert` fields set as it will cause errors when used alongside `send_to_sync`&#8212;however, you can include data `extras` within the object.

{% alert tip %}
When you [compose your push notification message]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message), you can send a silent Android push notification by sending a message with only a single space. Keep in mind, this is **not** the recommended method for sending push notifications, but can be helpful in some cases.
{% endalert %}
