---
nav_title: In-App Messages
article_title: In-App Messages for Flutter
platform: Flutter
page_order: 4
page_type: reference
description: "This article covers in-app messages for iOS and Android apps using Flutter, including customizing and logging analytics."
channel: in-app messages

---

# In-app messages

Native in-app messages display automatically out of the box on Android and iOS when using Flutter. This article covers different customization options for in-app messages when using Flutter.

## Analytics

To log analytics using your `BrazeInAppMessage`, pass the instance into the desired analytics function:
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (along with the button index)

For example:
```dart
// Log a click
myBrazePlugin.logInAppMessageClicked(inAppMessage);
// Log an impression
myBrazePlugin.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
myBrazePlugin.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Disabling automatic display

{% tabs %}
{% tab Android %}

// Need to update this for automatic registration since you can't do this anymore - it is in IntegrationInitializer.kt

To disable automatic in-app message display for Android, implement the `IInAppMessageManagerListener` delegate as described in our Android section on [Custom Manager Listener]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#custom-manager-listener). Your `beforeInAppMessageDisplayed` method implementation should return `InAppMessageOperation.DISCARD`.

// For an example, see `MainActivity.kt` in our sample app.

{% endtab %}
{% tab iOS %}

To disable automatic in-app message display for iOS, implement the `ABKInAppMessageControllerDelegate` delegate as described in our iOS section on [Core In-App Message Delegate]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#core-in-app-message-controller-delegate).

Your `beforeInAppMessageDisplayed` delegate implementation should return `ABKInAppMessageDisplayChoice.discardInAppMessage`.

For an example, see [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in our sample app.

{% endtab %}
{% endtabs %}

## In-app message data callback

You can set a callback in Dart to receive Braze in-app message data in the Flutter host app.

To set the callback, call `BrazePlugin.setBrazeInAppMessageCallback()` from your Flutter app with a function that takes a `BrazeInAppMessage` instance.

The `BrazeInAppMessage` object supports a subset of fields available in the native model objects, including `uri`, `message`, `header`, `buttons`, `extras`, and more.

{% tabs %}
{% tab Android %}

This callback works with no additional integration required.

{% endtab %}
{% tab iOS %}

Implement the `ABKInAppMessageControllerDelegate` delegate as described in our iOS section on [Core In-App Message Delegate]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#core-in-app-message-controller-delegate).

Your `beforeInAppMessageDisplayed` delegate implementation must call `BrazePlugin.process(inAppMessage)`.

For an example, see [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in our sample app.

{% endtab %}
{% endtabs %}

### Replaying the callback for in-app messages

To store any in-app messages triggered before the callback is available and replay them once it is set, add the following entry to the `customConfigs` map in the `BrazePlugin` constructor:
```
BrazePlugin myBrazePlugin = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Test displaying a sample in-app message

Follow the steps below to test a sample in-app message.

1. Set an active user in the React application by calling `myBrazePlugin.changeUser('your-user-id')` method.
2. Head to **Campaigns** and follow [this guide][5] to create a new **In-App Messaging** campaign.
3. Compose your test in-app messaging campaign and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**.
4. Tap the push notification and that should display the in-app message on your device.

![In-App Messaging Campaign Test][6]

[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[6]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
