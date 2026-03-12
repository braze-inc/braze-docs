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

### Replaying the callback for in-app messages (optional)

To store any in-app messages triggered before the callback is available and replay them after it is set, add the following entry to the `customConfigs` map when initializing the `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
