---
nav_title: Rejet de message
article_title: Rejet de message in-app pour le Web
platform: Web
channel: messages In-App
page_order: 2
page_type: reference
description: "Cet article couvre le rejet de messages in-app pour votre application Web."

---

# Rejet de message

> Cet article explique comment traiter le rejet de messages in-app pour votre application Web.

Par défaut, lorsqu’un message in-app s’affiche, appuyer sur le bouton d’échappement ou cliquer sur l’arrière-plan grisé de la page va rejeter le message. Configurez l’`requireExplicitInAppMessageDismissal`[option d’initialisation][41] sur `true` pour empêcher ce comportement et exiger un clic de bouton explicite pour ignorer les messages. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions
