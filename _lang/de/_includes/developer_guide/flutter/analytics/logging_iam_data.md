{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Protokollierung von Nachrichten-Daten

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

## Zugriff auf Nachrichten-Daten

Für den Zugriff auf In-App-Nachricht-Daten in Ihrer Flutter App unterstützt `BrazePlugin` das Senden von In-App-Nachricht-Daten über [Dart Streams](https://dart.dev/tutorials/language/streams).

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
{% subtabs %}

Sie können In-App-Nachricht-Daten auf eine von zwei Arten weiterleiten:

{% subtab ui deligate %}

1. Implementieren Sie den Delegaten `BrazeInAppMessageUIDelegate` wie im iOS-Artikel zum [Delegaten für In-App-Nachrichten](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) beschrieben.

2. Aktualisieren Sie Ihre [`willPresent` Delegatenimplementierung](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv), um `BrazePlugin.process(inAppMessage)` aufzurufen.
{% endsubtab %}

{% subtab custom presenter %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Schritt 3: Wiederholung des Callbacks für In-App-Nachrichten (optional)

Um alle vor dem Callback getriggerten In-App-Nachrichten zu speichern und nach dem Setzen des Callbacks erneut wiederzugeben, fügen Sie bei der Initialisierung von `BrazePlugin` Folgendes in `customConfigs` ein:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
