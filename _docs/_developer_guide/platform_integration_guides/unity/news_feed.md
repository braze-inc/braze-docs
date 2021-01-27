---
nav_title: News Feed
platform: Unity
page_order: 4
---
# News Feed

## Overview of the News Feed Models

- The News Feed is represented as a [Feed][11] object, which has a list of [Card][12] objects
- Various [card models][13] extend the base Card object
- Cards can additionally be grouped by [CardCategory][14]

## Retrieving the News Feed

To retrieve the News Feed from Braze, call either of the following methods:

- [`AppboyBinding.RequestFeedRefresh()`][2] requests a News Feed refresh directly from BRaze's servers
- [`AppboyBinding.RequestFeedRefreshFromCache()`][3] pulls the locally-stored News Feed

Both methods will notify your News Feed listener and pass the News Feed along to your callback method.

## Logging News Feed Analytics

If you wish to log News Feed analytics, you can do so using the following methods.

### Logging Feed Displayed

To log a Feed Displayed event whenever a user views the News Feed, use [`AppboyBinding.LogFeedDisplayed()`][1].

### Logging Card Impressions

To log a News Feed Card impression and mark the card as viewed, call the [`LogImpression()`][15] method on the associated Card object.

### Logging Card Clicks

To log a News Feed Card click, call the [`LogClick()`][16] method on the associated Card object.

## Implementation Example {#feed-implementation-example}

Check out the [`FeedReceivedCallback`][7] implementation in `AppboyBindingTester.cs` for an implementation example.

[1]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/AppboyBinding.cs#L330
[2]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/AppboyBinding.cs#L680
[3]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/AppboyBinding.cs#L684
[7]: https://github.com/Appboy/unity-sdk/blob/develop/Assets/Plugins/Appboy/Tests/AppboyBindingTester.cs#L56
[11]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Feed.cs
[12]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/Card.cs
[13]: https://github.com/Appboy/appboy-unity-sdk/tree/master/Assets/Plugins/Appboy/models/Cards
[14]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/CardCategory.cs
[15]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/Card.cs#L55
[16]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/Card.cs#L73
