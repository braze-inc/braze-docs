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

Für den Zugriff auf In-App-Nachrichten-Daten in Ihrer Flutter-App unterstützt das `BrazePlugin` das Senden von In-App-Nachrichten-Daten über [Dart Streams](https://dart.dev/tutorials/language/streams).

Das `BrazeInAppMessage`-Objekt unterstützt eine Teilmenge der Felder, die in den nativen Modellobjekten verfügbar sind, darunter `uri`, `message`, `header`, `buttons`, `extras` und weitere.

### Auf In-App-Nachrichten-Daten im Dart-Layer lauschen

Um In-App-Nachrichten-Daten im Dart-Layer zu empfangen, verwenden Sie den folgenden Code, um eine `StreamSubscription` zu erstellen und `braze.subscribeToInAppMessages()` aufzurufen. Denken Sie daran, das Stream-Abo mit `cancel()` zu beenden, wenn es nicht mehr benötigt wird.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

Ein Beispiel finden Sie in [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) in der Braze Flutter SDK Beispiel-App.

### In-App-Nachrichten-Daten aus dem nativen Layer weiterleiten

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

In-App-Nachrichten-Daten werden automatisch von den nativen Android- und iOS-Layern weitergeleitet. Es ist keine zusätzliche Einrichtung erforderlich.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Wenn Sie Flutter SDK 17.1.0 oder älter verwenden, erfordert die Weiterleitung von In-App-Nachrichten-Daten aus dem nativen iOS-Layer eine manuelle Einrichtung. Ihre Anwendung enthält wahrscheinlich eine der folgenden Varianten. Um auf Flutter SDK 18.0.0 zu migrieren, entfernen Sie den Aufruf von `BrazePlugin.processInAppMessage(_:)` – die Datenweiterleitung wird jetzt automatisch gehandhabt.

{% subtabs %}
{% subtab UI Delegate %}

Entfernen Sie den Aufruf von `BrazePlugin.processInAppMessage(_:)` aus Ihrer [`willPresent`-Delegatenimplementierung](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv).

{% endsubtab %}

{% subtab Custom presenter %}

Entfernen Sie den Aufruf von `BrazePlugin.processInAppMessage(message)` aus der [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra)-Implementierung Ihres angepassten Presenters:

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

### Callback für In-App-Nachrichten erneut abspielen (optional)

Um alle In-App-Nachrichten zu speichern, die getriggert wurden, bevor der Callback verfügbar ist, und sie nach dem Setzen des Callbacks erneut abzuspielen, fügen Sie bei der Initialisierung des `BrazePlugin` den folgenden Eintrag in die `customConfigs`-Map ein:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
