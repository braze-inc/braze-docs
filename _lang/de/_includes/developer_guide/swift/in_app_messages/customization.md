{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Einrichten des UI-Delegierten (erforderlich)

Um die Darstellung von In-App-Nachrichten anzupassen und auf verschiedene Ereignisse im Lebenszyklus zu reagieren, müssen Sie Folgendes einrichten [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). Dies ist ein Delegatenprotokoll, das für den Empfang und die Verarbeitung von getriggerten In-App-Nachricht-Payloads, den Empfang von Display-Lebenszyklus-Ereignissen und die Steuerung des Display-Timings verwendet wird. Um `BrazeInAppMessageUIDelegate` zu verwenden, müssen Sie:
- Verwenden Sie die Standard [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) Implementierung als Ihre `inAppMessagePresenter`. 
- Binden Sie die Bibliothek `BrazeUI` in Ihr Projekt ein.

### Schritt 1: Implementieren Sie das Protokoll `BrazeInAppMessageUIDelegate`  

Implementieren Sie zunächst das Protokoll `BrazeInAppMessageUIDelegate` und die gewünschten Methoden. In unserem Beispiel unten implementieren wir dieses Protokoll in der Klasse `AppDelegate` unserer Anwendung.

{% tabs %}
{% tab schnell %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### Schritt 2: Weisen Sie das Objekt `delegate` zu 

Weisen Sie das Objekt `delegate` auf der Instanz `BrazeInAppMessageUI` zu, bevor Sie diese In-App-Nachricht UI als Ihre `inAppMessagePresenter` zuweisen.

{% tabs %}
{% tab schnell %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
In Objective-C sind nicht alle Delegate-Methoden verfügbar, da ihre Parameter nicht mit der Laufzeit der Sprache kompatibel sind.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Eine schrittweise Implementierung des Delegaten für die In-App-Nachrichten-UI finden Sie in diesem [Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## On-Click-Verhalten

Jedes Objekt des Typs `Braze.InAppMessage` enthält eine entsprechende [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction), die das Verhalten beim Klicken definiert. 

### Arten von Klickaktionen

Die Eigenschaft `clickAction` auf Ihrem `Braze.InAppMessage` ist standardmäßig auf `.none` eingestellt, kann aber auf einen der folgenden Werte gesetzt werden:

| `ClickAction` | On-Click-Verhalten |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Öffnet die angegebene URL in einem externen Browser. Wenn `useWebView` auf `true` festgelegt ist, wird sie in einer Webansicht geöffnet. |
| `.none` | Die Nachricht wird ausgeblendet, wenn sie angeklickt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Bei In-App-Nachrichten mit Buttons wird die `clickAction` der Nachricht ebenfalls in die endgültige Nutzlast aufgenommen, wenn die Klickaktion vor dem Hinzufügen des Button-Textes hinzugefügt wird.
{% endalert %}

### Anpassen des Verhaltens bei einem Klick

Um dieses Verhalten anzupassen, können Sie die Eigenschaft `clickAction` ändern. Ziehen Sie dazu das folgende Beispiel zurate:

{% tabs %}
{% tab schnell %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

Die Methode `inAppMessage(_:prepareWith:)` ist in Objective-C nicht verfügbar.

{% endtab %}
{% endtabs %}

### Anpassen des Kundenverhaltens

Wenn auf eine In-App-Nachricht geklickt wird, wird die folgende Delegate-Methode [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) aufgerufen: Für Klicks auf In-App-Nachrichten-Buttons und HTML-In-App Nachrichten-Buttons (Links) wird eine Button-ID als optionaler Parameter angegeben.

{% tabs %}
{% tab schnell %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

Diese Methode gibt einen booleschen Wert zurück, der angibt, ob Braze die Klickaktion weiter ausführen soll.

{% tabs %}
{% tab schnell %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }
    
    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Anpassen von Modal-Entlassungen

Um Ausblendungen durch Tippen außerhalb des Fensters zu aktivieren, können Sie die Eigenschaft `dismissOnBackgroundTap` in der Struktur `Attributes` des In-App-Nachrichtentyps ändern, den Sie anpassen möchten. 

Wenn Sie beispielsweise dieses Feature für modale In-App-Nachrichten mit Bildern aktivieren möchten, können Sie Folgendes konfigurieren:

{% tabs %}
{% tab schnell %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

Die Anpassung über `Attributes` ist in Objective-C nicht möglich.

{% endtab %}
{% endtabs %}

Der Standardwert ist `false`. Hierdurch wird festgelegt, ob die modale In-App-Nachricht ausgeblendet wird, wenn der Nutzer auf eine Stelle außerhalb der In-App-Nachricht tippt.

| `DismissModalOnOutsideTap` | Beschreibung |
|----------|-------------|
| `true`         | Modale In-App-Nachrichten werden ausgeblendet, wenn auf eine Stelle außerhalb des Fensters getippt wird.     |
| `false`        | Standardmäßig werden modale In-App-Nachrichten beim Tippen auf eine Stelle außerhalb des Fensters nicht ausgeblendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Einzelheiten zur Anpassung von In-App-Nachrichten finden Sie in diesem [Artikel](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).

## Anpassen der Ausrichtung von Nachrichten

Sie können die Ausrichtung Ihrer In-App-Nachrichten anpassen. Sie können eine neue Standardausrichtung für alle Nachrichten festlegen oder eine angepasste Ausrichtung für eine einzelne Nachricht einstellen.

{% tabs local %}
{% tab alle Nachrichten %}
Um eine Standard-Ausrichtung für alle In-App-Nachrichten zu wählen, verwenden Sie die [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) Methode die Eigenschaft `preferredOrientation` auf `PresentationContext`. 

Zum Beispiel, um Hochformat als Standardausrichtung festzulegen:

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab einzelne Nachricht %}
Um die Ausrichtung für eine einzelne Nachricht festzulegen, ändern Sie die Eigenschaft `orientation` von `Braze.InAppMessage`:

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Nachdem die In-App-Nachricht angezeigt wurde, führt jede Änderung der Geräteausrichtung, während die Nachricht noch angezeigt wird, dazu, dass sich die Nachricht mit dem Gerät dreht (vorausgesetzt, dies wird von der Konfiguration der Nachricht `orientation` unterstützt).

Die Ausrichtung des Geräts muss auch von der Eigenschaft `orientation` der In-App-Nachricht unterstützt werden, damit die Nachricht angezeigt werden kann. Außerdem wird die Einstellung `preferredOrientation` nur beachtet, wenn sie in den unterstützten Ausrichtungen der Benutzeroberfläche Ihrer Anwendung unter dem Abschnitt **Deployment Info** in den Einstellungen Ihres Ziels in Xcode enthalten ist.

![Unterstützte Ausrichtungen in Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
Die Ausrichtung wird nur für die Präsentation der Nachricht verwendet. Nachdem das Gerät die Ausrichtung geändert hat, nimmt die Nachrichtenansicht eine der von ihr unterstützten Ausrichtungen an. Auf kleineren Geräten (iPhones, iPod Touch) kann die Ausrichtung im Querformat für eine modale oder vollständige In-App-Nachricht dazu führen, dass der Inhalt abgeschnitten wird.
{% endalert %}

## Anpassen der Anzeigezeit 

Sie können steuern, ob eine verfügbare In-App-Nachricht an bestimmten Punkten des Nutzererlebnisses angezeigt werden soll. Wenn es Situationen gibt, in denen die In-App-Nachricht nicht angezeigt werden soll – z. B. während eines Spiels im Vollbildmodus oder auf einem Ladebildschirm – können Sie ausstehende In-App-Nachrichten verzögern oder ausblenden. Um das Timing von In-App-Nachrichten zu steuern, verwenden Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)`, um die Eigenschaft `BrazeInAppMessageUI.DisplayChoice` festzulegen. 

{% tabs %}
{% tab schnell %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

Konfigurieren Sie `BrazeInAppMessageUI.DisplayChoice` so, dass einer der folgenden Werte zurückgegeben wird:

| Anzeigeoptionen                      | Verhalten                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | Die Nachricht wird sofort angezeigt. Dies ist der Standardwert.                                                       |
| `.reenqueue`                        | Die Nachricht wird nicht angezeigt und wird wieder oben auf dem Stack platziert.                                       |
| `.later`                            | Die Nachricht wird nicht angezeigt und wird wieder oben auf dem Stack platziert. (Veraltet, bitte verwenden Sie `.reenqueue`) |
| `.discard`                          | Die Nachricht wird ausgeblendet und nicht angezeigt.                                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Ein Beispiel für `InAppMessageUI` finden Sie in unserem [Swift Braze SDK Repository](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) und [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI).
{% endalert %}

## Ausblenden der Statusleiste

Bei In-App-Nachrichten des Typs `Full`, `FullImage` und `HTML` blendet das SDK die Statusleiste standardmäßig aus. Bei anderen Arten von In-App-Nachrichten bleibt die Statusleiste unangetastet. Um dieses Verhalten zu konfigurieren, verwenden Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`, um die Eigenschaft `statusBarHideBehavior` auf `PresentationContext` festzulegen. Dieses Feld kann einen der folgenden Werte annehmen:

| Verhalten beim Ausblenden der Statusleiste            | Beschreibung                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | Die Nachrichtenansicht entscheidet, ob die Statusleiste ausgeblendet wird.                                 |
| `.hidden`                           | Blenden Sie die Statusleiste immer aus.                                                           |
| `.visible`                          | Zeigen Sie immer die Statusleiste an.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Deaktivieren des Dunkelmodus

Um zu verhindern, dass In-App-Nachrichten den Dark-Mode-Stil übernehmen, wenn auf dem Nutzergerät der Dark Mode aktiviert ist, implementieren Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`. Der an die Methode übergebene `PresentationContext` enthält einen Verweis auf das darzustellende `InAppMessage`-Objekt. Jede `InAppMessage` verfügt über eine Eigenschaft des Typs `themes` mit den Modelldesigns `dark` und `light`. Wenn Sie die Eigenschaft `themes.dark` auf `nil` setzen, werden die e In-App-Nachricht automatisch im hellen Design dargestellt.

In-App-Nachrichten mit Buttons verfügen über ein zusätzliches `themes`-Objekt in der Eigenschaft `buttons`. Um zu verhindern, dass Schaltflächen das Styling des dunklen Modus übernehmen, können Sie mit [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) ein neues Array von Schaltflächen mit einem `light` Thema und keinem `dark` Thema erstellen.

{% tabs %}
{% tab schnell %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup
    
    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal
    
    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage
    
    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full
    
    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage
    
    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## Anpassen der Aufforderung zur Bewertung im App Store

Sie können In-App-Nachrichten in einer Kampagne verwenden, um Nutzer:innen um eine Bewertung im App Store zu bitten.

{% alert note %}
Da diese Beispielabfrage das Standardverhalten von Braze außer Kraft setzt, können wir Impressionen nicht automatisch tracken. Sie müssen [Ihre eigenen Analytics protokollieren]({{site.baseurl}}/developer_guide/analytics/).
{% endalert %}

### Schritt 1: Legen Sie den Delegaten für In-App-Nachrichten fest

Setzen Sie zunächst die [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_setting-up-the-ui-delegate-required) in Ihrer App ein. 

### Schritt 2: Deaktivieren Sie die standardmäßige Review-Mitteilung des App Store

Als Nächstes implementieren Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)`, um die Standard Nachrichten des App Store zu deaktivieren.

{% tabs %}
{% tab schnell %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### Schritt 3: Setzen Sie einen Deeplink

Fügen Sie in Ihrem Code zur Behandlung von Deeplinks den folgenden Code hinzu, um den `{YOUR-APP-SCHEME}:app-store-review`-Deeplink zu verarbeiten. Beachten Sie, dass Sie `StoreKit` importieren müssen, um `SKStoreReviewController` zu verwenden:

{% tabs %}
{% tab schnell %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### Schritt 4: Angepasstes Verhalten beim Klicken einstellen

Als Nächstes erstellen Sie eine In-App-Nachricht-Kampagne mit den folgenden Elementen:

- Das Schlüssel-Wert-Paar `"AppStore Review" : "true"`
- Das Klickverhalten ist auf "Deep Link Into App" gesetzt, unter Verwendung des Deeplinks `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple begrenzt die Aufforderungen zur Überprüfung im App Store auf maximal drei Mal pro Jahr und Nutzer:innen. Daher sollte Ihre Kampagne auf drei Mal pro Jahr und Nutzer:innen [begrenzt]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) sein.<br><br>Nutzer:innen können die Aufforderungen zur Überprüfung im App Store deaktivieren. Daher sollte Ihre angepasste Bewertungsaufforderung nicht versprechen, dass eine native App Store-Bewertungsaufforderung erscheint oder direkt um eine Bewertung bitten.
{% endalert %}
