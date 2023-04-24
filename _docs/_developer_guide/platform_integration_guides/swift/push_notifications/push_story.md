---
nav_title: Push Stories
article_title: Integrating Push Stories for iOS
platform: Swift
page_order: 27
description: "This article shows how to set up Push Stories for your iOS application."
channel:
  - push

---

# Integrating Push Stories for iOS

[Push Stories][5] allow marketers to use photo carousel functionality to create a sequence of pages within a push notification. These pages consist of an image, click action, title, and description. Setting up Push Stories for your iOS app requires additional steps beyond integrating standard push notifications, which are outlined in this article.

## Prerequisites

The following SDK versions is required to receive Push Stories:

{% sdk_min_versions swift:5.0.0%}

Ensure that you have followed the [push notification integration tutorial][1] to enable push in your app. As part of this task, you should have implemented the `UNNotification` framework, which is required for this feature.

## Step 1: Adding the Notification Content Extension target {#notification-content-extension}

In your app project, go to menu **File > New > Target** and add a new `Notification Content Extension` target and activate it.

![][2]

Xcode should generate a new target for you and create files automatically for you including:

- `NotificationViewController.swift`
- `MainInterface.storyboard`

## Step 2: Enable capabilities {#enable-capabilities}

In Xcode, add the Background Modes capability using the **Signing & Capabilities** pane to the main app target. Select both the **Background fetch** and **Remote notifications** checkboxes.

![][3]

Additionally, from the **Signing & Capabilities** pane in Xcode, add the App Groups capability to your main app target as well as the Notification Content Extension targets. Then, click the **+** button. Use your app's bundle ID to create the app group. For example, if your app's bundle ID is `com.company.appname`, you can name your app group `group.com.company.appname.xyz`.

{% alert important %}
App Groups in this context refer to Apple's [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) and not your Braze app group ID.
{% endalert %}

## Step 3: Adding the Push Story framework to your app {#enable-capabilities}

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

Download the latest `BrazePushStory.zip` from the [GitHub release page](https://github.com/braze-inc/braze-swift-sdk/releases), extract it, and add the `BrazePushStory.xcframework` to your project's `Notification Content Extension`:

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
Make sure that **Do Not Embed** is selected for **BrazePushStory.xcframework** under the **Embed** column.
{% endalert %}

{% endtab %}
{% endtabs %}

## Step 4: Updating your notification view controller {#enable-capabilities}

In `NotificationViewController.swift`, add the following line to import the header files:

```swift
import BrazePushStory
```

Next, replace the default implementation by inheriting `BrazePushStory.NotificationViewController`:

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

## Step 5: Setting the Notification Content Extension plist {#notification-content-extension}

Open the `Info.plist` file of the `Notification Content Extension`, then add and change the following keys under `NSExtension \ NSExtensionAttributes`:

| Key                                              | Type    | Value                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | String  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Boolean | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Number  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Boolean | `YES`                  |

Your `Info.plist` file should match the following image:

![][12]

## Step 6: Updating the Braze integration in your main app {#update-braze}

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
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/
[12]: {% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %}