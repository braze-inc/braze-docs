---
nav_title: Integration
article_itle: News Feed Integration for Web
platform: Web
page_order: 0
page_type: reference
description: "This article covers News Feed card type and how to integrate the News Feed into your web application via the Braze SDK."
channel: news feed

---

# News Feed

The News Feed is a fully customizable in-app content feed for your users. Our targeting and segmentation allow you to create a stream of content that is individually catered to the interests of each user. Depending on their position in the user life cycle and the nature of your app, this could be an onboarding content server, an advertisement center, an achievement center, or a generic news center.

## Example News Feed

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="An example News Feed displaying several notifications such as follow request, update notices, ads, and more." height="600" />

## Card types

The Braze Web SDK supports 3 unique News Feed card types, [ab.ClassicCard][3], [ab.Banner][4], [ab.CaptionedImage][5] which share a base model, [ab.Card][1].

## Integration

To toggle the display of the News Feed through the Braze Web SDK, simply call:

``` javascript
appboy.display.toggleFeed();
```

This will display the most recent cached News Feed cards (kicking off a refresh if these cards are more than 1 minute stale, or if the News Feed has never been refreshed) and will automatically update the display when new cards are received from Braze servers for as long as it's on the screen.

By default, the feed will be shown in a fixed-position sidebar on the right-hand side of the website (or as a full-screen overlay on mobile devices, through responsive CSS). If you wish to override this behavior and display a statically positioned News Feed inside your own parent element, provide the following element as the first argument to `showFeed`:

``` javascript
appboy.display.toggleFeed(document.getElementById('my-news-feed-parent'));
```

If you wish to display a specific static set of News Feed cards, filter the cards from the server, or provide your own refresh semantics, you can disable automatic updating and supply your own cards:

``` javascript
appboy.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  appboy.display.showFeed(undefined, cards);
});
appboy.requestFeedRefresh();
```

See the [JSDocs][2] for full documentation on `showFeed`, `destroyFeed`, and `toggleFeed`.

[1]: https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html
[2]: https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showFeed
[3]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ClassicCard.html
[4]: https://js.appboycdn.com/web-sdk/latest/doc/ab.Banner.html
[5]: https://js.appboycdn.com/web-sdk/latest/doc/ab.CaptionedImage.html

