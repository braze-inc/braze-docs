---
nav_title: "Objet SMS"
article_title: Objet de messagerie SMS
page_order: 10
page_type: reference
channel: SMS
description: "Cet article explique les différents composants de l’objet SMS de Braze."

---
# Spécification d’objet de SMS

L’objet `sms` vous permet de modifier ou de créer des SMS via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

```json
{
    "subscription_group_id": (required, string) L’ID de votre groupe d’abonnement,
    "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi,
    "body": (required, string),
    "app_id": (required, string) voir Identifiant de l’application,
    "media_items" :(optional, array) utilisez ce champ pour transmettre une URL d’image dans un MMS pour envoyer une image avec votre message.    
}
```

- [Identifiant d’application]({{site.baseurl}}/api/api_key#the-app-identifier-api-key)