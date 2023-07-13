---
nav_title: In-App Messages
article_title: In-App Messages for React Native
platform: React Native
page_order: 4
page_type: reference
description: "This article covers in-app messages for iOS and Android apps using React Native, including customizing and logging analytics."
channel: in-app messages

---

# In-app message integration

> Native in-app messages display automatically on Android and iOS when using React Native. This article covers customizing and logging analytics for your in-app messages for apps using React Native.

## Accessing in-app message data

If you want to access the in-app message data in the JavaScript layer, call the `Braze.subscribeToInAppMessage` method to have the SDKs to publish an `inAppMessageReceived` event when an in-app message is triggered. You can pass a callback to this method to execute your own code when the in-app message is triggered and received by the listener.

This method additionally takes in a parameter that tells the Braze SDK whether or not to use the built-in Braze UI to display in-app messages. If you prefer to use a custom UI, you can pass `false` to this method and use the in-app message data to construct your own message in Javascript.

{% alert note %}
`Braze.subscribeToInAppMessage` is provided as a JavaScript interface method for situations where you may want to customize the default behavior further. It is recommended to use this method if you wish to disable the default UI while still receiving in-app message events from Braze, or in cases where you may not have access to customize the native iOS or Android code, such as in the Braze Expo Plugin.

In all other cases, calling `Braze.addListener` should be sufficient.
{% endalert %}

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});

// Option 2: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});
```

## Advanced customization

If you want to include more advanced logic to determine whether or not to show an in-app message using the built-in UI, you should implement in-app messages through the native layer.

{% alert warning %}
Since this is an advanced customization option, note that overriding the default Braze implementation will also nullify the logic to emit in-app message events to your JavaScript listeners. If you wish to still use `Braze.subscribeToInAppMessage` or `Braze.addListener` as described in [Accessing in-app message data](#accessing-in-app-message-data), you will need to handle publishing the events yourself.
{% endalert %}

{% tabs %}
{% tab Android %}

Implement the `IInAppMessageManagerListener` as described in our Android article on [Custom Manager Listener]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener). In your `beforeInAppMessageDisplayed` implementation, you can access the `inAppMessage` data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value.

For more on these values, see our [Android documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/).

```java
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Note: return InAppMessageOperation.DISCARD if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab iOS %}
### Overriding the default UI delegate

By default, [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) is created and assigned when you initialize the `braze` instance. `BrazeInAppMessageUI` is an implementation of the [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) protocol and comes with a `delegate` property that can be used to customize the handling of in-app messages that have been received.

1. Implement the `BrazeInAppMessageUIDelegate` delegate as described in [our iOS article here](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. In the `inAppMessage(_:displayChoiceForMessage:)` delegate method, you can access the `inAppMessage` data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value.

For more details on these values, see our [iOS documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert the message to a JavaScript representation.
  NSData *inAppMessageData = [message json];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };

  // Send to JavaScript.
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```
{% endsubtab %}
{% endsubtabs %}

To use this delegate, assign it to `brazeInAppMessagePresenter.delegate` after initializing the `braze` instance. (Note: BrazeUI can only be imported in Objective-C or Swift. If you are using Objective-C++, you will need to handle this in a separate file.)

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

### Overriding the default native UI

If you wish to fully customize the presentation of your in-app messages at the native iOS layer, conform to the [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) protocol and assign your custom presenter following the sample below:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Analytics

To log analytics using your `BrazeInAppMessage`, pass the instance into the desired analytics function:
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (along with the button index)

For example:
```js
// Log a click
Braze.logInAppMessageClicked(inAppMessage);
// Log an impression
Braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
Braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Test displaying a sample in-app message

Follow these steps to test a sample in-app message.

1. Set an active user in the React application by calling `Braze.changeUserId('your-user-id')` method.
2. Head to **Campaigns** and follow [this guide][5] to create a new in-app message campaign.
3. Compose your test in-app messaging campaign and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**. You should be able to launch an in-app message on your device shortly.

![A Braze in-app message campaign showing you can add your own user ID as a test recipient to test your in-app message.][6]

A sample implementation can be found in BrazeProject, within the [React Native SDK][7]. Additional Android and iOS implementation samples can be found in the [Android][8] and [iOS][9] SDK.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#step-1-implement-an-in-app-message-manager-listener
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[6]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
[7]: https://github.com/braze-inc/braze-react-native-sdk
[8]: https://github.com/braze-inc/braze-android-sdk
[9]: https://github.com/braze-inc/braze-swift-sdk
