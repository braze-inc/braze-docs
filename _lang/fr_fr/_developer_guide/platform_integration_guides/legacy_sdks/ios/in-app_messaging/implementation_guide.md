---
nav_title: Implémentation avancée (facultatif)
article_title: Guide d’implémentation des messages in-app pour iOS (facultatif)
platform: iOS
page_order: 6
description: "Ce guide d’implémentation avancée couvre les considérations relatives au code de message in-app iOS, trois cas d’utilisation créés par notre équipe et les extraits de code qui l’accompagnent."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Vous recherchez le guide d’intégration de base du développeur de messages in-app ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/).
{% endalert %}

# Guide d’implémentation de la messagerie in-app

> Ce Guide d’implémentation avancé optionnel couvre les considérations du code des messages in-app, trois cas d’utilisation personnalisés créés par notre équipe et les extraits de code qui l’accompagnent. Visitez notre dépôt de démonstration Braze [ici](https://github.com/braze-inc/braze-growth-shares-ios-demo-app) ! Ce guide d’implémentation est centré sur une implémentation Swift, mais des extraits de code Objective-C sont fournis aux personnes intéressées. Vous recherchez des implémentations HTML ? Jetez un coup d'œil à notre [référentiel de modèles HTML](https://github.com/braze-inc/in-app-message-templates)!

## Considérations du code

Le guide suivant propose une intégration de développeur personnalisée facultative à utiliser en plus des messages in-app par défaut. Les contrôleurs de vue personnalisés sont inclus dans chaque cas d’utilisation, ils offrent des exemples pour étendre la fonctionnalité et personnaliser nativement l’apparence et la convivialité de vos messages in-app.

### Sous-classes ABKinAppMessage

L’extrait de code suivant est une méthode de délégation de l’interface utilisateur du SDK Braze qui détermine la vue de sous-classe avec laquelle vous souhaitez remplir votre message in-app. Nous couvrons une implémentation de base dans ce guide et montrons comment les sous-classes complètes, coulissantes et modales peuvent être implémentées de manière captivante. Notez que si vous souhaitez configurer votre contrôleur de visualisation personnalisée, vous devez configurer toutes les autres sous-classes de messages in-app. Après avoir bien compris les concepts derrière la sous-classe, consultez nos [cas d'utilisation](#sample-use-cases) pour commencer à implémenter des sous-classes de messagerie dans l'application.

{% tabs %}
{% tab Swift %}
**Sous-classes ABKinAppMessage**<br>

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
{% tab Objectif-C %}
**Sous-classes ABKinAppMessage**<br> 

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

## Cas d’utilisation

Nous avons fourni trois cas d'utilisation ci-dessous. Chaque cas d’utilisation offre une explication détaillée, des extraits de code pertinents et un aperçu de la manière dont les messages in-app peuvent être examinés et utilisés dans le tableau de bord de Braze :
- [Message in-app personnalisé à glissement vers le haut](#custom-slide-up-in-app-message)
- [Message in-app modal personnalisé](#custom-modal-in-app-message)
- [Message in-app complet personnalisé](#custom-full-in-app-message)

### Message in-app personnalisé à glissement vers le haut

![Deux iPhone côte à côte. Le premier iPhone a le message coulissant touchant le bas de l'écran du téléphone. Sur le deuxième iPhone, le message in-app est placé plus haut sur l'écran, ce qui permet de voir le bouton de navigation de l'application.]({% image_buster /assets/img/iam_implementation/slideup.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0;"}

Lors de la création de votre message in-app à glissement vers le haut, vous remarquerez peut-être que vous ne pouvez pas modifier l’emplacement du message à l’aide des méthodes par défaut. Une telle modification est rendue possible en sous-classant le `ABKInAppMessageSlideupViewController` et en remplaçant la variable `offset` par votre propre variable personnalisée. L’image à droite montre un exemple de la façon dont cela peut être utilisé pour ajuster vos messages in-app à glissement vers le haut. 

Visitez le [`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift) pour commencer.

#### Ajouter un comportement supplémentaire à notre interface utilisateur par défaut<br><br>

{% tabs %}
{% tab Swift %}
**Mettre à jour la variable `offset`**<br>
Mettre à jour la variable `offset` et définissez votre propre décalage pour répondre à vos besoins.
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

{% details Version 3.34.0 ou antérieure  %}
**Mettre à jour la variable `slideConstraint`**<br>
La variable publique `slideConstraint` provient de la super classe `ABKInAppMessageSlideupViewController`. 

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
Visitez le dépôt de démonstration Braze pour la fonction [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17).
{% enddetails %}
{% endtab %}
{% tab Objectif-C %}
**Mettre à jour la variable `offset`**<br>
Mettre à jour la variable `offset` et définissez votre propre décalage pour répondre à vos besoins.
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
{% details Version 3.34.0 ou antérieure  %}
**Mettre à jour la variable `slideConstraint`**<br>
La variable publique `slideConstraint` provient de la super classe `ABKInAppMessageSlideupViewController`. 

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
**Remplacer et définir une contrainte personnalisée**<br>
Remplacez `beforeMoveInAppMessageViewOnScreen()` et définissez votre propre valeur de contrainte personnalisée pour répondre à vos besoins. La valeur originale est définie dans la superclasse.

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details Version 3.34.0 ou antérieure %}
```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objectif-C %}
**Remplacer et définir une contrainte personnalisée**<br> 
Remplacez `beforeMoveInAppMessageViewOnScreen()` et définissez votre propre valeur de contrainte personnalisée pour répondre à vos besoins. La valeur originale est définie dans la superclasse.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details Version 3.34.0 ou antérieure  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

**Modifier la contrainte pour l'orientation de l'appareil**<br>
Ajustez la valeur respective dans `viewWillTransition()`, car la sous-classe assume la responsabilité de maintenir la contrainte synchronisée lors des changements de mise en page.

### Message in-app modal personnalisé

![Un iPhone affichant un message in-app modal qui vous permet de parcourir une liste d’équipes sportives et de sélectionner celle que vous préférez. Au bas de cet envoi in-app, il y a un grand bouton bleu de soumission.]({% image_buster /assets/img/iam_implementation/modal.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Un `ABKInAppMessageModalViewController` peut être sous-classé pour tirer parti de `UIPickerView` offrant des moyens attrayants de collecter de précieux attributs d’utilisateur. Le message in-app modal personnalisé vous permet d’utiliser le contenu connecté ou toute liste disponible pour afficher et recueillir des attributs à partir d’une liste dynamique d’éléments. 

Vous pouvez interjeter vos propres vues dans des messages in-app sous-classés. Cet exemple illustre comment un `UIPickerView` peut être utilisé pour étendre la fonctionnalité d’un `ABKModalInAppMessageViewController`.

Visitez le [ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift) pour commencer.

#### Configuration du tableau de bord

Pour configurer un message in-app modal dans le tableau de bord, vous devez fournir une liste d’éléments formatés comme une chaîne séparée par des virgules. Dans notre exemple, nous utilisons le contenu connecté pour extraire une liste de noms d’équipes JSON et les formater en conséquence.

![Le composeur de messages in-app montre un aperçu de ce à quoi le message in-app ressemblera, mais à la place affiche la liste des articles que vous avez fournis à Braze. Comme l'interface utilisateur de Braze n'affiche pas votre message personnalisé in-app à moins qu'il ne soit envoyé à un téléphone, l'aperçu n'est pas représentatif de l'aspect de votre message. Nous vous recommandons donc de le tester avant de l'envoyer.]({% image_buster /assets/img/iam_implementation/dashboard1.png %})

Dans les paires clé-valeur, fournissez un `attribute_key` ; cette clé, ainsi que la valeur sélectionnée par l’utilisateur, seront enregistrées dans son profil d’utilisateur en tant qu’attribut personnalisé. Votre logique d’affichage personnalisé doit gérer les attributs utilisateur envoyés à Braze.

Le dictionnaire `extras` dans l’objet `ABKInAppMessage` vous permet de rechercher une clé `view_type` (le cas échéant) qui signale la vue correcte à afficher. Il est important de noter que les messages in-app sont configurés par message, de sorte que les vues modales personnalisées et par défaut puissent fonctionner harmonieusement.

![Deux paires clé-valeur présentes dans le compositeur de messages. La première paire clé-valeur a pour "attribute_key" "Favorite Teams", et la seconde a pour "view_type" "picker".]({% image_buster /assets/img/iam_implementation/dashboard2.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
**Utilisation de `view_type` pour le comportement d'affichage de l'interface utilisateur**<br>
Interroger le dictionnaire `extras` pour votre `view_type` pour charger le contrôleur de visualisation sous-classé souhaité.

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
{% tab Objectif-C %}
**Utilisation de `view_type` pour le comportement d'affichage de l'interface utilisateur**<br>
Interroger le dictionnaire `extras` pour votre `view_type` pour charger le contrôleur de visualisation sous-classé souhaité.

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
**Remplacer et fournir une vue personnalisée**<br>
Remplacez `loadView()` et définissez votre propre affichage personnalisé pour répondre à vos besoins.
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab Objectif-C %}
**Remplacer et fournir une vue personnalisée**<br>
Remplacez `loadView()` et définissez votre propre affichage personnalisé pour répondre à vos besoins.
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
**Formater les variables pour une liste dynamique**<br>
Avant de recharger les composants `UIPickerView`, la variable de message `inAppMessage` sort sous forme de _chaîne de caractères_. Ce message doit être formaté comme un ensemble d’éléments à afficher correctement. Par exemple, cela peut être effectué en utilisant [`components(separatedBy: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components).
```swift
override func viewDidLoad() {
  super.viewDidLoad()
 
  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objectif-C %}
**Formater les variables pour PickerView**<br>
Avant de recharger les composants `UIPickerView`, la variable de message `inAppMessage` sort sous forme de _chaîne de caractères_. Ce message doit être formaté comme un ensemble d’éléments à afficher correctement. Par exemple, cela peut être effectué en utilisant [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc).
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
**Attribuer un attribut personnalisé**<br>
À l’aide de la sous-classe, après qu’un utilisateur appuie sur Envoyer, transmettez l’attribut avec sa valeur sélectionnée correspondante à Braze.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objectif-C %}
**Attribuer un attribut personnalisé**<br>
À l’aide de la sous-classe, après qu’un utilisateur appuie sur Envoyer, transmettez l’attribut avec sa valeur sélectionnée correspondante à Braze.
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
Intéressé par l’utilisation de nos messages in-app modaux personnalisés pour partager des vidéos sur FaceTime ? Consultez notre [guide d’implémentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/shareplay/) des messages in-app SharePlay.
{% endalert%}

### Message in-app complet personnalisé

![Un message in-app qui affiche une liste d’options de configuration avec des interrupteurs à côté de chaque option. Au bas du message se trouve un grand bouton bleu d'envoi.]({% image_buster /assets/img/iam_implementation/fullscreen.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Utilisez des messages in-app complets personnalisés pour créer des invites interactives et conviviales pour recueillir de précieuses données client. L’exemple à droite montre une implémentation du message in-app personnalisé complet réinventée comme un primer push interactif avec des préférences de notification. 

Visitez le [`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift) pour commencer.

#### Configuration du tableau de bord

Pour configurer un message in-app complet dans le tableau de bord, vous devez fournir une liste de vos balises formatées en tant que chaîne séparée par des virgules. 

Dans les paires clé-valeur, fournissez un `attribute_key` ; cette clé, ainsi que la valeur sélectionnée par l’utilisateur, seront enregistrées dans son profil d’utilisateur en tant qu’attribut personnalisé. Votre logique d’affichage personnalisé doit gérer les attributs utilisateur envoyés à Braze.

![Trois paires clé-valeur présentes dans le compositeur de messages. La première paire clé-valeur "attribute_key" est définie comme "Push Tags", la deuxième "subtitle_text" est définie comme "Enabling notifications will also...", et la troisième "view_type" est définie comme "table_list".]({% image_buster /assets/img/iam_implementation/dashboard3.png %}){: style="max-width:65%;"}

#### Interception des touches de message in-app
![Un appareil Apple affichant des rangées de paramètres et d’interrupteurs. La vue personnalisée gère les boutons, et tout contact en dehors des boutons est traité par le message in-app et le fait disparaître.]({% image_buster /assets/img/iam_implementation_guide.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
L’interception des touchés de message in-app est essentielle pour que les boutons du message in-app personnalisé complet fonctionnent correctement. Par défaut, le `ABKInAppMessageImmersive` ajoute un outil de reconnaissance des gestes tactiles au message, afin que les utilisateurs puissent ignorer les messages sans boutons.. En ajoutant un `UISwitch` ou un bouton à la hiérarchie de la vue`UITableViewCell`, les touches sont maintenant gérées par notre affichage personnalisé. À partir d’iOS 6, les boutons et autres commandes ont la priorité lors de l’utilisation de reconnaissances de gestes, ce qui permet à notre message in-app personnalisé de fonctionner comme il se doit. 

