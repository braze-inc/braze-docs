---
nav_title: Implémentation avancée (facultatif)
article_title: Guide d'implémentation de messages dans l'application pour iOS (facultatif)
platform: iOS
page_order: 6
description: "Ce guide de mise en œuvre avancé couvre les considérations de code de message intégré à l'application iOS, trois cas d'utilisation construits par notre équipe, et des extraits de code qui l'accompagnent."
channel:
  - messages intégrés à l'application
---

{% alert important %}
Vous cherchez le guide d'intégration des développeurs de messages dans l'application? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/).
{% endalert %}

# Guide d'implémentation de la messagerie intégrée

> Ce guide d'implémentation optionnel et avancé couvre les considérations de code de message dans l'application, trois cas d'utilisation personnalisés construits par notre équipe, et des extraits de code qui l'accompagnent. Visitez notre dépôt de démo de Braze [ici](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Veuillez noter que ce guide de mise en œuvre est centré sur une implémentation Swift, mais des extraits Objective-C sont fournis pour ceux qui sont intéressés.  Vous cherchez des implémentations HTML ? Jetez un coup d'oeil à notre [dépôt de modèles HTML](https://github.com/braze-inc/in-app-message-templates)!

## Considérations de code

Le guide suivant offre une intégration personnalisée optionnelle de développeurs à utiliser en plus des messages intégrés hors de la boîte de réception. Les contrôleurs de vue personnalisés sont inclus ci-dessous avec chaque cas d'utilisation, offrant des exemples pour étendre les fonctionnalités et personnaliser nativement l'apparence de vos messages dans l'application.

### Sous-classes ABKInAppMessage

Le code snippet ci-dessous est une méthode de délégation de l'interface utilisateur du Braze SDK qui détermine avec quelle vue de sous-classe vous voulez remplir votre message dans l'application. Nous couvrons une implémentation de base dans ce guide et montrons comment les sous-classes complètes, glissantes et modales peuvent être implémentées de manière captivante. Veuillez noter que si vous voulez configurer votre contrôleur de vue personnalisé, vous devez configurer toutes les autres sous-classes de messages dans l'application. Une fois que vous avez une bonne compréhension des concepts derrière la sous-classe, Consultez nos [cas d'utilisation](#sample-use-cases) ci-dessous pour commencer à implémenter des sous-classes de messagerie dans l'application.

{% tabs %}
{% tab Swift %}
Sous-classes __ABKInAppMessage__<br>

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
Sous-classes __ABKInAppMessage__<br>

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [self slideupViewControllerWithInAppMessage:inAppMessage]; //Méthode personnalisée
  } sinon if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [self modalViewControllerWithInAppMessage:inAppMessage]; //Méthode personnalisée
  } sinon if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [self fullViewControllerWithInAppMessage:inAppMessage]; //Méthode personnalisée
  } sinon if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

## Exemple de cas d'utilisation

Il y a trois exemples de cas d'utilisation des clients fournis. Chaque échantillon a des transmissions vidéo, des extraits de code et un aperçu de l'apparence et de l'utilisation des messages dans l'application dans le tableau de bord Braze :
- [Message personnalisé dans l'application](#custom-slideup-in-app-message)
- [Message personnalisé dans l'application modale](#custom-modal-in-app-message)
- [Message In-App personnalisé](#custom-full-in-app-message)

### Message de glissement personnalisé dans l'application

Lors de la création de votre message glissant vers le haut dans l'application, il se peut que vous ne puissiez pas modifier le placement du message. Bien que cette option ne soit pas explicitement proposée en dehors de la liste, la modification de ce type est rendue possible en sous-classant le `ABKInAppMessageSlideupViewController` et en écrasant la valeur de `slideConstraint` avec votre propre valeur de contrainte personnalisée. Visitez le [SlideFromBottomViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift) pour commencer.

{% include video.html id="j6dvNSbK2-8" align="center" %}

#### __Ajouter un comportement supplémentaire à notre interface utilisateur par défaut__<br><br>

{% tabs %}
{% tab Swift %}
__Remplacer et définir Constraint__ personnalisé<br> Remplacer `beforeMoveInAppMessageViewOnScreen()` et définir votre propre valeur de contrainte personnalisée pour répondre à vos besoins. La valeur originale est définie dans la superclasse.

```swift
remplacer func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details Version 3.34.0 or earlier %}
```swift
remplacer func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objective-C %}
__Remplacer et définir Constraint__ personnalisé<br> Remplacer `beforeMoveInAppMessageViewOnScreen()` et définir votre propre valeur de contrainte personnalisée pour répondre à vos besoins. La valeur originale est définie dans la superclasse.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details Version 3.34.0 or earlier  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self-setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
__Mettre à jour la variable `offset` Variable__<br> Mettez à jour la variable `offset` et définissez votre propre décalage pour répondre à vos besoins.
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

{% details Version 3.34.0 or earlier  %}
__Update `slideConstraint` Variable__<br> La variable publique `slideConstraint` provient de la superclasse `ABKInAppMessageSlideupViewController`.

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
Visitez le dépôt de démonstration de Braze pour la fonction [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17) référencée ci-dessus.
{% enddetails %}
{% endtab %}
{% tab Objective-C %}
__Mettre à jour la variable `offset` Variable__<br> Mettez à jour la variable `offset` et définissez votre propre décalage pour répondre à vos besoins.
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
  [super setOffset:offset + [auto ajustéOffset]];
}
```
{% details Version 3.34.0 or earlier  %}
__Update `slideConstraint` Variable__<br> La variable publique `slideConstraint` provient de la superclasse `ABKInAppMessageSlideupViewController`.

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

__Ajuster la contrainte pour l'Orientation de l'appareil__<br> Ajuste la valeur respective dans `viewWillTransition()` car la sous-classe assume la responsabilité de garder la contrainte synchronisée lors des changements de mise en page.

### Message modal personnalisé dans l'application

Un `ABKInAppMessageModalViewController` peut être sous-classé pour tirer parti d'un `UIPickerView` offrant des moyens engageants de collecter des attributs utilisateur précieux. L'exemple ci-dessous montre comment vous pouvez utiliser le Contenu Connecté pour capturer des attributs personnalisés à partir d'une liste dynamique d'éléments. Visitez le [ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift) pour commencer.

{% include video.html id="FhRCxkLRr3M" align="center" %}

{% tabs %}
{% tab Swift %}
__En utilisant `view_type` pour le comportement d'affichage de l'IU__<br> L'objet `ABKInAppMessage` a un dictionnaire `extras` que nous pouvons demander pour trouver la clé `view_type` (le cas échéant) et afficher le bon type de vue. Il est important de noter que les messages dans l'application sont configurés par message, de sorte que les vues modales personnalisées et hors de la boîte peuvent fonctionner harmonieusement.

```swift
func modalViewController(inAppMessage: ABKInAppMessage) -> ABKInAppMessageModalViewController {
  switch inAppMessage.extras?[InAppMessageKey.viewType.rawValue] comme? String {
  case InAppMessageViewType.picker.rawValue:
    return ModalPickerViewController(inAppMessage: inAppMessage)
  default:
    return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
  }
}
```
{% endtab %}
{% tab Objective-C %}
__En utilisant `view_type` pour le comportement d'affichage de l'IU__<br> L'objet `ABKInAppMessage` a un dictionnaire `extras` que nous pouvons demander pour trouver la clé `view_type` (le cas échéant) et afficher le bon type de vue. Il est important de noter que les messages dans l'application sont configurés par message, de sorte que les vues modales personnalisées et hors de la boîte peuvent fonctionner harmonieusement.

```objc
- (ABKInAppMessageModalViewController *)modalViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyViewType];
  NSString *viewType = [inAppMessageData rawValueForInAppMessageViewTypeTypePicker];

  if ([inAppMessage. xtras objectForKey:key] && [inAppMessage. xtras[key] isEqualToString:viewType]) {
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
__Remplacez et fournissez une vue personnalisée__<br> remplacez `loadView()` et définissez votre propre vue personnalisée en fonction de vos besoins.
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
__Remplacez et fournissez une vue personnalisée__<br> remplacez `loadView()` et définissez votre propre vue personnalisée en fonction de vos besoins.
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
__Formater des variables pour une liste dynamique__<br> Avant de recharger les composants `UIPickerView` , la variable de message `inAppMessage` est affichée sous la forme d'une _String_. Ce message doit être formaté comme un tableau d'éléments à afficher correctement. À titre d'exemple, cela peut être réalisé en utilisant les composants [`(séparés: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components).
```swift
remplacer func viewDidLoad() {
  super.viewDidLoad()

  éléments = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective-C %}
__Format des variables pour PickerView__<br> Avant de recharger les composants `UIPickerView` , la variable de message `inAppMessage` est affichée sous la forme d'une _String_. Ce message doit être formaté comme un tableau d'éléments à afficher correctement. Par exemple, cela peut être réalisé en utilisant [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc).
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
__Assigner un attribut personnalisé__<br> En utilisant la sous-classe, après avoir appuyé sur soumettre, passer l'attribut avec sa valeur sélectionnée correspondante à Braze.
```swift
@IBAction func primaryButtonTapped(_ expéditeur: Any) {
  garde let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] comme? String else { return }

  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
__Assigner un attribut personnalisé__<br> En utilisant la sous-classe, après avoir appuyé sur soumettre, passer l'attribut avec sa valeur sélectionnée correspondante à Braze.
```objc
- (IBAction)primaryButtonTapped:(id)sender {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyAttributeKey];

  if (self. electedItem.length > 0 && [self.inAppMessage.extras objectForKey:key]) {
    [[AppboyManager partagé] setCustomAttributeWithKey:self. nAppMessage.extras[key] andStringValue:self.selectedItem] ;
  }
}
```
{% endtab %}
{% endtabs %}

### Message complet dans l'application personnalisé

Utilisez des messages personnalisés complets dans l'application pour créer des messages interactifs et conviviaux afin de collecter des données précieuses pour vos clients. L'exemple ci-dessous montre une implémentation du message personnalisé complet dans l'application, réimaginé comme un préfixe de notification interactif avec les préférences de notification. Visitez le [FullistViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift) pour commencer.

{% include video.html id="_P-LNHpXI88" align="center" %}

#### Interception du message dans l'application
!\[Touches\]\[1\]{: style="float:right;max-width:30%;margin-left:10px;border:0"} Intercepter les touches de message dans l'application est crucial pour que les boutons de message personnalisés fonctionnent correctement. Par défaut, le `ABKInAppMessageImmersive` ajoute un détecteur de geste d'appui sur le message afin que les utilisateurs puissent rejeter les messages sans boutons. En utilisant l'ajout d'un `UISwitch` ou d'un bouton à la hiérarchie de vue `UITableViewCell` , les touches sont maintenant traitées par notre vue personnalisée. Depuis iOS 6, les boutons et autres contrôles ont la préséance lorsque vous travaillez avec des détecteurs de gestes, ce qui fait que notre message in-app personnalisé fonctionne comme il se doit.
[1]: {% image_buster /assets/img/iam_implementation_guide.png %}
