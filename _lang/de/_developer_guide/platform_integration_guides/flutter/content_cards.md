---
nav_title: Content-Cards
article_title: Inhaltskarten für Flutter
platform: Flutter
page_order: 3
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie Content-Cards für Flutter-Apps einsetzen können."
channel: content cards

---

# Integration von Inhaltskarten

> Dieser Artikel beschreibt, wie Sie Content-Cards für Ihre Flutter-App einrichten.

Das Braze SDK enthält einen Standard-Kartenfeed, der Ihnen den Einstieg in die Arbeit mit Content-Cards erleichtert. Sie können den Kartenfeed mit der Methode `braze.launchContentCards()` anzeigen. Der im Braze SDK enthaltene Standard-Kartenfeed verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content-Cards.

## Anpassung

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

## Test mit Anzeige der Beispiel-Inhaltskarte

Gehen Sie zum Testen einer Beispiel-Content-Card wie folgt vor.

1. Legen Sie einen aktiven Nutzer in der React-Anwendung fest, indem Sie die Methode `braze.changeUserId('your-user-id')` aufrufen.
2. Gehen Sie zu **Kampagnen** und folgen Sie [dieser Anleitung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create), um eine neue Content Card Kampagne zu erstellen.
3. Erstellen Sie Ihre Test-Inhaltskarten-Kampagne und gehen Sie auf die Registerkarte **Test**. Fügen Sie die gleiche `user-id` wie der Testbenutzer hinzu und klicken Sie auf **Test senden**.
4. Tippen Sie auf die Push-Benachrichtigung, um eine Content Card auf Ihrem Gerät zu starten. Möglicherweise müssen Sie Ihren Feed aktualisieren, damit er angezeigt wird.

![Eine Braze Content Card Kampagne, bei der Sie Ihre eigene Benutzer-ID als Testempfänger hinzufügen können, um Ihre Content Card zu testen.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

Weitere Details zu den einzelnen Plattformen finden Sie in den Anleitungen zur [Android-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/) oder [iOS-Integration](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui).

## GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/content_cards.md %}

