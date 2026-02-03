{% multi_lang_include developer_guide/prerequisites/web.md %}

## Styles personnalisés

Les éléments de l’IU de Braze sont dotés d’un aspect et d’une convivialité par défaut qui créent une expérience de message in-app neutre et visent à assurer la cohérence avec d’autres plateformes mobiles Braze. Les styles par défaut de Braze sont définis en CSS dans le SDK de Braze. 

### Définition d'un style par défaut

En écrasant des styles sélectionnés dans votre application, vous pouvez personnaliser nos types de messages in-app standard avec vos propres images de fond, des familles de polices, des styles, des tailles, des animations, et bien plus encore. 

Par exemple, ce qui suit est un exemple de remplacement qui entraînera la mise en italique des en-têtes d’un message in-app :

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

Consultez les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) pour plus d'informations.

### Personnaliser le z-index

Par défaut, les messages in-app sont affichés en utilisant `z-index: 9001`. Ceci est configurable en utilisant l'option d'initialisation `inAppMessageZIndex ` [initiale](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) dans le cas où votre site web stylise des éléments avec des valeurs plus élevées que cela.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Cette fonctionnalité n'est disponible que pour le SDK Braze v3.3.0 et les versions ultérieures.
{% endalert %}

## Personnalisation des envois de messages

Par défaut, lorsqu'un message in-app s'affiche, le message peut être supprimé en appuyant sur la touche Échap ou en cliquant sur l'arrière-plan grisé de la page. Configurez l'[option d'initialisation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` sur `true` pour éviter ce comportement et exiger un clic de bouton explicite pour rejeter les messages. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Ouverture des liens dans un nouvel onglet

Pour configurer les liens de messages in-app pour qu’ils s’ouvrent dans un nouvel onglet, définissez l’option `openInAppMessagesInNewTab` sur `true` pour forcer tous les liens du message in-app à s’ouvrir dans un nouvel onglet ou une nouvelle fenêtre.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
