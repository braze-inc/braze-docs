---
nav_title: "Objet SMS"
article_title: Objet Messagerie SMS
page_order: 10
page_type: reference
channel: SMS
description: "Cet article de référence explique les différents composants de l'objet SMS de Braze."

---
# Objet SMS

> L'objet `sms` vous permet de modifier ou de créer des messages SMS via nos [points d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging)

```json
{
    "subscription_group_id": (required, string) the ID of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message,
    "link_shortening_enabled": (optional, boolean) use this field to turn on link shortening and campaign-level click tracking,
    "user_click_tracking_enabled": (optional, boolean) if link_shortening_enabled is true, use this field to turn on link shortening, and campaign-level and user-level click tracking.     
}
```

- [Identifiant de l'application]({{site.baseurl}}/api/identifier_types/)
  - Toute adresse `app_id` valide provenant d'une application configurée dans votre espace de travail fonctionnera pour tous les utilisateurs de votre espace de travail, que l'utilisateur ait ou non l'application spécifique sur son profil.