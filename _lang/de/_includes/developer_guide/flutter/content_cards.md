## Über Flutter-Content-Cards

Das Braze SDK enthält einen Standard-Kartenfeed, der Ihnen den Einstieg in die Arbeit mit Content-Cards erleichtert. Sie können den Kartenfeed mit der Methode `braze.launchContentCards()` anzeigen. Der im Braze SDK enthaltene Standard-Kartenfeed verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content-Cards.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Karten-Methoden

Sie können diese zusätzlichen Methoden verwenden, um einen angepassten Content-Cards-Feed in Ihrer App zu erstellen. Die folgenden Methoden sind in der [öffentlichen Schnittstelle des Plugins](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart) verfügbar:

| Methode                                         | Beschreibung                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Fordert die neuesten Content-Cards vom Braze SDK-Server an.                                           |
| `braze.logContentCardClicked(contentCard)`    | Protokolliert einen Klick für das angegebene Content-Card-Objekt.                                                            |
| `braze.logContentCardImpression(contentCard)` | Protokolliert eine Impression für das angegebene Content-Card-Objekt.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Protokolliert eine Ausblendung für das angegebene Content-Card-Objekt.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Empfangen von Content-Card-Daten

Um Content-Card-Daten in Ihrer Flutter-App zu empfangen, unterstützt `BrazePlugin` das Senden von Content-Card-Daten mithilfe von [Dart-Streams](https://dart.dev/tutorials/language/streams).

Das [Objekt](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` unterstützt eine Teilmenge der Felder, die in den nativen Modellobjekten verfügbar sind, darunter `description`, `title`, `image`, `url`, `extras` und weitere.

### Auf Content-Card-Daten im Dart-Layer lauschen

Um Content-Card-Daten im Dart-Layer zu empfangen, verwenden Sie den folgenden Code, um eine `StreamSubscription` zu erstellen und `braze.subscribeToContentCards()` aufzurufen. Denken Sie daran, das Stream-Abo mit `cancel()` zu beenden, wenn Sie es nicht mehr benötigen.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Ein Beispiel finden Sie in [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) in der Braze Flutter SDK-Beispiel-App.

### Weiterleitung von Content-Card-Daten aus der nativen iOS-Schicht

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Content-Card-Daten werden automatisch von der nativen Android- und iOS-Schicht weitergeleitet. Es ist keine zusätzliche Einrichtung erforderlich.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Wenn Sie Flutter SDK 17.1.0 oder älter verwenden, muss die Weiterleitung von Content-Card-Daten aus der nativen iOS-Schicht manuell eingerichtet werden. Ihre Anwendung enthält wahrscheinlich einen `contentCards.subscribeToUpdates`-Callback, der `BrazePlugin.processContentCards(contentCards)` aufruft. Um auf Flutter SDK 18.0.0 zu migrieren, entfernen Sie den Aufruf von `BrazePlugin.processContentCards(_:)` – die Datenweiterleitung wird jetzt automatisch verarbeitet.

Ein Beispiel finden Sie in [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in der Braze Flutter SDK-Beispiel-App.

{% endtab %}
{% endtabs %}

#### Wiederholung des Callbacks für Content-Cards

Um alle Content-Cards zu speichern, die getriggert wurden, bevor der Callback verfügbar ist, und sie nach dem Setzen des Callbacks erneut abzuspielen, fügen Sie bei der Initialisierung von `BrazePlugin` den folgenden Eintrag in die `customConfigs`-Map ein:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
