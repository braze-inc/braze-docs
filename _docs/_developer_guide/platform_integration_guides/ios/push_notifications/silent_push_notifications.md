---
nav_title: Silent Push Notifications
article_title: Silent Push Notifications for iOS
platform: iOS
page_order: 4
description: "This article covers implementing silent push notifications in your iOS application."
channel:
  - push

---

# Silent push notifications

Remote notifications allow you to notify your app when important events occur. You might have new instant messages to deliver, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. Remote notifications are great for sporadic but immediately important content, where the delay between background fetches might not be acceptable. Remote Notifications can also be much more efficient than Background Fetch, as your application only launches when necessary. However, remote notifications are limited by the system and cannot automatically launch your application if the user has force-quit it.

A remote notification is really just a normal push notification with the `content-available` flag set. You might send a push with an alert message informing the user that something has happened, while you update the UI in the background, but remote notifications can also be silent, containing no alert message or sound, used only to update your app's interface or trigger background work. You might then post a local notification when you've finished downloading or processing the new content.

Silent push notifications are rate-limited, so don't be afraid of sending as many as your application needs. iOS and the APNs servers will control how often they are delivered, and you won't get into trouble for sending too many. If your push notifications are throttled, they might be delayed until the next time the device sends a keep-alive packet or receives another notification.

## Sending silent remote notifications

To send a silent remote notification, set the `content-available` flag to `1` in a push notification payload. When sending a silent remote notification, you might also want to include some data in the notification payload, so your application can reference the event. This could save you a few networking requests and increase the responsiveness of your app.

The `content-available` flag can be set in the Braze dashboard as well as within our [Apple push object]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) in the [messaging API][1].

![The Braze dashboard showing the "content-available" checkbox found in the "settings" tab of the push composer.][2]

## Use silent remote notifications to trigger background work

Silent remote notifications can wake your app from a "Suspended" or "Not Running" state to update content or run certain tasks without notifying your users. 

To use silent remote notifications to trigger background work, set up the `content-available` flag following the preceding instructions with no message or sound. Set up your app's background mode to enable `remote notifications` under the **Capabilities** tab in your project settings.

![Xcode showing the "remote notifications" mode checkbox under "capabilities".][3]

Enabling background mode for remote notifications is required for Braze's [uninstall tracking][6] feature.

Even with the remote notifications background mode enabled, the system will not launch your app into the background if the user has force-quit the application. The user must explicitly launch the application or reboot the device before the app can be automatically launched into the background by the system.

For more information, refer to [pushing background updates][4] and [`application:didReceiveRemoteNotification:fetchCompletionHandler:`][5].

## iOS silent notifications limitations

The iOS operating system may gate notifications for some features. Note that if you are experiencing difficulties with these features, the iOS's silent notifications gate might be the cause.

Braze has several features which rely on iOS silent push notifications:

|Feature|User Experience|
|---|---|
|Uninstall Tracking | User receives a silent, nightly uninstall tracking push.|
|Geofences | Silent syncing of geofences from server to device.|
{: .reset-td-br-1 .reset-td-br-2}

Refer to Apple's [instance method][7] and [unreceived notifications][8] documentation for more details.

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {% image_buster /assets/img_archive/remote_notification.png %} "content available"
[3]: {% image_buster /assets/img_archive/background_mode.png %} "background mode enabled"
[4]: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc
[5]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/uninstall_tracking/
[7]: https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application
[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23