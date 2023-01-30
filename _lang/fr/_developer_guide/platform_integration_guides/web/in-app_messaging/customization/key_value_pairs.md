---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur de message in-app pour le Web
platform: Web
channel: messages in-app
page_order: 9
page_type: reference
description: "Cet article couvre les paires clé-valeur de messagerie in-app pour votre application Web."

---

# Paires clé-valeur

Les objets de message in-app peuvent porter des paires clé-valeur en tant que leur propriété `extras`. Elles sont spécifiés sur le tableau de bord sous **Paramètres** lors de la création d’une campagne de messages in-app. Elles peuvent être utilisées pour envoyer des données avec un message in-app pour un traitement ultérieur par votre site. Par exemple :

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // les messages du groupe de contrôle doivent toujours être « affichés"
  // ceci journalise une impression et n’affiche pas un message visible
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
