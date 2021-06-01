---
nav_title: Data Models
page_order: 5

platform: Web
page_type: reference
description: "This article covers the content card types for Web, including how to request the number of unread content cards."
channel: content cards

---

# Content Card Types for Web

The Braze Web SDK supports several unique Content Card card types, [ab.ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/ab.ClassicCard.html), [ab.Banner](https://js.appboycdn.com/web-sdk/latest/doc/ab.Banner.html), [ab.CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/ab.CaptionedImage.html) which share a base model, [ab.Card](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html).

## Requesting Unviewed Content Card Count for Web

You can request the number of unread cards at any time by calling:

```javascript
appboy.getCachedContentCards().getUnviewedCardCount();
```

This is often used to power badges signifying how many unread content cards there are. See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/ab.ContentCards.html#toc4) for more information.

{% comment %}

Braze will not refresh Content Cards on new page loads (and so this function will return 0) until you show the feed or call `appboy.requestContentCardsRefresh();`.

{% endcomment %}

## Key-Value Pairs
`ab.Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down along with a card for further handling by the application. Call [`card.extras`](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html) to access these values.
