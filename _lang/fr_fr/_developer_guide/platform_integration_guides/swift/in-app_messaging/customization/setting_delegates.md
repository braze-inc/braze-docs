---
nav_title: "Message in-app délégué à l'interface utilisateur"
article_title: "Délégué à l'interface utilisateur des messages in-app pour iOS"
platform: Swift
page_order: 2
description: "Cet article de référence porte sur la configuration d'un délégué de messages in-app iOS pour le SDK Swift."
channel:
  - in-app messages

---

# Délégué à l'interface utilisateur pour les messages in-app

> Utilisez l'option [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) pour personnaliser la présentation des messages in-app et réagir à divers événements du cycle de vie. Ce protocole délégué peut être utilisé pour recevoir des envois de messages in-app déclenchés en vue d'un traitement ultérieur, pour recevoir des événements liés au cycle de vie de l'affichage et pour contrôler la synchronisation de l'affichage. 

## Conditions préalables

Pour utiliser `BrazeInAppMessageUIDelegate`:
* Vous devez utiliser l'implémentation par défaut [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) comme `inAppMessagePresenter`. 
* Vous devez inclure la bibliothèque `BrazeUI` dans votre projet.

## Configuration du délégué pour les messages in-app

Définissez votre objet délégué [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) sur l'instance Braze en suivant cet exemple de code :

{% tabs %}
{% tab swift %}

Tout d'abord, implémentez le protocole `BrazeInAppMessageUIDelegate` et toutes les méthodes correspondantes que vous souhaitez. Dans l'exemple ci-dessous, nous implémentons ce protocole dans la classe `AppDelegate` de notre application.

```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```

Attribuez ensuite l'objet `delegate` à l'instance `BrazeInAppMessageUI` avant d'attribuer l'interface utilisateur du message in-app à votre `inAppMessagePresenter`.

```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```

{% endtab %}
{% tab OBJECTIF-C %}

Tout d'abord, implémentez le protocole `BrazeInAppMessageUIDelegate` et toutes les méthodes correspondantes que vous souhaitez. Dans l'exemple ci-dessous, nous implémentons ce protocole dans la classe `AppDelegate` de notre application.

```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```

Attribuez ensuite l'objet `delegate` à l'instance `BrazeInAppMessageUI` avant d'attribuer l'interface utilisateur du message in-app à votre `inAppMessagePresenter`.

```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

Toutes les méthodes de délégation ne sont pas disponibles en Objective-C en raison de l'incompatibilité de leurs paramètres avec l’exécution du langage.

{% endtab %}
{% endtabs %}

### Guide étape par étape

Pour obtenir une description étape par étape de l’implémentation du délégué de l'interface utilisateur des messages in-app, reportez-vous à ce [tutoriel](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

## Personnalisation de l'envoi des messages in-app pour iOS

### Définir une orientation préférée

Vous pouvez configurer tous les messages in-app pour qu'ils soient présentés dans une orientation spécifique, quelle que soit l'orientation de l'appareil. Pour définir une orientation préférée, utilisez la [méthode de délégué](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` pour définir la propriété `preferredOrientation` sur le `PresentationContext`. 

{% tabs %}
{% tab swift %}

Par exemple, pour créer une orientation préférée de portrait :

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endtab %}
{% endtabs %}

Une fois le message in-app présenté, tout changement d'orientation de l'appareil alors que le message est encore affiché entraînera la rotation du message avec l'appareil, à condition que la configuration du message `orientation` le permette.

Notez que l’orientation de l’appareil doit également être prise en charge par la propriété `orientation` du message in-app à afficher. En outre, le paramètre `preferredOrientation` ne sera respecté que s'il est inclus dans les orientations d'interface prises en charge par votre application, dans la section **Informations sur le déploiement** des paramètres de votre cible dans Xcode.

![Orientations prises en charge dans Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
L'orientation n'est appliquée que pour la présentation du message. Lorsque l'appareil change d'orientation, l'affichage des messages adopte l'une des orientations qu'il prend en charge. Sur les appareils de petite taille (iPhones, iPod Touch), l'orientation paysage d'une fenêtre modale ou d'un message in-app complet peut conduire à un contenu tronqué.
{% endalert %}

### Modification de l'orientation des messages

Vous pouvez également définir l'orientation pour chaque message. Cette propriété définit tous les types d'orientation disponibles pour ce message. Pour ce faire, définissez la propriété `orientation` sur un `Braze.InAppMessage` donné :

{% tabs %}
{% tab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab OBJECTIF-C %}

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

## Désactivation du mode sombre

Pour empêcher les messages in-app d'adopter le style du mode sombre lorsque l'appareil de l'utilisateur a activé le mode sombre, implémentez la [méthode de délégué](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`. Le `PresentationContext` transmis à la méthode contient une référence à l'objet `InAppMessage` à présenter. Chaque `InAppMessage` possède une propriété `themes` contenant un thème de mode `dark` et `light`. Si vous définissez la propriété `themes.dark` sur la valeur `nil`, Braze présentera automatiquement le message in-app à l'aide de son thème lumineux.

Les types de messages in-app avec boutons ont un objet `themes` supplémentaire sur leur propriété `buttons`. Pour empêcher les boutons d'adopter le style du mode sombre, vous pouvez utiliser l'option [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) pour créer un nouveau tableau de boutons avec un thème `light` et sans thème `dark`.

{% tabs %}
{% tab swift %}

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
{% tab OBJECTIF-C %}

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

## Personnalisation des clics sur les boutons

Pour accéder aux informations relatives au bouton de message in-app ou pour modifier le comportement du clic, implémentez la commande [`BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:shouldprocess:buttonid:message:view:)-122yi). Renvoyez `true` pour permettre à Braze de traiter l'action de clic, ou renvoyez `false` pour modifier le comportement.
{% tabs %}
{% tab swift %}

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
{% tab OBJECTIF-C %}
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


## Masquer la barre d’état pendant l’affichage

Pour les messages in-app `Full`, `FullImage` et `HTML`, le SDK masque la barre d'état par défaut. Pour les autres types de messages in-app, la barre d'état reste intacte. Pour configurer ce comportement, utilisez la [méthode de délégué](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` pour définir la propriété `statusBarHideBehavior` sur le `PresentationContext`. Ce champ prend l'une des valeurs suivantes :

| Comportement de masquage de la barre d'état            | Description                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | L'affichage des messages décide de l'état masqué de la barre d'état.                                 |
| `.hidden`                           | Masquez toujours la barre d'état.                                                           |
| `.visible`                          | Affichez toujours la barre d'état.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Personnalisation de la durée d'affichage 

Vous pouvez contrôler si un message in-app disponible s'affichera à certains moments de votre expérience sur communication. Si, dans certaines situations, vous ne souhaitez pas que le message in-app apparaisse, par exemple pendant un jeu en plein écran ou sur un écran de chargement, vous pouvez retarder ou supprimer les messages in-app en attente. Pour contrôler le moment de l'envoi du message in-app, utilisez la [méthode de délégué](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` pour définir la propriété `BrazeInAppMessageUI.DisplayChoice`. 

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

Configurez `BrazeInAppMessageUI.DisplayChoice` pour qu'il renvoie l'une des valeurs suivantes :

| Choix de l'affichage                      | Comportement                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | Le message s’affichera immédiatement Il s'agit de la valeur par défaut.                                                       |
| `.reenqueue`                        | Le message ne s’affichera pas et sera replacé sur le dessus de la pile.                                       |
| `.later`                            | Le message ne s’affichera pas et sera replacé sur le dessus de la pile. (Déclassé, veuillez utiliser `.reenqueue`) |
| `.discard`                          | Le message sera supprimé et ne sera pas affiché.                                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Exemples d’implémentation

Voir `InAppMessageUI` dans notre dossier Exemples pour un exemple en [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) et [Objective-C.](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)

