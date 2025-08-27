---
nav_title: Triggern von Nachrichten
article_title: Auslösen von In-App-Nachrichten über das Braze SDK
page_order: 0.2
description: "Erfahren Sie, wie Sie In-App-Nachrichten über das Braze SDK triggern können."
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# Triggern von In-App-Nachrichten

> Erfahren Sie, wie Sie In-App-Nachrichten über das Braze SDK triggern können.

## Auslöser und Zustellung von Nachrichten

In-App-Nachrichten werden ausgelöst, wenn das SDK einen der folgenden angepassten Event-Typen protokolliert: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase`, und `Custom Event` (die letzten beiden enthalten robuste Filter für Eigenschaften).

Zu Beginn der Sitzung eines Nutzers stellt Braze alle in Frage kommenden In-App-Nachrichten auf dessen Gerät zu, während gleichzeitig Assets vorab abgerufen werden, um die Anzeige-Latenz zu minimieren. Wenn das triggernde Ereignis mehr als eine in Frage kommende In-App-Nachricht hat, wird nur die Nachricht mit der höchsten Priorität zugestellt. Weitere Informationen finden Sie unter [Session Lifecycle]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

{% alert note %}
In-App-Nachrichten können nicht über die API oder durch API-Ereignisse ausgelöst werden, sondern nur durch angepasste Events, die vom SDK protokolliert werden. Wenn Sie mehr über die Protokollierung erfahren möchten, lesen Sie den Abschnitt [Protokollierung angepasster Events]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

## Schlüssel-Wert-Paare

Wenn Sie eine Kampagne in Braze erstellen, können Sie Schlüssel-Wert-Paare als `extras` festlegen, die das In-App-Nachricht-Objekt verwenden kann, um Daten an Ihre App zu senden.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Weitere Informationen finden Sie in der [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab schnell %}
Das folgende Beispiel verwendet eine angepasste Logik, um die Darstellung einer In-App-Nachricht auf der Grundlage ihrer Schlüssel-Wert-Paare in `extras` festzulegen. Ein Beispiel für eine vollständige Anpassung finden Sie in [unserer Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Internet %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}
{% endtabs %}

## Deaktivieren von automatischen Triggern

In-App-Nachrichten werden standardmäßig automatisch getriggert. Um dies zu deaktivieren:

{% tabs %}
{% tab android %}
1. Überprüfen Sie, ob Sie die automatische Initialisierung der Integration verwenden, die in den Versionen `2.2.0` und höher standardmäßig aktiviert ist.
2. Setzen Sie die Standardeinstellung für In-App-Nachrichten auf `DISCARD`, indem Sie die folgende Zeile in Ihre Datei `braze.xml` einfügen.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab schnell %}
1. Implementieren Sie den Delegaten `BrazeInAppMessageUIDelegate` in Ihrer App. Eine vollständige Anleitung finden Sie unter [Tutorial: In-App-Nachricht UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Aktualisieren Sie die Delegate-Methode `inAppMessage(_:displayChoiceForMessage:)`, um `.discard` zurückzugeben.
{% endtab %}

{% tab Internet %}
Entfernen Sie den Aufruf von `braze.automaticallyShowInAppMessages()` in Ihrem Lade-Snippet und erstellen Sie dann eine angepasste Logik für die Anzeige oder Nichtanzeige einer In-App-Nachricht.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Wenn Sie `braze.showInAppMessage` aufrufen, ohne `braze.automaticallyShowInAppMessages()` zu entfernen, werden Nachrichten möglicherweise doppelt angezeigt.
{% endalert %}
{% endtab %}

{% tab Unity %}
{% subtabs %}
{% subtab Android %}
Für Android deaktivieren Sie die Option **In-App-Nachrichten automatisch anzeigen** im Braze Konfigurationseditor. Alternativ können Sie auch `com_braze_inapp_show_inapp_messages_automatically` auf `false` in Ihrem Unity-Projekt `braze.xml` einstellen.

Die anfängliche Anzeige von In-App-Nachrichten kann in der Braze-Konfiguration über die Option "In-App Message Manager Initial Display Operation" eingestellt werden.
{% endsubtab %}

{% subtab iOS %}
Für iOS stellen Sie Spielobjekt-Listener im Braze-Konfigurationseditor ein und stellen Sie sicher, dass **Braze zeigt In-App-Nachrichten** nicht ausgewählt ist.

Die anfängliche Anzeige von In-App-Nachrichten kann in der Braze-Konfiguration über die Option "In-App Message Manager Initial Display Operation" eingestellt werden.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Außerkraftsetzen des Standard Rate-Limits

Standardmäßig können Sie einmal alle 30 Sekunden eine In-App-Nachricht senden. Um dies außer Kraft zu setzen, fügen Sie die folgende Eigenschaft zu Ihrer Konfigurationsdatei hinzu, bevor die Braze-Instanz initialisiert wird. Dieser Wert wird als das neue Rate-Limit in Sekunden verwendet.

{% tabs %}
{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab schnell %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Internet %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}
{% endtabs %}

## Manuelles Auslösen von Nachrichten

Standardmäßig werden In-App-Nachrichten automatisch getriggert, wenn das SDK ein angepasstes Event protokolliert. Darüber hinaus können Sie Nachrichten aber auch manuell triggern, indem Sie die folgenden Methoden verwenden.

### Ein serverseitiges Ereignis verwenden

{% tabs %}
{% tab android %}
Um eine In-App-Nachricht über ein vom Server gesendetes Ereignis auszulösen, senden Sie eine stille Push-Benachrichtigung an das Gerät, die einen angepassten Push-Callback zur Protokollierung eines SDK-basierten Ereignisses ermöglicht. Dieses Ereignis triggert dann die In-App-Nachricht für den Nutzer:innen.

#### Schritt 1: Erstellen Sie einen Push-Callback, um den stillen Push zu empfangen

Registrieren Sie Ihren angepassten Push-Callback, um auf eine bestimmte stille Push-Benachrichtigung zu warten. Weitere Informationen finden Sie unter [Standard Android Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback).

Für die zuzustellende In-App-Nachricht werden zwei Events protokolliert, eines vom Server und eines von Ihrem angepassten Push-Callback. Um sicherzustellen, dass dasselbe Event nicht doppelt vorkommt, sollte das von Ihrem Push Callback protokollierte Event einer generischen Namenskonvention folgen, z. B. "In-App-Nachricht triggern", und nicht denselben Namen tragen wie das vom Server gesendete Event. Andernfalls können die Segmentierung und die Nutzerdaten dadurch beeinträchtigt werden, dass für eine einzelne Nutzer:innen-Aktion doppelte Ereignisse protokolliert werden.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### Schritt 2: Erstellen Sie eine Push-Kampagne

Erstellen Sie eine [stille Push-Kampagne]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android), die über das vom Server gesendete Event getriggert wird.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

Die Push-Kampagne muss Schlüssel-Wert-Paare enthalten, die angeben, dass diese Push-Kampagne gesendet wird, um ein angepasstes SDK-Event zu protokollieren. Dieses Event wird verwendet, um die In-App-Nachricht zu triggern.

![Zwei Sätze von Schlüssel-Wert-Paaren: IS_SERVER_EVENT auf "true" und CAMPAIGN_NAME auf "example campaign name" gesetzt.]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Der frühere Code für den Push Callback erkennt die Schlüssel-Wert-Paare und protokolliert das entsprechende angepasste SDK-Event.

Wenn Sie Ihrem "In-App-Nachricht triggern"-Event Event-Eigenschaften hinzufügen möchten, können Sie diese in den Schlüssel-Wert-Paaren des Push-Payloads übergeben. In diesem Beispiel wurde der Kampagnen-Name der nachfolgenden In-App-Nachricht eingefügt. Ihr angepasster Push Callback kann dann bei der Protokollierung des angepassten Events den Wert als Parameter der Event-Eigenschaft übergeben.

#### Schritt 3: In-App-Kampagne erstellen

Erstellen Sie Ihre für Nutzer sichtbare In-App-Nachricht-Kampagne im Braze-Dashboard. Diese Kampagne sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event ausgelöst werden, das in Ihrem Push-Callback protokolliert wird.

Im folgenden Beispiel wurde die zu triggernde In-App-Nachricht konfiguriert, indem die Event-Eigenschaft im Rahmen des usprünglichen stillen Push gesendet wurde.

![Eine aktionsbasierte Zustellung, bei der eine In-App-Nachricht ausgelöst wird, wenn "campaign_name" gleich "IAM-Kampagnenname Beispiel" ist.]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Wenn ein vom Server gesendetes Event protokolliert wird, während sich die App nicht im Vordergrund befindet, wird das Event protokolliert, aber die In-App-Nachricht wird nicht angezeigt. Wenn Sie möchten, dass das Event verzögert wird, bis die Anwendung im Vordergrund ist, müssen Sie in Ihrem angepassten Push-Empfänger ein Häkchen setzen, um das Event zu verwerfen oder zu verzögern, bis die App in den Vordergrund getreten ist.
{% endtab %}

{% tab schnell %}
#### Schritt 1: Stille Push-Benachrichtigungen und Schlüssel-Wert-Paare verarbeiten

Implementieren Sie die folgende Funktion und rufen Sie sie in der [Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) auf:

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

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
{% endtab %}

{% tab Internet %}
Zur Zeit unterstützt das Internet Braze SDK das manuelle Triggern von Nachrichten über serverseitige Ereignisse nicht.
{% endtab %}
{% endtabs %}

### Anzeige einer vordefinierten Nachricht

Um eine vordefinierte In-App-Nachricht manuell anzuzeigen, verwenden Sie die folgende Methode:

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab schnell %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}

{% tab Internet %}
```javascript
braze.requestInAppMessageDisplay();
```
{% endtab %}
{% endtabs %}

### Anzeige einer Nachricht in Realtime 

Sie können auch In-App-Nachrichten in Echtzeit erstellen und anzeigen, indem Sie dieselben Lokalisierungsoptionen nutzen, die auch auf dem Dashboard zur Verfügung stehen. Um dies zu tun:

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Zeigen Sie keine In-App-Nachrichten an, wenn die Softtastatur auf dem Bildschirm angezeigt wird, da das Rendering unter diesen Umständen undefiniert ist.
{% endalert %}
{% endtab %}

{% tab schnell %}
Rufen Sie manuell die [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) Methode auf Ihrer `inAppMessagePresenter` auf. Zum Beispiel:

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Wenn Sie Ihre eigene In-App-Nachricht erstellen, verzichten Sie auf jegliches Analytics Tracking und müssen die Protokollierung von Klicks und Impressionen manuell über Ihr `message.context` vornehmen.
{% endalert %}
{% endtab %}

{% tab Internet %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab Unity %}
Um die nächste Nachricht im Stack anzuzeigen, verwenden Sie die Methode `DisplayNextInAppMessage()`. Nachrichten werden in diesem Stack gespeichert, wenn `DISPLAY_LATER` oder `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` als Aktion zur Anzeige von In-App-Nachrichten gewählt wurde.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Exit-Intent Nachrichten für das Internet

Exit-Intent-Nachrichten sind In-App-Nachrichten, die ohne Unterbrechung verwendet werden, um Besuchern wichtige Informationen mitzuteilen, bevor sie Ihre Website verlassen.

Um Auslöser für diese Nachrichtentypen im Web SDK einzurichten, implementieren Sie eine Exit-Intent-Bibliothek in Ihrer Website (wie z.B. [die Open-Source-Bibliothek von ouibounce](https://github.com/carlsednaoui/ouibounce)) und verwenden Sie dann den folgenden Code, um `'exit intent'` als angepasstes Event in Braze zu protokollieren. Jetzt können Ihre zukünftigen In-App-Nachricht-Kampagnen diesen Nachrichtentyp als angepassten Event-Trigger verwenden.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
