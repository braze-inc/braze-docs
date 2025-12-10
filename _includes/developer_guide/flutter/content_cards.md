## About Flutter Content Cards

The Braze SDK includes a default card feed to get you started with Content Cards. To show the card feed, you can use the `braze.launchContentCards()` method. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Card methods

You can use these additional methods to build a custom Content Cards Feed within your app by using the following methods available on the [plugin public interface](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Method                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Requests the latest Content Cards from the Braze SDK server.                                           |
| `braze.logContentCardClicked(contentCard)`    | Logs a click for the given Content Card object.                                                            |
| `braze.logContentCardImpression(contentCard)` | Logs an impression for the given Content Card object.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Logs a dismissal for the given Content Card object.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Receiving Content Card data

To receive Content Card data in your Flutter app, the `BrazePlugin` supports sending Content Card data by using [Dart Streams](https://dart.dev/tutorials/language/streams).

The `BrazeContentCard` [object](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) supports a subset of fields available in the native model objects, including `description`, `title`, `image`, `url`, `extras`, and more.

### Step 1: Listen for Content Card data in the Dart layer

To receive to the content card data in the Dart layer, use the code below to create a `StreamSubscription` and call `braze.subscribeToContentCards()`. Remember to `cancel()` the stream subscription when it is no longer needed.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

For an example, see [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) in our sample app.

### Step 2: Forward Content Card data from the native layer

{% alert note %}
This step is for iOS only. The Content Card data is automatically forwarded from the Android layer.
{% endalert %}

To receive the data in the Dart layer from step 1, add the following code to forward the Content Card data from the native iOS layer.

1. Implement `contentCards.subscribeToUpdates` to subscribe to content cards updates as described in the [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) documentation.

2. Your `contentCards.subscribeToUpdates` callback implementation must call `BrazePlugin.processContentCards(contentCards)`.

For an example, see [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in our sample app.

#### Replaying the callback for Content Cards

To store any Content Cards triggered before the callback is available and replay them after it is set, add the following entry to the `customConfigs` map when initializing the `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
