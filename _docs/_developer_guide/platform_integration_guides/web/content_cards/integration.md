---
nav_title: Integration
page_order: 0.1

platform: Web
---

# Integrating Content Cards on Web

To integrate Content Cards on a website, you can either use the default out-of-the-box feed, or you can customize your own feed and cards, and place them anywhere on your site.

## Default Card Feed

The quickest way to integrate Content Cards for web is to simply call [`appboy.display.toggleContentCards()`](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards). This will add the Content Cards feed to a fixed-position sidebar on the right-hand side of the page. To customize where this feed is rendered, you can supply an additional argument as noted in each method's documentation.

### Displaying the Feed

The following methods can be used to hide or show the default Content Cards feed:

|Method | Description | Link|
|---|---|---|
|`appboy.display.showContentCards(parentNode, filterFunction)`| Display the Content Cards feed. | [Documentation](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards)|
|`appboy.display.hideContentCards()`| Hide the Braze Content Cards feed. | [Documentation](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.hideContentCards)|
|`appboy.display.toggleContentCards(parentNode, filterFunction)`| Toggle the visibility of the Content Cards. | [Documentation](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards)|

### Customizing the Feed

You can use custom CSS to change the default styling of the Content Cards Feed, and its individual cards. To see more examples, take a look at the [Customization examples][/docs/developer_guide/platform_integration_guides/web/content_cards/customization/] page.

## Custom Card Feed

You can create a completely customized Content Card feed or place individual cards anywhere on your website using our Javascript SDK. For example, instead of a fixed feed, you can integrate Content Cards as individual tiles on your website, or add a horizontal scrollable area for users to swipe through on a mobile site.

### Retrieving a list of cards

The following methods can be used to get Content Cards in Javascript:

|Method | Description | Link|
|---|---|---|
|`appboy.subscribeToContentCardsUpdates(callback)`| Subscribe to content cards updates. <br> The callback will be called whenever content cards are updated. | [Documentation](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.subscribeToContentCardsUpdates)|
|`appboy.getCachedContentCards()`|Get all currently available cards from the last content cards refresh.| [Documentation](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.getCachedContentCards)|

#### Examples

A common pattern for showing a customized Content Cards feed is to start off by showing previously cached cards while you watch for new cards to be refreshed. For example:


```javascript
var list_of_cards = [];

// get the last known list of Content Cards
const {cards, lastUpdated} = appboy.getCachedContentCards();
console.log(`This user has ${cards.length} cards which were last refreshed ${lastUpdated || "never"}`);

// update your website to use this cached list of cards
list_of_cards = cards;

// listen for changes to the cards feed (e.g. the feed was refreshed)
appboy.subscribeToContentCardUpdates(updates => {
    const {cards, lastUpdated} = updates;
    console.log(`The feed was refreshed and now has ${cards.length} cards as of ${lastUpdated}`);
    // update your website to use the latest list of cards
    list_of_cards = cards;
});
```

{% alert tip %}
These methods return a new instance of each card, and will therefore note update automatically when the feed is refreshed. You should use the `appboy.subscribeToContentCardUpdates` method instead to handle updates to a user's feed.
{% endalert %}

### Creating a custom feed

For more examples on how to customize your Content Cards implementation, take a look at the [Customization examples][/docs/developer_guide/platform_integration_guides/web/content_cards/customization/] page.