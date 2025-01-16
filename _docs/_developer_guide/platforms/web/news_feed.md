---
nav_title: News Feed
article_title: News Feed for the Braze Web SDK
description: "Learn about News Feed for the Braze Web SDK."
platform: Web
page_order: 4
page_type: reference
channel: news feed
---

# News Feed

> Learn about News Feed for the Braze Web SDK, including card types, card properties, and optional configurations.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## What's News Feed?

News Feed is a fully customizable in-app content feed for your users. Our targeting and segmentation allow you to create a stream of content that is individually catered to the interests of each user. Depending on their position in the user life cycle and the nature of your app, this could be an onboarding content server, an advertisement center, an achievement center, or a generic news center.

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="An example News Feed displaying several notifications such as follow request, update notices, ads, and more." height="600" />

## Card types

The Braze Web SDK supports the following card types which all share the same [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) base model:

|Type|Description|
|----|-----------|
|[`ClassicCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)|A card with a title, body, and optionally a small image, which can be passed to `showFeed` or handled manually.|
|[`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)|A card with only an image (also known as a banner card), which can be passed to `showFeed` or handled manually.|
|[`CaptionedImage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)|A card with a large image and descriptive text, which can be passed to `showFeed` or handled manually.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Using News Feed

### Displaying the feed

To toggle the display of the News Feed through the Braze Web SDK, simply call:

``` javascript
braze.toggleFeed();
```

This will display the most recent cached News Feed cards (kicking off a refresh if these cards are more than 1 minute stale, or if the News Feed has never been refreshed) and will automatically update the display when new cards are received from Braze servers for as long as it's on the screen.

By default, the feed will be shown in a fixed-position sidebar on the right-hand side of the website (or as a fullscreen overlay on mobile devices, through responsive CSS). If you wish to override this behavior and display a statically positioned News Feed inside your own parent element, provide the following element as the first argument to `showFeed`:

``` javascript
braze.toggleFeed(document.getElementById('my-news-feed-parent'));
```

If you wish to display a specific static set of News Feed cards, filter the cards from the server, or provide your own refresh semantics, you can disable automatic updating and supply your own cards:

``` javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showfeed) for full documentation on `showFeed`, `destroyFeed`, and `toggleFeed`.

### Requesting unread card count

You can request the number of unread cards at any time by calling:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

This is often used to power badges signifying how many unread News Feed cards there are. See the [JS Reference Docs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) for more information. Note that Braze will not refresh News Feed cards on new page loads (and so this function will return 0) until you show the feed or call `braze.requestFeedRefresh();`

### Accessing key-value pairs

You can optionally use `Card` objects to carry key-value pairs as `extras`, which can be used to send data alongside a card for your application to handle later. To access these your key-value pairs, call `card.extras`.

## Customizing the feed

To maintain consistency throughout all Braze mobile platforms, UI elements for the News Feed will match the composers found in the Braze dashboard. However, you can add custom CSS to the Braze SDK so you can customize your feed with your own background images, font families, styles, sizes, animations, and more.

In the following example, CSS is used to set the News Feed width to 800 pixels.

``` css
body .ab-feed {
  width: 800px;
}
```

{% alert tip %}
For a full walkthrough, see [News Feed Customization]({{site.baseurl}}/developer_guide/platforms/web/news_feed/customization/).
{% endalert %}

## Adding multiple feeds in one app

You can add multiple News Feed streams to a single app by setting the feed to only receive cards from certain categories.

To set a single category for your News Feed, add the category as a parameter in the array of your [`toggleFeed`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglefeed) method.

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.FIRST_CATEGORY]);
```

To set multiple categories for a single News Feed, add additional categories to the same array in your `toggleFeed` method.

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.FIRST_CATEGORY, braze.Card.Category.SECOND_CATEGORY, braze.Card.Category.THIRD_CATEGORY]);
```

## Disabling unread indicators

By default, News Feed cards show whether they're read or unread.

![A News Feed card showing an image of a watch along with some text. In the upper right corner of the text is a blue or gray triangle that indicates if a card has been read or not. A blue triangle signifies that a card has been read.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

To disable this feature, add the following style to the CSS in the Braze SDK.

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```
