{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Nachrichten triggern

### Auslöser-Typen

In-App-Nachrichten werden automatisch getriggert, wenn das SDK einen der folgenden angepassten Event-Typen protokolliert: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, und `Push Click`. Beachten Sie, dass die Trigger `Specific Purchase` und `Custom Event` auch robuste Filter für Eigenschaften enthalten.

{% alert note %}
In-App-Nachrichten können nicht über die API oder durch API-Ereignisse ausgelöst werden, sondern nur durch angepasste Events, die vom SDK protokolliert werden. Wenn Sie mehr über die Protokollierung erfahren möchten, lesen Sie den Abschnitt [Protokollierung angepasster Events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift).
{% endalert %}

### Semantik der Zustellung

Alle in Frage kommenden In-App-Nachrichten werden dem Gerät eines Nutzers:innen zu Beginn seiner Sitzung zugestellt. Wenn es zugestellt wird, holt das SDK die Assets im Voraus, so dass sie zum Zeitpunkt des Triggerns verfügbar sind und die Anzeige-Latenzzeit minimiert wird. Wenn das triggernde Ereignis mehr als eine in Frage kommende In-App-Nachricht hat, wird nur die Nachricht mit der höchsten Priorität zugestellt.

Weitere Informationen über die Semantik des SDK für den Sitzungsstart finden Sie[unterSitzungslebenszyklus]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift).

### Standard Rate-Limits

Standardmäßig können Sie einmal alle 30 Sekunden eine In-App-Nachricht senden.

Um dies außer Kraft zu setzen, fügen Sie die Eigenschaft `triggerMinimumTimeInterval` zu Ihrer Braze-Konfiguration hinzu, bevor die Braze-Instanz initialisiert wird. Er kann auf eine beliebige positive ganze Zahl gesetzt werden und stellt das minimale Zeitintervall in Sekunden dar. Zum Beispiel:

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

## Schlüssel-Wert-Paare

Wenn Sie eine Kampagne in Braze erstellen, können Sie Schlüssel-Wert-Paare als `extras` festlegen, die das In-App-Nachricht-Objekt verwenden kann, um Daten an Ihre App zu senden. Zum Beispiel:

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

## Deaktivieren von automatischen Triggern

So verhindern Sie, dass In-App-Nachrichten automatisch ausgelöst werden:

1. Implementieren Sie den Delegaten `BrazeInAppMessageUIDelegate` wie im [iOS-Artikel ](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) beschrieben.
2. Aktualisieren Sie die Delegate-Methode `inAppMessage(_:displayChoiceForMessage:)`, um `.discard` zurückzugeben.

## Manuelles Auslösen von Nachrichten

### Ein serverseitiges Ereignis verwenden

Um In-App-Nachrichten über serverseitige Events zu triggern, senden Sie eine stille Push-Benachrichtigung an das Gerät, damit das Gerät ein SDK-basiertes Event protokollieren kann. Dieses SDK-Event kann dann die In-App-Nachricht für den Nutzer auslösen.

#### Schritt 1: Stille Push-Benachrichtigungen und Schlüssel-Wert-Paare verarbeiten

Implementieren Sie die folgende Funktion und rufen Sie sie in der [Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) auf:

{% tabs %}
{% tab schnell %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Beim Empfang einer stillen Push-Benachrichtigung wird ein vom SDK aufgezeichnetes Event des Typs "In-App-Nachrichten-Trigger" im Nutzerprofil protokolliert. 

{% alert important %}
Da eine Push-Nachricht verwendet wird, um ein vom SDK protokolliertes angepasstes Event aufzuzeichnen, muss Braze ein Push-Token für jeden Nutzer speichern, um diese Lösung zu aktivieren. Für iOS-Nutzer speichert Braze ein Token erst ab dem Zeitpunkt, an dem ein Nutzer den Push-Prompt des Betriebssystems erhalten hat. Davor ist der Nutzer nicht per Push erreichbar und die obige Lösung nicht möglich.
{% endalert %}

#### Schritt 2: Erstellen Sie eine stille Push-Kampagne

Erstellen Sie eine [Kampagne mit einer stillen Push-Benachrichtigung]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift), die über das vom Server gesendete Event ausgelöst wird. 

![In-App-Nachrichten-Kampagne mit aktionsbasierter Zustellung an die Nutzer, deren Nutzerprofile das angepasste Event "server_event" enthalten.]({% image_buster /assets/img_archive/iosServerSentPush.png %})

Die Push-Kampagne muss zusätzliche Schlüssel-Wert-Paare (Extras) enthalten, die angeben, dass diese Push-Kampagne gesendet wird, um ein angepasstes SDK-Event zu protokollieren. Dieses Event wird zum Triggern der In-App-Nachricht verwendet.

![In-App-Nachrichten-Kampagne mit aktionsbasierter Zustellung und zwei Schlüssel-Wert-Paaren. "CAMPAIGN_NAME" ist auf "In-app message name example" und "IS_SERVER_EVENT" ist auf "true" gesetzt.]({% image_buster /assets/img_archive/iOSServerPush.png %})

Der Code in der Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` prüft auf den Schlüssel `IS_SERVER_EVENT` und protokolliert ein angepasstes SDK-Event, wenn dieser vorhanden ist.

Sie können entweder den Event-Namen oder die Event- Eigenschaften ändern, indem Sie den gewünschten Wert in den zusätzlichen Schlüssel-Wert-Paaren (Extras) der Push-Nutzlast senden. Bei der Protokollierung des angepassten Events können diese Extras entweder als Parameter des Event-Namens oder der Event- Eigenschaft verwendet werden.

#### Schritt 3: In-App-Kampagne erstellen

Erstellen Sie im Braze-Dashboard eine für Ihre Nutzer sichtbare In-App-Nachrichten-Kampagne. Diese Kampagne sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event ausgelöst werden, das in der Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` protokolliert wird.

Im folgenden Beispiel wurde die zu triggernde In-App-Nachricht konfiguriert, indem die Event-Eigenschaft im Rahmen der ursprünglichen stillen Push-Benachrichtigung gesendet wurde.

![In-App-Nachrichten-Kampagne mit aktionsbasierter Zustellung an die Nutzer, die das angepasste Event "In-App-Nachrichten-Trigger" ausführen, wobei "campaign_name" auf "IAM Campaign Name Example" gesetzt ist.]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Beachten Sie, dass diese In-App-Nachrichten nur ausgelöst werden, wenn sich die Anwendung beim Empfang der stillen Push-Benachrichtigung im Vordergrund befindet.
{% endalert %}

### Anzeigen einer vordefinierten

Um eine vordefinierte In-App-Nachricht manuell anzuzeigen, verwenden Sie die folgende Methode:

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### Anzeige einer Nachricht in Realtime

Sie können auch lokale In-App-Nachrichten in Realtime anzeigen, indem Sie manuell die [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) Methode auf Ihrer `inAppMessagePresenter` aufrufen. Zum Beispiel:

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

{% alert note %}
Wenn Sie Ihre eigene In-App-Nachricht erstellen, verzichten Sie auf jegliches Analytics Tracking und müssen die Protokollierung von Klicks und Impressionen manuell über Ihr `message.context` vornehmen.
{% endalert %}

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
