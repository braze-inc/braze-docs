---
nav_title: Push Notifications
page_order: 1

layout: featured
guide_top_header: "Push notifications"
guide_top_text: "[Push notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) allow you to send out notifications from your app when important events occur. You might send a push notification when you have new instant messages to deliver, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. Push notifications can also be [silent]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/), being used only to update your app's interface or trigger background work.<br><br>Push notifications are great for sporadic but immediately important content, where the delay between background fetches might not be acceptable. Push notifications can also be much more efficient than background fetch, as your application only launches when necessary.<br><br>Push notifications are rate-limited, so don't be afraid of sending as many as your application needs. iOS and the Apple Push Notification service (APNs) servers will control how often they are delivered, and you won't get into trouble for sending too many. If your push notifications are throttled, they might be delayed until the next time the device sends a keep-alive packet or receives another notification."
description: "This landing page is home to all things related to Swift push customization."

guide_featured_title: "Section articles"
guide_featured_list:
  - name: Initial Setup
    link: /docs/developer_guide/platform_integration_guides/swift/push_notifications/initial_setup
    image: /assets/img/braze_icons/annotation-alert.svg
  - name: Customizing Notifications
    link: /docs/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/
    image: /assets/img/braze_icons/play-square.svg
  - name: Deep Linking
    link: /docs/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/
    image: /assets/img/braze_icons/brush-02.svg
  - name: Push Stories
    link: /docs/developer_guide/platform_integration_guides/swift/push_notifications/customization/badges/
    image: /assets/img/braze_icons/key-01.svg
  - name: Silent Push Notifications
    link: /docs/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/
    image: /assets/img/braze_icons/eye-off.svg
  - name: Advanced features
    link: /docs/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/
    image: /assets/img/braze_icons/settings-01.svg


---
<br><br>
