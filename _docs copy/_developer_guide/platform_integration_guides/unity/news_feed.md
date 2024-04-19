---
nav_title: News Feed
article_title: News Feed for Unity
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "This reference article covers News Feed integration for the Unity platform, such as parsing cards, receiving News Feed data, and analytics."

---

# News Feed integration

> This article covers how to set up a News Feed for the Unity platform.

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

## Receiving News Feed data in Unity

You may register Unity game objects to be notified of incoming News Feed cards. 

On iOS, we recommend setting game object listeners from the Braze configuration editor.

On Android, set `com_braze_feed_listener_callback_method_name` and `com_braze_feed_listener_game_object_name` in your Unity project's `braze.xml`.

To configure your game object listener at runtime on either platform, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.NEWS_FEED`.

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

## Refreshing the News Feed

To refresh the News Feed from Braze, call either of the following methods:

```csharp
// results in a network request to Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

Both methods will notify your News Feed listener and pass the News Feed along to your callback method.

## Analytics

Clicks and impressions must be manually logged for cards not displayed directly by Braze.

Use `LogClick()` and `LogImpression()` on [Card][12] to log clicks and impressions for specific cards.

To log that the user viewed the feed as a whole, call `AppboyBinding.LogFeedDisplayed()`.

[11]: https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs
[12]: https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs
