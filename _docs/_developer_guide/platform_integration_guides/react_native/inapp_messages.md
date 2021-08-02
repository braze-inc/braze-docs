---
nav_title: In-App Messages
platform: React Native
subplatform: iOS
page_order: 4
page_type: reference
description: "This article covers in-app messages for iOS apps using React Native, including customizing and logging analytics."
channel: in-app messages

---

# In-App Messages

Native in-app messages display automatically on Android and iOS when using React Native.

## Customizing (Android)

### Accessing In-App Message Data
If you would like to access the in-app message data in the JavaScript layer, implement the `IInAppMessageManagerListener` as described in our public documentation [for Android][1]. In your `beforeInAppMessageDisplayed` implementation, you can access the `inAppMessage` data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value (for more on these values, see our [Android documentation][2]).

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

## Customizing (iOS)

### Accessing In-App Message Data
If you would like to access the in-app message data in the JavaScript layer, implement the `ABKInAppMessageControllerDelegate` delegate as described in our public documentation [for iOS][3]. In the `beforeInAppMessageDisplayed:` delegate method, you can access the `inAppMessage` data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value (for more on these values, see our [iOS documentation][4]).

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// In-app messaging
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  NSData *inAppMessageData = [inAppMessage serializeToData];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };
  // Send to JavaScript
  [self.bridge.eventDispatcher
             sendDeviceEventWithName:@"inAppMessageReceived"
             body:arguments];
  // Note: return ABKDiscardInAppMessage if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return ABKDisplayInAppMessageNow;
}
```
{% endtab %}
{% tab swift %}
```swift
// In-app messaging
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice {
    let inAppMessageData = inAppMessage?.serializeToData()
    var inAppMessageString: String? = nil
    if let inAppMessageData = inAppMessageData {
        inAppMessageString = String(data: inAppMessageData, encoding: .utf8)
    }
    let arguments = [
        "inAppMessage": inAppMessageString ?? ""
    ]
    // Send to JavaScript
    bridge.eventDispatcher.sendDeviceEvent(
        withName: "inAppMessageReceived",
        body: arguments)
    // Note: return ABKDiscardInAppMessage if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return ABKDisplayInAppMessageNow
}
```
{% endtab %}
{% endtabs %}

### Receiving In-App Message in JavaScript

On the JavaScript side, this data can be used to instantiate a `BrazeInAppMessage`:
```javascript
this._listener = DeviceEventEmitter.addListener("inAppMessageReceived", function(event) {
    let inAppMessage = new ReactAppboy.BrazeInAppMessage(event.inAppMessage)
})
```

### Analytics

To log analytics using your `BrazeInAppMessage`, pass the instance into the desired analytics function:
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (along with the button index)

For example:
```js
// Log a click
ReactAppboy.logInAppMessageClicked(inAppMessage);
// Log an impression
ReactAppboy.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
ReactAppboy.logInAppMessageButtonClicked(inAppMessage, 0);

```

## Test Displaying a Sample In-App Message

Follow the steps below to test a sample In-App Message.

1. Set an active user in the React application by calling `ReactAppboy.changeUserId('your-user-id')` method.
2. Head to **Campaigns** and follow [this guide][5] to create a new **In-App Messaging** campaign.
3. Compose your test in-app messaging campaign and head over to the **Test** tab. Add the same *user-id* as the test user and `Send Test`. You should be able to launch an in-app message on your device shortly.

![In-App Messaging Campaign Test][6]

A sample implementation of this is contained in AppboyProject, within the [React SDK][7]. Additional Android implementation samples are contained in the [Android SDK][8].    Additional iOS implementation samples are contained in the [iOS SDK][9].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-a-custom-manager-listener
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#step-1-implement-an-in-app-message-manager-listener
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#core-in-app-message-controller-delegate
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#custom-handling-in-app-message-display
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[6]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
[7]: https://github.com/Appboy/appboy-react-sdk
[8]: https://github.com/Appboy/appboy-android-sdk
[9]: https://github.com/Appboy/appboy-ios-sdk
