{% multi_lang_include archive/web-v4-rename.md %}

## Prerequisites

Before you can use Content Cards, you'll need to [integrate the Braze Web SDK]({{site.baseurl}}/developer_guide/platforms/web/sdk_integration/) into your app. However, no additional setup is required. To build your own UI instead, see [Content Card Customization Guide]({{site.baseurl}}/developer_guide/content_cards/).

## Standard feed UI

To use the included Content Cards UI, you'll need to specify where to show the feed on your website. 

In this example, we have a `<div id="feed"></div>` in which we want to place the Content Cards feed. We'll use three buttons to hide, show, or toggle (hide or show based on its current state) the feed.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script> 
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

When using the `toggleContentCards(parentNode, filterFunction)` and `showContentCards(parentNode, filterFunction)` methods, if no arguments are provided, all Content Cards will be shown in a fixed-position sidebar on the right-hand side of the page. Otherwise, the feed will be placed in the specified `parentNode` option.

|Parameters | Description |
|---|---|
|`parentNode` | The HTML node to render the Content Cards into. If the parent node already has a Braze Content Cards view as a direct descendant, the existing Content Cards will be replaced. For example, you should pass in `document.querySelector(".my-container")`.|
|`filterFunction` | A filter or sort function for cards displayed in this view. Invoked with the array of `Card` objects, sorted by `{pinned, date}`. Expected to return an array of sorted `Card` objects to render for this user. If omitted, all cards will be displayed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[See the SDK reference docs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) for more information on Content Card toggling.

## Card types and properties

The Content Cards data model is available in the Web SDK and offers the following Content Card types: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), and [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Each type inherits common properties from a base model [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) and has the following additional properties.

{% alert tip %}
To log Content Card data, see [Logging analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/).
{% endalert %}

### Base card model

All Content Cards have these shared properties:

|Property|Description|
|---|---|
| `expiresAt` | The UNIX timestamp of the card's expiration time.|
| `extras`| (Optional) Key-value pair data formatted as a string object with a value string. |
| `id` | (Optional) The id of the card. This will be reported back to Braze with events for analytics purposes. |
| `pinned` | This property reflects if the card was set up as "pinned" in the dashboard.|
| `updated` | The UNIX timestamp of when this card was last modified. |
| `viewed` | This property reflects whether the user viewed the card or not.|
| `isControl` | This property is `true` when a card is a "control" group within an A/B test.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image only

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) cards are clickable full-sized images.

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The UNIX timestamp of the card's creation time from Braze. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captioned image

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) cards are clickable, full-sized images with accompanying descriptive text.

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The UNIX timestamp of the card's creation time from Braze. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `title` | The title text for this card. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classic

The [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) model can contain an image with no text or a text with image.

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The UNIX timestamp of the card's creation time from Braze. |
| `description` | The body text for this card. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `title` | The title text for this card. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Control group

If you use the default Content Cards feed, impressions and clicks will be automatically tracked.

If you use a custom integration for Content Cards, you need need [log impressions]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) when a Control Card would have been seen. As part of this effort, make sure to handle Control cards when logging impressions in an A/B test. These cards are blank, and while they aren’t seen by users, you should still log impressions in order to compare how they perform against non-Control cards.

To determine if a Content Card is in the Control group for an A/B test, check the `card.isControl` property (Web SDK v4.5.0+) or check if the card is a `ControlCard` instance (`card instanceof braze.ControlCard`).

## Card methods

|Method | Description |
|---|---|
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Logs an impression event for the given list of cards. This is required when using a customized UI and not the Braze UI.|
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Logs an click event for a given card. This is required when using a customized UI and not the Braze UI.| 
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Display the user's Content Cards. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Hide any Braze Content Cards currently showing. | 
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Display the user's Content Cards. | 
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|Get all currently available cards from the last Content Cards refresh.|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Subscribe to Content Cards updates. <br> The subscriber callback will be called whenever Content Cards are updated. | 
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|Dismiss the card programmatically (available in v2.4.1).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For more details, refer to the [SDK reference documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
