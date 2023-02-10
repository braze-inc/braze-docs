---
nav_title: Customizing Orientation
article_title: Customizing In-App Message Orientation for iOS
platform: Swift
page_order: 3
description: "This reference article covers how to set in-app message orientation for your iOS application."
channel:
  - in-app messages

---

# Customizing orientation

## Setting a preferred orientation

To define your preferred message orientation, you can set an [in-app message delegate][1]. Then, in your `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog), set the `preferredOrientation` property on the `PresentationContext`:

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

The `inAppMessage(_:prepareWith:)` method is not available in Objective-C.

{% endtab %}
{% endtabs %}

Following this, all in-app messages will be displayed in the supported orientation, regardless of device orientation. Note that the device orientation must also be supported by the in-app message's `orientation` property for the message to display.

## Modifying message orientations

You may alternatively set the orientation on a per-message basis. To do this, set the `orientation` property on a given `Braze.InAppMessage`:

{% tabs %}
{% tab swift %}

```swift    
// Set inAppMessage orientation to portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endtab %}
{% endtabs %}

In-app messages will not display if the device orientation does not match the `orientation` property on the in-app message.

{% alert note %}
For iPads, in-app messages will appear in the user's preferred orientation style regardless of actual screen orientation.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/