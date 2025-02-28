---
nav_title: Zustellung von In-App-Nachrichten
article_title: In-App Nachrichtenzustellung für iOS
platform: Swift
page_order: 2
description: "Dieser Artikel beschreibt die Zustellung von iOS-In-App-Nachrichten. Außerdem behandelt er verschiedene Trigger-Typen, Zustellungssemantiken und Schritte zur Auslösung von Events für das Swift SDK."
channel:
  - in-app messages

---

# Zustellung von In-App-Nachrichten

> Dieser Referenzartikel gibt einen Überblick über die Zustellung von iOS-In-App-Nachrichten. Außerdem behandelt er verschiedene Trigger-Typen, Zustellungssemantiken und Schritte zur Auslösung von Events.

## Auslöser-Typen

In-App-Nachrichten werden durch Events ausgelöst, die vom SDK protokolliert werden. Sie können eine In-App-Nachricht auf Basis der folgenden Event-Typen triggern: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Außerdem enthalten die Trigger `Specific Purchase` und `Custom Event` robuste Eigenschaftsfilter.

{% alert note %}
Ausgelöste In-App-Nachrichten funktionieren nur bei angepassten Events, die über das Braze SDK protokolliert werden. In-App-Nachrichten können nicht über die API oder durch API-Event (wie Kauf-Events) getriggert werden. Wenn Sie mit iOS arbeiten, lesen Sie unseren Artikel über [das Verfolgen von benutzerdefinierten Ereignissen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/), um mehr zu erfahren.
{% endalert %}

## Aktivieren von In-App-Nachrichten

Damit Braze In-App-Nachrichten anzeigen kann, erstellen Sie eine Implementierung des Protokolls `BrazeInAppMessagePresenter` und weisen Sie es dem optionalen `inAppMessagePresenter` auf Ihrer Braze-Instanz zu. Sie können auch den standardmäßigen UI-Presenter von Braze verwenden, indem Sie ein `BrazeInAppMessageUI`-Objekt instanziieren.

Beachten Sie, dass Sie die Bibliothek `BrazeUI` importieren müssen, um auf die Klasse `BrazeInAppMessageUI` zuzugreifen.

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

## Semantik der Zustellung

Alle In-App-Nachrichten, für die ein Nutzer berechtigt ist, werden zu Beginn der Sitzung an das Gerät des Nutzers gesendet. Bei der Zustellung ruft das SDK die Assets mittels Prefetching ab, damit sie zum Trigger-Zeitpunkt sofort verfügbar sind und die Anzeige-Latenzzeit minimiert wird.

Wenn ein Trigger-Event mit mehr als einer in Frage kommenden In-App-Nachricht verbunden ist, wird nur die In-App-Nachricht mit der höchsten Priorität zugestellt.

Bei In-App-Nachrichten, die sofort nach der Zustellung angezeigt werden (Sitzungsstart, Push-Klick), kann es zu einer gewissen Latenz kommen, da die Assets nicht mittels Prefetching abgerufen werden. Weitere Informationen über die Sitzungsstart-Semantik des SDK finden Sie unter [Lebenszyklus einer Sitzung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

## Mindestzeitintervall zwischen Auslösern

Standardmäßig begrenzen wir die Anzahl der In-App-Nachrichten auf einmal alle 30 Sekunden, um ein hochwertiges Nutzererlebnis zu ermöglichen.

Sie können diesen Wert überschreiben, indem Sie die Eigenschaft `triggerMinimumTimeInterval` in Ihrer Braze-Konfiguration festlegen. Stellen Sie sicher, dass Sie diesen Wert konfigurieren, bevor Sie Ihre Braze-Instanz initialisieren. Stellen Sie `triggerMinimumTimeInterval` auf den ganzzahligen Wert ein, den Sie als Mindestzeit in Sekunden zwischen In-App-Nachrichten angeben möchten:

{% tabs %}
{% tab schnell %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## Wenn kein passender Trigger gefunden wird

Wenn Braze keinen passenden Trigger für ein bestimmtes Event findet, wird [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/) aufgerufen. Implementieren Sie diese Methode in Ihrer Klasse und verwenden Sie `BrazeDelegate` für dieses Szenario. 

## In-App-Nachrichten-Stack

### Hinzufügen von In-App-Nachrichten zum Stapel

In den folgenden Situationen sind Nutzer zum Empfang von In-App-Nachrichten berechtigt:

- Wenn ein Event zum Triggern einer In-App-Nachricht ausgelöst wird
- Wenn eine Sitzung gestartet wird
- Die App wird über eine Push-Benachrichtigung geöffnet

Wenn das Event zum Triggern einer In-App-Nachricht ausgelöst wird, wird die Nachricht auf einem "Stack" platziert. Wenn sich mehrere In-App-Nachrichten im Stack befinden und darauf warten, angezeigt zu werden, zeigt Braze die zuletzt empfangene In-App-Nachricht zuerst an ("Last In-First Out"-Prinzip).

Wenn ein Nutzer zum Empfang einer In-App-Nachricht berechtigt ist, fordert `BrazeInAppMessagePresenter` die neueste In-App-Nachricht aus dem In-App-Nachrichten-Stack an. Der Stack hält nur gespeicherte In-App-Nachrichten im Speicher und wird zwischen den App-Starts aus dem angehaltenen Modus geleert.

### Rückgabe von In-App-Nachrichten an den Stack

Eine getriggerte In-App-Nachricht kann in den folgenden Situationen an den Stack zurückgegeben werden:

- Die In-App-Nachricht wird ausgelöst, wenn sich die App im Hintergrund befindet.
- Eine weitere In-App-Nachricht ist derzeit sichtbar.
- Die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` hat `.reenqueue` zurückgegeben.

Die ausgelöste In-App-Nachricht wird oben auf dem Stapel platziert, damit sie später angezeigt werden kann, wenn ein Nutzer für den Empfang einer In-App-Nachricht berechtigt ist.

### Verwerfen von In-App-Nachrichten

Eine getriggerte In-App-Nachricht wird in den folgenden Situationen verworfen:

- Die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` hat `.discard` zurückgegeben.
- Das Asset (Bild oder ZIP-Datei) der In-App-Nachricht konnte nicht heruntergeladen werden.
- Die In-App-Nachricht ist zur Anzeige bereit, aber das Timeout wurde überschritten.
- Die Ausrichtung des Geräts stimmt nicht mit der Ausrichtung der ausgelösten In-App-Nachricht überein.

Die In-App-Nachricht wird aus dem Stapel entfernt. Eine In-App-Nachricht, die verworfen wurde, kann zu einem späteren Zeitpunkt durch eine andere Instanz des Trigger-Events ausgelöst werden.

## Erstellung und Anzeige von In-App-Nachrichten in Echtzeit

Wenn Sie eine In-App-Nachricht zu anderen Zeitpunkten in Ihrer App anzeigen möchten, können Sie manuell die Methode [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) im `inAppMessagePresenter` aufrufen. In-App-Nachrichten können lokal in der App erstellt und über Braze angezeigt werden. Dies ist besonders nützlich für die Anzeige von Nachrichten, die Sie in Echtzeit in der App auslösen möchten.

Beachten Sie, dass Sie durch die Erstellung einer eigenen In-App-Nachricht das Analytics-Tracking ablehnen und die Protokollierung von Klicks und Impressionen manuell über Ihre `message.context` vornehmen müssen.

{% tabs %}
{% tab schnell %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

## Schlüssel-Wert-Paar-Extras

Objekte des Typs `Braze.InAppMessage` können Schlüssel-Wert-Paare als `extras` enthalten. Diese werden bei der Erstellung einer Kampagne auf dem Dashboard angegeben. Schlüssel-Wert-Paare können verwendet werden, um Daten mit einer In-App-Nachricht zur weiteren Bearbeitung durch Ihre App zu senden.

Angenommen, wird möchten die Darstellung einer In-App-Nachricht auf der Grundlage der Inhalte ihrer Extras anpassen. Wir könnten auf die Schlüssel-Wert-Paare in der Eigenschaft `extras` zugreifen und eine angepasste Logik für die Ausführung definieren:

{% tabs %}
{% tab schnell %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

Eine vollständige Implementierung finden Sie in den Beispielen für die Anpassung von In-App-Nachrichten in unserer [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

