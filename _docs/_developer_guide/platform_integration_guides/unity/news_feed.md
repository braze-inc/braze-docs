---
nav_title: News Feed
article_title: News Feed for Unity
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "This reference article covers News Feed integration for the Unity platform."

---

# News feed

## Receiving news feed data in unity

You may register Unity Game Objects to be notified of incoming News Feed cards. 

On iOS, we recommend setting game object listeners from the Braze configuration editor.

On Android, set `com_appboy_feed_listener_callback_method_name` and `com_appboy_feed_listener_game_object_name` in your Unity project's `braze.xml`.

- To configure your game object listener at runtime on either platform, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.NEWS_FEED`.

## Parsing cards

Incoming `string` messages received in your game object callback can be parsed into our pre-supplied [Feed][11] object, which has a list of [Card][12] objects for convenience.

See the following example for details:

### Example callback

```csharp
void FeedReceivedCallback(string message) {
  Feed feed = new Feed(message);
  Debug.Log("Feed received: " + feed);
  foreach (Card card in feed.Cards) {
    Debug.Log("Card: " + card);
  }
}
```

## Refreshing the news feed

To refresh the News Feed from Braze, call either of the following methods:

```csharp
// results in a network request to Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

Both methods will notify your News Feed listener and pass the News Feed along to your callback method.

## Analytics

clicks and impressions must be manually logged for cards not displayed directly by braze.

Use `LogClick()` and `LogImpression()` on [Card][12] to log clicks and impressions for specific cards.

To log that the user viewed the feed as a whole, call `AppboyBinding.LogFeedDisplayed()`.

[11]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Feed.cs
[12]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/Card.cs
