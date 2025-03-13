{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Receiving News Feed data in Unity

You may register Unity game objects to be notified of incoming News Feed cards. 

On iOS, we recommend setting game object listeners from the Braze configuration editor.

On Android, set `com_braze_feed_listener_callback_method_name` and `com_braze_feed_listener_game_object_name` in your Unity project's `braze.xml`.

To configure your game object listener at runtime on either platform, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.NEWS_FEED`.

## Parsing cards

Incoming `string` messages received in your game object callback can be parsed into our pre-supplied [Feed](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs) object, which has a list of [Card](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) objects for convenience.

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

Use `LogClick()` and `LogImpression()` on [Card](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) to log clicks and impressions for specific cards.

To log that the user viewed the feed as a whole, call `AppboyBinding.LogFeedDisplayed()`.

