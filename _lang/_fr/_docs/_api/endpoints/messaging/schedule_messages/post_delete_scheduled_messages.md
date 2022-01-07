---
nav_title: "POST: Supprimer les messages programmés"
article_title: "POST: Supprimer les messages programmés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Supprimer les messages planifiés Braze."
---

{% api %}
# Supprimer les messages programmés
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/messages/schedule/delete
{% endapimethod %}

Le point de terminaison des messages planifiés de suppression vous permet d'annuler un message que vous avez précédemment planifié _avant_ qu'il ait été envoyé.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' category='message endpoints' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (requis, chaîne) le `schedule_id` à supprimer (obtenu de la réponse pour créer un planning)
}
```

## Paramètres de la requête

| Paramètre        | Requis | Type de données      | Libellé                                                                  |
| ---------------- | ------ | -------------------- | ------------------------------------------------------------------------ |
| `Id du planning` | Requis | Chaîne de caractères | Le `schedule_id` à supprimer (obtenu de la réponse à créer un planning). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}
'
```

{% endapi %}
