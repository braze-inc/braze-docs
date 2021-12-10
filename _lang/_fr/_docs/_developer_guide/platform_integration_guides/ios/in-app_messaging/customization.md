---
nav_title: Personnalisation
article_title: Personnalisation des messages In-App pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence couvre les options de personnalisation de la messagerie intégrée pour votre application iOS."
channel:
  - messages intégrés à l'application
---

# Personnalisation {#in-app-message-customization}

Tous les types de messages de Braze dans l'application sont hautement personnalisables entre les messages, les images, les icônes [Font Awesome][26] , cliquez sur actions, analytique, style modifiable, options d'affichage personnalisées et options de livraison personnalisées. Plusieurs options peuvent être configurées par message dans l'application à partir de [dans le tableau de bord][13]. Braze offre en outre de multiples niveaux de personnalisation avancée pour satisfaire une variété de cas d'utilisation et de besoins.

{% alert important %}
Par défaut, les messages dans l'application sont activés après avoir terminé l'intégration standard du SDK, y compris la prise en charge du GIF. <br><br> __Notez que l'intégration de `SDWebImage` est nécessaire si vous prévoyez d'utiliser notre interface utilisateur Braze pour afficher des images__ dans les messages In-App iOS, Flux d'actualités ou Cartes de contenu.
{% endalert %}

## Suppléments de la paire Key-value

`Les objets ABKInAppMessage` peuvent porter des paires clé-valeur sous la forme `d'extras`. Elles sont spécifiées sur le tableau de bord lors de la création d'une campagne. Les paires de valeurs clés peuvent être utilisées pour envoyer des données en même temps qu'un message dans l'application pour une gestion ultérieure de votre application.

## Paramétrage des délégués

L'affichage des messages et la personnalisation de la livraison dans l'application peuvent être réalisés en code en définissant nos délégués optionnels.

### Délégué du message dans l'application

Le délégué [`ABKInAppMessageUIDelegate`][34] peut être utilisé pour recevoir des payloads de messages déclenchés dans l'application pour un traitement ultérieur, recevoir les événements du cycle de vie de l'affichage et contrôler l'affichage du timing.

Définissez votre objet délégué `ABKInAppMessageUIDelegate` sur l'instance Braze en appelant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

Voir notre [application d'échantillon de message dans l'application][35] pour un exemple. Notez que si vous n'incluez pas la bibliothèque de l'interface utilisateur de Braze dans votre projet (rare), ce délégué n'est pas disponible.

### Délégué du message dans l'application principale

Si vous n'incluez pas la bibliothèque de l'interface utilisateur de Braze dans votre projet et que vous souhaitez recevoir des payloads de messages dans l'application pour un traitement ultérieur ou un affichage personnalisé dans votre application, implémentez le protocole [`ABKInAppMessageControllerDelegate`][16].

Définissez votre objet délégué `ABKInAppMessageControllerDelegate` sur l'instance Braze en appelant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

Vous pouvez également définir votre délégué de message dans l'application au moment de l'initialisation via `appboyOptions` en utilisant la clé `ABKInAppMessageControllerDelegateKey`.
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"VOTRE API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "VOTRE-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## Personnalisation de l'orientation

### Définition de l'orientation pour tous les messages dans l'application

Pour définir une orientation fixe pour tous les messages dans l'application, vous pouvez définir la propriété `supporttedOrientationMask` sur `ABKInAppMessageUIController`. Ajoute le code suivant après l'appel de votre application à `startWithApiKey:inApplication:withLaunchOptions:`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Définit l'orientation du message dans l'application sur le portrait.
// Utilisez UIInterfaceOrientationMaskLandscape pour afficher les messages dans l'application dans le paysage
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Définit l'orientation du message dans l'application au portrait
// Utiliser .landscape pour afficher les messages dans l'application en mode paysage
si let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController comme? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

Ensuite, tous les messages dans l'application seront affichés dans l'orientation prise en charge, quelle que soit l'orientation de l'appareil. Veuillez noter que l'orientation de l'appareil doit également être prise en charge par la propriété `orientation` du message dans l'application afin que le message puisse s'afficher. Pour plus d'informations, voir la section ci-dessous.

### Réglage de l'orientation par message in-app

Vous pouvez également définir l'orientation par message. Pour ce faire, [définissez un délégué de message dans l'application][23]. Ensuite, dans votre `beforeInAppMessageDisplayed:` méthode de délégation, définissez la propriété `orientation` sur le `ABKInAppMessage`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Définit l'orientation inAppMessage au portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Définit l'orientation inAppMessage au paysage
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift    
  // Définit l'orientation de inAppMessage au portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Définit l'orientation inAppMessage au paysage
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

Les messages dans l'application ne s'afficheront pas si l'orientation de l'appareil ne correspond pas à la propriété `orientation` du message dans l'application.

Pour *iPads*, les messages dans l'application apparaîtront dans le style de l'orientation préférée de l'utilisateur, quelle que soit l'orientation réelle de l'écran.

## Gestion personnalisée de l'affichage des messages dans l'application

Lorsque le Délégué [`ABKInAppMessageControllerDelegate`][16] est défini, la méthode de délégué suivante sera appelée avant que les messages intégrés ne soient affichés :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Si vous n'avez implémenté que [`ABKInAppMessageUIDelegate`][34], la méthode de délégation de l'interface utilisateur suivante sera appelée à la place :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Vous pouvez personnaliser la gestion des messages dans l'application en implémentant cette méthode de délégué et en renvoyant l'une des valeurs suivantes pour `ABKInAppMessageDisplayChoice`:

| `format@@0 ABKInAppMessageDisplay Choice`      | Comportement                                                    |
| ---------------------------------------------- | --------------------------------------------------------------- |
| `format@@0 ABKDisplayInAppMessageNow`          | Le message sera affiché immédiatement                           |
| `Afficher plus tard dans l'application`        | Le message ne sera pas affiché et sera placé en haut de la pile |
| `AbkDiscardé dans le message de l'application` | Le message sera supprimé et ne sera pas affiché                 |

Vous pouvez utiliser la méthode `beforeInAppMessageDisplay:` pour ajouter la logique d'affichage des messages dans l'application, personnalisez les messages dans l'application avant que Braze ne les affiche, ou opt-out de la logique d'affichage des messages dans l'application de Braze et de l'interface utilisateur entièrement.

Pour un exemple d'implémentation, voir notre [Application Exemple de Message In-App][36].

### Remplacer les messages dans l'application avant l'affichage

Si vous souhaitez modifier le comportement d'affichage des messages dans l'application, vous devriez ajouter toute logique d'affichage nécessaire à votre `beforeInAppMessageDisplayed:` méthode de délégation. Par exemple, vous pourriez vouloir afficher le message dans l'application en haut de l'écran si le clavier est en cours d'affichage, ou prenez le modèle de données du message intégré et affichez le message dans l'application vous-même.

Si la campagne IAM ne s'affiche pas au début de la session, assurez-vous que vous avez la logique d'affichage nécessaire ajoutée à votre `beforeInAppMessageDisplayed:` méthode de délégation. Cela permet à la campagne IAM de s'afficher en haut de l'écran, même si le clavier est affiché.

### Masquer la barre d'état pendant l'affichage

Pour les messages dans l'application `Full` et `HTML` , le SDK tentera par défaut de placer le message au-dessus de la barre d'état. Cependant, dans certains cas, la barre d'état peut toujours apparaître au-dessus du message dans l'application. Depuis la version [3.21. du SDK iOS](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211), vous pouvez forcer la barre d'état à se cacher lors de l'affichage de messages dans l'application `Full` et `HTML` en définissant `ABKInAppMessageHideStatusBarKey` à `YES` dans les `appboyOptions` passé à `startWithApiKey :`.

### Impressions et clics de journalisation

La connexion dans l'application des messages d'impressions et de clics n'est pas automatique lorsque vous implémentez une gestion entièrement personnalisée (*i.e.* si vous contournez l'affichage du message dans l'application de Braze en retournant `ABKDiscardInAppMessage` dans votre `beforeInAppMessageDisplay:`). Si vous choisissez d'implémenter votre propre interface utilisateur en utilisant nos modèles de messages intégrés, vous devez enregistrer les statistiques avec les méthodes suivantes sur la classe `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Enregistre qu'un utilisateur a vu un message dans l'application avec le serveur Braze.
- (void) logInAppMessageImpression;
// enregistre qu'un utilisateur a cliqué sur un message dans l'application avec le serveur Braze.
- (void) logInAppMessageClick;
```

{% endtab %}
{% tab swift %}

```swift
// Enregistre qu'un utilisateur a vu un message dans l'application avec le serveur Braze.
func logInAppMessageImpression()
// enregistre qu'un utilisateur a cliqué sur un message dans l'application avec le serveur Braze.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

De plus, vous devriez faire des clics sur les sous-classes de `ABKInAppMessageImmersive` (*i.*., `Modal` et `Plein` messages dans l'application):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Logs bouton clic analytique
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs bouton clic analytique
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## Personnalisation du comportement des messages dans l'application au clic
La propriété `inAppMessageClickActionType` sur le `ABKInAppMessage` définit le comportement de l'action après que le message intégré soit cliqué. Cette propriété est en lecture seule. Si vous souhaitez modifier le comportement de clic du message dans l'application, vous pouvez appeler la méthode suivante sur `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

Le `inAppMessageClickActionType` peut être réglé sur une des valeurs suivantes :

| `ABKinAppMessageClickActionType`             | Comportement au clic                                                                                                                                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Afficher le flux de nouvelles`              | Le fil d'actualité s'affichera lorsque le message sera cliqué, et le message sera rejeté. **Note**: Le paramètre `uri` sera ignoré, et la propriété `uri` sur le `ABKInAppMessage` sera définie à nil. |
| `Rediriger vers les URI du message ABKInApp` | L'URI donnée sera affichée lorsque le message sera cliqué, et le message sera rejeté. **Note**: Le paramètre `uri` ne peut pas être nul.                                                               |
| `format@@0 ABKinAppMessageNoneClickAction`   | Le message sera rejeté quand il sera cliqué. **Note**: Le paramètre `uri` sera ignoré, et la propriété `uri` sur le `ABKInAppMessage` sera définie à nil.                                              |

### Personnalisation des clics du corps du message dans l'application

La méthode de délégation [`ABKInAppMessageUIDelegate`][34] suivante est appelée quand un message intégré est cliqué :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

### Personnalisation des clics sur le bouton de message dans l'application

Pour les clics sur les boutons de messages intégrés à l'application et les boutons de messages HTML dans l'application (*i.e.*, liens), [`ABKInAppMessageUIDelegate`][34] inclut les méthodes de délégués suivantes :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             bouton:(ABKInAppMessageButton *)bouton;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             cliqué:(nullable NSURL *)clickedURL
                               boutonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 bouton: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Chaque méthode renvoie une valeur `BOOL` pour indiquer si Braze doit continuer à exécuter l'action de clic.

Pour accéder au type d'action de clic d'un bouton dans une méthode déléguée, vous pouvez utiliser le code suivant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *boutons = immersiveIAM. uttons;
      pour (ABKInAppMessageButton *bouton en boutons) {
         // Type d'action du bouton est accessible par le bouton. uttonClickActionType
      }
}
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage est ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage com! ABKInAppMessageImmersive;
      pour le bouton dans inAppMessage.buttons comme! [ABKInAppMessageButton]{
        // Le type d'action du bouton est accessible via button.buttonClickActionType
      }
}
```

{% endtab %}
{% endtabs %}

> Lorsqu'un message intégré a des boutons, les seules actions de clic qui seront exécutées sont celles du modèle ABKInAppMessageButton. Le corps du message dans l'application ne sera pas cliquable même si le modèle ABKInAppMessage aura l'action de clic par défaut ("Fil d'actualité") assignée.

## Rejeter la fenêtre modale sur appui extérieur

La valeur par défaut est `NO`. Ceci détermine si le message modal dans l'application sera rejeté lorsque l'utilisateur clique en dehors du message dans l'application.

Pour activer les rejets de robinet externe, ajoutez un dictionnaire nommé `Braze` à votre fichier `Info.plist`. Dans le dictionnaire `Braze` , ajoutez la sous-entrée booléenne `DismissModalOnOutsideTap` et définissez la valeur à `OUI`. Notez qu'avant Braze iOS SDK v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Exemple `Info.plist` contenu:

```
<key>Braze</key>
<dict>
    <key>DismissModalOnOutsideTap</key>
    <boolean>OUI</boolean>
</dict>
```

Vous pouvez également activer la fonctionnalité au moment de l'exécution en définissant `ABKEnableDismissModalOnOutsideTapKey` à `OUI` dans `appboyOptions`.

### Libellé du rejet de la modale sur appui extérieur

| DismissModalOnOutsideTap | Libellé                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| OUI                      | Les messages modaux dans l'application seront rejetés sur un appui extérieur                    |
| NON                      | Par défaut, les messages modaux dans l'application ne seront pas rejetés sur un appui extérieur |
{: .reset-td-br-1 .reset-td-br-2}

## Afficher les messages dans l'application dans un contrôleur de vue personnalisé

Les messages intégrés peuvent également être affichés dans un contrôleur de vue personnalisé que vous passez à Braze. Braze animera le message personnalisé dans l'application, ainsi que l'analyse du message dans l'application. Le contrôleur de vue doit répondre aux exigences suivantes :

- Il doit s'agir d'une sous-classe ou d'une instance de `ABKInAppMessageViewController`.
- La vue du contrôleur de vue retourné doit être une instance de `ABKInAppMessageView` ou de sa sous-classe.

La méthode de délégué de l'interface utilisateur suivante est appelée chaque fois qu'un message intégré est proposé à `ABKInAppMessageViewController` pour permettre à l'application de passer un contrôleur de vue personnalisé à Braze pour l'affichage des messages dans l'application :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

Tous nos contrôleurs de messages intégrés à l'application sont open-source. Vous pouvez utiliser des sous-classes ou des catégories pour personnaliser l'affichage ou le comportement des messages dans l'application.

Voir les [contrôleurs de visualisation des messages dans l'application][37] pour plus de détails.

## Déclenchement de messages personnalisés dans l'application

Par défaut, les messages dans l'application sont déclenchés par les types d'événements qui sont enregistrés par le SDK. Si vous souhaitez déclencher des messages dans l'application par des événements envoyés par le serveur, vous pouvez également y arriver.

Pour activer cette fonctionnalité, vous enverriez un push silencieux au périphérique qui permet au périphérique d'enregistrer un événement basé sur le SDK. Cet événement SDK déclencherait par la suite le message de l'utilisateur dans l'application.

### Étape 1 : Manipuler les paires push silencieux et les paires clé-valeur
Ajoute le code suivant dans l'application `(_:didReceiveRemoteNotification:fetchCompletionHandler:)` méthode :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"Un push a été reçu. );
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]! nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("Un push a été reçu");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] comme? String) != nil && (userInfo["CAMPAIGN_NAME"] comme? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

Lorsque le push silencieux est reçu, un événement SDK enregistré "In-App Message Trigger" sera connecté au profil de l'utilisateur. Notez que ces messages In-App ne se déclencheront que si le push silencieux est reçu pendant que l'application est au premier plan.

### Étape 2 : Créer une campagne de push

Créer une campagne de push silencieuse qui est déclenchée via l'événement envoyé par le serveur. Pour plus de détails sur la façon de créer une campagne de push silencieuse, reportez-vous à notre article sur [les notifications push silencieuses][39].

!\[Déclenchement d'événements du serveur\]\[40\]

La campagne "push" doit inclure des extras de la paire "clé-valeur" qui indiquent que cette campagne "push" est envoyée avec l'intention d'enregistrer un événement personnalisé du SDK. Cet événement sera utilisé pour déclencher le message dans l'application:

!\[IAM Silent Push\]\[41\]

Le code au sein de l'application `(_:didReceiveRemoteNotification:fetchCompletionHandler:)` méthode vérifie la clé `IS_SERVER_EVENT` et va enregistrer un événement personnalisé SDK si cela est présent.

Vous pouvez modifier le nom de l'événement ou les propriétés de l'événement en envoyant la valeur désirée dans les options de la paire clé-valeur du bloc push. Ces options peuvent être utilisées comme paramètre du nom de l'événement ou comme propriété d'événement lors de la journalisation de l'événement personnalisé.

### Étape 3 : Créer une campagne de message dans l'application

Créez votre campagne de message dans l'application à partir du tableau de bord de Brase. Cette campagne doit avoir une livraison basée sur l'action et être déclenchée à partir de l'événement personnalisé enregistré à partir de l'application `(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

Dans l'exemple ci-dessous, le message spécifique dans l'application à déclencher a été configuré en envoyant la propriété événement dans le cadre de la poussée silencieuse initiale.

!\[IAM Push Trigger Example\]\[42\]

> En raison d'un message push utilisé pour enregistrer un événement personnalisé enregistré par SDK, Braze devra stocker un jeton push pour chaque utilisateur pour activer cette solution. Pour les utilisateurs d'iOS, Braze ne stockera qu'un jeton à partir du moment où un utilisateur a reçu l'invite push de l'OS. Avant cela, l'utilisateur ne sera pas joignable en utilisant push et la solution ci-dessus ne sera pas possible.

## Déclarations de méthode

Pour plus d'informations, voir les fichiers d'en-tête suivants :

- [`ABKInAppMessage.h`][14]
- [`ABKInAppMessageController.h`][15]
- [`ABKInAppMessageControllerDelegate.h`][16]

## Exemples d'implémentation

Voir [`AppDelegate.m`][36], [`ViewController.m`][35] et [`CustomInAppMessageViewController.m`][19] dans l'application d'exemple de message.
[40]: {% image_buster /assets/img_archive/iosServerSentPush.png %} [41]: {% image_buster /assets/img_archive/iOSServerPush.png %} [42]: {% image_buster /assets/img_archive/iosIAMeventTrigger.png %}

[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageController.h
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h
[19]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/CustomInAppMessageViewController.m
[23]: #setting-delegates
[26]: http://fortawesome.github.io/Font-Awesome/
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[37]: https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
