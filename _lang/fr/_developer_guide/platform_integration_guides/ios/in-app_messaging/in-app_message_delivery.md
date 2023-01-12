---
nav_title: Livraison de messages in-app
article_title: Livraison de messages in-app pour iOS
platform: iOS
page_order: 3
description: "Cet article couvre la livraison de messages in-app iOS, répertoriant différents types de déclencheurs, de sémantiques de livraison et d’étapes de déclenchement d’événements."
channel:
  - messages in-app

---

{% multi_lang_include archive/swift_upgrade_banner.md %}


# Livraison de messages in-app

## Types de déclencheurs

Notre produit de messages in-app vous permet de déclencher un affichage de messages in-app suite à plusieurs types d’événements différents : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` et `Push Click`. En outre, les déclencheurs `Specific Purchase` et `Custom Event` contiennent des filtres de propriétés robustes.

{% alert note %}
Les messages in-app déclenchés ne fonctionnent qu’avec des événements personnalisés enregistrés via le SDK et non par le biais des API REST. Si vous travaillez avec iOS, consultez notre article sur le [suivi des événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) pour en savoir plus. 
{% endalert %}

## Sémantiques de livraison

Tous les messages in-app qu’un utilisateur peut recevoir sont livrés au périphérique de l’utilisateur au démarrage de session. Pour plus d’informations sur les sémantiques de début de session du SDK, renseignez-vous au sujet de la [durée de vie des sessions][45]. Dès la livraison, le SDK capture à l’avance les actifs à mettre immédiatement à disponibilité au moment du déclenchement, réduisant ainsi la latence d’affichage.

Lorsqu’un événement déclencheur comporte plus d’un message in-app éligible associé, seul le message in-app avec la priorité la plus élevée sera livré.

Il peut y avoir une latence pour les messages in-app qui s’affichent immédiatement à la livraison (démarrage de la session et lors du clic d’une notification push) en raison des actifs ne faisant pas l’objet d’une capture à l’avance.

## Intervalle de temps minimum entre les déclencheurs

Par défaut, nos limites de débit des messages in-app sont à une fois toutes les 30 secondes afin de garantir une expérience utilisateur de qualité.

Vous pouvez remplacer cette valeur par la `ABKMinimumTriggerTimeIntervalKey` dans le paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définir le `ABKMinimumTriggerTimeIntervalKey` avec la valeur entière désirée comme durée minimale en secondes entre les messages in-app :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## Livraison locale de messages in-app

### La pile de messages in-app

#### Affichage des messages in-app

Lorsqu’un utilisateur est éligible à la réception d’un message in-app, le `ABKInAppMessageController` recevra le dernier message in-app sur la pile de messages in-app. La pile ne conserve que les messages in-app stockés en mémoire et est effacée entre les lancements de l’application depuis le mode suspendu.

{% alert important %}
N’affichez pas les messages in-app lorsque le clavier est affiché à l’écran, car le rendu n’est pas défini dans ce cas.
{% endalert %}

#### Ajout de messages in-app à la pile

Les utilisateurs peuvent recevoir un message in-app dans les situations suivantes :

- Un événement déclencheur de message in-app est déclenché
- Événement de début de session
- L’application est ouverte à partir d’une notification push

Les messages in-app déclenchés sont placés sur la pile lorsque leur événement déclencheur est déclenché. Si plusieurs messages in-app sont dans la pile et en attente d’être affichés, Braze affichera le message in-app le plus récemment reçu (dernier entré, premier sorti).

#### Retour des messages in-app à la pile

Un message in-app déclenché peut être renvoyé à la pile dans les situations suivantes :

- Le message in-app est déclenché lorsque l’application est en arrière-plan.
- Un autre message in-app est actuellement visible.
- La [méthode de délégation de l’IU][38]`beforeInAppMessageDisplayed:withKeyboardIsUp:` obsolète n’a pas été implémentée et le clavier est actuellement affiché.
- La [méthode de délégation][30] `beforeInAppMessageDisplayed:` ou la [méthode de délégation de l’IU][38] `beforeInAppMessageDisplayed:withKeyboardIsUp:` obsolète est renvoyée `ABKDisplayInAppMessageLater`.

#### Écarter les messages in-app

Un message in-app déclenché sera écarté dans les situations suivantes :

- La [méthode de délégation][30] `beforeInAppMessageDisplayed:` ou la [méthode de délégation de l’IU][38] `beforeInAppMessageDisplayed:withKeyboardIsUp:` obsolète est renvoyée `ABKDiscardInAppMessage`.
- L’actif (fichier image ou ZIP) du message in-app n’a pas pu être téléchargé.
- Le message in-app est prêt à être affiché, mais a dépassé le délai d’expiration.
- L’orientation du périphérique ne correspond pas à l’orientation du message in-app déclenché.
- Le message in-app est un message in-app complet, mais n’a pas d’image.
- Le message in-app est un message in-app modal uniquement composé d’image, mais n’a pas d’image.

#### Mettre manuellement en file d’attente l’affichage des messages in-app

Si vous souhaitez afficher un message in-app à d’autres moments dans votre application, vous pouvez afficher manuellement le message in-app le plus haut sur la pile en employant la méthode suivante :

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

### Création et affichage de messages in-app en temps réel

Les messages in-app peuvent également être créés localement dans l’application et affichés via Braze. Ceci est particulièrement utile pour afficher les messages que vous souhaitez déclencher dans l’application en temps réel. Braze ne prend pas en charge les analytiques des messages in-app créés localement.

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

[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate
[45]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
