---
nav_title: In-App Message Delivery
article_title: In-App Message Delivery for iOS
platform: iOS
page_order: 3
description: "This article covers iOS in-app message delivery, listing different trigger types, delivery semantics, and event triggering steps."
channel:
  - in-app messages

---

# In-app message delivery

## Trigger types

Our in-app message product allows you to trigger in-app message display as a result of several different event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, and `Push Click`. Furthermore, `Specific Purchase` and `Custom Event` triggers contain robust property filters.

{% alert note %}
Triggered in-app messages only work with custom events logged through the SDK and not through the REST APIs. If you're working with iOS, visit our [tracking custom events]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) article to learn more. 
{% endalert %}

## Delivery semantics

All in-app messages that a user is eligible for are delivered to the user's device on session start. For more information about the SDK's session start semantics, read about our [session lifecycle][45]. Upon delivery, the SDK will prefetch assets to be available immediately at trigger time, minimizing display latency.

When a trigger event has more than one eligible in-app message associated with it, only the in-app message with the highest priority will be delivered.

There can be some latency for in-app messages that display immediately on delivery (session start, push click) due to assets not being prefetched.

## Minimum time interval between triggers

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

## Local in-app message delivery

### The in-app message stack

#### Showing in-app messages

When a user is eligible to receive an in-app message, the `ABKInAppMessageController` will be offered the latest in-app message off the in-app message stack. The stack only persists stored in-app messages in memory and is cleared up between app launches from suspended mode.

{% alert important %}
Do not display in-app messages when the keyboard is displayed on screen, as rendering is undefined in this circumstance.
{% endalert %}

#### Adding in-app messages to the stack

Users are eligible to receive an in-app message in the following situations:

- An in-app message trigger event is fired
- Session start event
- The app is opened from a push notification

Triggered in-app messages are placed on the stack when their trigger event is fired. If multiple in-app messages are in the stack and waiting to be displayed, Braze will display the most recently received in-app message first (last in, first out).

#### Returning in-app messages to the stack

A triggered in-app message can be returned to the stack in the following situations:

- The in-app message is triggered when the app is in the background.
- Another in-app message is currently visible.
- The deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI delegate method][38] has not been implemented, and the keyboard is currently being displayed.
- The `beforeInAppMessageDisplayed:` [delegate method][30] or the deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI delegate method][38] returned `ABKDisplayInAppMessageLater`.

#### Discarding in-app messages

A triggered in-app message will be discarded in the following situations:

- The `beforeInAppMessageDisplayed:` [delegate method][30] or the deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI delegate method][38] returned `ABKDiscardInAppMessage`.
- The asset (image or ZIP file) of the in-app message failed to download.
- The in-app message is ready to be displayed but past the timeout duration.
- The device orientation doesn't match the triggered in-app message's orientation.
- The in-app message is a full in-app message but has no image.
- The in-app message is an image-only modal in-app message but has no image.

#### Manually queue in-app message display

If you wish to display an in-app message at other times within your app, you may manually display the top-most in-app message on the stack by calling the following method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Real-time in-app message creation and display

In-app messages can also be locally created within the app and displayed via Braze. This is particularly useful for displaying messages you wish to trigger within the app in real-time. Braze does not support analytics on in-app messages created locally.

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

[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate
[45]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
