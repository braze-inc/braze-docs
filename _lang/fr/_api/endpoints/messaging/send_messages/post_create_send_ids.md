---
nav_title: "POST : créer des ID d’envoi"
article_title: "POST : créer des ID d’envoi"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer des ID d’envoi."

---
{% api %}
# Créer des ID d’envoi pour le suivi d’envoi de message
{% apimethod post %}
/sends/id/create
{% endapimethod %}

Utilisez cet endpoint pour créer des ID d’envoi pouvant être utilisés pour envoyer des messages et suivre leur performance de manière programmatique sans créer de campagne pour chaque envoi. L’utilisation de l’identifiant d’envoi pour suivre et envoyer des messages est utile si vous prévoyez de générer et d’envoyer du contenu via un programme.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Requis | String | Voir [Identifiant de campagne]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Facultatif | String | Voir [Identifiant d’envoi]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## Réponse

### Exemple de réponse réussie

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}
