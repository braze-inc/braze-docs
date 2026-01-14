{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Message triggers

### Trigger types

In-app messages are automatically triggered when the SDK logs one of the following custom event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, and `Push Click`. Note that the `Specific Purchase` and `Custom Event` triggers also contain robust property filters.

{% alert note %}
In-app messages can't be triggered through the API or by API events&#8212;only custom events logged by the SDK. To learn more about logging, see [Logging Custom Events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift).
{% endalert %}

### Delivery semantics

All eligible in-app messages are delivered to a user's device at the start of their session. When delivered, the SDK will prefetch assets, so they're available at trigger time, minimizing display latency. If the trigger event has more than one eligible in-app message, only the message with the highest priority will be delivered.

For more information about the SDK's session start semantics, see[Session Lifecycle]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift).

### Default rate limit

By default, you can send an in-app message once every 30 seconds.

To override this, add the `triggerMinimumTimeInterval` property to your Braze configuration before the Braze instance is initialized. It can be set to any positive integer and represents the minimum time interval in seconds. For example:

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

## Key-value pairs

When you create a campaign in Braze, you can set key-value pairs as `extras`, which the the in-app messaging object can use to send data to your app. For example:

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

## Disabling automatic triggers

To prevent in-app messages from automatically triggering:

1. Implement the `BrazeInAppMessageUIDelegate` delegate as described in our [iOS article here](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Update your `inAppMessage(_:displayChoiceForMessage:)` delegate method to return `.discard`.

## Manually triggering messages

### Using a server-side event

To trigger in-app messages using server-side events, send a silent push to the device to allow the device to log an SDK-based event. This SDK event can subsequently trigger the user-facing in-app message.

#### Step 1: Handle silent push and key-value pairs

Implement the following function and call it within the [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/):

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

When the silent push is received, an SDK recorded event "in-app message trigger" will be logged against the user profile. 

{% alert important %}
Due to a push message being used to record an SDK logged custom event, Braze will need to store a push token for each user to enable this solution. For iOS users, Braze will only store a token from the point that a user has been served the OS's push prompt. Before this, the user will not be reachable using push, and the preceding solution will not be possible.
{% endalert %}

#### Step 2: Create a silent push campaign

Create a [silent push campaign]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) that is triggered via the server-sent event. 

![An action-based delivery in-app message campaign that will be delivered to users whose user profiles have the custom event "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

The push campaign must include key-value pair extras, which indicate that this push campaign is sent to log an SDK custom event. This event will be used to trigger the in-app message.

![An action-based delivery in-app message campaign that has two key-value pairs. "CAMPAIGN_NAME" set as "In-app message name example", and "IS_SERVER_EVENT" set to "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

The code within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method checks for key `IS_SERVER_EVENT` and will log an SDK custom event if this is present.

You can alter either the event name or event properties by sending the desired value within the key-value pair extras of the push payload. When logging the custom event, these extras can be used as the parameter of either the event name or as an event property.

#### Step 3: Create an in-app message campaign

Create your user-visible in-app message campaign in the Braze dashboard. This campaign should have an action-based delivery and be triggered from the custom event logged from within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method.

In the following example, the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![An action-based delivery in-app message campaign that will be delivered to users who perform the custom event "In-app message trigger" where "campaign_name" equals "IAM Campaign Name Example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Note that these in-app messages will only trigger if the silent push is received while the application is in the foreground.
{% endalert %}

### Displaying a pre-defined

To manually display a pre-defined in-app message, use the following method:

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### Displaying a message in real-time

You can also display local in-app messages in real-time by manually calling the [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) method on your `inAppMessagePresenter`. For example:

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

{% alert note %}
Creating your own in-app message, you opt out of any analytics tracking and will have to manually handle click and impression logging using your `message.context`.
{% endalert %}

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
