---
nav_title: Push Stories
article_title: Push Stories for iOS
platform: Swift
page_order: 27
description: "This article shows how to set up Push Stories for your iOS application."
channel:
  - push

---

# Push Story setup

The Push Story feature requires the `UNNotification` framework and is only available in Swift.

## Step 1: Enable push in your app

Follow the [push notification integration][1] to enable push in your app.

## Step 2: Adding the Notification Content Extension target

In your app project, go to menu **File > New > Target...** and add a new `Notification Content Extension` target and activate it.

![][2]

Xcode should generate a new target for you and create files automatically for you including:

- `NotificationViewController.swift`
- `MainInterface.storyboard`

## Step 3: Enable capabilities

The Push Story feature requires the background mode in the **Signing & Capabilities** section of the main app target. After turning on the background modes, select **Background fetch** and **Remote notifications**.

![][3]

You also need to add `Capability App Groups`. If you haven't had any app group in your app, go to the **Capability** of the main app target, turn on the `App Groups`, and click the **+** button. Use your app's bundle ID to create the app group. For example, if your app's bundle ID is `com.company.appname`, you can name your app group `group.com.company.appname.xyz`. You need to turn on the `App Groups` for both the main app and content extension targets.

{% alert important %}
`App Groups` in this context refer to Apple's [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) and not your Braze app group ID.
{% endalert %}

## Step 4: Adding the Push Story framework to your app

{% tabs local %}
{% tab Swift Package Manager %}

After following the [Swift Package Manager integration guide]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/), add `BrazePushStory` to your `Notification Content Extension`:

![In Xcode, under frameworks and libraries, select the "+" icon to add a framework.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Add the following line to your Podfile:

```ruby
target 'YourContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

After updating the Podfile, navigate to the directory of your Xcode app project within your terminal and run `pod install`.

{% endtab %}
{% tab Manual %}

Download the latest `BrazePushStory.zip` from the [GitHub release page](https://github.com/braze-inc/braze-swift-sdk/releases), unzip it, and add the `BrazePushStory.xcframework` to your project's `Notification Content Extension`:

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
Make sure that **Do Not Embed** is selected for **BrazePushStory.xcframework** under the **Embed** column.
{% endalert %}

{% endtab %}
{% endtabs %}

## Step 5: Updating your notification view controller

In your `NotificationViewController.swift`, add the following line to import the header files:

```swift
import BrazePushStory
```

Next, replace the default implementation by simply inheriting `BrazePushStory.NotificationViewController`:

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

## Step 6: Set the notification content extension plist

Open the `Info.plist` file of the `Notification Content Extension` and add and change the following keys under `NSExtension \ NSExtensionAttributes`:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (`String` type)
`UNNotificationExtensionDefaultContentHidden` = `YES` (`Boolean` type)
`UNNotificationExtensionInitialContentSizeRatio` = `0.6` (`Number` type)
`UNNotificationExtensionUserInteractionEnabled` = `YES` (`Boolean` type)

![][12]

## Step 8: Updating the Braze integration in your main app

Before initializing Braze, assign the name of your App Group to your Braze configuration's [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) property.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[2]: {% image_buster /assets/img/swift/push_story/add_content_extension.png %}
[3]: {% image_buster /assets/img/swift/push_story/enable_background_mode.png %}
[4]: {% image_buster /assets/img/swift/push_story/add_app_groups.png %}
[12]: {% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %}
