{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Card Feeds

The Braze SDK includes a default card feed. To show the default card feed, you can use the `launchContentCards()` method. This method handles all analytics tracking, dismissals, and rendering for a user's Content Cards.

## Content Cards

You can use these additional methods to build a custom Content Cards Feed within your app:

|Method | Description |
|---|---|
|`requestContentCardsRefresh()`|Sends a background request to request the latest Content Cards from the Braze SDK server.|
|`getContentCardsFromServer(successCallback, errorCallback)`|Retrieves Content Cards from the Braze SDK. This will request the latest Content Cards from the server and return the list of cards upon completion.|
|`getContentCardsFromCache(successCallback, errorCallback)`|Retrieves Content Cards from the Braze SDK. This will return the latest list of cards from the local cache, which was updated at the last refresh.|
|`logContentCardClicked(cardId)`|Logs a click for the given Content Card ID.|
|`logContentCardImpression(cardId)`|Logs an impression for the given Content Card ID.|
|`logContentCardDismissed(cardId)`|Logs a dismissal for the given Content Card ID.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
