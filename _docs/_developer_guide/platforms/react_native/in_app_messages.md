---
nav_title: In-App Messages
article_title: In-App Messages for React Native
platform: React Native
page_order: 4
page_type: reference
description: "This article covers in-app messages for iOS and Android apps using React Native, including customizing and logging analytics."
channel: in-app messages

---

# In-app messages

> Native in-app messages display automatically on Android and iOS when using React Native. This article covers customizing and logging analytics for your in-app messages for apps using React Native.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Accessing message data

In most cases, you can use the `Braze.addListener` method to register event listeners to handle data coming from in-app messages. 

Additionally, you can access the in-app message data in the JavaScript layer by calling the `Braze.subscribeToInAppMessage` method to have the SDKs publish an `inAppMessageReceived` event when an in-app message is triggered. Pass a callback to this method to execute your own code when the in-app message is triggered and received by the listener.

### Basic customization

To customize the default behavior further, or if you don't have access to customize the native iOS or Android code, we recommend that you disable the default UI while still receiving in-app message events from Braze. To disable the default UI, pass `false` to the `Braze.subscribeToInAppMessage` method and use the in-app message data to construct your own message in JavaScript. Note that you will need to [manually log analytics](#analytics) on your messages if you choose to disable the default UI.

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

### Advanced customization

To include more advanced logic to determine whether or not to show an in-app message using the built-in UI, implement in-app messages through the native layer.

{% alert warning %}
Since this is an advanced customization option, note that overriding the default Braze implementation will also nullify the logic to emit in-app message events to your JavaScript listeners. If you wish to still use `Braze.subscribeToInAppMessage` or `Braze.addListener` as described in [Accessing in-app message data](#accessing-in-app-message-data), you will need to handle publishing the events yourself.
{% endalert %}

{% tabs %}
{% tab Android %}

Implement the `IInAppMessageManagerListener` as described in our Android article on [Custom Manager Listener]({{site.baseurl}}/developer_guide/platforms/android/in_app_messages/customization/listeners/). In your `beforeInAppMessageDisplayed` implementation, you can access the `inAppMessage` data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value.

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
#### Overriding the default UI delegate

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

To use this delegate, assign it to `brazeInAppMessagePresenter.delegate` after initializing the `braze` instance. 

{% alert note %}
`BrazeUI` can only be imported in Objective-C or Swift. If you are using Objective-C++, you will need to handle this in a separate file.
{% endalert %}

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

#### Overriding the default native UI

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

### Analytics and action methods

You can use these methods by passing your `BrazeInAppMessage` instance to log analytics and perform actions:

| Method                                                    | Description                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Logs a click for the provided in-app message data.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Logs an impression for the provided in-app message data.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Logs a button click for the provided in-app message data and button ID.               |
| `hideCurrentInAppMessage()`                               | Dismisses the currently displayed in-app message.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Performs the action for an in-app message.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Performs the action for an in-app message button.                                     |

## Testing an in-app message

To test a sample in-app message:

1. Set an active user in the React application by calling `Braze.changeUserId('your-user-id')` method.
2. Head to **Campaigns** and follow [this guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) to create a new in-app message campaign.
3. Compose your test in-app messaging campaign and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**. You should be able to launch an in-app message on your device shortly.

![A Braze in-app message campaign showing you can add your own user ID as a test recipient to test your in-app message.]({% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test")

A sample implementation can be found in BrazeProject, within the [React Native SDK](https://github.com/braze-inc/braze-react-native-sdk). Additional Android and iOS implementation samples can be found in the [Android](https://github.com/braze-inc/braze-android-sdk) and [iOS](https://github.com/braze-inc/braze-swift-sdk) SDK.

## In-app message data model

The in-app message model is available in the React Native SDK. Braze has four in-app message types that share the same data model: **slideup**, **modal**, **full** and **HTML full**.

### Message model

The in-app message model provides the base for all in-app messages.

|Property          | Description                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | The message JSON representation.                                                                                |
|`message`         | The message text.                                                                                                      |
|`header`          | The message header.                                                                                                    |
|`uri`             | The URI associated with the button click action.                                                                       |
|`imageUrl`        | The message image URL.                                                                                                 |
|`zippedAssetsUrl` | The zipped assets prepared to display HTML content.                                                                    |
|`useWebView`      | Indicates whether the button click action should redirect using a web view.                                            |
|`duration`        | The message display duration.                                                                                          |
|`clickAction`     | The button click action type. The three types are: `NEWS_FEED`, `URI`, and `NONE`.                                     |
|`dismissType`     | The message close type. The two types are: `SWIPE` and `AUTO_DISMISS`.                                                 |
|`messageType`     | The in-app message type supported by the SDK. The four types are: `SLIDEUP`, `MODAL`, `FULL` and `HTML_FULL`.          |
|`extras`          | The message extras dictionary. Default value: `[:]`.                                                                   |
|`buttons`         | The list of buttons on the in-app message.                                                                             |
|`toString()`      | The message as a String representation.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the in-app message model, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage) documentation.

### Button model

Buttons can be added to in-app messages to perform actions and log analytics. The button model provides the base for all in-app message buttons.

|Property          | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | The text on the button.                                                                                                     |
|`uri`             | The URI associated with the button click action.                                                                            |
|`useWebView`      | Indicates whether the button click action should redirect using a web view.                                                 |
|`clickAction`     | The type of click action processed when the user clicks on the button. The three types are: `NEWS_FEED`, `URI`, and `NONE`. |
|`id`              | The button ID on the message.                                                                                               |
|`toString()`      | The button as a String representation.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of button model, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button) documentation.

## GIF Support

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

