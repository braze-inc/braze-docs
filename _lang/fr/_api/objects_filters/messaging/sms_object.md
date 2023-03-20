---
nav_title: "Objet SMS"
article_title: Objet Messagerie SMS
page_order: 10
page_type: reference
channel: SMS
description: "Cet article de référence explique les différents composants de l’objet SMS de Braze."

---
# Spécification d’objet SMS

Le `sms` vous permet de modifier ou de créer des SMS via nos [endpoints de messagerie]({{site.baseurl}}/api/endpoints/messaging).

```json
{
    "subscription_group_id": (required, string) the id of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message.    
}
```

- [Identifiant d’application]({{site.baseurl}}/api/api_key#the-app-identifier-api-key)