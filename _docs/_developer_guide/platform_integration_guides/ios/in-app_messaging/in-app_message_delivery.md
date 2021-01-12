---
nav_title: In-App Message Delivery
platform: iOS
page_order: 3

---

# In-App Message Delivery

## Trigger Types

Our in-app message product allows you to trigger in-app message display as a result of several different event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  Furthermore, `Specific Purchase` and `Custom Event` triggers can contain robust property filters.

{% alert important %}
Triggered in-app messages only work with custom events logged through the SDK and not through the REST APIs. If you're working with iOS, check out how to log custom events [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

## Delivery Semantics

All in-app messages that a user is eligible for are delivered to the user's device on session start. For more information about the SDK's session start semantics, see our [session lifecycle documentation][45]. Upon delivery, the SDK will pre-fetch assets so that they are available immediately at trigger time, minimizing display latency.

When a trigger event has more than one eligible in-app message associated with it, only the in-app message with the highest priority will be delivered.

For in-app messages that display immediately on delivery, (session start, push click) there can be some latency due to assets not being prefetched.

## Minimum Time Interval Between Triggers

By default, we rate limit in-app messages to once every 30 seconds to ensure a quality user experience.

You can override this value via the `ABKMinimumTriggerTimeIntervalKey` inside the `appboyOptions` parameter passed to `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Set the `ABKMinimumTriggerTimeIntervalKey` to the integer value you want as your minimum time in seconds between in-app messages:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

An example of overriding the default trigger interval can be found in our sample application's [`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) file.

## Local In-App Message Delivery

### The In-App Message Stack

#### Showing In-App Messages

When a user is eligible to receive an in-app message, the `ABKInAppMessageController` will be offered the latest in-app message off the in-app message stack. The stack only persists stored in-app messages in memory and is cleared up between app launches from suspended mode.

{% alert important %}
Do not display in-app messages when the keyboard is displayed on screen, as rendering is undefined in this circumstance.
{% endalert %}

#### Adding In-App Messages to the Stack

Users are eligible to receive an in-app message in the following situations:

- An in-app message trigger event is fired
- Session start event
- The app is opened from a push notification

Triggered in-app messages are placed on top of the stack when their trigger event is fired. If multiple in-app messages are in the stack and waiting to be displayed, Braze will display the most recently received in-app message first (last in, first out).

#### Returning In-App Messages to the Stack

A triggered in-app message can be returned back to the stack in the following situations:

- The in-app message is triggered when the app is in the background
- Another in-app message is currently visible
- The deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI delegate method][38] has **NOT** been implemented, and the keyboard is currently being displayed
- The `beforeInAppMessageDisplayed:` [delegate method][30] or the deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI delegate method][38] returned `ABKDisplayInAppMessageLater`

#### Discarding In-App Messages

A triggered in-app message will be discarded in the following situations:

- The `beforeInAppMessageDisplayed:` [delegate method][30] or the deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI delegate method][38] returned `ABKDiscardInAppMessage`
- The asset (image or zip file) of the in-app message failed to download
- The in-app message is ready to be displayed but past the timeout duration
- The device orientation doesn't match the triggered in-app message's orientation
- The in-app message is a full in-app message but has no image
- The in-app message is an image-only modal in-app message but has no image

#### Manually Queue In-App Message Display

If you wish to display an in-app message at other times within your app, you may manually display the top-most in-app message on the stack by calling the following method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessageWithDelegate:YOUR_IN_APP_MESSAGE_DELEGATE]
// YOUR_IN_APP_MESSAGE_DELEGATE should be replaced with your in-app message controller delegate, if you have implemented one.
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage(with: YOUR_IN_APP_MESSAGE_DELEGATE?)
// YOUR_IN_APP_MESSAGE_DELEGATE should be replaced with your in-app message controller delegate, if you have implemented one.
```

{% endtab %}
{% endtabs %}

### Real Time In-App Message Creation & Display

In-app messages can also be locally created within the app and displayed via Braze. This is particularly useful for displaying messages that you wish to trigger within the app in real-time. Braze does not support analytics on in-app messages created locally.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}

[1]: #customize-inAppMessage-dashboard
[2]: #customize-inAppMessage-code
[3]: #set-delegate
[4]: #customize-inAppMessage-display
[5]: #before-display
[6]: #manual-cue
[7]: #situational-display
[8]: #inAppMessage-click
[9]: #custom-view
[10]: #custom-inAppMessage
[11]: #custom-complete
[12]: #method-declarations
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessage.h
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageController.h
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageControllerDelegate.h
[19]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/CustomInAppMessageViewController.m
[23]: #setting-delegates
[25]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#2121
[26]: http://fortawesome.github.io/Font-Awesome/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-messages-triggered
[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}
[30]: #in-app-message-controller-delegate
[31]: #customizing-appboy-on-startup
[32]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageControllerDelegate.h
[33]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[37]: https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers
[38]: #in-app-mssage-ui-delegate
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[40]: {% image_buster /assets/img_archive/iosServerSentPush.png %}
[41]: {% image_buster /assets/img_archive/iOSServerPush.png %}
[42]: {% image_buster /assets/img_archive/iosIAMeventTrigger.png %}
[44]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events
[45]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
