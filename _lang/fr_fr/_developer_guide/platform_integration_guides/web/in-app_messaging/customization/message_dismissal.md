---
nav_title: Rejet de message
article_title: Rejet de message in-app pour le Web
platform: Web
channel: in-app messages
page_order: 2
page_type: reference
description: "Cet article couvre le rejet de messages in-app pour votre application Web."

---

# Rejet de message

> Cet article explique comment traiter le rejet de messages in-app pour votre application Web.

Par défaut, lorsqu’un message in-app s’affiche, si vous appuyez sur la touche Échap ou si vous cliquez sur l’arrière-plan grisé de la page, le message est rejeté. Configurez l'[option d'initialisation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` sur `true` pour éviter ce comportement et exiger un clic de bouton explicite pour rejeter les messages. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

