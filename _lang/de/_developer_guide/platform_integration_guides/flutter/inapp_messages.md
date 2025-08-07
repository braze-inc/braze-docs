---
nav_title: In-App-Nachrichten
article_title: In-App-Nachrichten für Flutter
platform: Flutter
page_order: 4
page_type: reference
description: "Dieser Artikel behandelt In-App-Nachrichten für iOS- und Android-Apps mit Flutter, einschließlich der Anpassung und Protokollierung von Analysen."
channel: in-app messages

---

# Integration von In-App-Nachrichten

> Erfahren Sie, wie Sie In-App-Nachrichten für Android und iOS mit Flutter integrieren und anpassen können.

## In-App-Nachrichten-UI aktivieren

Um das In-App-Messaging von Flutter mit iOS zu integrieren, [aktivieren Sie das In-App Messaging mit dem Braze Swift SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#enabling-in-app-messages). Für Android gibt es keine zusätzlichen Schritte.

## Protokollieren von Analytics

Um Analytics mit Ihrer `BrazeInAppMessage` zu protokollieren, übergeben Sie die Instanz an die gewünschte Analytics-Funktion:
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (zusammen mit dem Button-Index)

Zum Beispiel:
```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Deaktivieren der automatischen Anzeige

Um die automatische Anzeige von In-App-Nachrichten zu deaktivieren, nehmen Sie diese Aktualisierungen in der nativen Ebene vor.

{% tabs %}
{% tab Android %}

1. Stellen Sie sicher, dass Sie die automatische Initialisierung der Integration verwenden, die ab Version `2.2.0` standardmäßig aktiviert ist.
2. Setzen Sie die Standardeinstellung für In-App-Nachrichten auf `DISCARD`, indem Sie die folgende Zeile in Ihre Datei `braze.xml` einfügen.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

{% endtab %}
{% tab iOS %}

1. Implementieren Sie den Delegaten `BrazeInAppMessageUIDelegate` wie im [iOS-Artikel ](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) beschrieben.

2. Aktualisieren Sie die Delegate-Methode `inAppMessage(_:displayChoiceForMessage:)`, um `.discard` zurückzugeben.

{% endtab %}
{% endtabs %}

## Empfang von In-App-Nachrichten-Daten

Um In-App-Nachrichten-Daten in der Flutter App zu empfangen, unterstützt das `BrazePlugin` das Senden von In-App-Nachrichten-Daten mithilfe von [Dart-Streams](https://dart.dev/tutorials/language/streams).

Das Objekt `BrazeInAppMessage` unterstützt eine Teilmenge der Felder, die in den nativen Modellobjekten verfügbar sind, darunter `uri`, `message`, `header`, `buttons`, `extras` und weitere.

### Schritt 1: Auf In-App-Nachrichten-Daten im Dart-Layer achten

Um die Daten der In-App-Nachricht im Dart-Layer zu empfangen, verwenden Sie den folgenden Code, um `StreamSubscription` zu erstellen und `braze.subscribeToInAppMessages()` aufzurufen. Denken Sie daran, das Stream-Abo auf `cancel()` zu setzen, wenn Sie es nicht mehr benötigen.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

Ein Beispiel finden Sie [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) in unserer Beispiel-App.

### Schritt 2: In-App-Nachrichten-Daten aus dem nativen Layer weiterleiten

Um die Daten im Dart-Layer aus Schritt 1 zu empfangen, fügen Sie den folgenden Code hinzu, um die In-App-Nachrichten-Daten aus den nativen Layern weiterzuleiten.

{% tabs %}
{% tab Android %}

Die In-App-Nachrichtendaten werden automatisch von der Android-Ebene weitergeleitet.

{% endtab %}
{% tab iOS %}

### Option 1: Verwendung von `BrazeInAppMessageUIDelegate`

1. Implementieren Sie den Delegaten `BrazeInAppMessageUIDelegate` wie im iOS-Artikel zum [Delegaten für In-App-Nachrichten](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) beschrieben.

2. Aktualisieren Sie Ihre [`willPresent` Delegatenimplementierung](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv), um `BrazePlugin.process(inAppMessage)` aufzurufen.

### Option 2 - Benutzerdefinierter In-App-Nachrichtenpräsenter

1. Vergewissern Sie sich, dass Sie die In-App-Nachrichten-Benutzeroberfläche aktiviert haben und stellen Sie `inAppMessagePresenter` auf Ihren benutzerdefinierten Präsentator ein.
```swift
    let inAppMessageUI = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = inAppMessageUI
```
2. Erstellen Sie Ihre eigene Presenter-Klasse und rufen Sie `BrazePlugin.process(inAppMessage)` innerhalb von [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra).
```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    // Pass in-app message data to the Dart layer.
    BrazePlugin.processInAppMessage(message)

    // If you want the default UI to display the in-app message.
    super.present(message: message)
  }
}
```

{% endtab %}
{% endtabs %}

#### Wiederholung des Rückrufs für In-App-Nachrichten

Um alle vor dem Callback getriggerten In-App-Nachrichten zu speichern und nach dem Setzen des Callbacks erneut wiederzugeben, fügen Sie bei der Initialisierung von `BrazePlugin` Folgendes in `customConfigs` ein:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Testen einer Beispiel-In-App-Nachricht

Gehen Sie zum Testen einer Beispiel-In-App-Nachricht wie folgt vor.

1. Legen Sie einen aktiven Nutzer in der React-Anwendung fest, indem Sie die Methode `braze.changeUser('your-user-id')` aufrufen.
2. Gehen Sie auf die Seite **Kampagnen** in Ihrem Dashboard und folgen Sie [dieser Anleitung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), um eine neue In-App-Kampagne zu erstellen.
3. Erstellen Sie Ihre In-App-Messaging-Kampagne und gehen Sie auf die Registerkarte **Test**. Fügen Sie die gleiche `user-id` wie der Testbenutzer hinzu und klicken Sie auf **Test senden**.
4. Tippen Sie auf die Push-Benachrichtigung und die In-App-Nachricht sollte auf Ihrem Gerät angezeigt werden.

## GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

![In-App-Nachrichten-Kampagne von Braze, bei der Sie Ihre eigene Nutzer-ID als Testempfänger hinzufügen können, um Ihre In-App-Nachrichten zu testen.]({% image_buster /assets/img/react-native/iam-test.png %} "In-App-Messaging-Test")

