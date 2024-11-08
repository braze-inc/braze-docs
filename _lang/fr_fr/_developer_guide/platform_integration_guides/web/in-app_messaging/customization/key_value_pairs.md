---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur de message in-app pour le Web
platform: Web
channel: in-app messages
page_order: 9
page_type: reference
description: "Cet article indique comment tirer parti des paires clé-valeur de l’envoi de messages in-app pour afficher les informations dans votre application Web."

---

# Paires clé-valeur

> Cet article indique comment tirer parti des paires clé-valeur de l’envoi de messages in-app pour afficher les informations dans votre application Web.

Les objets de message in-app peuvent porter des paires clé-valeur en tant que leur propriété `extras`. Ces éléments sont spécifiés sur le tableau de bord sous **Paramètres** lors de la création d'une campagne de messages intégrés à l'application. Elles peuvent être utilisées pour envoyer des données avec un message in-app pour un traitement ultérieur par votre site. Par exemple :

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
