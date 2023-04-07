---
nav_title: "POST : supprimer des campagnes planifiées déclenchées par API"
article_title: "POST : supprimer des campagnes planifiées déclenchées par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Planifier des campagnes déclenchées par API et planifiées."

---
{% api %}
# Supprimer des campagnes planifiées déclenchées par API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/campaigns/trigger/schedule/delete
{% endapimethod %}

Utilisez cet endpoint pour annuler un message Canvas que vous avez déjà planifié dans des campagnes déclenchées par API avant qu’il ne soit envoyé.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

Les messages ou déclencheurs planifiés qui sont supprimés peu de temps avant ou pendant l’heure où ils sont censés être envoyés seront mis à jour dans les meilleurs délais, de sorte que les suppressions de dernière minute pourraient être appliquées à tous, certains ou aucun de vos utilisateurs ciblés.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id`| Requis | String | Voir [Identifiant de campagne]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Requis | String | Le `schedule_id` à supprimer (obtenu à partir de la réponse pour créer une planification). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
