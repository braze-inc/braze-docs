---
nav_title: Set delegates
article_title: Set In-App Message Delegates for iOS
platform: iOS
page_order: 2
description: "This reference article covers setting in-app messaging delegates for your iOS application."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Set delegates

In-app message display and delivery customizations can be accomplished in code by setting our optional delegates.

## In-app message delegate

The [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) delegate can be used to receive triggered in-app message payloads for further processing, receive display lifecycle events, and control display timing. 

Set your `ABKInAppMessageUIDelegate` delegate object on the Braze instance by calling:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

Check out our in-app message [sample app](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) for an example implementation. Note that if you are not including the Braze UI library in your project (uncommon), this delegate is unavailable.

## Core in-app message delegate

If you are not including the Braze UI library in your project and want to receive triggered in-app message payloads for further processing or custom display in your app, implement the [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates/) protocol.

Set your `ABKInAppMessageControllerDelegate` delegate object on the Braze instance by calling:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

You can alternatively set your core in-app message delegate at initialization time via `appboyOptions` using the key `ABKInAppMessageControllerDelegateKey`:
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## Method declarations

For additional information, see the following header files:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Implementation samples

See [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) in the in-app message sample app.


