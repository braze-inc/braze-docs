{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Setting up rich push notifications

### Step 1: Creating a service extension

To create a [notification service extension](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), navigate to **File > New > Target** in Xcode and select **Notification Service Extension**.

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Ensure that **Embed In Application** is set to embed the extension in your application.

### Step 2: Setting up the notification service extension

A notification service extension is its own binary that is bundled with your app. It must be set up in the [Apple Developer Portal](https://developer.apple.com) with its own app ID and provisioning profile.

The notification service extension's bundle ID must be distinct from your main app target's bundle ID. For example, if your app's bundle ID is `com.company.appname`, you can use `com.company.appname.AppNameServiceExtension` for your service extension.

### Step 3: Integrating rich push notifications

For a step-by-step guide on integrating rich push notifications with `BrazeNotificationService`, refer to our [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

To see a sample, refer to the usage in [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) of our Examples app.

#### Adding the rich push framework to your app

{% tabs local %}
{% tab Swift Package Manager %}

After following the [Swift Package Manager integration guide]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), add `BrazeNotificationService` to your `Notification Service Extension` by doing the following:

1. In Xcode, under frameworks and libraries, select the <i class="fas fa-plus"></i> add icon to add a framework. <br><br>![The plus icon is located under frameworks and libraries in Xcode.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. Select the "BrazeNotificationService" framework. <br><br>![The "BrazeNotificationService framework can be selected in the modal that opens.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

Add the following to your Podfile:

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
For instructions to implement Push Stories, see the [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

After updating the Podfile, navigate to the directory of your Xcode app project within your terminal and run `pod install`.

{% endtab %}

{% tab Manual %}

To add `BrazeNotificationService.xcframework` to your `Notification Service Extension`, see [Manual integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### Using your own UNNotificationServiceExtension

If you need to use your own UNNotificationServiceExtension, you can instead call [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) in your `didReceive` method.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### Step 4: Creating a rich notification in your dashboard

Your Marketing team can also create rich notifications from the dashboard. Create a push notification through the push composer and simply attach an image or GIF, or provide a URL that hosts an image, GIF, or video. Note that assets are downloaded on the receipt of push notifications, so you should plan for large, synchronous spikes in requests if you are hosting your content.
