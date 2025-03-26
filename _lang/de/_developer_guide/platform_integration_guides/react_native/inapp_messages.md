---
nav_title: In-App-Nachrichten
article_title: In-App-Nachrichten für React Native
platform: React Native
page_order: 4
page_type: reference
description: "Dieser Artikel behandelt In-App-Nachrichten für iOS- und Android-Apps mit React Native, einschließlich der Anpassung und Protokollierung von Analytics."
channel: in-app messages

---

# Integration von In-App-Nachrichten

> In-App-Nachrichten werden bei Verwendung von React Native automatisch auf Android und iOS angezeigt. Dieser Artikel behandelt die Anpassung und Protokollierung von Analytics für Ihre In-App-Nachrichten für Apps, die React Native verwenden.

## Zugriff auf In-App-Nachricht-Daten

In den meisten Fällen können Sie die Methode `Braze.addListener` verwenden, um Event-Listener zu registrieren, die Daten aus In-App-Nachrichten verarbeiten. 

Außerdem können Sie auf die Daten der In-App-Nachricht im JavaScript-Layer zugreifen, indem Sie die Methode `Braze.subscribeToInAppMessage` aufrufen, damit die SDKs ein `inAppMessageReceived`-Event veröffentlichen, wenn eine In-App-Nachricht getriggert wird. Übergeben Sie einen Callback an diese Methode, um Ihren eigenen Code auszuführen, wenn die In-App-Nachricht getriggert und vom Listener empfangen wird.

Um das Standard-Verhalten weiter anzupassen oder wenn Sie keinen Zugang zur Anpassung des nativen iOS- oder Android-Codes haben, empfehlen wir Ihnen, das Standard UI zu deaktivieren, während Sie weiterhin In-App Nachrichten-Events von Braze erhalten. Um die Standard-UI zu deaktivieren, übergeben Sie `false` an die Methode `Braze.subscribeToInAppMessage` und verwenden Sie die Daten der In-App-Nachricht, um Ihre eigene Nachricht in JavaScript zu erstellen. Beachten Sie, dass Sie die Analytics Ihrer Nachrichten [manuell protokollieren](#analytics) müssen, wenn Sie die Standard-Benutzeroberfläche deaktivieren möchten.

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});
```

## Fortschrittliche Anpassung

Um eine fortschrittlichere Logik einzubauen, die bestimmt, ob eine In-App-Nachricht über die integrierte UI angezeigt wird oder nicht, implementieren Sie In-App-Nachrichten über den nativen Layer.

{% alert warning %}
Da es sich hierbei um eine fortgeschrittene Anpassungsoption handelt, beachten Sie bitte, dass durch das Überschreiben der Standard-Implementierung von Braze auch die Logik zum Senden von In-App-Nachricht-Events an Ihre JavaScript-Listener aufgehoben wird. Wenn Sie weiterhin `Braze.subscribeToInAppMessage` oder `Braze.addListener` verwenden möchten, wie unter [Zugriff auf In-App-Nachricht-Daten](#accessing-in-app-message-data) beschrieben, müssen Sie die Veröffentlichung der Events selbst übernehmen.
{% endalert %}

{% tabs %}
{% tab Android %}

Implementieren Sie `IInAppMessageManagerListener` wie in unserem Android-Artikel über [angepasste Manager-Listener]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener) beschrieben. In Ihrer `beforeInAppMessageDisplayed`-Implementierung können Sie auf die Daten von `inAppMessage` zugreifen, sie an den JavaScript-Layer senden und anhand des Rückgabewerts entscheiden, ob Sie die native Nachricht anzeigen oder nicht.

Mehr über diese Werte erfahren Sie in unserer [Android Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/).

```java
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Note: return InAppMessageOperation.DISCARD if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab iOS %}
### Überschreiben des Standard UI Delegaten

Standardmäßig wird [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) erstellt und zugewiesen, wenn Sie die Instanz `braze` initialisieren. `BrazeInAppMessageUI` ist eine Implementierung des [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter)-Protokolls und verfügt über die Eigenschaft `delegate`, mit der Sie die Behandlung von empfangenen In-App-Nachrichten anpassen können.

1. Implementieren Sie den Delegaten `BrazeInAppMessageUIDelegate` wie in [diesem iOS-Artikel ](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) beschrieben.

2. In der Delegate-Methode `inAppMessage(_:displayChoiceForMessage:)` können Sie auf die Daten von `inAppMessage` zugreifen, sie an die JavaScript-Schicht senden und anhand des Rückgabewerts entscheiden, ob die native Nachricht angezeigt werden soll oder nicht.

Weitere Einzelheiten zu diesen Werten finden Sie in unserer [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert the message to a JavaScript representation.
  NSData *inAppMessageData = [message json];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };

  // Send to JavaScript.
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```
{% endsubtab %}
{% endsubtabs %}

Um den Delegaten zu verwenden, weisen Sie ihn `brazeInAppMessagePresenter.delegate` zu, nachdem Sie die Instanz `braze` initialisiert haben. 

{% alert note %}
`BrazeUI` kann nur in Objective-C oder Swift importiert werden. Wenn Sie Objective-C++ verwenden, müssen Sie dies in einer separaten Datei behandeln.
{% endalert %}

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

### Native Standard-UI überschreiben

Wenn Sie die Darstellung Ihrer In-App-Nachrichten auf der nativen iOS-Ebene vollständig anpassen möchten, halten Sie sich an das [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter)-Protokoll und weisen Sie Ihren angepassten Presenter nach dem folgenden Beispiel zu:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Analytics und Aktionsmethoden

Sie können diese Methoden nutzen, indem Sie Ihre `BrazeInAppMessage`-Instanz zur Protokollierung von Analytics und zur Durchführung von Aktionen übergeben:

| Methode                                                    | Beschreibung                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Protokolliert einen Klick für die bereitgestellten Daten der In-App-Nachricht.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Protokolliert eine Impression für die bereitgestellten In-App-Nachricht-Daten.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Protokolliert einen Button-Klick für die angegebenen In-App-Nachricht-Daten und die Button-ID.               |
| `hideCurrentInAppMessage()`                               | Beendet die aktuell angezeigte In-App-Nachricht.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Führt die Aktion für eine In-App-Nachricht aus.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Führt die Aktion für einen Button für In-App-Nachrichten aus.                                     |

## Test der Anzeige einer beispielhaften In-App-Nachricht

Folgen Sie diesen Schritten, um eine In-App-Nachricht zu testen.

1. Legen Sie einen aktiven Benutzer in der React-Anwendung fest, indem Sie die Methode `Braze.changeUserId('your-user-id')` aufrufen.
2. Gehen Sie zu **Kampagnen** und folgen Sie [dieser Anleitung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), um eine neue In-App-Nachricht-Kampagne zu erstellen.
3. Erstellen Sie Ihre In-App-Messaging-Kampagne und gehen Sie auf die Registerkarte **Test**. Fügen Sie die gleiche `user-id` wie der Testbenutzer hinzu und klicken Sie auf **Test senden**. Sie sollten in Kürze in der Lage sein, eine In-App-Nachricht auf Ihrem Gerät zu starten.

![Eine Kampagne für In-App-Nachrichten von Braze, bei der Sie Ihre eigene Nutzer als Testempfänger hinzufügen können, um Ihre In-App-Nachrichten zu testen.]({% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test")

Eine Beispielimplementierung finden Sie in BrazeProject im [React Native SDK](https://github.com/braze-inc/braze-react-native-sdk). Weitere Beispiele für Android- und iOS-Implementierungen finden Sie im [Android-](https://github.com/braze-inc/braze-android-sdk) und [iOS-SDK](https://github.com/braze-inc/braze-swift-sdk).

## Datenmodell für In-App-Nachricht

Das Modell für In-App-Nachrichten ist im React Native SDK verfügbar. Braze verfügt über vier In-App-Nachrichtentypen, die dasselbe Datenmodell verwenden: **Slideup**, **Modal**, **Full** und **HTML Full**.

### Eigenschaften des In-App-Nachricht-Modells

Das In-App-Nachricht-Modell bildet die Grundlage für alle In-App-Nachrichten.

|Eigenschaft          | Beschreibung                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | Die JSON-Darstellung der Nachricht.                                                                                |
|`message`         | Der Text der Nachricht.                                                                                                      |
|`header`          | Die Kopfzeile der Nachricht.                                                                                                    |
|`uri`             | Die URI, die mit dem Klick auf den Button verbunden ist.                                                                       |
|`imageUrl`        | Die URL des Bildes der Nachricht.                                                                                                 |
|`zippedAssetsUrl` | Die gezippten Assets, die für die Anzeige von HTML-Inhalten vorbereitet sind.                                                                    |
|`useWebView`      | Gibt an, ob der Klick auf den Button über eine Webansicht umgeleitet werden soll.                                            |
|`duration`        | Die Anzeigedauer der Nachrichten.                                                                                          |
|`clickAction`     | Der Aktionstyp für den Klick auf den Button. Die drei Typen sind: `NEWS_FEED`, `URI`, und `NONE`.                                     |
|`dismissType`     | Die Art des Abschlusses der Nachricht. Die beiden Arten sind: `SWIPE` und `AUTO_DISMISS`.                                                 |
|`messageType`     | Der vom SDK unterstützte Typ der In-App-Nachricht. Die vier Typen sind: `SLIDEUP`, `MODAL`, `FULL` und `HTML_FULL`.          |
|`extras`          | Das Wörterbuch der Nachrichten-Extras. Standardwert: `[:]`.                                                                   |
|`buttons`         | Die Liste der Buttons in der In-App-Nachricht.                                                                             |
|`toString()`      | Die Nachricht als String-Darstellung.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz des In-App-Nachricht-Modells finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) und [für iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### Eigenschaften des Modells für In-App-Nachricht-Buttons

In-App-Nachrichten können Buttons hinzugefügt werden, um Aktionen durchzuführen und Analytics zu protokollieren. Das Button-Modell bildet die Grundlage für alle In-App-Nachricht-Buttons.

|Eigenschaft          | Beschreibung                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | Der Text auf dem Button.                                                                                                     |
|`uri`             | Die URI, die mit dem Klick auf den Button verbunden ist.                                                                            |
|`useWebView`      | Gibt an, ob der Klick auf den Button über eine Webansicht umgeleitet werden soll.                                                 |
|`clickAction`     | Die Art der Klick-Aktion, die verarbeitet wird, wenn der Nutzer auf den Button klickt. Die drei Typen sind: `NEWS_FEED`, `URI`, und `NONE`. |
|`id`              | Die ID des Buttons in der Nachricht.                                                                                               |
|`toString()`      | Der Button als String-Darstellung.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz des Button-Modells finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).

## GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

