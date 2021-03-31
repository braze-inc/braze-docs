---
nav_title: Customization
page_order: 1

platform: Web
---

# Content Cards Customization

Braze UI elements come with a default look and feel that matches the composers within the Braze Dashboard and aims for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK.

By overriding selected styles in your application, it is possible to customize our standard feed with your own background images, font families, styles, sizes, animations, and more. For instance, the following is an example override that will cause Content Cards to appear 800px wide:

``` css
body .ab-feed {
  width: 800px;
}
```

## Other Methods to Note

|Method | Description | Link|
|---|---|---|
|`logCardImpressions`| Logs an impression event for the given list of cards. This is required when using a customized UI and not the Braze UI.| [JS Docs for logCardImpressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logcardimpressions)|
|`logCardClick`| Logs an click event for a given card. This is required when using a customized UI and not the Braze UI.| [JS Docs for logCardClick](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logcardclick)|
|`showContentCards`| Display the user's Content Cards. | [JS Docs for showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards)|
|`hideContentCards`| Hide any Braze content cards currently showing. | [JS Docs for hideContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.hideContentCards)
|`toggleContentCards`| Display the user's content cards. | [JS Docs for toggleContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards)
|`getCachedContentCards()`|Get all currently available cards from the last content cards refresh.| [JS Docs for getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.getCachedContentCards)|
|`subscribeToContentCardsUpdates(subscriber)`| Subscribe to content cards updates. <br> The subscriber callback will be called whenever content cards are updated. |  [JS Docs for subscribeToContentCardsUpdates](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.subscribeToContentCardsUpdates)|
|`dismissCard()`|Dismiss the card programmatically (available in v2.4.1).| [JS Docs for dismissCard](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html#dismissCard)|
