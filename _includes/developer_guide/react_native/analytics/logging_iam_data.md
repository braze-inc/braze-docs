{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Methods for logging

You can use these methods by passing your `BrazeInAppMessage` instance to log analytics and perform actions:

| Method                                                    | Description                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Logs a click for the provided in-app message data.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Logs an impression for the provided in-app message data.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Logs a button click for the provided in-app message data and button ID.               |
| `hideCurrentInAppMessage()`                               | Dismisses the currently displayed in-app message.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Performs the action for an in-app message.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Performs the action for an in-app message button.                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Handling message data

In most cases, you can use the `Braze.addListener` method to register event listeners to handle data coming from in-app messages. 

Additionally, you can access the in-app message data in the JavaScript layer by calling the `Braze.subscribeToInAppMessage` method to have the SDKs publish an `inAppMessageReceived` event when an in-app message is triggered. Pass a callback to this method to execute your own code when the in-app message is triggered and received by the listener.

To customize how message data is handled, refer to the following implementation examples:

{% tabs local %}
{% tab basic %}
To enhance the default behavior, or if you don't have access to customize the native iOS or Android code, we recommend that you disable the default UI while still receiving in-app message events from Braze. To disable the default UI, pass `false` to the `Braze.subscribeToInAppMessage` method and use the in-app message data to construct your own message in JavaScript. Note that you will need to manually log analytics on your messages if you choose to disable the default UI.

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});
```
{% endtab %}

{% tab advanced %}
To include more advanced logic to determine whether or not to show an in-app message using the built-in UI, implement in-app messages through the native layer.

{% alert warning %}
Since this is an advanced customization option, note that overriding the default Braze implementation will also nullify the logic to emit in-app message events to your JavaScript listeners. If you wish to still use `Braze.subscribeToInAppMessage` or `Braze.addListener` as described in [Accessing in-app message data](#accessing-in-app-message-data), you will need to handle publishing the events yourself.
{% endalert %}

{% subtabs %}
{% subtab Android %}
Implement the `IInAppMessageManagerListener` as described in our Android article on [Custom Manager Listener]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). In your `beforeInAppMessageDisplayed` implementation, you can access the `inAppMessage` data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value.

For more on these values, see our [Android documentation]({{site.baseurl}}/developer_guide/in_app_messages/).

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
{% endsubtab %}
{% subtab iOS %}
### Overriding the default UI delegate

By default, [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) is created and assigned when you initialize the `braze` instance. `BrazeInAppMessageUI` is an implementation of the [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) protocol and comes with a `delegate` property that can be used to customize the handling of in-app messages that have been received.

1. Implement the `BrazeInAppMessageUIDelegate` delegate as described in [our iOS article here](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. In the `inAppMessage(_:displayChoiceForMessage:)` delegate method, you can access the `inAppMessage` data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value.

For more details on these values, see our [iOS documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

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

To use this delegate, assign it to `brazeInAppMessagePresenter.delegate` after initializing the `braze` instance. 

{% alert note %}
`BrazeUI` can only be imported in Objective-C or Swift. If you are using Objective-C++, you will need to handle this in a separate file.
{% endalert %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```

### Overriding the default native UI

If you wish to fully customize the presentation of your in-app messages at the native iOS layer, conform to the [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) protocol and assign your custom presenter following the sample below:

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
