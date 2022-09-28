---
nav_title: "GET : Répertorier les campagnes et Canvas planifiés à venir"
article_title: "GET : Répertorier les campagnes et Canvas planifiés à venir"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Obtenir les messages planifiés."

---
{% api %}
# Obtenir les campagnes et les Canvas planifiés à venir
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

Vous pouvez afficher une liste JSON des campagnes et Canvas planifiés à venir à l’aide des informations et paramètres suivants. L’endpoint renverra des informations sur les campagnes planifiées et les Canvas saisis entre maintenant et l’`end_time` spécifié dans la demande. Les messages quotidiens et récurrents n’apparaîtront qu’une seule fois lors de leur occurrence suivante. Les résultats renvoyés dans cet endpoint ne concernent que les campagnes et Canvas créés et planifiés dans Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Limite de débit

{% include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `end_time` | Requis | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Date de fin de la plage pour récupérer les campagnes et Canvas planifiés. Ce traitement est effectué à minuit (UTC) par l’API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "scheduled_broadcasts": [
    # Example Canvas
    {
      "name" => String,
      "id" => String,
      "type" => "Canvas",
      "tags" => [String tag names],
      "next_send_time" => "YYYY-MM-DD HH:mm:ss" (may also include time zone if not local/intelligent delivery)
      "schedule_type" => one of "local_time_zones", "intelligent_delivery", or the name of your company's time zone
    },
    # Example Campaign
    {
      "name" => String,
      "id" => String,
      "type" => "Campaign",
      "tags" => [String tag names],
      "next_send_time" => "YYYY-MM-DD HH:mm:ss" (may also include time zone if not local/intelligent delivery)
      "schedule_type" => one of "local_time_zones", "intelligent_delivery", or the name of your company's time zone
    },
  ]
}
```

{% endapi %}
