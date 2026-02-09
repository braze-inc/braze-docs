---
nav_title: Custom view controller
article_title: In-App Message in a Custom View Controller for iOS
platform: iOS
page_order: 7
description: "This reference article covers how to leverage a custom in-app messaging view controller for your iOS application."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Display in-app messages in a custom view controller

In-app messages can also be displayed within a custom view controller, which you pass to Braze. Braze will animate the customized in-app message in and out and handle analytics of the in-app message. The view controller must meet the following requirements:

- It must be a subclass or an instance of `ABKInAppMessageViewController`.
- The view of the returned view controller should be an instance of `ABKInAppMessageView` or its subclass.

The following UI delegate method is called every time an in-app message is offered to `ABKInAppMessageViewController` to allow the app to pass a custom view controller to Braze for in-app message display:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

Our [in-app message view controllers](https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers) are customizable. You can use subclasses or categories to customize the display or behavior of in-app messages.

## Method declarations

For additional information, see the following header files:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

## Implementation samples

See [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) and [`CustomInAppMessageViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/) in the in-app message sample app.

