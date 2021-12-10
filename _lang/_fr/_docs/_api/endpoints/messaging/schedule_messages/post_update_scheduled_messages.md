---
nav_title: "POST: Mettre à jour les messages programmés"
article_title: "POST: Mettre à jour les messages programmés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails du point de terminaison de mise à jour des messages planifiés Braze."
---

{% api %}
# Mettre à jour les messages programmés
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/messages/schedule/update
{% endapimethod %}

Le calendrier de mise à jour des messages accepte les mises à jour du paramètre de terminaison `Schedule` ou `messages` ou les deux. Votre requête doit contenir au moins une de ces deux clés.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (requis, chaîne) le `schedule_id` à mettre à jour (obtenu à partir de la réponse pour créer le planning),
  "schedule": {
    // optionnel, voir la documentation de création d'horaire
  },
  "messages": {
    // optionnelle, voir la documentation des objets de messagerie disponibles
  }
}
```
## Paramètres de la requête

| Paramètre        | Requis    | Type de données      | Libellé                                                                                 |
| ---------------- | --------- | -------------------- | --------------------------------------------------------------------------------------- |
| `Id du planning` | Requis    | Chaîne de caractères | Le `schedule_id` à mettre à jour (obtenu de la réponse pour créer un planning).         |
| `Horaire`        | Optionnel | Objet                | Voir [l'objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/). |
| `Messages`       | Optionnel | Objet                | Voir les [objets de message disponibles](#available-message-objects), ci-dessous.       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


### Objets de messagerie disponibles {#available-message-objects}
Vous pouvez utiliser ces objets dans le corps de la [requête](#request-body) ci-dessus.

- [Objets Android]({{site.baseurl}}/api/objects_filters/android_objects/)
- [Objets Apple]({{site.baseurl}}/api/objects_filters/apple_objects/)
- [Objet Cartes de Contenu]({{site.baseurl}}/api/objects_filters/content_cards_object/)
- [Objet Email]({{site.baseurl}}/api/objects_filters/email_object/)
- [Objet Kindle ou FireOS]({{site.baseurl}}/api/objects_filters/kindle_and_fireos_object/)
- [Objet SMS]({{site.baseurl}}/api/objects_filters/sms_object/)
- [Objets Web]({{site.baseurl}}/api/objects_filters/web_objects/)
- [Objet Webhook]({{site.baseurl}}/api/objects_filters/webhook_object/)
- [Objets Windows]({{site.baseurl}}/api/objects_filters/windows_object/)

## Exemple de requête
```
curl --location --request POST 'https://rest.iad-01.braze. om/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
     "apple_push": {
       "alert": "Message mis à jour! ,
       "badge": 1
     },
     "android_push": {
       "title": "Titre mis à jour ! ,
       "alerte": "Message mis à jour!"
     },
     "sms": {  
        "subscription_group_id": "subscription_group_identifier",
        "message_variation_id": "message_variation_identifier",
        "corps": "C'est mon corps SMS. ,
        "app_id": "app_identifier"
      }
  }
}'
```

{% endapi %}
