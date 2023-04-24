---
nav_title: Example - App Store Review Prompt
article_title: Example - App Store Review Prompt
platform: Swift
page_order: 8
description: "This reference article provides an example of a custom in-app message to prompt users to provide review for your app."
channel:
  - in-app messages

---

# Example - App Store review prompt

{% alert note %}
Because this example prompt overrides Braze's default behavior, Braze cannot automatically track impressions if it is implemented. You must log your own [analytics]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/#logging-impressions-and-clicks).
{% endalert %}

Creating a campaign to ask users for an App Store review is a popular usage of in-app messages. This example walks you through creating a custom in-app message that prompts users to review your app.

## Step 1: Set the in-app message delegate
First, set the [`BrazeInAppMessageUIDelegate`][1] in your app. 

## Step 2: Disable the default App Store review message
Next, implement the `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) to disable the default App Store review message.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

## Step 3: Create a deep link
In your deep link handling code, add the following code to process the `{YOUR-APP-SCHEME}:app-store-review` deep link. Note that you will need to import `StoreKit` to use `SKStoreReviewController`:

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

## Step 4: Set custom on-click behavior

Next, create an in-app messaging campaign with the following:

- The key-value pair `"AppStore Review" : "true"`
- The on-click behavior set to "Deep Link Into App", using the deep link `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple limits App Store review prompts to a maximum of three times per year for each user, so your campaign should be [rate-limited]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) to three times per year per user.<br><br>Users may turn off App Store review prompts. As a result, your custom review prompt should not promise that a native App Store review prompt will appear or directly ask for a review.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/
