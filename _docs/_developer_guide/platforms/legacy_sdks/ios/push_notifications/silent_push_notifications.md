---
nav_title: Silent push notifications
article_title: Silent Push Notifications for iOS
platform: iOS
page_order: 4
description: "This reference article covers implementing silent push notifications in your iOS application."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Silent push notifications

Push notifications allow you to notify your app when important events occur. You might send a push notification when you have new instant messages to deliver, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. Push notifications can also be silent, containing no alert message or sound, being used only to update your app's interface or trigger background work. 

Push notifications are great for sporadic but immediately important content, where the delay between background fetches might not be acceptable. Push notifications can also be much more efficient than background fetch, as your application only launches when necessary. 

Push notifications are rate-limited, so don't be afraid of sending as many as your application needs. iOS and the APNs servers will control how often they are delivered, and you won't get into trouble for sending too many. If your push notifications are throttled, they might be delayed until the next time the device sends a keep-alive packet or receives another notification.

## Sending silent push notifications

To send a silent push notification, set the `content-available` flag to `1` in a push notification payload. When sending a silent push notification, you might also want to include some data in the notification payload, so your application can reference the event. This could save you a few networking requests and increase the responsiveness of your app.

{% alert warning %}
Attaching both a title and body with `content-available=1` is not recommended because it can lead to undefined behavior. To ensure that a notification is truly silent, exclude both the title and body when setting the `content-available` flag to `1.` For further details, refer to the official [Apple documentation on background updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

The `content-available` flag can be set in the Braze dashboard as well as within our [Apple push object]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) in the [messaging API]({{site.baseurl}}/api/endpoints/messaging/).

![The Braze dashboard showing the "content-available" checkbox found in the "settings" tab of the push composer.]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

## Use silent push notifications to trigger background work

Silent push notifications can wake your app from a "Suspended" or "Not Running" state to update content or run certain tasks without notifying your users. 

To use silent push notifications to trigger background work, set up the `content-available` flag following the preceding instructions with no message or sound. Set up your app's background mode to enable `remote notifications` under the **Capabilities** tab in your project settings. A remote notification is just a normal push notification with the `content-available` flag set. 

![Xcode showing the "remote notifications" mode checkbox under "capabilities".]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

Enabling background mode for remote notifications is required for [uninstall tracking]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift).

Even with the remote notifications background mode enabled, the system will not launch your app into the background if the user has force-quit the application. The user must explicitly launch the application or reboot the device before the app can be automatically launched into the background by the system.

For more information, refer to [pushing background updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc) and [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:).

## iOS silent notifications limitations

The iOS operating system may gate notifications for some features. Note that if you are experiencing difficulties with these features, the iOS's silent notifications gate might be the cause.

Braze has several features which rely on iOS silent push notifications:

|Feature|User Experience|
|---|---|
|Uninstall Tracking | User receives a silent, nightly uninstall tracking push.|
|Geofences | Silent syncing of geofences from server to device.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Refer to Apple's [instance method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) and [unreceived notifications](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) documentation for more details.

[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23