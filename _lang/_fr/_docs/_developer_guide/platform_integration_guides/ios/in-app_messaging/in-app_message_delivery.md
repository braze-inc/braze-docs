---
nav_title: Livraison de Message In-App
article_title: Livraison de Message In-App pour iOS
platform: iOS
page_order: 3
description: "Cet article couvre la livraison de messages dans l'application iOS, la liste des différents types de déclenchements, la sémantique de livraison et les étapes de déclenchement d'événements."
channel:
  - messages intégrés à l'application
---

# Envoi de messages dans l'application

## Types de déclenchement

Notre produit de message intégré vous permet de déclencher l'affichage de messages dans l'application en raison de plusieurs types d'événements différents : `Tout achat`, `Achat spécifique`, `Début de session`, `Événement personnalisé`, `Clic Push`.  De plus, les déclencheurs `Achat spécifique` et `Événement personnalisé` peuvent contenir des filtres de propriétés robustes.

{% alert note %}
Les messages activés dans l'application ne fonctionnent qu'avec les événements personnalisés enregistrés via le SDK et non via les API REST. Si vous travaillez avec iOS, regardez comment enregistrer les événements personnalisés [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

## Sémantique de livraison

Tous les messages dans l'application pour lesquels un utilisateur est éligible sont envoyés à l'appareil de l'utilisateur au démarrage de la session. Pour plus d'informations sur la sémantique de démarrage de la session SDK, consultez notre [documentation sur le cycle de vie de la session][45]. Lors de la livraison, le SDK va préextraire les actifs afin qu'ils soient disponibles immédiatement au moment du déclenchement, ce qui minimise la latence d'affichage.

Lorsqu'un événement déclencheur a plus d'un message admissible dans l'application, seul le message dans l'application avec la plus haute priorité sera distribué.

Pour les messages dans l'application qui s'affichent immédiatement à la livraison, (démarrage de la session, clic push), il peut y avoir une certaine latence en raison du fait que les actifs ne sont pas préludés.

## Intervalle de temps minimum entre les déclencheurs

Par défaut, nous évaluons la limite des messages dans l'application à une fois toutes les 30 secondes pour assurer une expérience utilisateur de qualité.

Vous pouvez remplacer cette valeur par le paramètre `ABKMinimumTriggerTimeIntervalKey` dans le paramètre `appboyOptions` passé à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez la `ABKMinimumTriggerTimeIntervalKey` à la valeur entière que vous voulez comme temps minimum en secondes entre les messages dans l'application:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Définit l'intervalle de temps de déclenchement minimum à 5 secondes
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "VOTRE-API-KEY", en:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## Envoi de messages locaux dans l'application

### La pile de messages dans l'application

#### Affichage des messages dans l'application

Lorsqu'un utilisateur est éligible à recevoir un message dans l'application, le `ABKInAppMessageController` sera offert le dernier message dans l'application de la pile de messages dans l'application. La pile ne persiste que dans les messages stockés dans l'application et est effacée entre le lancement de l'application en mode suspendu.

{% alert important %}
Ne pas afficher les messages dans l'application lorsque le clavier est affiché à l'écran, car le rendu n'est pas défini dans cette circonstance.
{% endalert %}

#### Ajout de messages dans l'application à la pile

Les utilisateurs peuvent recevoir un message dans l'application dans les situations suivantes :

- Un événement de déclenchement de message est déclenché dans l'application
- Événement de début de session
- L'application est ouverte depuis une notification push

Les messages déclenchés dans l'application sont placés au-dessus de la pile lorsque leur événement de déclenchement est déclenché. Si plusieurs messages dans l'application sont dans la pile et en attente d'être affichés, Braze affichera d'abord le message reçu le plus récemment dans l'application (dernier entré, premier sorti).

#### Retour des messages dans l'application à la pile

Un message dans l'application déclenché peut être renvoyé à la pile dans les situations suivantes :

- Le message dans l'application est déclenché lorsque l'application est en arrière-plan
- Un autre message dans l'application est actuellement visible
- La dépréciée `beforeInAppMessageDisplayed:withKeyboardIsUp:` [méthode déléguée de l'interface utilisateur][38] n'a **PAS** été implémentée, et le clavier est actuellement affiché
- La `beforeInAppMessageDisplayed:` [méthode déléguée][30] ou la dépréciée `beforeInAppMessageDisplayed:withKeyboardIsUp:` [méthode de déléguation UI][38] a retourné `ABKDisplayInAppMessageLater`

#### Abandon des messages dans l'application

Un message dans l'application déclenché sera supprimé dans les situations suivantes :

- La `beforeInAppMessageDisplayed:` [méthode déléguée][30] ou la dépréciée `beforeInAppMessageDisplayed:withKeyboardIsUp:` [méthode de déléguation de l'interface utilisateur][38] a retourné `ABKDiscardInAppMessage`
- La ressource (image ou fichier zip) du message intégré n'a pas pu être téléchargée
- Le message dans l'application est prêt à être affiché mais a dépassé la durée d'expiration
- L'orientation de l'appareil ne correspond pas à l'orientation du message dans l'application déclenchée
- Le message dans l'application est un message complet dans l'application, mais n'a pas d'image
- Le message dans l'application est un message modal dans l'application mais n'a pas d'image

#### Mettre en file d'attente manuellement l'affichage des messages dans l'application

Si vous souhaitez afficher un message dans l'application à d'autres moments dans votre application, vous pouvez afficher manuellement le message le plus haut de la pile en appelant la méthode suivante :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Création et affichage de messages en temps réel dans l'application

Les messages intégrés peuvent également être créés localement dans l'application et affichés via Braze. Ceci est particulièrement utile pour afficher les messages que vous souhaitez déclencher dans l'application en temps réel. Braze ne prend pas en charge les analyses des messages créés localement dans l'application.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}

[30]: #in-app-message-controller-delegate
[38]: #in-app-mssage-ui-delegate
[38]: #in-app-mssage-ui-delegate
[38]: #in-app-mssage-ui-delegate
[45]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
