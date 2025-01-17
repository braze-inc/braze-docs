---
nav_title: Message Delivery
article_title: In-App Message Delivery for the Braze Swift SDK
platform: Swift
page_order: 2
description: "This article covers iOS in-app message delivery, listing different trigger types, delivery semantics, and event triggering steps for the Swift SDK."
channel:
  - in-app messages

---

# In-app message delivery

> This reference article provides an overview of iOS in-app message delivery, listing different trigger types, delivery semantics, and event triggering steps.

## Trigger types

In-app messages are triggered by events logged by the SDK. You can trigger an in-app message off of the following event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, and `Push Click`. Furthermore, the `Specific Purchase` and `Custom Event` triggers contain robust property filters.

{% alert note %}
Triggered in-app messages only work with custom events logged through the Braze SDK. In-app messages can't be triggered through the API or by API events (such as purchase events). If you're working with iOS, visit our [tracking custom events]({{site.baseurl}}/developer_guide/platforms/swift/analytics/tracking_custom_events/) article to learn more. 
{% endalert %}

## Enabling in-app messages

To allow Braze to display in-app messages, create an implementation of the `BrazeInAppMessagePresenter` protocol and assign it to the optional `inAppMessagePresenter` on your Braze instance. You can also use the default Braze UI presenter by instantiating a `BrazeInAppMessageUI` object.

Note that you will need to import the `BrazeUI` library to access the `BrazeInAppMessageUI` class.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

## Delivery semantics

All in-app messages that a user is eligible for are delivered to the user's device on session start. Upon delivery, the SDK will prefetch assets to be available immediately at trigger time, minimizing display latency.

When a trigger event has more than one eligible in-app message associated with it, only the in-app message with the highest priority will be delivered.

There can be some latency for in-app messages that display immediately on delivery (session start, push click) due to assets not being prefetched. For more information about the SDK's session start semantics, read about our [session lifecycle]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

## Minimum time interval between triggers

By default, we rate limit in-app messages to once every 30 seconds to faciliate a quality user experience.

You can override this value by setting the `triggerMinimumTimeInterval` property in your Braze configuration. Be sure to configure this value before initializing your Braze instance. Set the `triggerMinimumTimeInterval` to the integer value you want as your minimum time in seconds between in-app messages:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## Failing to find a matching trigger

When Braze fails to find a matching trigger for a particular event, it will call [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/). Implement this method in your class adopting `BrazeDelegate` to handle this scenario. 

## The in-app message stack

### Adding in-app messages to the stack

Users are eligible to receive an in-app message in the following situations:

- An in-app message trigger event is fired
- A session is started
- The app is opened from a push notification

When an in-app message's trigger event is fired, it is placed on a "stack." If multiple in-app messages are in the stack and waiting to be displayed, Braze will display the most recently received in-app message first (last in, first out).

When a user is eligible to receive an in-app message, the `BrazeInAppMessagePresenter` will request the latest in-app message off the in-app message stack. The stack only persists stored in-app messages in memory and is cleared up between app launches from suspended mode.

### Returning in-app messages to the stack

A triggered in-app message can be returned to the stack in the following situations:

- The in-app message is triggered when the app is in the background.
- Another in-app message is currently visible.
- The `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) returned `.reenqueue`.

The triggered in-app message will be placed on top of the stack for later display when a user is eligible to receive an in-app message.

### Discarding in-app messages

A triggered in-app message will be discarded in the following situations:

- The `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) returned `.discard`.
- The asset (image or ZIP file) of the in-app message failed to download.
- The in-app message is ready to be displayed but passed the timeout duration.
- The device orientation doesn't match the triggered in-app message's orientation.

The in-app message will be removed from the stack. After being discarded, the in-app message can be triggered later on by another instance of the trigger event.

## Real-time in-app message creation and display

If you wish to display an in-app message at other times within your app, you may manually call the [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) method on your `inAppMessagePresenter`. In-app messages can be locally created within the app and displayed via Braze. This is particularly useful for displaying messages you wish to trigger within the app in real-time.

Note that by creating your own in-app message, you opt out of any analytics tracking and will have to manually handle click and impression logging using your `message.context`.

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

## Key-value pair extras

`Braze.InAppMessage` objects may carry key-value pairs as `extras`. These are specified on the dashboard when creating a campaign. Key-value pairs can be used to send data down with an in-app message for further handling by your app.

For example, consider a case where we want to customize the presentation of an in-app message based on the contents of its extras. We could access the key-value pairs in its `extras` property and define custom logic to execute around it:

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

For a full implementation, you may refer to the in-app message customization samples in our [Example app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

