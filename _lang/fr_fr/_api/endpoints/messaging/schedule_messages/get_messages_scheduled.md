---
nav_title: "GET : Répertorier les campagnes et Canvas planifiés à venir"
article_title: "GET : Répertorier les campagnes et Canvas planifiés à venir"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Répertorier les campagnes et Canvas planifiés à venir."

---
{% api %}
# Répertorier les campagnes et Canvas planifiés à venir
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer une liste JSON des informations sur les campagnes planifiées et les Canvas saisis entre maintenant et un `end_time` spécifié dans la demande.

Les messages quotidiens et récurrents n’apparaîtront qu’une seule fois lors de leur occurrence suivante. Les résultats renvoyés dans cet endpoint comprennent les campagnes et les toiles créées et planifiées dans le tableau de bord Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `messages.schedule_broadcasts`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `end_time` | Requis | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Date de fin de la plage pour récupérer les campagnes et Canvas planifiés. Ce traitement est effectué à minuit (UTC) par l’API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

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
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone,
    },
  ]
}
```

{% endapi %}
