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

The Braze SDK includes a default card feed to get you started with Content Cards. To show the card feed, you can use the `braze.launchContentCards()` method. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards.

## Customization

You can use these additional methods to build a custom Content Cards Feed within your app by using the following methods available on the [plugin public interface][7]:

| Method                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Requests the latest Content Cards from the Braze SDK server.                                           |
| `braze.logContentCardsDisplayed()`       | Logs a Content Content feed displayed event. This is useful when using a custom UI.                                                           |
| `braze.logContentCardClicked(contentCard)`    | Logs a click for the given Content Card object.                                                            |
| `braze.logContentCardImpression(contentCard)` | Logs an impression for the given Content Card object.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Logs a dismissal for the given Content Card object.                                                        |
{: .reset-td-br-1 .reset-td-br-2}

## Content Card data callback

You may set a callback in Dart to receive Braze Content Card data in the Flutter host app.

To set the callback, call `braze.setBrazeContentCardsCallback()` from your Flutter app with a function that takes a `List<BrazeContentCard>` instance. The `BrazeContentCard` object supports a subset of fields available in the native model objects, including `description`, `title`, `image`, `url`, `extras`, and more.

{% tabs %}
{% tab Android %}

This callback works with no additional integration required.

{% endtab %}
{% tab iOS %}

1. Create a `NotificationCenter` listener for `NSNotification.Name.ABKContentCardsProcessed` events as described in our [Content Cards view controller integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/#getting-the-data) article.

2. Your `NotificationCenter` callback implementation must call `BrazePlugin.processContentCards(contentCards)`.

For an example, see [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in our sample app.

{% endtab %}
{% endtabs %}

### Replaying the callback for Content Cards

To store any Content Cards triggered before the callback is available and replay them once it is set, add the following entry to the `customConfigs` map when intializing the `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Test displaying sample Content Card

Follow these steps to test a sample Content Card.

1. Set an active user in the React application by calling `braze.changeUserId('your-user-id')` method.
2. Head to **Campaigns** and follow [this guide][3] to create a new Content Card campaign.
3. Compose your test Content Card campaign and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**.
4. Tap the push notification and that should launch a Content Card on your device. You may need to refresh your feed for it to display.

![A Braze Content Card campaign showing you can add your own user ID as a test recipient to test your Content Card.][4]

For more details on each platform, follow the [Android integration][5] or [iOS integration][6] guides.


[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
[4]: {% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test"
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/
[7]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart
