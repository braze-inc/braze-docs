---
nav_title: Integration
article_title: Content Card Integration for Web
page_order: 0.2
platform: Web
channel: content cards
page_type: reference
description: "This article covers the content card integration for Web, including contend card types and how to request the number of unread Content Cards."

---

# Content Card integration

The Braze Web SDK includes a Content Cards feed UI to speed up your integration efforts. If you would prefer to build your own UI instead, see our [Customization guide]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/).

## Standard feed UI

To use the included Content Cards UI, you'll need to specify where to show the feed on your website. 

In this example, we have a `<div id="feed"></div>` in which we want to place the Content Cards feed. 

We'll use three buttons to hide, show, or toggle (hide or show based on its current state) the feed.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script>
   // we'll assume we have window.appboy
   // you can also use our npm integration instead:
   // import braze from "@braze/web-sdk";
    
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

When using the `toggleContentCards(parentNode, filterFunction)` and `showContentCards(parentNode, filterFunction)` methods, if no arguments are provided, all Content Cards will be shown in a fixed-position sidebar on the right-hand side of the page. Otherwise, the feed will be placed in the specified `parentNode` option.

|Parameters | Description |
|---|---|
|`parentNode` | The HTML node to render the Content Cards into. If the parent node already has a Braze Content Cards view as a direct descendant, the existing Content Cards will be replaced. For example, you should pass in `document.querySelector(".my-container")`.|
|`filterFunction` | A filter or sort function for cards displayed in this view. Invoked with the array of `ab.Card` objects, sorted by `{pinned, date}`. Expected to return an array of sorted `ab.Card` objects to render for this user. If omitted, all cards will be displayed. |
{: .reset-td-br-1 .reset-td-br-2}

[See the JS docs](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards) for more information on Content Card toggling.

## Requesting unviewed Content Card count

You can request the number of unread cards at any time by calling:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

This is often used to power badges signifying how many unread Content Cards there are. See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/ab.ContentCards.html#toc4) for more information.

{% comment %}
Braze will not refresh Content Cards on new page loads (and so this function will return 0) until you show the feed or call `braze.requestContentCardsRefresh();`.
{% endcomment %}

## Control group 

If you use Braze's default Content Cards feed, impressions and clicks will be automatically tracked.

If you use a custom integration for Content Cards, your integration needs to log impressions when a Control Card would have been seen.

Here is an example of how to determine if a Content Card is a "Control" card:

```javascript
function isControlCard(card) {
    return card instanceof braze.ControlCard;
}
```

## Key-value pairs

`ab.Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down along with a card for further handling by the application. Call [`card.extras`](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html) to access these values.

## Additional card methods

|Method | Description | Link|
|---|---|---|
|`logCardImpressions`| Logs an impression event for the given list of cards. This is required when using a customized UI and not the Braze UI.| [JS Docs for logCardImpressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcardimpressions)|
|`logCardClick`| Logs an click event for a given card. This is required when using a customized UI and not the Braze UI.| [JS Docs for logCardClick](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcardclick)|
|`showContentCards`| Display the user's Content Cards. | [JS Docs for showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards)|
|`hideContentCards`| Hide any Braze Content Cards currently showing. | [JS Docs for hideContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.hideContentCards)
|`toggleContentCards`| Display the user's Content Cards. | [JS Docs for toggleContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards)
|`getCachedContentCards()`|Get all currently available cards from the last Content Cards refresh.| [JS Docs for getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-braze.html#.getCachedContentCards)|
|`subscribeToContentCardsUpdates(subscriber)`| Subscribe to Content Cards updates. <br> The subscriber callback will be called whenever Content Cards are updated. |  [JS Docs for subscribeToContentCardsUpdates](https://js.appboycdn.com/web-sdk/latest/doc/module-braze.html#.subscribeToContentCardsUpdates)|
|`dismissCard()`|Dismiss the card programmatically (available in v2.4.1).| [JS Docs for dismissCard](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html#dismissCard)|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
