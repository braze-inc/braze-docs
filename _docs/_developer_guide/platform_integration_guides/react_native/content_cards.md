---
nav_title: Content Cards
article_title: Content Cards for React Native
platform: React Native
page_order: 3
page_type: reference
description: "This article covers how to get started with Content Cards for React Native apps."
channel: content cards

---

# Content Card integration

> This article covers how to set up Content Cards for React Native.

The Braze SDKs include a default card feed to get you started with Content Cards. To show the card feed, you can use the `Braze.launchContentCards()` method. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards.

## Customization

To build your own UI, you can get a list of available cards, and listen for updates to cards:

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
If you choose to build your own UI to display cards, you must call `logContentCardImpression` in order to receive analytics for those cards. This includes `control` cards, which must be tracked even though they are not displayed to the user.
{% endalert %}

You can use these additional methods to build a custom Content Cards Feed within your app:

| Method                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Launches the Content Cards UI element.                                                                 |
| `requestContentCardsRefresh()`           | Requests the latest Content Cards from the Braze SDK server. The resulting list of cards is passed to each of the previously registered [content card event listeners](#customization). |
| `getContentCards()`                      | Retrieves Content Cards from the Braze SDK. This returns a promise that resolves with the latest list of cards from the server. |
| `getCachedContentCards()`                | Returns the most recent Content Cards array from the cache.                                            |
| `logContentCardClicked(cardId)`          | Logs a click for the given Content Card ID. This method is used only for analytics. To execute the click action, call `processContentCardClickAction(cardId)` in addition.                                                        |
| `logContentCardImpression(cardId)`       | Logs an impression for the given Content Card ID.                                                      |
| `logContentCardDismissed(cardId)`        | Logs a dismissal for the given Content Card ID.                                                        |
| `processContentCardClickAction(cardId)`  | Perform the action of a particular card.                                                               |
{: .reset-td-br-1 .reset-td-br-2}

## Test displaying sample Content Card

Follow these steps to test a sample Content Card.

1. Set an active user in the React application by calling the [`Braze.changeUser('your-user-id')`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) method.
2. Head to **Campaigns** and follow [this guide][4] to create a new Content Card campaign.
3. Compose your test Content Card campaign and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**. You should be able to launch a Content Card on your device shortly.

![A Braze Content Card campaign showing you can add your own user ID as a test recipient to test your Content Card.][5]

For more integrations, follow the [Android integration instructions][2] or the [iOS integration instructions][3], depending on your platform.

A sample implementation of this can be found in BrazeProject within the [React Native SDK][1].

## Content Card data model

The Content Cards data model is available in the React Native SDK. For a full reference of the Content Card data model, see the [Android][6] and [iOS][7] documentation.

The Braze React Native SDK has three unique Content Cards card types that share a base model: **image only**, **captioned image**, and **classic**.

There is also a special **control** card type, which is returned to users that are in the control group for a given card.

Each type inherits common properties from a base model and has the following additional properties.

### Base Content Card model properties

The base card model provides foundational behavior for all cards.

|Property      | Description                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`          | The card's ID set by Braze.                                                                                            |
|`created`     | The UNIX timestamp of the card's creation time from Braze.                                                             |
|`expiresAt`   | The UNIX timestamp of the card's expiration time. When the value is less than 0, it means the card never expires.      |
|`viewed`      | Whether the card is read or unread by the user. This does not log analytics.                                           |
|`clicked`     | Whether the card has been clicked by the user.                                                                         |
|`pinned`      | Whether the card is pinned.                                                                                            |
|`dismissed`   | Whether the user has dismissed this card. Marking a card as dismissed that has already been dismissed will be a no-op. |
|`dismissible` | Whether the card is dismissible by the user.                                                                           |
|`url`         | (Optional) The url string associated with the card click action.                                                       |
|`openURLInWebView` | Whether URLs for this card should be opened in Braze's WebView or not.                                            |
|`isControl`   | Whether this card is a control card. Control cards should not be displayed to the user.                                |
|`extras`      | The map of key-value extras for this card.                                                                             |
{: .reset-td-br-1 .reset-td-br-2}

For a full reference of the base card, see the [Android][8] and [iOS][9] documentation.

### Image only Content Card model properties

Image only cards are clickable, full-sized images.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `IMAGE_ONLY`.                                                                              |
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
{: .reset-td-br-1 .reset-td-br-2}

For a full reference of the image only card, see the [Android][10] and [iOS][11] documentation.

### Captioned image Content Card model properties

Captioned image cards are clickable, full-sized images with accompanying descriptive text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `CAPTIONED`.                                                                               |
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2}

For a full reference of the captioned image card, see the [Android][12] and [iOS][13] documentation.

### Classic Content Card model properties

Classic cards have a title, description, and an optional image on the left of the text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `CLASSIC`.                                                                                 |
|`image`            | (Optional) The URL of the card's image.                                                                           |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2}

For a full reference of the classic (text announcement) Content Card, see the [Android][14] and [iOS][15] documentation. For a full reference of the classic image (short news) card, see the [Android][16] and [iOS][17] documentation.

### Control Content Card model properties

Control cards include all of the base properties, with a few important differences. Most importantly:

- The `isControl` property is guaranteed to be `true`.
- The `extras` property is guaranteed to be empty.

For a full reference of the control card, see the [Android][18] and [iOS][19] documentation.

## GIF Support

The Braze React Native SDK allows you to incorporate animated GIFs into your Content Cards, with distinct implementation methods for Android and iOS platforms.

{% tabs %}
{% tab Android %}
The Android SDK requires an external image library to display animated GIFs with Content Cards. For more details, refer to the guide for [GIFs]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/GIFs/).
{% endtab %}
{% tab iOS %}
The Swift SDK does not provide animated GIF support by default. Support can be added by wrapping a third party or your own view in an instance of `GIFViewProvider`. For more details on GIF support, refer to the tutorial for [GIF Support](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support/).
{% endtab %}
{% endtabs %}

[1]: https://github.com/braze-inc/braze-react-native-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[3]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
[5]: {% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test"
[6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html
[7]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html
[9]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct
[10]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html
[11]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct
[12]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html
[13]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct
[14]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html
[15]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct
[16]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html
[17]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct
[18]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html
[19]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct
