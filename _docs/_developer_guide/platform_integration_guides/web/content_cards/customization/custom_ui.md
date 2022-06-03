---
nav_title: Custom UI
article_title: Content Card Custom UI for Web
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "This article covers components of creating a custom UI for your web application."

---

# Create a custom UI

## Refreshing the feed

To refresh and sync a user's feed with Braze servers, use the [`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) method:

```javascript
import * as braze from "@braze/web-sdk";

function refresh(){
  braze.requestContentCardsRefresh();    
}
```
## Listening for card updates

When cards are refreshed, a callback function can be subscribed to:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates(function(updates){
  const cards = updates.cards;
  // do something with the latest instance of `cards`
});
```

## Logging events

Log impression events when cards are viewed by users:

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardImpressions(cards, true);
```

Log card click events when users interact with a card:

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardClick(card, true);
```

