---
nav_title: "Objet SMS"
article_title: Objet SMS Messaging
page_order: 10
page_type: Référence
channel: SMS
description: "Cet article explique les différents composants de l'objet SMS de Brase."
---

# Spécification de l'objet SMS

```json
{
  "sms": (optionnel, objet SMS),
  {  
    "subscription_group_id": (requis, chaîne) l'id de votre groupe d'abonnement,
    "message_variation_id": (optionnel, chaîne) utilisé lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi,
    "body": (requis, chaîne),
    "app_id": (requis, string) voir l'identifiant de l'application ci-dessus
    "media_items" :(optionnel, tableau) utilisez ce champ pour passer une URL d'image dans un MMS pour envoyer une image avec votre message.    
  }
}
```
