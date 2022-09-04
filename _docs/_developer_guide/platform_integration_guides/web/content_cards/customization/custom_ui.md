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

A callback function can be registered to subscribe for updates when cards are refreshed. 

{% alert important %}
Content Cards will only refresh on session start if `subscribeToContentCardsUpdates()` is called before `openSession()`. You can always manually refresh Content Cards using `requestContentCardsRefresh()`.
{% endalert %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates(function(updates){
  const cards = updates.cards;
  // do something with the latest instance of `cards`
});

braze.openSession();
```

## Logging events

Log impression events when cards are viewed by users:

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardImpressions([card1, card2, card3], true);
```

Log card click events when users interact with a card:

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardClick(card, true);
```

## Handling changes in users

Handling changeUser() and fetching the latest content cards for the new user.

```javascript
import * as braze from "@braze/web-sdk";


braze.initialize("YOUR_SDK_API_KEY", {
  baseUrl: "YOUR_SDK_URL",
  enableLogging: true,
  doNotLoadFontAwesome: true,
});

braze.subscribeToContentCardsUpdates(({ cards }) => {
  console.log("Braze - subscribeToContentCardsUpdates: ", cards);
  //This will be invoked every time the feed is successfully refreshed following a requestContentCardsRefresh request
  //Here you can render the cards to the UI as well as logging impressions.
});

braze.changeUser("test-user-1");

braze.openSession();


braze.requestContentCardsRefresh(
 () => {console.log("Feed Refresh Request successfully submitted");}
 () => {console.log("Feed Refresh Request Failed");}
);


//Wait to run this next block until after the the content cards have been logged to the console following the above content card refresh
braze.changeUser("test-user-2");
braze.requestContentCardsRefresh(
 () => {console.log("Feed Refresh Request successfully submitted");}
 () => {console.log("Feed Refresh Request Failed");}
);
```
