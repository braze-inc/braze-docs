---
nav_title: Personnalisation
article_title: Personnalisation des messages dans l'application pour le Web
platform: Web
channel: messages intégrés à l'application
page_order: 3
page_type: Référence
description: "Cet article couvre la personnalisation de la messagerie dans l'application via le Braze SDK."
---

# Personnalisation {#in-app-message-customization}

Tous les types de messages dans l'application de Braze sont hautement personnalisables à travers les messages, les images, les icônes [Font Awesome][15]  , cliquez sur actions, analytique, style modifiable, options d'affichage personnalisées et options de livraison personnalisées. Plusieurs options peuvent être configurées par message dans l'application à partir de [dans le tableau de bord]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/). Braze offre en outre de multiples niveaux de personnalisation avancée pour satisfaire une variété de cas d'utilisation et de besoins.

## Suppléments de la paire Key-value

Les objets de message intégrés peuvent transporter des paires clé-valeur comme propriété `extras`. Celles-ci sont spécifiées dans le tableau de bord sous « Paramètres de messages supplémentaires » lors de la création d'une campagne de message dans l'application. Celles-ci peuvent être utilisées pour envoyer des données en même temps qu'un message dans l'application pour une gestion ultérieure de votre site. Par exemple :

```javascript
import braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  if (inAppMessage instanceof braze.InAppMessage) {
    var extras = inAppMessage. xtras;
    if (extras) {
      for (var key in extras) {
        console. og("clé : " + clé + ", valeur: " + extras[key]);
      }
    }
  }
  braze. isplay.showInAppMessage(inAppMessage);
});
```

### Index par défaut des messages dans l'application

Par défaut, les messages In-App sont affichés en utilisant `z-index: 1050`. Ceci est configurable en utilisant l'option d'initialisation `inAppMessageZIndex` [][41] dans le scénario où votre site web propose des éléments avec des valeurs plus élevées que cela.

**Note**: Cette option a été introduite dans Web SDK v3.3.0. Les anciens SDK doivent être mis à jour pour utiliser cette option.

```javascript
importer le braze depuis "@braze/web-sdk";
braze.initialize("VOTRE-API-KEY", {
    baseUrl: "VOTRE-API-ENDPOINT",
    inAppMessageZIndex: 9001
});
```

### Style personnalisé

Les éléments de Braze UI sont fournis avec une apparence par défaut qui créent une expérience de message neutre dans l'application et vise à la cohérence avec d'autres plates-formes mobiles de Braze. Les styles par défaut de Braze sont définis en CSS dans le Braze SDK. En écrasant les styles sélectionnés dans votre application, il est possible de personnaliser nos types de messages standards dans l'application avec vos propres images d'arrière-plan. familles de polices, styles, tailles, animations, et plus encore. Par exemple, ce qui suit est un exemple de remplacement qui fera apparaître les en-têtes d'un message dans l'application en italique :

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
}
```

Voir les [JSDocs][2] pour plus d'informations.

## Ouvrir le lien du message dans un nouvel onglet

Pour définir vos liens de message dans l'application à ouvrir dans un nouvel onglet, définissez l'option `openInAppMessagesInNewTab` à `true` pour forcer tous les liens des clics de message dans l'application à ouvrir dans un nouvel onglet ou une nouvelle fenêtre.

```javascript
appboy.initialize('clé api', { openInAppMessagesInNewTab: true});
```

## Annulation du message dans l'application

Par défaut, quand un message dans l'application apparaît, En appuyant sur le bouton d'échappement ou en cliquant sur l'arrière-plan grisé de la page, le message sera ignoré. Configurer l'option `requireExplicitInAppMessageDismissal` [d'initialisation][41] pour empêcher ce comportement et exiger un clic de bouton explicite pour rejeter les messages.

```javascript
importer le braze depuis "@braze/web-sdk";
braze.initialize("VOTRE-API-KEY", {
    baseUrl: "VOTRE-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html
[15]: https://fontawesome.com/?from=io
[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions
[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions
[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions
