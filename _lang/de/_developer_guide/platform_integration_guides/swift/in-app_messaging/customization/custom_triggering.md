---
nav_title: Benutzerdefinierte Triggerung
article_title: Anpassen des Auslösens von In-App-Nachrichten für iOS
platform: Swift
page_order: 6
description: "Dieser Referenzartikel beschreibt das angepasste Triggern von iOS-In-App-Nachrichten für das Swift SDK."
channel:
  - in-app messages
---

# Angepasstes Triggern

> Standardmäßig werden In-App-Nachrichten durch Events ausgelöst, die vom SDK protokolliert werden. Alternativ können Sie In-App-Nachrichten auch durch vom Server gesendete Events triggern.

Um In-App-Nachrichten über serverseitige Events zu triggern, senden Sie eine stille Push-Benachrichtigung an das Gerät, damit das Gerät ein SDK-basiertes Event protokollieren kann. Dieses SDK-Event kann dann die In-App-Nachricht für den Nutzer auslösen.

## Schritt 1: Stille Push-Benachrichtigungen und Schlüssel-Wert-Paare verarbeiten

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

## Schritt 2: Erstellen Sie eine stille Push-Kampagne

Erstellen Sie eine [Kampagne mit einer stillen Push-Benachrichtigung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/), die über das vom Server gesendete Event ausgelöst wird. 

![In-App-Nachrichten-Kampagne mit aktionsbasierter Zustellung an die Nutzer, deren Nutzerprofile das angepasste Event "server_event" enthalten.]({% image_buster /assets/img_archive/iosServerSentPush.png %})

Die Push-Kampagne muss zusätzliche Schlüssel-Wert-Paare (Extras) enthalten, die angeben, dass diese Push-Kampagne gesendet wird, um ein angepasstes SDK-Event zu protokollieren. Dieses Event wird zum Triggern der In-App-Nachricht verwendet.

![In-App-Nachrichten-Kampagne mit aktionsbasierter Zustellung und zwei Schlüssel-Wert-Paaren. "CAMPAIGN_NAME" ist auf "In-app message name example" und "IS_SERVER_EVENT" ist auf "true" gesetzt.]({% image_buster /assets/img_archive/iOSServerPush.png %})

Der Code in der Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` prüft auf den Schlüssel `IS_SERVER_EVENT` und protokolliert ein angepasstes SDK-Event, wenn dieser vorhanden ist.

Sie können entweder den Event-Namen oder die Event- Eigenschaften ändern, indem Sie den gewünschten Wert in den zusätzlichen Schlüssel-Wert-Paaren (Extras) der Push-Nutzlast senden. Bei der Protokollierung des angepassten Events können diese Extras entweder als Parameter des Event-Namens oder der Event- Eigenschaft verwendet werden.

## Schritt 3: In-App-Kampagne erstellen

Erstellen Sie im Braze-Dashboard eine für Ihre Nutzer sichtbare In-App-Nachrichten-Kampagne. Diese Kampagne sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event ausgelöst werden, das in der Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` protokolliert wird.

Im folgenden Beispiel wurde die zu triggernde In-App-Nachricht konfiguriert, indem die Event-Eigenschaft im Rahmen der ursprünglichen stillen Push-Benachrichtigung gesendet wurde.

![In-App-Nachrichten-Kampagne mit aktionsbasierter Zustellung an die Nutzer, die das angepasste Event "In-App-Nachrichten-Trigger" ausführen, wobei "campaign_name" auf "IAM Campaign Name Example" gesetzt ist.]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Beachten Sie, dass diese In-App-Nachrichten nur ausgelöst werden, wenn sich die Anwendung beim Empfang der stillen Push-Benachrichtigung im Vordergrund befindet.
{% endalert %}

