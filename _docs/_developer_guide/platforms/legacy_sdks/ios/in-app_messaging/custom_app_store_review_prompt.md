---
nav_title: Custom app store review prompt
article_title: Custom App Store review prompt
platform: iOS
page_order: 4
description: "This reference article shows how to set up a custom iOS App Store review prompt."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Custom App Store review prompt

{% alert note %}
Once you implement this prompt, Braze stops automatically tracking impressions, and you must log your own [analytics]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks).
{% endalert %}

Creating a campaign to ask users for an App Store review is a popular usage of in-app messages.

Start by setting the [in-app message delegate](#in-app-message-controller-delegate) in your app. Next, implement the following delegate method to disable the default App Store review message:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  if (inAppMessage.extras != nil && inAppMessage.extras[@"Appstore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:inAppMessage.uri options:@{} completionHandler:nil];
    return ABKDiscardInAppMessage;
  } else {
    return ABKDisplayInAppMessageNow;
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  if inAppMessage.extras?["Appstore Review"] != nil && inAppMessage.uri != nil {
    UIApplication.shared.open(inAppMessage.uri!, options: [:], completionHandler: nil)
    return ABKInAppMessageDisplayChoice.discardInAppMessage
  } else {
    return ABKInAppMessageDisplayChoice.displayInAppMessageNow
  }
}
```

{% endtab %}
{% endtabs %}

In your deep link handling code, add the following code to process the `{YOUR-APP-SCHEME}:appstore-review` deep link. Note that you will need to import `StoreKit` to use `SKStoreReviewController`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:appstore-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:appstore-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

Next, create an in-app messaging campaign with the following:

- The key-value pair `"Appstore Review" : "true"`
- The on-click behavior set to "Deep Link Into App", using the deep link `{YOUR-APP-SCHEME}:appstore-review`.

{% endraw %}

{% alert tip %}
Apple limits App Store review prompts to a maximum of three (3) times per year for each user, so your campaign should be [rate-limited]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) to three times per year per user.<br><br>Users may turn off App Store review prompts. As a result, your custom review prompt should not promise that a native App Store review prompt will appear or directly ask for a review.
{% endalert %}

