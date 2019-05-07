---
nav_title: Content Cards for Web
permalink: /content_cards_web/

---
# Content Cards for Web

Content Cards are Braze’s new messaging channel which will allow you to create individual messages that appear in a user’s message inbox. This feature is set to, in the future, replace the legacy feature _News Feed channel_, as it provides superior behavior and functionality.

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card [analytics]({{ site.baseurl }}/content_cards/#content-cards-analytics), and easy coordination with push notifications.


## Example Content Card


![Content Card Example][1]


## Content Cards for Web Integration

To toggle display of Content Cards through the Braze Web SDK, call
`appboy.display.toggleContentCards();`


This will show the Content Cards if they are not shown, and hide them if they are. If no parameters are defined (null), all Content Cards will be shown in a fixed-position sidebar on the right-hand side of the page.

|Parameters | Description |
|---|---|
|`parentNode` | The HTML node to render the content cards into. If the parent node already has a Braze content cards view as a direct descendant, the existing content cards will be replaced. |
|`filterFunction` | A filter/sort function for cards displayed in this view. Invoked with the array of ab.Card objects, sorted by {pinned, date}. Expected to return an array of sorted ab.Card objects to render for this user. If omitted, all cards will be displayed. |

[See the JS docs](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards) for more information on toggling Content Cards.

### Other Methods to Note

|Method | Description | Link|
|---|---|---|
|`showContentCards`| Display the user's Content Cards. | [JS Docs for showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards)|
|`hideContentCards`| Hide any Braze content cards currently showing. | [JS Docs for hideContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.hideContentCards)
|`showContentCards`| Display the user's content cards. | [JS Docs for showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards)
|`getCachedContentCards()`|Get all currently available cards from the last content cards refresh.| [JS Docs for getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.getCachedContentCards)|
|`subscribeToContentCardsUpdates(subscriber)`| Subscribe to content cards updates. The subscriber callback will be called whenever content cards are updated. |  [JS Docs for subscribeToContentCardsUpdates](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.getCachedContentCards)|


## Content Cards Customization

Braze UI elements come with a default look and feel that matches the composers within the Braze Dashboard and aims for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK. By overriding selected styles in your application, it is possible to customize our standard feed with your own background images, font families, styles, sizes, animations, and more. For instance, the following is an example override that will cause Content Cards to appear 800px wide:

``` css
body .ab-feed {
  width: 800px;
}
```


## Read/Unread Indicators

Braze provides indicators on Content Cards as pictured below:

![Read and Unread Behavior][2]

### Disabling the Indicators

In order to disable this functionality add the following style to your css:

``` css
.ab-unread-indicator { display: none; }
```

## Content Card Types for Web
The Braze Web SDK supports several unique Content Card card types, [ab.ClassicCard](), [ab.Banner](), [ab.CaptionedImage]() which share a base model, [ab.Card][().

### Requesting Unviewed Content Card Count for Web

You can request the number of unread cards at any time by calling:

``` javascript
appboy.getCachedContentCards().getUnviewedCardCount();
```

This is often used to power badges signifying how many unread content cards there are. See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/ab.ContentCards.html#toc4) for more information.

> Braze will not refresh Content Cards on new page loads (and so this function will return 0) until you show the feed or call `appboy.requestContentCardsRefresh();`.

### Key-Value Pairs
`ab.Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down along with a card for further handling by the application. Call `card.extras` to access these values.




[1]:{% image_buster /assets/img_archive/contentcard.png %}
[2]:{% image_buster /assets/img_archive/braze-content-cards-seen-unseen-behavior.png %}
[3]:{% image_buster /assets/img_archive/unreadcontentcard.png %}
