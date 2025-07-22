{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), which includes implementing the `UNNotification` framework.

The following minimum SDK version is required to receive Push Stories:

{% sdk_min_versions swift:5.0.0 %}

## Setting up Push Stories

### Step 1: Adding the Notification Content Extension target {#notification-content-extension}

In your app project, go to menu **File > New > Target** and add a new `Notification Content Extension` target and activate it.

![]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

Xcode should generate a new target for you and create files automatically for you including:

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### Step 2: Enable capabilities {#enable-capabilities}

In Xcode, add the Background Modes capability using the **Signing & Capabilities** pane to the main app target. Select both the **Background fetch** and **Remote notifications** checkboxes.

![]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

#### Adding an App Group

Additionally, from the **Signing & Capabilities** pane in Xcode, add the App Groups capability to your main app target as well as the Notification Content Extension targets. Then, click the **+** button. Use your app's bundle ID to create the app group. For example, if your app's bundle ID is `com.company.appname`, you can name your app group `group.com.company.appname.xyz`.

{% alert important %}
App Groups in this context refer to Apple's [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) and not your Braze workspace (previously app group) ID.
{% endalert %}

If you do not add your app to an App Group, your app may fail to populate certain fields from the push payload and will not work fully as expected.

### Step 3: Adding the Push Story framework to your app {#enable-capabilities}

{% tabs local %}
{% tab Swift Package Manager %}

After following the [Swift Package Manager integration guide]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), add `BrazePushStory` to your `Notification Content Extension`:

![In Xcode, under frameworks and libraries, select the "+" icon to add a framework.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Add the following line to your Podfile:

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```

{% alert note %}
For instructions to implement Rich Push, see [Rich notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager).
{% endalert %}

After updating the Podfile, navigate to the directory of your Xcode app project within your terminal and run `pod install`.

{% endtab %}
{% tab Manual %}

Download the latest `BrazePushStory.zip` from the [GitHub release page](https://github.com/braze-inc/braze-swift-sdk/releases), extract it, and add the `BrazePushStory.xcframework` to your project's `Notification Content Extension`.

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
Make sure that **Do Not Embed** is selected for **BrazePushStory.xcframework** under the **Embed** column.
{% endalert %}

{% endtab %}
{% endtabs %}

### Step 4: Updating your notification view controller {#enable-capabilities}

In `NotificationViewController.swift`, add the following line to import the header files:

```swift
import BrazePushStory
```

Next, replace the default implementation by inheriting [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/):

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### Custom handling push story events

If you want to implement your own custom logic to handle push story notification events, inherit `BrazePushStory.NotificationViewController` as above and override the [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:)) methods as below.

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)
    
    // Custom handling logic
  }
  
  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)
    
    // Custom handling logic
  }
}
```

### Step 5: Setting the Notification Content Extension plist {#notification-content-extension}

Open the `Info.plist` file of the `Notification Content Extension`, then add and change the following keys under `NSExtension \ NSExtensionAttributes`:

| Key                                              | Type    | Value                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | String  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Boolean | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Number  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Boolean | `YES`                  |

Your `Info.plist` file should match the following image:

![]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

### Step 6: Updating the Braze integration in your main app {#update-braze}

Before initializing Braze, assign the name of your app group to your Braze configuration's [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) property.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```
