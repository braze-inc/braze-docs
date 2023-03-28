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

## Accessing in-app message data

If you want to access the in-app message data in the Javascript layer, call the `Braze.subscribeToInAppMessage()` method to have the SDKs to publish an `inAppMessageReceived` event when an in-app message is triggered. You can pass a callback to this method or set a listener for this event to perform a callback when the in-app message is triggered.

This method takes in a parameter that tells the Braze SDK whether or not to use the built-in Braze UI to display in-app messages. If you prefer to use a custom UI, you can pass `false` to this method and use the in-app message data to construct your own message in Javascript.

```javascript
import Braze from "@braze/react-native-sdk";

Braze.subscribeToInAppMessage(false, (event) => {
  const inAppMessage = new Braze.BrazeInAppMessage(event.inAppMessage);
});

// You can also set a listener for the event directly
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  const inAppMessage = new Braze.BrazeInAppMessage(event.inAppMessage);
});
```

## Advanced customization

If you would like to include more advanced logic to determine whether or not to show an in-app message using the built-in UI, you should implement in-app messages through the native layer.

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

1. Implement the `BrazeInAppMessageUIDelegate` delegate as described in [our iOS article here](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. In the `inAppMessage(_:displayChoiceForMessage:)` delegate method, you can access the `inAppMessage` data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value.

For more details on these values, see our [iOS documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert message to JSON representation
  NSData *json = [message json];
  NSDictionary *arguments = @{
    @"inAppMessage" : json
  };

  // Send to JavaScript layer
  [self.bridge.eventDispatcher
             sendDeviceEventWithName:@"inAppMessageReceived"
             body:arguments];

  // Note: return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Receiving in-app message in JavaScript

On the JavaScript side, this data can be used to instantiate a `BrazeInAppMessage`:
```javascript
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  const inAppMessage = new Braze.BrazeInAppMessage(event.inAppMessage);
});
```

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

A sample implementation can be found in BrazeProject, within the [React SDK][7]. Additional Android and iOS implementation samples can be found in the [Android][8] and [iOS][9] SDK.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#step-1-implement-an-in-app-message-manager-listener
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[6]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
[7]: https://github.com/braze-inc/braze-react-native-sdk
[8]: https://github.com/braze-inc/braze-android-sdk
[9]: https://github.com/braze-inc/braze-swift-sdk
