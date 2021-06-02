---
nav_title: Integration
page_order: 0.2

platform: Web
page_type: reference
description: "This article covers the content card integration for Web, including contend card types and how to request the number of unread content cards."
channel: content cards

---

# Content Cards Integration

To toggle display of Content Cards through the Braze Web SDK, call:

[`appboy.display.toggleContentCards();`](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards)

This method will toggle the visibility of the Content Cards. By default, if no arguments are provided, all Content Cards will be shown in a fixed-position sidebar on the right-hand side of the page.

|Parameters | Description |
|---|---|
|`parentNode` | The HTML node to render the content cards into. If the parent node already has a Braze content cards view as a direct descendant, the existing content cards will be replaced. |
|`filterFunction` | A filter/sort function for cards displayed in this view. Invoked with the array of ab.Card objects, sorted by {pinned, date}. Expected to return an array of sorted ab.Card objects to render for this user. If omitted, all cards will be displayed. |
{: .reset-td-br-1 .reset-td-br-2}

[See the JS docs](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards) for more information on toggling Content Cards.

## Content Card Data Models

The Braze Web SDK supports several unique Content Card card types, [ab.ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/ab.ClassicCard.html), [ab.Banner](https://js.appboycdn.com/web-sdk/latest/doc/ab.Banner.html), [ab.CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/ab.CaptionedImage.html) which share a base model, [ab.Card](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html).

### Requesting Unviewed Content Card Count

You can request the number of unread cards at any time by calling:

```javascript
appboy.getCachedContentCards().getUnviewedCardCount();
```

This is often used to power badges signifying how many unread content cards there are. See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/ab.ContentCards.html#toc4) for more information.

{% comment %}
Braze will not refresh Content Cards on new page loads (and so this function will return 0) until you show the feed or call `appboy.requestContentCardsRefresh();`.
{% endcomment %}

### Control Group 

If you use Braze's default Content Cards feed, impressions and clicks will be automatically tracked.

If you use a custom integration for Content Cards, your integration needs to log impressions when a Control Card _would have been seen_.

Here is an example of how to determine if a Content Card is a "Control" card:

```javascript
function isControlCard(card) {
    return card instanceof appboy.ControlCard;
}
```

### Key-Value Pairs

`ab.Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down along with a card for further handling by the application. Call [`card.extras`](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html) to access these values.

### Additional Card Methods

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
