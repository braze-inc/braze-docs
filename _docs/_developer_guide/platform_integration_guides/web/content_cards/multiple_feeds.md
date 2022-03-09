---
nav_title: Multiple Feeds
article_title: Using Multiple Content Card Feeds for Web
page_order: 5
platform: Web
channel: content cards
page_type: reference
description: "This article describes how to set up and use multiple content card feeds."

---

# Using multiple Content Card feeds

Content Cards can be filtered on the app to only display specific cards, enabling you to have multiple Content Card feeds for different use cases (for example, having a `Transactional` feed and a `Marketing` feed).

The following documentation demonstrates an example implementation that can be changed to fit your specific integration.

## Step 1: Setting key-value pairs on cards

When creating a Content Card campaign, key-value pair data can be set on each card. Our filtering logic will use this key-value pair data to categorize cards.

For this example, we'll set a key-value pair with the key `feed_type` that will designate which Content Card feed the card should be displayed in. The value will be whatever your custom feeds will be (`Transactional`, `Marketing`, or other custom feed names).

## Step 2: Set up your custom feed

The following example will show the Content Cards feed for `Transactional` type cards:

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  appboy.display.showContentCards(null, function(cards) {
    return cards.filter(function(card) {
      return card.extras["feed_type"] === feed_type;
    });
  })
}
```

Then, you can set up a toggle for your custom feed:

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```

For more information, see [our JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards).

## Step 3: Set key-value pairs in your campaign

When creating a Content Card campaign, set a key-value pair where `feed_type` is the key and `Transactional` is the value.
