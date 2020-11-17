---
nav_title: Rich Notifications
platform: iOS
page_order: 0.1

---

# iOS 10 Rich Notifications

iOS 10 introduces the ability to send push notifications with images, gifs, and video. To enable this functionality, clients must create a `Service Extension`, a new type of extension that enables modification of a push payload before it is displayed.

## Creating A Service Extension
To create a [Notification Service Extension][23], navigate to `File > New > Target` and select `Notification Service Extension`.

![Adding a Service Extension][26]

Ensure that `Embed In Application` is set to embed the extension in your application.

## Setting Up The Service Extension
A `Notification Service Extension` is its own binary that is bundled with your app. As such, it must be set up in the [Apple Developer Portal][27] with its own App ID and Provisioning Profile. Typically extensions are named with a suffix on the main application's ID (e.g., `com.appboy.stopwatch.stopwatchnotificationservice`).

### Configuring The Service Extension To Work With Braze
Braze sends down an attachment payload in the APNs payload under the `ab` key that we use to configure, download and display rich content:

For example:

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

The relevant payload values are:

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

To manually display push with a Braze payload, download the content from the value under `AppboyAPNSDictionaryAttachmentURLKey`, save it as a file with the file type stored under the `AppboyAPNSDictionaryAttachmentTypeKey` key, and add it to the notification attachments.
We provide sample code that you can copy into your `Notification Service Extension`. Simply changing the class name to the one you picked will automatically provide this functionality.

You can write the Service Extension in either Objective-C or Swift.

For our sample code, see the [Stopwatch sample application][30]. For Swift sample code, see the [Hello Swift sample application][38].

## Creating A Rich Notification In Your Dashboard

To create a rich notification in your Braze dashboard, simple create an iOS push and attach an image or gif, or provide a url that hosts an image, gif, or video.  Note that assets are downloaded on the receipt of push notifications, so that if you are hosting your own content you should plan for large, synchronous spikes in requests.

Also note the supported file types and sizes, listed [here][28].


[0]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/
[1]: https://developer.apple.com/ios/manage/overview/index.action "iOS Provisioning Portal"
[2]: {% image_buster /assets/img_archive/ios_provisioning.png %} "pushNotification2.png"
[3]: {% image_buster /assets/img_archive/AppleProvisioningOptions.png %} "AppleProvisioningOptions.png"
[4]: {% image_buster /assets/img_archive/push_cert_gen.png %} "pushNotification3.png"
[5]: https://dashboard-01.braze.com/app_settings/app_settings
[6]: {% image_buster /assets/img_archive/push_cert_upload.png %} "push upload example image"
[7]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m#L34-62 "sample AppController.mm"
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation
[11]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3 "iOS Lifecycle Methods"
[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[14]: https://developer.apple.com/reference/usernotifications/unnotificationcategory "Categories Docs"
[17]: {{site.baseurl}}/assets/img_archive/push_example_category.png
[18]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:
[19]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[23]: https://developer.apple.com/reference/usernotifications/unnotificationserviceextension
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[26]: {% image_buster /assets/img_archive/ios10_se_at.png %}
[27]: https://developer.apple.com
[28]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[30]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m
[32]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m#L218-L223
[33]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m#L245-L249
[34]: {% image_buster /assets/img_archive/xcode8_auto_signing.png %}
[35]: #push-action-buttons-integration
[36]: #step-4-register-for-push-notifications
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/#push-action-buttons-customization
[38]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift
