## Über Flutter Content-Cards

Das Braze SDK enthält einen Standard-Kartenfeed, der Ihnen den Einstieg in die Arbeit mit Content-Cards erleichtert. Sie können den Kartenfeed mit der Methode `braze.launchContentCards()` anzeigen. Der im Braze SDK enthaltene Standard-Kartenfeed verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content-Cards.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Karten-Methoden

Sie können diese zusätzlichen Methoden verwenden, um einen benutzerdefinierten Content Cards Feed in Ihrer App zu erstellen, indem Sie die folgenden Methoden verwenden, die in der [öffentlichen Schnittstelle des Plugins](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart) verfügbar sind:

| Methode                                         | Beschreibung                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Fordert die neuesten Inhaltskarten vom Braze SDK-Server an.                                           |
| `braze.logContentCardClicked(contentCard)`    | Protokolliert einen Klick für das angegebene Content Card Objekt.                                                            |
| `braze.logContentCardImpression(contentCard)` | Protokolliert einen Abdruck für das angegebene Content Card Objekt.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Protokolliert eine Kündigung für das angegebene Content Card Objekt.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Empfangen von Content-Card-Daten

Um Content-Card-Daten in Ihrer Flutter-App zu empfangen, unterstützt `BrazePlugin` das Senden von Content-Card-Daten mithilfe von [Dart-Streams](https://dart.dev/tutorials/language/streams).

Das [Objekt](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` unterstützt eine Teilmenge der Felder, die in den nativen Modellobjekten verfügbar sind, darunter `description`, `title`, `image`, `url`, `extras` und weitere.

### Schritt 1: Auf Content-Card-Daten im Dart-Layer achten

Um die Daten der Content-Cards im Dart-Layer zu empfangen, verwenden Sie den folgenden Code, um `StreamSubscription` zu erstellen und `braze.subscribeToContentCards()` aufzurufen. Denken Sie daran, das Stream-Abo auf `cancel()` zu setzen, wenn Sie es nicht mehr benötigen.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Ein Beispiel finden Sie [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) in unserer Beispiel-App.

### Schritt 2: Weiterleitung von Content Card-Daten aus der nativen Schicht

Um die Daten im Dart-Layer aus Schritt 1 zu empfangen, fügen Sie den folgenden Code hinzu, um die Content-Card-Daten aus den nativen Layern weiterzuleiten.

{% tabs %}
{% tab Android %}

Die Daten der Content Card werden automatisch von der Android-Ebene weitergeleitet.

{% endtab %}
{% tab iOS %}

1. Implementieren Sie `contentCards.subscribeToUpdates`, um Content-Cards Updates zu abonnieren. Eine Beschreibung hierzu finden Sie in der Dokumentation [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)).

2. Ihre `contentCards.subscribeToUpdates` Callback-Implementierung muss `BrazePlugin.processContentCards(contentCards)` aufrufen.

Ein Beispiel finden Sie [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in unserer Beispiel-App.

{% endtab %}
{% endtabs %}

#### Wiederholung des Rückrufs für Inhaltskarten

Um alle vor dem Callback getriggerten Content-Cards zu speichern und nach dem Setzen des Callbacks erneut wiederzugeben, fügen Sie bei der Initialisierung von `BrazePlugin` Folgendes in `customConfigs` ein:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
