{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Methoden zur Protokollierung

Sie können diese Methoden nutzen, indem Sie Ihre `BrazeInAppMessage`-Instanz zur Protokollierung von Analytics und zur Durchführung von Aktionen übergeben:

| Methode                                                    | Beschreibung                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Protokolliert einen Klick für die bereitgestellten Daten der In-App-Nachricht.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Protokolliert eine Impression für die bereitgestellten In-App-Nachricht-Daten.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Protokolliert einen Button-Klick für die angegebenen In-App-Nachricht-Daten und die Button-ID.               |
| `hideCurrentInAppMessage()`                               | Beendet die aktuell angezeigte In-App-Nachricht.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Führt die Aktion für eine In-App-Nachricht aus.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Führt die Aktion für einen Button für In-App-Nachrichten aus.                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Umgang mit Nachrichten-Daten

In den meisten Fällen können Sie die Methode `Braze.addListener` verwenden, um Event-Listener zu registrieren, die Daten aus In-App-Nachrichten verarbeiten. 

Außerdem können Sie auf die Daten der In-App-Nachricht im JavaScript-Layer zugreifen, indem Sie die Methode `Braze.subscribeToInAppMessage` aufrufen, damit die SDKs ein `inAppMessageReceived`-Event veröffentlichen, wenn eine In-App-Nachricht getriggert wird. Übergeben Sie einen Callback an diese Methode, um Ihren eigenen Code auszuführen, wenn die In-App-Nachricht getriggert und vom Listener empfangen wird.

Um die Behandlung von Nachrichten-Daten anzupassen, sehen Sie sich die folgenden Implementierungsbeispiele an:

{% tabs local %}
{% tab grundlegend %}
Um das Standard-Verhalten zu verbessern oder wenn Sie keinen Zugang zur Anpassung des nativen iOS- oder Android-Codes haben, empfehlen wir Ihnen, das Standard UI zu deaktivieren, während Sie weiterhin In-App Nachrichten-Events von Braze erhalten. Um die Standard-UI zu deaktivieren, übergeben Sie `false` an die Methode `Braze.subscribeToInAppMessage` und verwenden Sie die Daten der In-App-Nachricht, um Ihre eigene Nachricht in JavaScript zu erstellen. Beachten Sie, dass Sie Analytics für Ihre Nachrichten manuell protokollieren müssen, wenn Sie das Standard UI deaktivieren möchten.

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
{% endtab %}

{% tab vorangebracht %}
Um eine fortschrittlichere Logik einzubauen, die bestimmt, ob eine In-App-Nachricht über die integrierte UI angezeigt wird oder nicht, implementieren Sie In-App-Nachrichten über den nativen Layer.

{% alert warning %}
Da es sich hierbei um eine fortgeschrittene Anpassungsoption handelt, beachten Sie bitte, dass durch das Überschreiben der Standard-Implementierung von Braze auch die Logik zum Senden von In-App-Nachricht-Events an Ihre JavaScript-Listener aufgehoben wird. Wenn Sie weiterhin `Braze.subscribeToInAppMessage` oder `Braze.addListener` verwenden möchten, wie unter [Zugriff auf In-App-Nachricht-Daten](#accessing-in-app-message-data) beschrieben, müssen Sie die Veröffentlichung der Events selbst übernehmen.
{% endalert %}

{% subtabs %}
{% subtab Android %}
Implementieren Sie `IInAppMessageManagerListener` wie in unserem Android-Artikel über [angepasste Manager-Listener]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners) beschrieben. In Ihrer `beforeInAppMessageDisplayed`-Implementierung können Sie auf die Daten von `inAppMessage` zugreifen, sie an den JavaScript-Layer senden und anhand des Rückgabewerts entscheiden, ob Sie die native Nachricht anzeigen oder nicht.

Mehr über diese Werte erfahren Sie in unserer [Android Dokumentation]({{site.baseurl}}/developer_guide/in_app_messages/).

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
{% endsubtab %}
{% subtab iOS %}
### Überschreiben des Standard UI Delegaten

Standardmäßig wird [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) erstellt und zugewiesen, wenn Sie die Instanz `braze` initialisieren. `BrazeInAppMessageUI` ist eine Implementierung des [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter)-Protokolls und verfügt über die Eigenschaft `delegate`, mit der Sie die Behandlung von empfangenen In-App-Nachrichten anpassen können.

1. Implementieren Sie den Delegaten `BrazeInAppMessageUIDelegate` wie in [diesem iOS-Artikel ](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) beschrieben.

2. In der Delegate-Methode `inAppMessage(_:displayChoiceForMessage:)` können Sie auf die Daten von `inAppMessage` zugreifen, sie an die JavaScript-Schicht senden und anhand des Rückgabewerts entscheiden, ob die native Nachricht angezeigt werden soll oder nicht.

Weitere Einzelheiten zu diesen Werten finden Sie in unserer [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

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

Um den Delegaten zu verwenden, weisen Sie ihn `brazeInAppMessagePresenter.delegate` zu, nachdem Sie die Instanz `braze` initialisiert haben. 

{% alert note %}
`BrazeUI` kann nur in Objective-C oder Swift importiert werden. Wenn Sie Objective-C++ verwenden, müssen Sie dies in einer separaten Datei behandeln.
{% endalert %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```

### Native Standard-UI überschreiben

Wenn Sie die Darstellung Ihrer In-App-Nachrichten auf der nativen iOS-Ebene vollständig anpassen möchten, halten Sie sich an das [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter)-Protokoll und weisen Sie Ihren angepassten Presenter nach dem folgenden Beispiel zu:

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
