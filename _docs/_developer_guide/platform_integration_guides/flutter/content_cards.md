---
nav_title: Content Cards
article_title: Content Cards for Flutter
platform: Flutter
page_order: 3
page_type: reference
description: "This article covers how to get started with Content Cards for Flutter apps."
channel: content cards

---

# Content Cards

The Braze SDK includes a default card feed to get you started with Content Cards. To show the card feed, you can use the `myBrazePlugin.launchContentCards()` method. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards.

## Customization

You can use these additional methods to build a custom Content Cards Feed within your app by using these methods that are available on the [plugin public interface](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Method                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `myBrazePlugin.requestContentCardsRefresh()`     | Requests the latest Content Cards from the Braze SDK server.                                           |
| `myBrazePlugin.logContentCardsDisplayed()`       | Logs a Content Content feed displayed event. This is useful when using a custom UI.                                                           |
| `myBrazePlugin.logContentCardClicked(contentCard)`    | Logs a click for the given Content Card object.                                                            |
| `myBrazePlugin.logContentCardImpression(contentCard)` | Logs an impression for the given Content Card object.                                                      |
| `myBrazePlugin.logContentCardDismissed(contentCard)`  | Logs a dismissal for the given Content Card object.                                                        |

{: .reset-td-br-1 .reset-td-br-2}

## Content Card data callback

You may set a callback in Dart to receive Braze Content Card data in the Flutter host app.

To set the callback, call `myBrazePlugin.setBrazeContentCardsCallback()` from your Flutter app with a function that takes a `List<BrazeContentCard>` instance. The `BrazeContentCard` object supports a subset of fields available in the native model objects, including `description`, `title`, `image`, `url`, `extras`, and more.

{% tabs %}
{% tab Android %}

On Android, this callback works with no additional integration required.

{% endtab %}
{% tab iOS %}

Create an `NSNotificationCenter` listener for `ABKContentCardsProcessedNotification` events as described [here](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/content_cards/data_model/).

Your `ABKContentCardsProcessedNotification` callback implementation must call `myBrazePlugin.processContentCards(contentCards)`.

For an example, see [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in our sample app.

{% endtab %}
{% endtabs %}

### Replaying the callback for content cards

To store any content cards triggered before the callback is available and replay them once it is set, add the following entry to the `customConfigs` map when intializing the `BrazePlugin`:
```dart
BrazePlugin myBrazePlugin = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Test displaying sample Content Card

Follow the steps below to test a sample content card.

1. Set an active user in the React application by calling `myBrazePlugin.changeUserId('your-user-id')` method.
2. Head to **Campaigns** and follow [this guide][4] to create a new **Content Card** campaign.
3. Compose your test Content Card campaign and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**.
4. Tap the push notification and that should launch a Content Card on your device. You may need to refresh your feed for it to display.

![Content Card Campaign Test][5]

For more details on each platform, follow the [Android integration instructions][2] or the [iOS integration instructions][3].


[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
[5]: {% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test"