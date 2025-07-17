## About React Native Content Cards

The Braze SDKs include a default card feed to get you started with Content Cards. To show the card feed, you can use the `Braze.launchContentCards()` method. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Cards methods

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
| `requestContentCardsRefresh()`           | Requests the latest Content Cards from the Braze SDK server. The resulting list of cards is passed to each of the previously registered [content card event listeners](#reactnative_cards-methods). |
| `getContentCards()`                      | Retrieves Content Cards from the Braze SDK. This returns a promise that resolves with the latest list of cards from the server. |
| `getCachedContentCards()`                | Returns the most recent Content Cards array from the cache.                                            |
| `logContentCardClicked(cardId)`          | Logs a click for the given Content Card ID. This method is used only for analytics. To execute the click action, call `processContentCardClickAction(cardId)` in addition.                                                        |
| `logContentCardImpression(cardId)`       | Logs an impression for the given Content Card ID.                                                      |
| `logContentCardDismissed(cardId)`        | Logs a dismissal for the given Content Card ID.                                                        |
| `processContentCardClickAction(cardId)`  | Perform the action of a particular card.                                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Card types and properties

The Content Cards data model is available in the React Native SDK and offers the following Content Cards card types: [Image Only](#image-only), [Captioned Image](#captioned-image), and [Classic](#classic). There's also a special [Control](#control) card type, which is returned to users that are in the control group for a given card. Each type inherits common properties from a base model in addition to its own unique properties.

{% alert tip %}
For a full reference of the Content Card data model, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) documentation.
{% endalert %}

### Base card model

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
|`url`         | (Optional) The URL string associated with the card click action.                                                       |
|`openURLInWebView` | Whether URLs for this card should be opened in the Braze WebView or not.                                            |
|`isControl`   | Whether this card is a control card. Control cards should not be displayed to the user.                                |
|`extras`      | The map of key-value extras for this card.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the base card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) documentation.

### Image only

Image only cards are clickable, full-sized images.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `IMAGE_ONLY`.                                                                              |
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the image only card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) documentation.

### Captioned image

Captioned image cards are clickable, full-sized images with accompanying descriptive text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `CAPTIONED`.                                                                               |
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the captioned image card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct) documentation.

### Classic

Classic cards have a title, description, and an optional image on the left of the text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `CLASSIC`.                                                                                 |
|`image`            | (Optional) The URL of the card's image.                                                                           |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the classic (text announcement) Content Card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) documentation. For the classic image (short news) card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct) documentation.

### Control

Control cards include all of the base properties, with a few important differences. Most importantly:

- The `isControl` property is guaranteed to be `true`.
- The `extras` property is guaranteed to be empty.

For a full reference of the control card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct) documentation.
