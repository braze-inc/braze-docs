---
nav_title: Custom UI
article_title: Content Card Custom UI for Web
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "This article covers how to customize the default Content Cards style within the Braze SDK."

---

# Create a custom UI

## Refreshing the feed

To refresh and sync a user's feed with Braze servers, use the [`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#requestcontentcardsrefresh) method:

```javascript
import braze from "@braze/web-sdk"

function refresh(){
  braze.requestContentCardsRefresh();    
}
```
## Listening for card updates

When cards are refreshed, a callback function can be subscribed to:

```javascript
import braze from "@braze/web-sdk"

braze.subscribeToContentCardsUpdates(function(updates){
  const cards = updates.cards;
  // do something with the latest instance of `cards`
});
```

## Logging events

Log impression events when cards are viewed by users:

```javascript
import braze from "@braze/web-sdk"

braze.logCardImpressions(cards, true);
```

Log card click events when users interact with a card:

```javascript
import braze from "@braze/web-sdk"

braze.logCardClick(card, true);
```

## Control group 

If you use Braze's default Content Cards feed, impressions and clicks will be automatically tracked.

If you use a custom integration for Content Cards, your integration needs to log impressions when a Control Card would have been seen.

Here is an example of how to determine if a Content Card is a "Control" card:

```javascript
function isControlCard(card) {
    return card instanceof appboy.ControlCard;
}
```

