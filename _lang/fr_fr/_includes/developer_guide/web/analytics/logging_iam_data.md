{% multi_lang_include developer_guide/prerequisites/web.md %}

## Données d'envoi des messages

L'enregistrement des [impressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression) et des [clics](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick) des messages in-app est effectué automatiquement lorsque vous utilisez la méthode `showInAppMessage` ou `automaticallyShowInAppMessage`.

Si vous n’utilisez pas ces méthodes et choisissez d’afficher manuellement le message à l’aide de votre propre code d’interface utilisateur, utilisez les méthodes suivantes pour enregistrer les analyses :

```javascript
// Registers that a user has viewed an in-app message with the Braze server.
braze.logInAppMessageImpression(inAppMessage);
// Registers that a user has clicked on the specified in-app message with the Braze server.
braze.logInAppMessageClick(inAppMessage);
// Registers that a user has clicked a specified in-app message button with the Braze server.
braze.logInAppMessageButtonClick(button, inAppMessage);
// Registers that a user has clicked on a link in an HTML in-app message with the Braze server.
braze.logInAppMessageHtmlClick(inAppMessage, buttonId?, url?)
```
