---
nav_title: Multiple Feeds
page_order: 5
search_rank: 5
platform: Web
---

# Using Multiple Content Card Feeds

Content Cards can be filtered on the app to only display specific cards, which enables you to have multiple Content Card feeds for different use cases (having a `Transactional` feed versus a `Marketing` feed).

The following documentation demonstrates an example implementation that can be changed to fit your specific integration.

## Step 1: Setting Key-Value Pairs on Cards

When creating a Content Card campaign, key-value pair data can be set on each Card. Our filtering logic will use this key-value pair data to categorize cards.

For the purposes of this example, we'll set a key-value pair with the key `feed_type` that will designate which Content Card feed the card should be displayed in. The value will be whatever your custom feeds will be (`Transactional`, `Marketing`, or other custom feed name).

## Step 2: Set Up Your Custom Feed

The following example will show a `Transactional` feed:

```javascript
var toggleBespokeContentCardsFeed = function(desiredFeedType) {
  appboy.display.toggleContentCards(null, function(cards) {
    var cardsOfType = [];
    for (var i=0; i<cards.length; i++) {
      if (cards[i].extras["feed_type"] == desiredFeedType) {
        cardsOfType.push(cards[i]);
      }
    }
    return cardsOfType;
  }
}
```

Then, you can set up a toggle for your custom feed, like the example shown below:

```javascript
toggleBespokeContentCardsFeed("Transactional");

```
For more information, see [our JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards).

When you create a Content Card campaign, set your key-value pair as: `feed_type` > `Transactional` or whatever feed type you desire.
