{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Mise en place du délégué à l'interface utilisateur (obligatoire)

Pour personnaliser la présentation des messages in-app et réagir à divers événements du cycle de vie, vous devrez configurer des . [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). Il s'agit d'un protocole délégué utilisé pour la réception et le traitement des messages in-app déclenchés, la réception des événements du cycle de vie de l'affichage et le contrôle de la synchronisation de l'affichage. Pour utiliser `BrazeInAppMessageUIDelegate`, vous devez
- Utilisez l'implémentation par défaut [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) comme `inAppMessagePresenter`. 
- Incluez la bibliothèque `BrazeUI` dans votre projet.

### Étape 1 : Mettre en œuvre le protocole `BrazeInAppMessageUIDelegate`  

Tout d'abord, implémentez le protocole `BrazeInAppMessageUIDelegate` et toutes les méthodes correspondantes que vous souhaitez. Dans l'exemple ci-dessous, nous implémentons ce protocole dans la classe `AppDelegate` de notre application.

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIF-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### Étape 2 : Attribuer l'objet `delegate`  

Attribuez l'objet `delegate` à l'instance `BrazeInAppMessageUI` avant d'attribuer ce message in-app à l'interface utilisateur `inAppMessagePresenter`.

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIF-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
Toutes les méthodes de délégation ne sont pas disponibles en Objective-C en raison de l'incompatibilité de leurs paramètres avec l’exécution du langage.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour obtenir une description étape par étape de l’implémentation du délégué de l'interface utilisateur des messages in-app, reportez-vous à ce [tutoriel](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## Comportement lors du clic

Chaque objet `Braze.InAppMessage` contient une [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction) correspondante qui définit le comportement en cas de clic. 

### Cliquez sur les types d'action

La propriété `clickAction` de votre `Braze.InAppMessage` est par défaut `.none` mais peut être définie sur l'une des valeurs suivantes :

| `ClickAction` | Comportement au clic |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Ouvre l'URL donné dans un navigateur externe. Si `useWebView` est définie sur `true`, elle s'ouvrira dans une vue Web. |
| `.newsFeed` | Le fil d’actualité s’affiche lorsque l’on clique sur le message, et le message est rejeté.<br><br>**Remarque :** Le fil d'actualité est supprimé. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour plus de détails. |
| `.none` | Le message sera rejeté lorsque vous cliquerez. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Pour les messages in-app contenant des boutons, le message `clickAction` sera également inclus dans la charge utile finale si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

### Personnaliser le comportement du clic

Pour personnaliser ce comportement, vous pouvez modifier la propriété `clickAction` en vous référant à l'exemple suivant :

{% tabs %}
{% tab swift %}

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
{% tab OBJECTIF-C %}

La méthode `inAppMessage(_:prepareWith:)` n'est pas disponible en Objective-C.

{% endtab %}
{% endtabs %}

### Gestion du comportement personnalisé

La méthode de délégation [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) suivante est appelée en cas de clic sur un message in-app. Pour les clics sur les boutons de messages in-app et les boutons de messages in-app HTML (liens), un ID de bouton est fourni en tant que paramètre facultatif.

{% tabs %}
{% tab swift %}

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
{% tab OBJECTIF-C %}

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

Cette méthode renvoie une valeur booléenne indiquant si Braze doit continuer à exécuter l'action de clic.

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

## Personnalisation des fenêtres modales/boîtes de dialogue, etc.

Pour activer les rejets par touché extérieur, vous pouvez modifier la propriété `dismissOnBackgroundTap` de la structure `Attributes` du type de message in-app que vous souhaitez personnaliser. 

Par exemple, si vous souhaitez activer cette fonctionnalité pour les messages in-app de type fenêtre modale, vous pouvez configurer ce qui suit :

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIF-C %}

La personnalisation via `Attributes` n'est pas disponible en Objective-C.

{% endtab %}
{% endtabs %}

La valeur par défaut est `false`. Cela détermine si le message in-app modal sera rejeté lorsque l’utilisateur touche à l’extérieur du message in-app.

| `DismissModalOnOutsideTap` | Description |
|----------|-------------|
| `true`         | Les messages in-app modaux seront rejetés par touche extérieure.     |
| `false`        | Par défaut, les messages in-app modaux ne seront rejetés par touche extérieure. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus de détails sur la personnalisation des messages in-app, consultez cet [article](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).

## Personnalisation de l'orientation des messages

Vous pouvez personnaliser l'orientation de vos messages in-app. Vous pouvez définir une nouvelle orientation par défaut pour tous les messages ou définir une orientation personnalisée pour un seul message.

{% tabs local %}
{% tab tous les messages %}
Pour choisir une orientation par défaut pour tous les messages in-app, utilisez la méthode [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) pour définir la propriété `preferredOrientation` sur le site `PresentationContext`. 

Par exemple, pour définir le portrait comme orientation par défaut :

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

{% tab message unique %}
Pour définir l'orientation d'un seul message, modifiez la propriété `orientation` de `Braze.InAppMessage`:

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

Une fois le message in-app affiché, tout changement d'orientation de l'appareil pendant que le message est encore affiché entraînera la rotation du message avec l'appareil (à condition que la configuration du message `orientation` le permette).

L'orientation de l'appareil doit également être prise en charge par la propriété `orientation` du message in-app pour que le message s'affiche. En outre, le paramètre `preferredOrientation` ne sera respecté que s'il est inclus dans les orientations d'interface prises en charge par votre application, dans la section **Informations sur le déploiement** des paramètres de votre cible dans Xcode.

![Orientations prises en charge dans Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
L'orientation n'est appliquée que pour la présentation du message. Lorsque l'appareil change d'orientation, l'affichage des messages adopte l'une des orientations qu'il prend en charge. Sur les appareils de petite taille (iPhones, iPod Touch), l'orientation paysage d'une fenêtre modale ou d'un message in-app complet peut conduire à un contenu tronqué.
{% endalert %}

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

{% alert tip %}
Pour obtenir un exemple de `InAppMessageUI`, consultez notre [référentiel SDK Swift Bra](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) ze et [Objective-C.](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)
{% endalert %}

## Masquer la barre d'état

Pour les messages in-app `Full`, `FullImage` et `HTML`, le SDK masque la barre d'état par défaut. Pour les autres types de messages in-app, la barre d'état reste intacte. Pour configurer ce comportement, utilisez la [méthode de délégué](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` pour définir la propriété `statusBarHideBehavior` sur le `PresentationContext`. Ce champ prend l'une des valeurs suivantes :

| Comportement de masquage de la barre d'état            | Description                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | L'affichage des messages décide de l'état masqué de la barre d'état.                                 |
| `.hidden`                           | Masquez toujours la barre d'état.                                                           |
| `.visible`                          | Affichez toujours la barre d'état.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

## Personnalisation de l'invite d'évaluation de la boutique d'applications

Vous pouvez utiliser des messages in-app dans le cadre d'une campagne pour demander aux utilisateurs de rédiger un avis sur l'App Store.

{% alert note %}
Étant donné que cet exemple d'invite remplace le comportement par défaut de Braze, nous ne pouvons pas assurer automatiquement le suivi des impressions en cas de mise en œuvre. Vous devez [enregistrer vos propres analyses/analytiques]({{site.baseurl}}/developer_guide/analytics/)(si elles sont utilisées en tant qu'adjectifs).
{% endalert %}

### Étape 1 : Définir le délégué du message in-app

Tout d'abord, définissez l'élément [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_setting-up-the-ui-delegate-required) dans votre application. 

### Étape 2 : Désactiver le message par défaut d’évaluation de l’App Store

Ensuite, implémentez la `inAppMessage(_:displayChoiceForMessage:)` [méthode de délégation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) pour désactiver le message par défaut d'évaluation de l'App Store.

{% tabs %}
{% tab swift %}

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
{% tab OBJECTIF-C %}

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

### Étape 3 : Créer un lien profond

Dans votre code de traitement de liaison profonde, ajoutez le code suivant pour traiter le lien profond `{YOUR-APP-SCHEME}:app-store-review`. Notez que vous devrez importer `StoreKit` pour utiliser `SKStoreReviewController` :

{% tabs %}
{% tab swift %}

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
{% tab OBJECTIF-C %}

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

### Étape 4 : Définir un comportement personnalisé au clic

Créez ensuite une campagne de communication in-app avec les éléments suivants :

- La paire clé-valeur `"AppStore Review" : "true"`
- Le comportement en cours défini sur « Deep Link Into App », en utilisant le lien profond `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple limite les demandes d’évaluation de l’App Store à un maximum de trois fois par an pour chaque utilisateur. Votre campagne doit donc être [limitée]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) à trois fois par an et par utilisateur.<br><br>Les utilisateurs peuvent désactiver les invites de commentaires de l’App Store. Par conséquent, votre invite de révision personnalisée ne doit pas promettre qu’une invite de commentaire native de l’App Store s’affichera ou demander directement un commentaire.
{% endalert %}
