---
nav_title: Livraison de Message In-App
article_title: Livraison de message dans l'application pour le Web
platform: Web
channel: messages intégrés à l'application
page_order: 4
page_type: Référence
description: "Cet article décrit la livraison de messages dans l'application via le SDK de Braze, comme l'affichage manuel de messages dans l'application ou l'envoi de messages d'intention de sortie."
---

# Envoi de messages dans l'application

## Types de déclenchement

Notre produit de message intégré vous permet de déclencher un affichage de message dans l'application en raison de plusieurs types d'événements différents : `Tout achat`, `Achat spécifique`, `Début de session`, `Événement personnalisé`, `Clic Push`.  De plus, les déclencheurs `Achat spécifique` et `Événement personnalisé` peuvent contenir des filtres de propriétés robustes.

{% alert note %}
Les messages activés dans l'application ne fonctionnent qu'avec les événements personnalisés enregistrés via le SDK et non via les API REST. Si vous travaillez avec une application web, consultez comment enregistrer les événements personnalisés [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

## Demandes de livraison
Tous les messages dans l'application pour lesquels un utilisateur est éligible sont automatiquement téléchargés sur le périphérique/navigateur de l'utilisateur lors d'un événement de début de session. et déclenché selon les règles d'envoi du message. Pour plus d'informations sur la sémantique de démarrage de la session SDK, consultez notre [documentation sur le cycle de vie de la session][10].

## Intervalle de temps minimum entre les déclencheurs
Par défaut, nous évaluons la limite des messages dans l'application à une fois toutes les 30 secondes pour assurer une expérience utilisateur de qualité. Pour remplacer cette valeur, vous pouvez passer l'option de configuration `minimumIntervalBetweenTriggerActionsInSeconds` à votre fonction [`initialiser`][9].

```js
// Définit l'intervalle de temps minimum entre les messages déclenchés dans l'application à 5 secondes au lieu de la valeur par défaut 30
appboy.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Affichage manuel du message dans l'application

Si vous ne voulez pas que votre site affiche immédiatement les nouveaux messages dans l'application quand ils sont déclenchés, vous pouvez désactiver l'affichage automatique et enregistrer vos propres abonnés à l'écran. Tout d'abord, trouvez et supprimez l'appel à `appboy.display.automaticallyShowNewInAppMessages()` de votre snippet. Ensuite, créez votre propre logique pour gérer un message In-App déclenché, où vous montrez ou ne montrez pas le message :

```javascript
appboy.subscribeToInAppMessage(function(inAppMessage) {
  // Affiche le message dans l'application. Vous pouvez reporter l'affichage ici en envoyant ce message au code dans votre propre application.
  // Si vous ne voulez pas utiliser les fonctionnalités d'affichage intégrées de Brase, vous pouvez également passer le message dans l'application à votre propre code d'affichage ici.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      appboy.display.showInAppMessage(inAppMessage);
  } else {
      // ne fait rien
  }
});
```

{% alert important %}
Si vous ne supprimez pas `appboy.display.automaticallyShowNewInAppMessages()` de votre site Web lorsque vous appelez également `appboy.display.showInAppMessage`, le message peut être affiché deux fois.
{% endalert %}

Le paramètre `inAppMessage` sera un appboy [`. nAppMessage`][2] sous-classe ou un appboy [`. l'objet ontrolMessage`][8] , dont chacun a différentes méthodes d'abonnement à des événements de cycle de vie. Voir les [JSDocs][2] pour une documentation complète.

> Un seul message [`modal`][17] ou [`plein`][41] dans l'application peut être affiché à la fois Si vous essayez d'afficher un deuxième message modal ou Full alors que l'un d'entre eux est déjà affiché, `appboy. isplay.showInAppMessage` retournera false, et le second message ne s'affichera pas.

## Messages locaux dans l'application

Les messages intégrés peuvent également être créés sur votre site et affichés localement en temps réel.  Toutes les options de personnalisation disponibles sur le tableau de bord sont également disponibles localement.  Ceci est particulièrement utile pour afficher les messages que vous souhaitez déclencher dans l'application en temps réel. Cependant, les analytiques sur ces messages créés localement ne seront pas disponibles dans le tableau de bord de Braze.

```javascript
  // Affiche un message de type slideup dans l'application.
  var message = new appboy.SlideUpMessage("Bienvenue au Brésil! Ceci est un message dans l'application.");
  message.slideFrom = appboy.InAppMessage.SlideFrom.TOP;
  appboy.display.showInAppMessage(message);
```

## Messages d'intention de sortie

Les messages d'intention de quitter dans l'application apparaissent lorsque les visiteurs sont sur le point de quitter votre site. Ils offrent une autre occasion de communiquer des informations importantes aux utilisateurs, sans pour autant interrompre leur expérience sur votre site.

Pour pouvoir envoyer ces messages, ajoutez d'abord une bibliothèque entent de sortie, comme [cette bibliothèque open-source][50] à votre site web. Ensuite, utilisez le code ci-dessous pour enregistrer 'intention de sortie' comme un événement personnalisé. Les campagnes de messages intégrés peuvent ensuite être créées dans le tableau de bord en utilisant « intention de sortie» comme événement personnalisé de déclenchement.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { appboy.logCustomEvent('exit intent'); }
});
```


[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html


[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html
[8]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ControlMessage.html
[9]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[50]: https://github.com/carlsednaoui/ouibounce
