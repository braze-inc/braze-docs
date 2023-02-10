---
nav_title: Setting a Delegate
article_title: Setting an In-App Message Delegate for iOS
platform: Swift
page_order: 2
description: "This reference article covers setting an in-app messaging delegate for your iOS application."
channel:
  - in-app messages

---

# Setting a delegate

If you are using the default `BrazeInAppMessageUI` implementation as your `inAppMessagePresenter`, you can further customize your in-app message display and delivery in code by setting our optional delegate.

## In-app message delegate

The [`BrazeInAppMessageUIDelegate`][34] delegate can be used to receive triggered in-app message payloads for further processing, receive display lifecycle events, and control display timing. 

Set your `BrazeInAppMessageUIDelegate` delegate object on the Braze instance by following this sample code:

{% tabs %}
{% tab swift %}

First, implement the `BrazeInAppMessageUIDelegate` protocol and any corresponding methods you wish. In our example below, we are implementing this protocol in our application's `AppDelegate` class.

```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```

Then assign the `delegate` object on the `BrazeInAppMessageUI` instance before assigning this in-app message UI as your `inAppMessagePresenter`.

```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```

{% endtab %}
{% tab OBJECTIVE-C %}

First, implement the `BrazeInAppMessageUIDelegate` protocol and any corresponding methods you wish. In our example below, we are implementing this protocol in our application's `AppDelegate` class.

```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```

Then assign the `delegate` object on the `BrazeInAppMessageUI` instance before assigning this in-app message UI as your `inAppMessagePresenter`.

```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

Not all delegate methods may not be available in Objective-C due to the incompatibility of their parameters with the language runtime.

{% endtab %}
{% endtabs %}

Note that if you do not include the `BrazeUI` library in your project, this delegate protocol is unavailable.

## Step-by-step guide

For a step-by-step implementation of the in-app message UI delegate, refer to this [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

## Implementation samples

See `InAppMessageUI` in our Examples folder for a sample in [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) and [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)

[34]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate
