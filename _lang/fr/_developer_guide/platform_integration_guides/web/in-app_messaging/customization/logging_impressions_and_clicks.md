---
nav_title: Enregistrement des impressions et des clics
article_title: Enregistrement des impressions et des clics
platform: Web
channel: messages In-App
page_order: 3
page_type: reference
description: "Cet article concerne la journalisation des impressions des messages in-app et des clicks pour votre application web."

---

# Enregistrement des impressions et des clics

La journalisation des [impressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression) et des [clics](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick) s’effectue automatiquement lorsque vous utilisez `automaticallyDisplayInAppMessages` ou `showInAppMessage`.

Si vous n’utilisez pas ces méthodes et affichez manuellement le message à l’aide de votre propre code d’interface utilisateur, utilisez les méthodes suivantes pour enregistrer les analyses :

```javascript
// Enregistre qu’un utilisateur a visualisé un message in-app avec le serveur Braze.
braze.logInAppMessageImpression(message);
// Enregistre qu’un utilisateur a cliqué sur un message in-app avec le serveur Braze.
braze.logInAppMessageButtonClick(button, message);
```


