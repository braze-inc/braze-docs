{% multi_lang_include developer_guide/prerequisites/web.md %}

## Déclencheurs de messages

## Types de déclencheurs

Les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Any Purchase`, `Specific Purchase`,`Session Start` , `Custom Event`, et `Push Click`. Veuillez noter que les `Specific Purchase`déclencheurs`Custom Event` et contiennent également des filtres de propriétés robustes.

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API, mais uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, reportez-vous à la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Sémantiques de livraison

Tous les messages in-app éligibles sont envoyés sur l'appareil de l'utilisateur au début de sa session. À la livraison, le SDK préchargera les ressources afin qu'elles soient disponibles au moment du déclencheur, ce qui minimisera la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera délivré.

Pour plus d'informations sur la sémantique de démarrage de session du SDK, veuillez [consulter la section Cycle de vie de la session]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/).

### Limites de débit

Par défaut, vous pouvez envoyer un message in-app une fois toutes les 30 secondes.

Pour contourner cela, veuillez ajouter la propriété suivante à votre configuration Braze, avant l'initialisation de l'instance Braze. Vous pouvez le définir sur n'importe quel nombre entier positif, qui représente l'intervalle de temps minimum en secondes. Par exemple :

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Paires clé-valeur

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur que l'objet de message in-app peut utiliser pour`extras` envoyer des données à votre application. Par exemple :

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

## Désactivation des déclencheurs automatiques

Pour éviter que les messages in-app ne se déclenchent automatiquement :

Veuillez supprimer l'appel à`braze.automaticallyShowInAppMessages()`  dans votre extrait de code de chargement, puis créez une logique personnalisée pour gérer l'affichage ou non des messages in-app.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Si vous ne supprimez `braze.automaticallyShowInAppMessages()`pas  de votre site Web, veuillez contacter `braze.showInAppMessage`, le message pourrait s'afficher à plusieurs reprises.
{% endalert %}

Le paramètre `inAppMessage` sera une sous-classe [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) ou un objet [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html), chacun ayant des méthodes différentes d’abonnement aux événements de cycle de vie. Voir les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) pour une documentation complète.

Un seul message in-app [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) ou [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) peut être affiché à un instant donné. Si vous essayez de montrer un deuxième message modal ou complet, alors qu’un s’affiche déjà, `braze.showInAppMessage` renverra « faux » et le deuxième message ne s’affichera pas.

## Déclenchement manuel des messages

### Affichage d'un message en temps réel

Les messages in-app peuvent également être créés dans l’application et affichés localement en temps réel. Toutes les options de personnalisation disponibles sur le tableau de bord sont également disponibles localement. Ceci est particulièrement utile pour afficher les messages que vous souhaitez déclencher dans l’application en temps réel. Cependant, l’analyse de ces messages créés localement ne sera pas disponible dans le tableau de bord de Braze.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Déclenchement de messages d'intention de sortie

Les messages d'intention de sortie sont des messages in-app qui ne perturbent pas l'expérience utilisateur et qui servent à communiquer des informations importantes aux visiteurs avant qu'ils ne quittent votre site.

Pour configurer des déclencheurs pour ces types de messages, veuillez implémenter une bibliothèque d'intention de sortie sur votre site web (telle que [la bibliothèque open source ouibounce](https://github.com/carlsednaoui/ouibounce)), puis utilisez le code suivant pour enregistrer`'exit intent'`un événement personnalisé dans Braze. Désormais, vos futures campagnes de messages in-app peuvent utiliser ce type de message comme déclencheur d'événement personnalisé.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
