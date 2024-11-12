---
nav_title: "POST : Supprimer les messages planifiés"
article_title: "POST : Supprimer les messages planifiés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Supprimer les messages planifiés."

---
{% api %}
# Supprimer les messages planifiés
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/delete
{% endapimethod %}

> Utilisez cet endpoint pour annuler un message que vous avez déjà planifié avant qu’il ne soit envoyé.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `messages.schedule.delete`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Requis | Chaîne de caractères | Le `schedule_id` à supprimer (obtenu à partir de la réponse pour créer une planification). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
