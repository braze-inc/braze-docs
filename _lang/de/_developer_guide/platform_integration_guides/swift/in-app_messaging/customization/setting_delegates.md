---
nav_title: Delegat für In-App-Nachrichten-UI
article_title: In-App Message UI Delegate für iOS
platform: Swift
page_order: 2
description: "Dieser Artikel beschreibt die Einrichtung eines Delegaten für das iOS-In-App-Messaging für das Swift SDK."
channel:
  - in-app messages

---

# Delegat für In-App-Nachrichten-UI

> Verwenden Sie das optionale [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate), um die Darstellung von In-App-Nachrichten anzupassen und auf verschiedene Lifecycle-Events zu reagieren. Dieses Delegate-Protokoll kann verwendet werden, um Nutzlasten getriggerter In-App-Nachrichten zur weiteren Verarbeitung zu empfangen, Display-Lifecycle-Events zu empfangen und die Anzeigezeit zu steuern. 

## Voraussetzungen

So verwenden Sie `BrazeInAppMessageUIDelegate`:
* Sie müssen die Standard [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) Implementierung als Ihre `inAppMessagePresenter` verwenden. 
* Sie müssen die Bibliothek `BrazeUI` in Ihr Projekt einbinden.

## Einstellen des Delegaten für In-App-Nachrichten

Richten Sie das Delegate-Objekt [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) mithilfe des folgenden Beispielcodes auf der Braze-Instanz ein:

{% tabs %}
{% tab schnell %}

Implementieren Sie zunächst das Protokoll `BrazeInAppMessageUIDelegate` und die gewünschten Methoden. In unserem Beispiel unten implementieren wir dieses Protokoll in der Klasse `AppDelegate` unserer Anwendung.

```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```

Weisen Sie dann das Objekt `delegate` auf der Instanz `BrazeInAppMessageUI` zu, bevor Sie diese In-App-Nachrichten-UI als `inAppMessagePresenter` zuweisen.

```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```

{% endtab %}
{% tab OBJECTIVE-C %}

Implementieren Sie zunächst das Protokoll `BrazeInAppMessageUIDelegate` und die gewünschten Methoden. In unserem Beispiel unten implementieren wir dieses Protokoll in der Klasse `AppDelegate` unserer Anwendung.

```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```

Weisen Sie dann das Objekt `delegate` auf der Instanz `BrazeInAppMessageUI` zu, bevor Sie diese In-App-Nachrichten-UI als `inAppMessagePresenter` zuweisen.

```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

In Objective-C sind nicht alle Delegate-Methoden verfügbar, da ihre Parameter nicht mit der Laufzeit der Sprache kompatibel sind.

{% endtab %}
{% endtabs %}

### Schritt-für-Schritt-Anleitung

Eine schrittweise Implementierung des Delegaten für die In-App-Nachrichten-UI finden Sie in diesem [Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

## Anpassen der Ausrichtung von In-App-Nachrichten für iOS

### Einstellung einer bevorzugten Ausrichtung

Sie können alle In-App-Nachrichten so konfigurieren, dass sie unabhängig von der Geräteausrichtung in einer bestimmten Ausrichtung angezeigt werden. Um eine bevorzugte Ausrichtung festzulegen, verwenden Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`, um die Eigenschaft `preferredOrientation` auf `PresentationContext` festzulegen. 

{% tabs %}
{% tab schnell %}

Gehen Sie beispielsweise wie folgt vor, um eine bevorzugte Ausrichtung im Hochformat zu erstellen:

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endtab %}
{% endtabs %}

Sobald die In-App-Nachricht angezeigt wird, führt jede Änderung der Geräteausrichtung, während die Nachricht noch angezeigt wird, dazu, dass sich die Nachricht mit dem Gerät dreht, sofern dies in der Konfiguration der Nachricht `orientation` unterstützt wird.

Beachten Sie, dass die Geräteausrichtung auch von der Eigenschaft `orientation` der In-App-Nachricht unterstützt werden muss, damit die Nachricht angezeigt werden kann. Außerdem wird die Einstellung `preferredOrientation` nur beachtet, wenn sie in den unterstützten Ausrichtungen der Benutzeroberfläche Ihrer Anwendung unter dem Abschnitt **Deployment Info** in den Einstellungen Ihres Ziels in Xcode enthalten ist.

![Unterstützte Ausrichtungen in Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
Die Ausrichtung wird nur für die Präsentation der Nachricht verwendet. Nachdem das Gerät die Ausrichtung geändert hat, nimmt die Nachrichtenansicht eine der von ihr unterstützten Ausrichtungen an. Auf kleineren Geräten (iPhones, iPod Touch) kann die Ausrichtung im Querformat für eine modale oder vollständige In-App-Nachricht dazu führen, dass der Inhalt abgeschnitten wird.
{% endalert %}

### Ändern der Ausrichtung von Nachrichten

Alternativ können Sie die Ausrichtung auch für jede Nachricht separat festlegen. Diese Eigenschaft definiert alle verfügbaren Ausrichtungsarten für diese Nachricht. Legen Sie dazu die Eigenschaft `orientation` auf eine bestimmte `Braze.InAppMessage` fest:

{% tabs %}
{% tab schnell %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endtab %}
{% endtabs %}

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

## Anpassen von Button-Klicks

Um auf Button-Informationen in In-App-Nachrichten zuzugreifen oder das Klickverhalten zu überschreiben, implementieren Sie [`BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:shouldprocess:buttonid:message:view:)-122yi). Geben Sie `true` zurück, damit Braze die Klickaktion verarbeiten kann, oder geben Sie `false` zurück, um das Verhalten außer Kraft zu setzen.
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


## Ausblenden der Statusleiste während der Anzeige

Bei In-App-Nachrichten des Typs `Full`, `FullImage` und `HTML` blendet das SDK die Statusleiste standardmäßig aus. Bei anderen Arten von In-App-Nachrichten bleibt die Statusleiste unangetastet. Um dieses Verhalten zu konfigurieren, verwenden Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`, um die Eigenschaft `statusBarHideBehavior` auf `PresentationContext` festzulegen. Dieses Feld kann einen der folgenden Werte annehmen:

| Verhalten beim Ausblenden der Statusleiste            | Beschreibung                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | Die Nachrichtenansicht entscheidet, ob die Statusleiste ausgeblendet wird.                                 |
| `.hidden`                           | Blenden Sie die Statusleiste immer aus.                                                           |
| `.visible`                          | Zeigen Sie immer die Statusleiste an.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

## Beispiele für die Umsetzung

Unter `InAppMessageUI` in unserem Ordner Beispiele finden Sie ein Beispiel in [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) und [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI).

