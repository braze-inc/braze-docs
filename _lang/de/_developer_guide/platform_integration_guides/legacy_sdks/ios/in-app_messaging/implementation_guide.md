---
nav_title: Erweiterte Implementierung (optional)
article_title: Anleitung zur Implementierung von In-App-Nachrichten für iOS (optional)
platform: iOS
page_order: 6
description: "Dieser Leitfaden für die erweiterte Implementierung enthält Hinweise zur Code-Anpassung für iOS-In-App-Nachrichten, drei von unserem Team entwickelte Anwendungsfälle und begleitende Code-Snippets."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Suchen Sie den Entwickler-Leitfaden für die grundlegende Integration von In-App-Nachrichten? Sie finden es [hier]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/).
{% endalert %}

# Leitfaden für die Implementierung von In-App-Nachrichten

> Dieser Leitfaden für die optionale erweiterte Implementierung enthält Hinweise zur Code-Anpassung für In-App-Nachrichten, drei von unserem Team entwickelte Anwendungsfälle und begleitende Code-Snippets. Besuchen Sie unser Braze Demo Repository [hier](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Dieser Implementierungsleitfaden konzentriert sich auf eine Swift-Implementierung. Für Interessierte werden jedoch Objective-C-Snippets bereitgestellt. Suchen Sie nach HTML-Implementierungen? Dann sehen Sie sich unser [Repository mit HTML-Templates](https://github.com/braze-inc/in-app-message-templates) an!

## Code-Überlegungen

Der folgende Anleitung beschreibt eine optionale angepasste Entwickler-Integration, die zusätzlich zu den standardmäßigen In-App-Nachrichten verwendet werden kann. Zu jedem Anwendungsfall gibt es angepasste View-Controller mit Beispielen, wie Sie die Funktionalität erweitern und Aussehen und Handhabung Ihrer In-App-Nachrichten nativ anpassen können.

### ABKInAppMessage Unterklassen

Bei dem folgenden Code-Snippet handelt es sich um eine UI-Delegate-Methode aus dem Braze SDK, die festlegt, mit welcher Unterklassenansicht die In-App-Nachricht aufgefüllt werden soll. Wir beschreiben in dieser Anleitung eine grundlegende Implementierung und zeigen, wie die Unterklassen "Full", "Slide-up" und "Modal" implementiert werden können. Wenn Sie einen angepassten View-Controller einrichten möchten, müssen Sie alle anderen Unterklassen für In-App-Nachrichten einrichten. Nachdem Sie sich ein solides Verständnis der Konzepte hinter der Einrichtung von Unterklassen angeeignet haben, sehen Sie sich unsere [Anwendungsfälle](#sample-use-cases) an, um mit der Implementierung von Unterklassen für In-App-Nachrichten zu beginnen.

{% tabs %}
{% tab Swift %}
**ABKInAppMessage Unterklassen**<br>

```swift
extension AppboyManager: ABKInAppMessageUIDelegate {
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return slideupViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageModal: 
      return modalViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageFull:
      return fullViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
**ABKInAppMessage Unterklassen**<br> 

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [self slideupViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [self modalViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [self fullViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

## Anwendungsfälle

Im Folgenden finden Sie drei Anwendungsbeispiele. Jeder Anwendungsfall beinhaltet eine ausführliche Erklärung, relevante Code-Snippets sowie einen Blick darauf, wie In-App-Nachrichten im Braze-Dashboard aussehen und verwendet werden können:
- [Angepasste In-App-Nachricht des Typs "Slide-up"](#custom-slide-up-in-app-message)
- [Angepasste In-App-Nachricht des Typs "Modal"](#custom-modal-in-app-message)
- [Angepasste In-App-Nachricht des Typs "Full"](#custom-full-in-app-message)

### Benutzerdefinierte In-App-Nachricht zum Hochschieben

![Zwei iPhones nebeneinander. Beim ersten iPhone berührt die hochgeschobene Nachricht den unteren Rand des Telefondisplays. Auf dem zweiten iPhone ist die Slide-up-Nachricht höher auf dem Bildschirm platziert, sodass Sie den angezeigten App-Navigations-Button sehen können.]({% image_buster /assets/img/iam_implementation/slideup.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0;"}

Bei der Erstellung Ihrer Slide-up-Nachricht werden Sie feststellen, dass Sie die Platzierung der Nachricht mit den Standardmethoden nicht ändern können. Um eine Änderung wie diese vorzunehmen, verwenden Sie eine Unterklasse von `ABKInAppMessageSlideupViewController` und überschreiben die Variable `offset` mit Ihrer angepassten Variablen. Das Bild auf der rechten Seite zeigt ein Beispiel dafür, wie Sie damit Ihre In-App-Nachrichten anpassen können. 

Besuchen Sie die [`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift) um loszulegen.

#### Hinzufügen von zusätzlichem Verhalten zu unserer Standard-Benutzeroberfläche<br><br>

{% tabs %}
{% tab Swift %}
**Aktualisieren der Variablen `offset` **<br>
Aktualisieren Sie die Variable `offset` und legen Sie einen Offset fest, der Ihren Vorstellungen entspricht.
```swift
func setSlideConstraint() {
  offset = 0
}
```

```swift
override var offset: CGFloat {
  get {
    return super.offset
  }
  set {
    super.offset = newValue + adjustedOffset
  }
}
```

{% details Version 3.34.0 oder früher  %}
**Aktualisieren der Variablen `slideConstraint` **<br>
Die öffentliche Variable `slideConstraint` stammt aus der Superklasse `ABKInAppMessageSlideupViewController`. 

```swift
func setSlideConstraint() {
    slideConstraint?.constant = bottomSpacing
}
```

```swift
private var bottomSpacing: CGFloat {
    return AppboyManager.shared.activeApplicationViewController.topMostViewController().view.safeAreaInsets.bottom
}
``` 
Besuchen Sie das Braze Demo Repository für die [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17) Funktion.
{% enddetails %}
{% endtab %}
{% tab Objective-C %}
**Aktualisieren der Variablen `offset` **<br>
Aktualisieren Sie die Variable `offset` und legen Sie einen Offset fest, der Ihren Vorstellungen entspricht.
```objc
- (void)setOffset {
  self.offset = 0;
}
```

```objc
- (CGFloat)offset {
  return [super offset];
}
 
- (void)setOffset:(CGFloat)offset {
  [super setOffset:offset + [self adjustedOffset]];
}
```
{% details Version 3.34.0 oder früher  %}
**Aktualisieren der Variablen `slideConstraint` **<br>
Die öffentliche Variable `slideConstraint` stammt aus der Superklasse `ABKInAppMessageSlideupViewController`. 

```objc
- (void)self.setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = bottomSpacing;
}
```

```objc
- (CGFloat)bottomSpacing {
  return [AppboyManager shared].activeApplicationViewController.topMostViewController.view.safeAreaInsets.bottom;
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Benutzerdefinierte Einschränkung außer Kraft setzen und festlegen**<br>
Überschreiben Sie `beforeMoveInAppMessageViewOnScreen()` und legen Sie einen angepassten Constraint-Wert fest. Der ursprüngliche Wert wird in der Superklasse festgelegt.

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details Version 3.34.0 oder früher %}
```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objective-C %}
**Benutzerdefinierte Einschränkung außer Kraft setzen und festlegen**<br> 
Überschreiben Sie `beforeMoveInAppMessageViewOnScreen()` und legen Sie einen angepassten Constraint-Wert fest. Der ursprüngliche Wert wird in der Superklasse festgelegt.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details Version 3.34.0 oder früher  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

**Einschränkung für Geräteausrichtung anpassen**<br>
Passen Sie den entsprechenden Wert in `viewWillTransition()` an, da die Unterklasse für die Synchronisierung der Einschränkung bei Layoutänderungen zuständig ist.

### Benutzerdefinierte modale In-App-Nachricht

![Ein iPhone, das eine modale In-App-Nachricht anzeigt, mit der Sie durch eine Liste von Sportmannschaften blättern und Ihre Lieblingsmannschaft auswählen können. Am unteren Ende dieser In-App-Nachricht befindet sich ein großer blauer Senden-Button.]({% image_buster /assets/img/iam_implementation/modal.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Ein `ABKInAppMessageModalViewController` kann in Unterklassen unterteilt werden, um eine `UIPickerView` zur Erfassung wertvoller Nutzerattribute zu nutzen. Die angepasste modale In-App-Nachricht ermöglicht es Ihnen, Connected-Content oder eine beliebige verfügbare Liste zu verwenden, um Attribute aus einer dynamischen Artikelliste anzuzeigen und zu erfassen. 

Sie können Ihre eigenen Ansichten in unterklassifizierte In-App-Nachrichten einfügen. Dieses Beispiel zeigt, wie eine `UIPickerView` genutzt werden kann, um die Funktionalität eines `ABKModalInAppMessageViewController` zu erweitern.

Besuchen Sie den [ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift), um loszulegen.

#### Dashboard Konfiguration

Um eine modale In-App-Nachricht im Dashboard einzurichten, müssen Sie eine Artikelliste angeben, die als kommagetrennter String formatiert ist. In unserem Beispiel verwenden wir Connected-Content, um eine JSON-Liste mit Team-Namen abzurufen und die Namen entsprechend zu formatieren.

![Der In-App-Nachrichten-Editor zeigt eine Vorschau, wie die In-App-Nachricht aussehen wird. Stattdessen wird die Artikelliste angezeigt, die Sie an Braze übermittelt haben. Da die Braze-UI Ihre angepasste In-App-Nachrichten-UI erst anzeigt, wenn sie an ein Smartphone gesendet wird, ist die Vorschau zum Aussehen Ihrer Nachricht nicht aussagekräftig. Wir empfehlen Ihnen daher, sie vor dem Senden zu testen.]({% image_buster /assets/img/iam_implementation/dashboard1.png %})

Geben Sie in den Schlüssel-Wert-Paaren einen `attribute_key` an. Dieser Schlüssel wird zusammen mit dem vom Benutzer ausgewählten Wert als benutzerdefiniertes Attribut in seinem Benutzerprofil gespeichert. Ihre benutzerdefinierte Ansichtslogik muss die an Braze gesendeten Benutzerattribute verarbeiten.

Das Wörterbuch `extras` im Objekt `ABKInAppMessage` ermöglicht Ihnen die Abfrage eines Schlüssels des Typs `view_type` (falls vorhanden), der die korrekte Ansicht für die Anzeige angibt. Es ist wichtig zu wissen, dass In-App-Nachrichten für jede einzelne Nachricht konfiguriert werden, so dass benutzerdefinierte und standardmäßige modale Ansichten harmonisch zusammenarbeiten können.

![Zwei Schlüssel-Wert-Paare im Nachrichten-Editor. Für das erste Schlüssel-Wert-Paar wurde "attribute_key" auf "Favorite Team" und für das zweite Schlüssel-Wert-Paar wurde "view_type" auf "picker" festgelegt.]({% image_buster /assets/img/iam_implementation/dashboard2.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
**Verwendung von `view_type` für das Anzeigeverhalten der Benutzeroberfläche**<br>
Fragen Sie das Wörterbuch `extras` für Ihren `view_type` ab, um den gewünschten untergeordneten View-Controller zu laden.

```swift
func modalViewController(inAppMessage: ABKInAppMessage) -> ABKInAppMessageModalViewController {
  switch inAppMessage.extras?[InAppMessageKey.viewType.rawValue] as? String {
  case InAppMessageViewType.picker.rawValue:
    return ModalPickerViewController(inAppMessage: inAppMessage)
  default:
    return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Verwendung von `view_type` für das Anzeigeverhalten der Benutzeroberfläche**<br>
Fragen Sie das Wörterbuch `extras` für Ihren `view_type` ab, um den gewünschten untergeordneten View-Controller zu laden.

```objc
- (ABKInAppMessageModalViewController *)modalViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyViewType];
  NSString *viewType = [inAppMessageData rawValueForInAppMessageViewType:InAppMessageViewTypePicker];
   
  if ([inAppMessage.extras objectForKey:key] && [inAppMessage.extras[key] isEqualToString:viewType]) {
    return [[ModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Benutzerdefinierte Ansicht überschreiben und bereitstellen**<br>
Setzen Sie `loadView()` außer Kraft und stellen Sie Ihre eigene benutzerdefinierte Ansicht ein, die Ihren Bedürfnissen entspricht.
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab Objective-C %}
**Benutzerdefinierte Ansicht überschreiben und bereitstellen**<br>
Setzen Sie `loadView()` außer Kraft und stellen Sie Ihre eigene benutzerdefinierte Ansicht ein, die Ihren Bedürfnissen entspricht.
```objc
- (void)loadView {
  NSString *nibName = @"ModalPickerViewController";
  [[NSBundle mainBundle] loadNibNamed:nibName owner:self options:nil];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Formatvariablen für eine dynamische Liste**<br>
Bevor die Komponenten von `UIPickerView` neu geladen werden, wird die Nachrichten-Variable `inAppMessage` als _String_ ausgegeben. Diese Nachricht muss als Array formatiert werden, um korrekt angezeigt zu werden. Dies kann beispielsweise durch die Verwendung von [`components(separatedBy: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components) erreicht werden.
```swift
override func viewDidLoad() {
  super.viewDidLoad()
 
  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective-C %}
**Formatvariablen für PickerView**<br>
Bevor die Komponenten von `UIPickerView` neu geladen werden, wird die Nachrichten-Variable `inAppMessage` als _String_ ausgegeben. Diese Nachricht muss als Array formatiert werden, um korrekt angezeigt zu werden. Dies kann beispielsweise durch die Verwendung von [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc) erreicht werden.
```objc
- (void)viewDidLoad {
  [super viewDidLoad];
   
  self.items = [[NSArray alloc] initWithArray:[self.inAppMessage.message componentsSeparatedByString:@", "]];
  [self.pickerView reloadAllComponents];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Angepasstes Attribut zuweisen**<br>
Nachdem ein Nutzer auf "Senden" geklickt hat, übergeben Sie das Attribut mit dem entsprechend ausgewählten Wert unter Verwendung der Unterklasse an Braze.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
**Angepasstes Attribut zuweisen**<br>
Nachdem ein Nutzer auf "Senden" geklickt hat, übergeben Sie das Attribut mit dem entsprechend ausgewählten Wert unter Verwendung der Unterklasse an Braze.
```objc
- (IBAction)primaryButtonTapped:(id)sender {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyAttributeKey];
   
  if (self.selectedItem.length > 0 && [self.inAppMessage.extras objectForKey:key]) {
    [[AppboyManager shared] setCustomAttributeWithKey:self.inAppMessage.extras[key] andStringValue:self.selectedItem];
  }
}
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Möchten Sie unsere angepassten modalen In-App-Nachrichten nutzen, um Videos über FaceTime zu teilen? Dann sehen Sie sich unseren [Implementierungsleitfaden]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/shareplay/) für In-App-Nachrichten mit SharePlay an.
{% endalert%}

### Angepasste In-App-Nachricht des Typs "Full"

![Eine In-App-Meldung, die eine Liste von Konfigurationsoptionen mit Kippschaltern neben jeder Option anzeigt. Am Ende der Nachricht befindet sich ein großer blauer Senden-Button.]({% image_buster /assets/img/iam_implementation/fullscreen.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Verwenden Sie benutzerdefinierte, vollständige In-App-Nachrichten, um interaktive, benutzerfreundliche Aufforderungen zur Erfassung wertvoller Kundendaten zu erstellen. Das Beispiel auf der rechten Seite zeigt die Implementierung einer angepassten In-App-Nachricht des Typs "Full", die als interaktiver Push-Primer mit Benachrichtigungspräferenzen überarbeitet wurde. 

Besuchen Sie die [`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift) um loszulegen.

#### Dashboard Konfiguration

Um eine angepasste In-App-Nachricht des Typs "Full" im Dashboard einzurichten, müssen Sie eine Liste Ihrer Tags angeben, die als kommagetrennter String formatiert ist. 

Geben Sie in den Schlüssel-Wert-Paaren einen `attribute_key` an. Dieser Schlüssel wird zusammen mit den vom Benutzer ausgewählten Werten in seinem Benutzerprofil als benutzerdefiniertes Attribut gespeichert. Ihre benutzerdefinierte Ansichtslogik muss die an Braze gesendeten Benutzerattribute verarbeiten.

![Drei Schlüssel-Wert-Paare im Nachrichten-Editor. Das erste Schlüssel-Wert-Paar "attribute_key" ist auf "Push Tags", das zweite Schlüssel-Wert-Paar "subtitle_text" ist auf "Enabling notifications will also..." und das dritte Schlüssel-Wert-Paar "view_type" ist auf "table_list" festgelegt.]({% image_buster /assets/img/iam_implementation/dashboard3.png %}){: style="max-width:65%;"}

#### Abfangen von Touchgesten bei In-App-Nachrichten
![Ein Apple-Gerät, das Reihen von Einstellungen und Schaltern anzeigt. Die angepasste Ansicht verarbeitet die Buttons und alle Touchgesten außerhalb der Button-Steuerelemente werden von der In-App-Nachricht verarbeitet und bewirken, dass diese ausgeblendet wird.]({% image_buster /assets/img/iam_implementation_guide.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
Damit die Buttons in angepassten In-App-Nachrichten des Typs "Full" ordnungsgemäß funktionieren, ist das Abfangen von Touchgesten bei In-App-Nachrichten von entscheidender Bedeutung. Standardmäßig fügt `ABKInAppMessageImmersive` der Nachricht eine Tippgesten-Erkennung hinzu, sodass Nutzer die Nachrichten ohne Buttons ausblenden können. Durch Hinzufügen eines `UISwitch` oder eines Buttons zur Ansichtshierarchie `UITableViewCell` werden die Touchgesten nun von der angepassten Ansicht verarbeitet. Seit iOS 6 haben Buttons und andere Steuerelemente bei Arbeiten mit Gestenerkennung Vorrang, sodass unsere angepasste In-App-Nachricht des Typs "Full" genauso funktioniert, wie sie sollte. 

