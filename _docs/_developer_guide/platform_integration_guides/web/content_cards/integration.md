---
nav_title: Integration
article_title: Content Card Integration for Web
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "This article covers Content Card integration for Web, including Content Card data models, standard feed UI options, and additional card methods."

---

# Content Card integration

{% include archive/web-v4-rename.md %}

## Content Card data model {#data-models}

The Content Cards data model is available in the Web SDK.

## Content Card model
The Braze Web SDK offers three Content Card types: [Banner](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.banner.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), and [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Each type inherits common properties from a base model [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) and has the following additional properties.

### Base Content Card model properties - Card

|Property|Description|
|---|---|
| `expiresAt` | The unix timestamp of the card's expiration time.|
| `extras`| (Optional) Key-value pair data formatted as a string object with a value string. |
| `id` | (Optional) The id of the card. This will be reported back to Braze with events for analytics purposes. |
| `pinned` | This property reflects if the card was set up as "pinned" in the dashboard.|
| `updated` | The unix timestamp of when this card was last modified. |
| `viewed` | This property reflects whether the user viewed the card or not.|
{: .reset-td-br-1 .reset-td-br-2}

### Banner Content Card properties - Banner

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The unix timestamp of the card's creation time from Braze. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2}

### Captioned image Content Card properties - CaptionedImage

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The unix timestamp of the card's creation time from Braze. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `title` | The title text for this card. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2}

### Classic Content Card properties - ClassicCard

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The unix timestamp of the card's creation time from Braze. |
| `description` | The body text for this card. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `title` | The title text for this card. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2}

## Card methods

|Method | Description | Link|
|---|---|---|
|`logCardImpressions`| Logs an impression event for the given list of cards. This is required when using a customized UI and not the Braze UI.| [JS Docs for logCardImpressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcardimpressions)|
|`logCardClick`| Logs an click event for a given card. This is required when using a customized UI and not the Braze UI.| [JS Docs for logCardClick](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcardclick)|
|`showContentCards`| Display the user's Content Cards. | [JS Docs for showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)|
|`hideContentCards`| Hide any Braze Content Cards currently showing. | [JS Docs for hideContentCards](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)
|`toggleContentCards`| Display the user's Content Cards. | [JS Docs for toggleContentCards](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)
|`getCachedContentCards()`|Get all currently available cards from the last Content Cards refresh.| [JS Docs for getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|
|`subscribeToContentCardsUpdates(subscriber)`| Subscribe to Content Cards updates. <br> The subscriber callback will be called whenever Content Cards are updated. |  [JS Docs for subscribeToContentCardsUpdates](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)|
|`dismissCard()`|Dismiss the card programmatically (available in v2.4.1).| [JS Docs for dismissCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismissCard)|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

For more details, refer to the [JS documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)

## Content Card integration

The Braze Web SDK includes a Content Cards feed UI to speed up your integration efforts. If you would prefer to build your own UI instead, see [custom UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/).

### Standard feed UI

To use the included Content Cards UI, you'll need to specify where to show the feed on your website. 

In this example, we have a `<div id="feed"></div>` in which we want to place the Content Cards feed. 

We'll use three buttons to hide, show, or toggle (hide or show based on its current state) the feed.

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
{: .reset-td-br-1 .reset-td-br-2}

[See the JS docs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) for more information on Content Card toggling.

## Control group 

If you use Braze's default Content Cards feed, impressions and clicks will be automatically tracked.

If you use a custom integration for Content Cards, your integration needs to log impressions when a Control Card would have been seen.

Here is an example of how to determine if a Content Card is a "Control" card:

```javascript
function isControlCard(card) {
    return card instanceof braze.ControlCard;
}
```

{% alert note %}
Visit the following customization articles for documentation on adding [custom UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/), [custom styling]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling), [key-value pairs]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/key_value_pairs), [read and unread indicators]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/read_and_unread/), and [requesting unviewed Content Card counts]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/badges).
{% endalert %}

