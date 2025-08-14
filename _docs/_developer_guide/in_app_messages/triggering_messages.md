---
nav_title: Triggering Messages
article_title: Triggering in-app messages through the Braze SDK
page_order: 0.2
description: "Learn how to trigger in-app messages through the Braze SDK."
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# Triggering in-app messages

> Learn how to trigger in-app messages through the Braze SDK.

## Message triggers and delivery

In-app messages are triggered when the SDK logs one of the following custom event types: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase`,and `Custom Event` (the last two containing robust property filters).

At the start of a user's session, Braze will deliver all eligible in-app messages to their device, while simultaneously prefetching assets to minimize display latency. If the trigger event has more than one eligible in-app message, only the message with the highest priority will be delivered. For more information, see [Session Lifecycle]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

{% alert note %}
In-app messages can't be triggered through the API or by API events&#8212;only custom events logged by the SDK. To learn more about logging, see [Logging Custom Events]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

## Key-value pairs

When you create a campaign in Braze, you can set key-value pairs as `extras`, which the the in-app messaging object can use to send data to your app.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
For more information, refer to the [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab swift %}
The following example uses custom logic to set the presentation of an in-app message based on it's key-value pairs in `extras`. For a full customization example, check out [our sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}
{% endtabs %}

## Disabling automatic triggers

By default, in-app messages are triggered automatically. To disable this:

{% tabs %}
{% tab android %}
1. Verify you're using the automatic integration initializer, which is enabled by default in versions `2.2.0` and later.
2. Set the in-app message operation default to `DISCARD` by adding the following line to your `braze.xml` file.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```

For more advanced control over message timing, including deferring and restoring triggered messages, see our [Tutorial: Deferring and restoring triggered messages]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab swift %}
1. Implement the `BrazeInAppMessageUIDelegate` delegate in your app. For a full walkthrough, see [Tutorial: In-App Message UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Update your `inAppMessage(_:displayChoiceForMessage:)` delegate method to return `.discard`.

For more advanced control over message timing, including deferring and restoring triggered messages, see our [Tutorial: Deferring and restoring triggered messages]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab web %}
Remove the call to `braze.automaticallyShowInAppMessages()` within your loading snippet, then create custom logic to handle showing or not showing an in-app message.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
If you call `braze.showInAppMessage` without removing `braze.automaticallyShowInAppMessages()`, messages may display twice.
{% endalert %}

For more advanced control over message timing, including deferring and restoring triggered messages, see our [Tutorial: Deferring and restoring triggered messages]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
For Android, deselect **Automatically Display In-App Messages** in the Braze configuration editor. Alternatively, you can set `com_braze_inapp_show_inapp_messages_automatically` to `false` in your Unity project's `braze.xml`.

The initial in-app message display operation can be set in Braze config using the "In App Message Manager Initial Display Operation".
{% endsubtab %}

{% subtab iOS %}
For iOS,  set game object listeners in the Braze configuration editor and ensure **Braze Displays In-App Messages** is not selected.

The initial in-app message display operation can be set in Braze config using the "In App Message Manager Initial Display Operation".
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Overriding the default rate limit

By default, you can send an in-app message once every 30 seconds. To override this, add the following property to your configuration file before the Braze instance is initialized. This value will be used as the new rate limit in seconds.

{% tabs %}
{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}
{% endtabs %}

## Manually triggering messages

By default, in-app messages are automatically triggered when the SDK logs a custom event. However, in addition to this, you can manually trigger messages using the following methods.

### Using a server-side event

{% tabs %}
{% tab android %}
To trigger an in-app message using a server-sent event, send a silent push notification to the device, which allows a custom push callback to log an SDK-based event. This event will then trigger the user-facing in-app message.

#### Step 1: Create a push callback to receive the silent push

Register your custom push callback to listen for a specific silent push notification. For more information, refer to [Standard Android push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback).

Two events will be logged for the in-app message to be delivered, one by the server and one from within your custom push callback. To make sure the same event is not duplicated, the event logged from within your push callback should follow a generic naming convention, for example, "in-app message trigger event," and not the same name as the server sent event. If this is not done, segmentation and user data may be affected by duplicate events being logged for a single user action.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### Step 2: Create a push campaign

Create a [silent push campaign]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) triggered via the server sent event.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

The push campaign must include key-value pair extras that indicate that this push campaign is sent to log an SDK custom event. This event will be used to trigger the in-app message.

![Two sets of key-value pairs: IS_SERVER_EVENT set to "true", and CAMPAIGN_NAME set to "example campaign name".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

The earlier push callback sample code recognizes the key-value pairs and logs the appropriate SDK custom event.

Should you want to include any event properties to attach to your "in-app message trigger" event, you can achieve this by passing these in the key-value pairs of the push payload. In this example, the campaign name of the subsequent in-app message has been included. Your custom push callback can then pass the value as the parameter of the event property when logging the custom event.

#### Step 3: Create an in-app message campaign

Create your user-visible in-app message campaign in the Braze dashboard. This campaign should have an action-based delivery and be triggered from the custom event logged from within your custom push callback.

In the following example, the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![An action-based delivery campaign where an in-app message will trigger when "campaign_name" equals "IAM campaign name example."]({% image_buster /assets/img_archive/iam_event_trigger.png %})

If a server-sent event is logged while the app is not in the foreground, the event will log, but the in-app message will not be displayed. Should you want the event to be delayed until the application is in the foreground, a check must be included in your custom push receiver to dismiss or delay the event until the app has entered the foreground.
{% endtab %}

{% tab swift %}
#### Step 1: Handle silent push and key-value pairs

Implement the following function and call it within the [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/):

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

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
{% endtab %}

{% tab web %}
At this time, the Web Braze SDK does not support manually triggering messages using server-side events.
{% endtab %}
{% endtabs %}

### Displaying a pre-defined message

To manually display a pre-defined in-app message, use the following method:

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}

{% tab web %}
```javascript
braze.requestInAppMessageDisplay();
```
{% endtab %}
{% endtabs %}

### Displaying a message in real-time 

You can also create and display local in-app messages in real-time, using the same customization options available on the dashboard. To do so:

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Do not display in-app messages when the soft keyboard is displayed on the screen as rendering is undefined in this circumstance.
{% endalert %}
{% endtab %}

{% tab swift %}
Manually call the [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) method on your `inAppMessagePresenter`. For example:

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Creating your own in-app message, you opt out of any analytics tracking and will have to manually handle click and impression logging using your `message.context`.
{% endalert %}
{% endtab %}

{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab unity %}
To display the next message in the stack, use the `DisplayNextInAppMessage()` method. Messages will be saved to this stack if `DISPLAY_LATER` or `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` is chosen as the in-app message display action.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Exit-intent messages for Web

Exit-intent messages are non-disruptive in-app messages used to communicate important information to visitors before they leave your web site.

To set up triggers for these message types in the Web SDK, implement an exit-intent library in your website (such as [ouibounce's open-source library](https://github.com/carlsednaoui/ouibounce)), then use the following code to log `'exit intent'` as a custom event in Braze. Now your future in-app message campaigns can use this message type as a custom event trigger.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
