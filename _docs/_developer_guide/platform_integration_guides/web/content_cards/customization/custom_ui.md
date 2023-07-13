---
nav_title: Custom UI
article_title: Content Card Custom UI for Web
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "This article covers components of creating a custom UI for your web application."

---

# Custom UI

> This article covers components of creating a custom UI for your web application.

## Refreshing the feed {#refresh}

To refresh and sync a user's feed with Braze servers, use the [`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) method:

```javascript
import * as braze from "@braze/web-sdk";

function refresh(){
  braze.requestContentCardsRefresh();    
}
```

## Listening for card updates

A callback function can be registered to subscribe for updates when cards are refreshed. 

{% alert important %}
Content Cards will only refresh on session start if `subscribeToContentCardsUpdates()` is called before `openSession()`. You can always manually refresh Content Cards using `requestContentCardsRefresh()`.
{% endalert %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  // do something with the latest instance of `cards`
  // for example:
  cards.forEach(card => {
    if (card.isControl) {
      // do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.Banner) {
      // use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

## Logging events

{% alert note %}
Make sure to handle Control cards when logging impressions. These cards are blank, and while they aren't seen by users, you should still log impressions in order to compare how they perform against non-control cards. You can check for control cards using the `card.isControl` property.
{% endalert %}


Log impression events when cards are viewed by users:


```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Log card click events when users interact with a card:

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

