---
nav_title: Overriding In-App Message Logic
article_title: Overriding In-App Message Display Logic for iOS
platform: Swift
page_order: 4
description: "This reference article covers the timing of in-app messaging delivery for your iOS application."
channel:
  - in-app messages

---

# Overriding in-app message display logic for iOS

You can choose to override the in-app message display behavior, customize in-app messages before Braze displays them, or opt-out of Braze's in-app message display logic and UI entirely. For example, you might want to display the in-app message from the top of the screen if the keyboard is currently being displayed, or take the in-app message data model and display the in-app message yourself.

To do this, first set the [in-app message delegate][1]. Then, add your custom display logic to your `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog).

For example, if you would like to display an in-app message from the top of the screen, you can write the following code:

{% tabs %}
{% tab swift %}

```swift
public func inAppMessage(
  _ ui: BrazeInAppMessageUI, prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.message.slideup?.slideFrom = .top
}
```

Further, if you would like to control this logic according to the keyboard display, you can use the [`KeyboardFrameNotifier`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Sources/BrazeUI/Dependencies/KeyboardFrameNotifier.swift) class as a reference. `BrazeInAppMessageUI` uses this logic internally to manage the default keyboard behavior in the Swift SDK.

{% endtab %}
{% tab OBJECTIVE-C %}

The `inAppMessage(_:prepareWith:)` method is not available in Objective-C.

{% endtab %}
{% endtabs %}

## Logging impressions and clicks

Logging in-app message impressions and clicks is not automatic when you override Braze's default display logic and create completely customized behavior. If you choose to implement your own UI using our in-app message models, you must log analytics with the following methods on the `Braze.InAppMessage` class:

{% tabs %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
message.context?.logImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
message.context?.logClick(buttonId: "button-id")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
[message.context logImpression];
// Registers that a user has clicked on an in-app message with the Braze server.
[message.context logClickWithButtonId:@"button-id"];
```

{% endtab %}
{% endtabs %}

## Examples

See `InAppMessageUI` in our Examples folder for a sample in [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) and [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/
