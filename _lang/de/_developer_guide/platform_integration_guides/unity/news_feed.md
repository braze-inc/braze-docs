---
nav_title: Newsfeed
article_title: News Feed für Unity
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "Dieser Referenzartikel beschreibt die Newsfeed-Integration für die Unity-Plattform, z. B. das Parsen von Karten, den Empfang von Newsfeed-Daten und Analytics."

---

# Integration von News Feeds

> Dieser Artikel beschreibt, wie Sie einen Newsfeed für die Unity-Plattform einrichten.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Empfang von News Feed-Daten in Unity

Sie können Unity-Spielobjekte registrieren, um über eingehende Newsfeed-Cards benachrichtigt zu werden. 

Unter iOS empfiehlt es sich, Spielobjekt-Listener über den Braze-Konfigurationseditor festzulegen.

Unter Android legen Sie `com_braze_feed_listener_callback_method_name` und `com_braze_feed_listener_game_object_name` in der `braze.xml` Ihres Unity-Projekts fest.

Um den Spielobjekt-Listener zur Laufzeit auf beiden Plattformen zu konfigurieren, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.NEWS_FEED` an.

## Parsen von Karten

Eingehende `string` Nachrichten, die in Ihrem Spielobjekt-Callback empfangen werden, können in unser vordefiniertes [Feed-Objekt](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs) geparst werden, das der Einfachheit halber eine Liste von [Kartenobjekten](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) enthält.

Siehe das folgende Beispiel für Details:

### Beispiel Callback

```csharp
void FeedReceivedCallback(string message) {
  Feed feed = new Feed(message);
  Debug.Log("Feed received: " + feed);
  foreach (Card card in feed.Cards) {
    Debug.Log("Card: " + card);
  }
}
```

## Aktualisieren des Newsfeeds

Um den Newsfeed von Braze zu aktualisieren, rufen Sie eine der folgenden Methoden auf:

```csharp
// results in a network request to Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

Beide Methoden benachrichtigen Ihren News Feed-Hörer und geben den News Feed an Ihre Callback-Methode weiter.

## Analytics

Klicks und Impressionen müssen für Karten, die nicht direkt von Braze angezeigt werden, manuell protokolliert werden.

Verwenden Sie `LogClick()` und `LogImpression()` auf der [Karte](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs), um Klicks und Impressionen für bestimmte Karten zu protokollieren.

Um zu protokollieren, dass der Nutzer den Feed als Ganzes angesehen hat, rufen Sie `AppboyBinding.LogFeedDisplayed()` auf.

