---
nav_title: Customizing orientation
article_title: Customizing In-App Message Orientation for iOS
platform: iOS
page_order: 3
description: "This reference article covers how to set in-app message orientation for your iOS application."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Customizing orientation

## Setting orientation for all in-app messages

To set a fixed orientation for all in-app messages, you can set the `supportedOrientationMask` property on `ABKInAppMessageUIController`. Add the following code after your app's call to `startWithApiKey:inApplication:withLaunchOptions:`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set fixed in-app message orientation to portrait.
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
// Use .landscape to display in-app messages in landscape
if let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController as? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

Following this, all in-app messages will be displayed in the supported orientation, regardless of device orientation. Note that the device orientation must also be supported by the in-app message's `orientation` property for the message to display.

## Setting orientation per in-app message

You may alternatively set orientation on a per-message basis. To do this, set an [in-app message delegate]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates/). Then, in your `beforeInAppMessageDisplayed:` delegate method, set the `orientation` property on the `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift    
  // Set inAppMessage orientation to portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Set inAppMessage orientation to landscape
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

In-app messages will not display if the device orientation does not match the `orientation` property on the in-app message.

{% alert note %}
For iPads, in-app messages will appear in the user's preferred orientation style regardless of actual screen orientation.
{% endalert %}

## Method declarations

For additional information, see the following header file:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

