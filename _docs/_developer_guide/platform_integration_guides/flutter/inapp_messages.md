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

Native in-app messages display automatically out of the box on Android and iOS when using Flutter. This article covers different customization options for in-app messages.

## Analytics

To log analytics using your `BrazeInAppMessage`, pass the instance into the desired analytics function:
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (along with the button index)

For example:
```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Disabling automatic display

To disable automatic in-app message display, make these updates in the native layer.

{% tabs %}
{% tab Android %}

1. Ensure you are using the automatic integration intializer, which is enabled by default starting in version `2.2.0`.
2. Set the in-app message operation default to `DISCARD` by adding the line below to your `braze.xml` file.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

{% endtab %}
{% tab iOS %}

1. Implement the `ABKInAppMessageControllerDelegate` delegate as described in our iOS section on [Core In-App Message Delegate]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#core-in-app-message-delegate).

2. Update your `beforeInAppMessageDisplayed` delegate implementation to return `ABKInAppMessageDisplayChoice.discardInAppMessage`.

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

1. Implement the `ABKInAppMessageControllerDelegate` delegate as described in our iOS section on [Core In-App Message Delegate]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#core-in-app-message-delegate).

2. Update your `beforeInAppMessageDisplayed` delegate implementation to call `BrazePlugin.process(inAppMessage)`.

For an example, see [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in our sample app.

{% endtab %}
{% endtabs %}

### Replaying the callback for in-app messages

To store any in-app messages triggered before the callback is available and replay them once it is set, add the following entry to the `customConfigs` map when intializing the `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Test displaying a sample in-app message

Follow the steps below to test a sample in-app message.

1. Set an active user in the React application by calling `braze.changeUser('your-user-id')` method.
2. Head to the **Campaigns** page on your dashboard and follow [this guide][1] to create a new in-app message campaign.
3. Compose your test in-app messaging campaign and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**.
4. Tap the push notification and that should display the in-app message on your device.

![In-App Messaging Campaign Test][2]


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
