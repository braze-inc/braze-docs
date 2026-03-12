{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Logging message data

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

## Accessing message data

To access in-app message data in your Flutter app, the `BrazePlugin` supports sending in-app message data using [Dart Streams](https://dart.dev/tutorials/language/streams).

The `BrazeInAppMessage` object supports a subset of fields available in the native model objects, including `uri`, `message`, `header`, `buttons`, `extras`, and more.

### Listen for in-app message data in the Dart layer

To receive in-app message data in the Dart layer, use the code below to create a `StreamSubscription` and call `braze.subscribeToInAppMessages()`. Remember to `cancel()` the stream subscription when it is no longer needed.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

For an example, see [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) in our sample app.

### Forward in-app message data from the native layer

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

In-app message data is automatically forwarded from both the Android and iOS native layers. No additional setup is required.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

The in-app message data is automatically forwarded from the Android layer. To forward in-app message data from the iOS layer, choose one of the following approaches:

{% subtabs %}
{% subtab UI Delegate %}

1. Implement the `BrazeInAppMessageUIDelegate` delegate as described in our iOS article on [core in-app message delegate](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Update your [`willPresent` delegate implementation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv) to call `BrazePlugin.process(inAppMessage)`.
{% endsubtab %}

{% subtab custom presenter %}
1. Ensure you have enabled the in-app message UI and set the `inAppMessagePresenter` to your custom presenter.
```swift
    let inAppMessageUI = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = inAppMessageUI
```
2. Create your custom presenter class and call `BrazePlugin.process(inAppMessage)` within [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra).
```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    // Pass in-app message data to the Dart layer.
    BrazePlugin.processInAppMessage(message)

    // If you want the default UI to display the in-app message.
    super.present(message: message)
  }
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### Replaying the callback for in-app messages (optional)

To store any in-app messages triggered before the callback is available and replay them after it is set, add the following entry to the `customConfigs` map when initializing the `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
