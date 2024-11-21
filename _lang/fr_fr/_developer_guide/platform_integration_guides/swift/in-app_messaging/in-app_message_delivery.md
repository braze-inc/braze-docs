---
nav_title: Livraison de messages in-app
article_title: Livraison de messages in-app pour iOS
platform: Swift
page_order: 2
description: "Cet article traite de la distribution de messages in-app sous iOS. Il répertorie les différents types de déclencheurs, la sémantique de distribution et les étapes de déclenchement des événements pour le SDK Swift."
channel:
  - in-app messages

---

# Livraison de messages in-app

> Cet article de référence donne un aperçu de la distribution des messages in-app sous iOS. Il répertorie les différents types de déclencheurs, la sémantique de distribution et les étapes de déclenchement des événements.

## Types de déclencheurs

Les messages in-app sont déclenchés par des événements enregistrés par le SDK. Vous pouvez déclencher un message in-app à partir des types d'événements suivants : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, et `Push Click`. En outre, les déclencheurs `Specific Purchase` et `Custom Event` contiennent des filtres de propriétés robustes.

{% alert note %}
Les messages in-app déclenchés ne fonctionnent qu’avec des événements personnalisés enregistrés via le SDK de Braze. Les messages in-app peuvent être déclenchés via l’API ou les événements API (comme les événements d’achat). Si vous travaillez avec iOS, consultez notre article sur le [suivi des événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) pour en savoir plus.
{% endalert %}

## Activation des messages in-app

Pour permettre à Braze d'afficher des messages in-app, créez une implémentation du protocole `BrazeInAppMessagePresenter` et attribuez-la au `inAppMessagePresenter` facultatif de votre instance Braze. Vous pouvez également utiliser le présentateur par défaut de Braze UI en instanciant un objet `BrazeInAppMessageUI`.

Notez que vous devrez importer la bibliothèque `BrazeUI` pour accéder à la classe `BrazeInAppMessageUI`.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

## Sémantiques de livraison

Tous les messages in-app qu’un utilisateur peut recevoir sont délivrés à l’appareil de l’utilisateur au démarrage de session. Dès la livraison, le SDK capture à l’avance les actifs à mettre immédiatement à disponibilité au moment du déclenchement, réduisant ainsi la latence d’affichage.

Lorsqu’un événement déclencheur comporte plus d’un message in-app éligible associé, seul le message in-app avec la priorité la plus élevée sera livré.

Il peut y avoir une latence pour les messages in-app qui s’affichent immédiatement à la livraison (démarrage de la session et lors du clic d’une notification push) en raison des actifs ne faisant pas l’objet d’une capture à l’avance. Pour plus d’informations sur la sémantique de début de session du SDK, consultez notre documentation sur le [cycle de vie des sessions]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

## Intervalle de temps minimum entre les déclencheurs

Par défaut, nous appliquons des limites de débit d’une fois toutes les 30 secondes pour les messages in-app afin de garantir une expérience utilisateur de qualité.

Vous pouvez remplacer cette valeur en définissant la propriété `triggerMinimumTimeInterval` dans votre configuration Braze. Veillez à configurer cette valeur avant d'initialiser votre instance Braze. Définissez `triggerMinimumTimeInterval` sur la valeur d’entier souhaitée comme durée minimale en secondes entre les messages in-app :

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## Absence de déclencheur correspondant

Lorsque Braze ne parvient pas à trouver un déclencheur correspondant à un événement particulier, il appelle [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/). Implémentez cette méthode dans votre classe en adoptant `BrazeDelegate` pour gérer ce scénario. 

## La pile de messages in-app

### Ajout de messages in-app à la pile

Les utilisateurs peuvent recevoir un message in-app dans les situations suivantes :

- Un événement déclencheur de message in-app est déclenché
- Une session est lancée
- L’application est ouverte à partir d’une notification push

Lorsque l'événement déclencheur d'un message in-app est déclenché, il est placé sur une « pile ». Si plusieurs messages in-app sont dans la pile et en attente d’être affichés, Braze affichera le message in-app le plus récemment reçu (dernier entré, premier sorti).

Lorsqu'un utilisateur est éligible pour recevoir un message in-app, le `BrazeInAppMessagePresenter` demande le dernier message in-app de la pile de messages in-app. La pile ne conserve que les messages in-app stockés en mémoire et est effacée entre les lancements de l’application depuis le mode suspendu.

### Retour des messages in-app à la pile

Un message in-app déclenché peut être renvoyé à la pile dans les situations suivantes :

- Le message in-app est déclenché lorsque l’application est en arrière-plan.
- Un autre message in-app est actuellement visible.
- La [méthode de délégation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` a renvoyé `.reenqueue`.

Le message in-app déclenché sera placé en haut de la pile pour un affichage ultérieur lorsqu'un utilisateur est éligible pour recevoir un message in-app.

### Écarter les messages in-app

Un message in-app déclenché sera écarté dans les situations suivantes :

- La [méthode de délégation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` a renvoyé `.discard`.
- L’actif (fichier image ou ZIP) du message in-app n’a pas pu être téléchargé.
- Le message in-app est prêt à être affiché mais a dépassé le délai d'attente.
- L’orientation du appareil ne correspond pas à l’orientation du message in-app déclenché.

Le message in-app sera retiré de la pile. Après avoir été rejeté, le message in-app peut être déclenché ultérieurement par une autre instance de l'événement déclencheur.

## Création et affichage de messages in-app en temps réel

Si vous souhaitez afficher un message in-app à d'autres moments dans votre application, vous pouvez appeler manuellement la méthode [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) sur votre `inAppMessagePresenter`. Les messages in-app peuvent être créés localement dans l'application et affichés via Braze. Ceci est particulièrement utile pour afficher les messages que vous souhaitez déclencher dans l’application en temps réel.

Notez qu'en créant votre propre message in-app, vous vous désengagez de tout suivi analytique et devrez gérer manuellement l'enregistrement des clics et des impressions à l'aide de votre site `message.context`.

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

## Compléments de paires clé-valeur

Les objets `Braze.InAppMessage` peuvent porter des paires clé-valeur comme `extras`. Ces éléments sont spécifiés sur le tableau de bord lors de la création d’une campagne. Les paires clé-valeur peuvent être utilisées pour envoyer des données avec un message in-app pour un traitement ultérieur par votre application.

Prenons par exemple le cas où nous souhaitons personnaliser la présentation d'un message in-app en fonction du contenu de ses extras. Nous pourrions accéder aux paires clé-valeur dans sa propriété `extras` et définir une logique personnalisée à exécuter autour d'elle :

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

Pour une mise en œuvre complète, vous pouvez vous référer aux exemples de personnalisation des messages in-app dans notre [application Exemple.](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)

