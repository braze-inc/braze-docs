---
nav_title: Content Cards
article_title: Content Cards Integration for Cordova
platform: 
  - Cordova
  - iOS
  - Android
page_order: 3
channel: content cards
page_type: reference
description: "This article covers integrate and customize Content Cards for Cordova."

---

# Content Card integration

> This article covers how to set up Content Cards for Cordova. 

To get started, the Braze SDKs include a default card feed. To show the card feed you can use the `BrazePlugin.launchContentCards()` method.

The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards.

## Customization

You can use these additional methods to build a custom Content Cards Feed within your app:

|Method | Description |
|---|---|
|`BrazePlugin.requestContentCardsRefresh()`|Requests the latest Content Cards from the Braze SDK server.|
|`BrazePlugin.getContentCardsFromServer(successCallback, errorCallback)`|Retrieves Content Cards from the Braze SDK. This will return the latest list of cards from the server.|
|`BrazePlugin.getContentCardsFromCache(successCallback, errorCallback)`|Retrieves Content Cards from the Braze SDK. This will return the latest list of cards from the cache.|
|`BrazePlugin.logContentCardClicked(cardId)`|Logs a click for the given Content Card ID.|
|`BrazePlugin.logContentCardImpression(cardId)`|Logs an impression for the given Content Card ID.|
|`BrazePlugin.logContentCardDismissed(cardId)`|Logs a dismissal for the given Content Card ID.|
{: .reset-td-br-1 .reset-td-br-2}
