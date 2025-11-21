---
nav_title: "POST : Supprimer les toiles planifiées déclenchées par l'API"
article_title: "POST : Supprimer des Canvas planifiés déclenchés par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Supprimer des Canvas déclenchés par API et planifiés."

---
{% api %}
# Supprimer les toiles planifiées déclenchées par l'API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> L’endpoint de suppression de la planification vous permet d’annuler un message que vous avez déjà planifié dans des Canvas déclenchés par API avant qu’il ne soit envoyé.

Les messages ou déclencheurs planifiés qui sont supprimés peu de temps avant ou pendant l’heure où ils sont censés être envoyés seront mis à jour dans les meilleurs délais, de sorte que les suppressions de dernière minute pourraient être appliquées à tous, certains ou aucun de vos utilisateurs ciblés.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.trigger.schedule.delete`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `canvas_id`| Requis | Chaîne de caractères | Voir [Identifiant Canvas]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Requis | Chaîne de caractères | Le `schedule_id` à supprimer (obtenu à partir de la réponse pour créer une planification). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
