---
nav_title: Content Cards
article_title: Content Cards for Unity
platform: 
  - Unity
  - iOS
  - Android
channel: content cards
page_order: 4
description: "This reference article covers Content Card implementation guidelines for the Unity platform."

---

# Content Cards

## Displaying Content Cards natively {#unity-content-cards-native-ui}

You can display the default UI for Content Cards using the following call:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Receiving Content Card data in Unity

You may register Unity game objects to be notified of incoming Content Cards. We recommend setting game object listeners from the Braze configuration editor.

If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Note, you will additionally need to make a call to `AppboyBinding.RequestContentCardsRefresh()` to start receiving data in your game object listener on iOS.

## Parsing Content Cards

Incoming `string` messages received in your Content Cards game object callback can be parsed into our pre-supplied [`ContentCard`][17] model object for convenience.

Parsing Content Cards requires Json parsing, see the following example for details:

##### Example Content Cards callback

```csharp
void ExampleCallback(string message) {
  try {
    JSONClass json = (JSONClass)JSON.Parse(message);

    // Content Card data is contained in the `mContentCards` field of the top level object.
    if (json["mContentCards"] != null) {
      JSONArray jsonArray = (JSONArray)JSON.Parse(json["mContentCards"].ToString());
      Debug.Log(String.Format("Parsed content cards array with {0} cards", jsonArray.Count));

      // Iterate over the card array to parse individual cards.
      for (int i = 0; i < jsonArray.Count; i++) {
        JSONClass cardJson = jsonArray[i].AsObject;
        try {
          ContentCard card = new ContentCard(cardJson);
          Debug.Log(String.Format("Created card object for card: {0}", card));

          // Example of logging Content Card analytics on the ContentCard object 
          card.LogImpression();
          card.LogClick();
        } catch {
          Debug.Log(String.Format("Unable to create and log analytics for card {0}", cardJson));
        }
      }
    }
  } catch {
    throw new ArgumentException("Could not parse content card JSON message.");
  }
}
```

## Refreshing Content Cards

To refresh Content Cards from Braze, call either of the following methods:

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Analytics

Clicks and impressions must be manually logged for Content Cards not displayed directly by Braze.

Use `LogClick()` and `LogImpression()` on [ContentCard][17] to log clicks and impressions for specific cards.

[17]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/ContentCard.cs
