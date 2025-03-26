---
nav_title: Content-Cards
article_title: Inhaltskarten für Unity
platform: 
  - Unity
  - iOS
  - Android
channel: content cards
page_order: 4
description: "Dieser Referenzartikel behandelt die Richtlinien zur Implementierung von Content-Cards für die Unity-Plattform wie das Anzeigen von Karten, das Parsen von Karten und die Analyse."

---

# Integration von Inhaltskarten

> Dieser Referenzartikel behandelt die Richtlinien zur Implementierung von Content-Cards für die Unity-Plattform wie das Anzeigen von Karten, das Parsen von Karten und die Analyse.

## Native Anzeige von Content-Cards {#unity-content-cards-native-ui}

Mit dem folgenden Aufruf können Sie die Standard-Benutzeroberfläche für Inhaltskarten anzeigen:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Empfangen von Inhaltskartendaten in Unity

Sie können Unity-Spielobjekte registrieren, um über eingehende Content-Cards benachrichtigt zu werden. Wir empfehlen Ihnen, Spielobjekt-Listener über den Braze-Konfigurationseditor einzustellen.

Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.CONTENT_CARDS_UPDATED` an.

Beachten Sie, dass zusätzlich ein Aufruf an `AppboyBinding.RequestContentCardsRefresh()` erforderlich ist, um unter iOS Daten in Ihrem Spielobjekt-Listener zu empfangen.

## Parsen von Inhaltskarten

Eingehende Nachrichten des Typs `string`, die im Spielobjekt-Callback von Content-Cards empfangen werden, können in unser vorgefertigtes Modellobjekt [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) geparst werden.

Das Parsen von Content-Cards erfordert JSON-Parsing. Einzelheiten sind dem folgenden Beispiel zu entnehmen:

##### Beispiel für das Callback von Content-Cards

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

## Aktualisieren von Inhaltskarten

Um Content-Cards von Braze zu aktualisieren, rufen Sie eine der folgenden Methoden auf:

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/content_cards.md %}

## Analytics

Klicks und Impressionen müssen für Content-Cards, die nicht direkt von Braze angezeigt werden, manuell protokolliert werden.

Verwenden Sie `LogClick()` und `LogImpression()` auf [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs), um Klicks und Impressionen für bestimmte Karten zu protokollieren.

