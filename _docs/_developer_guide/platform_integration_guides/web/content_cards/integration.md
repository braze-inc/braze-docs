---
nav_title: Integration
page_order: 0.1

platform: Web
---

# Content Cards for Web Integration

To toggle display of Content Cards through the Braze Web SDK, call:

[`appboy.display.toggleContentCards();`](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards)


This method will toggle the visibility of the Content Cards. By default, if no arguments are provided, all Content Cards will be shown in a fixed-position sidebar on the right-hand side of the page.

|Parameters | Description |
|---|---|
|`parentNode` | The HTML node to render the content cards into. If the parent node already has a Braze content cards view as a direct descendant, the existing content cards will be replaced. |
|`filterFunction` | A filter/sort function for cards displayed in this view. Invoked with the array of ab.Card objects, sorted by {pinned, date}. Expected to return an array of sorted ab.Card objects to render for this user. If omitted, all cards will be displayed. |
{: .reset-td-br-1 .reset-td-br-2}

[See the JS docs](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards) for more information on toggling Content Cards.

### Control Group 

If you use Braze's default Content Cards feed, impressions and clicks will be automatically tracked.

If you use a custom integration for Content Cards, your integration needs to log impressions when a Control Card _would have been seen_.

Here is an example of how to determine if a Content Card is a "Control" card:

```javascript
function isControlCard(card) {
    return card instanceof appboy.ControlCard;
}
```

## Other Methods to Note

|Method | Description | Link|
|---|---|---|
|`showContentCards()`| Display the user's Content Cards. | [JS Docs for showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards)|
|`hideContentCards()`| Hide any Braze content cards currently showing. | [JS Docs for hideContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.hideContentCards)
|`toggleContentCards()`| Toggle the visibility of the Content Cards. | [JS Docs for showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards)
|`getCachedContentCards()`|Get all currently available cards from the last content cards refresh.| [JS Docs for getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.getCachedContentCards)|
|`subscribeToContentCardsUpdates(subscriber)`| Subscribe to content cards updates. <br> The subscriber callback will be called whenever content cards are updated. |  [JS Docs for subscribeToContentCardsUpdates](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.subscribeToContentCardsUpdates)|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
