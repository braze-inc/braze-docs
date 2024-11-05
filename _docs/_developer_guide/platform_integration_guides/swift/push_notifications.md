---
nav_title: Push Notifications
article_title: "Push notifications for the Braze Swift SDK"
page_order: 1
description: "This landing page is home to all things Swift push notifications."
---

# About push notifications

> [Push notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) allow you to send out notifications from your app when important events occur. You might send a push notification when you have new instant messages to deliver, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. They are also more efficient than background fetch, as your application only launches when necessary.

## Rate limits

Push notifications are rate-limited, so don't be afraid of sending as many as your application needs. iOS and the Apple Push Notification service (APNs) servers will control how often they are delivered, and you won't get into trouble for sending too many. If your push notifications are throttled, they might be delayed until the next time the device sends a keep-alive packet or receives another notification.

## Next steps

Before you can use push notifications, you'll need to complete the following:

1. Integrate the [Braze Swift SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/) into your app.
2. Complete the [initial push notification setup]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/initial_setup).
