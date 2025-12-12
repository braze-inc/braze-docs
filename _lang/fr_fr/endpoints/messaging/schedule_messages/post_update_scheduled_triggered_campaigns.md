---
nav_title: "POST : Mettre à jour les campagnes planifiées déclenchées par API"
article_title: "POST : Mettre à jour les campagnes déclenchées par l'API planifiées"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "Cet article présente en détail l’endpoint Braze Mettre à jour des campagnes planifiées déclenchées par API."

---
{% api %}
# Mettre à jour les campagnes planifiées déclenchées par API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour des campagnes planifiées déclenchées par API et créées dans le tableau de bord, ce qui vous permet de décider quelle action doit déclencher le message à envoyer.

Vous pouvez indiquer les `trigger_properties` qui seront modélisées dans le message lui-même.

Notez que pour envoyer des messages avec ce point de terminaison, vous devez avoir un ID de campagne, créé lorsque vous construisez une [campagne déclenchée par API]({{site.baseurl}}/api/api_campaigns/).

Toute planification remplacera complètement celle que vous avez fournie dans la demande de création de planification ou dans les demandes de mise à jour de planification précédentes. Par exemple, si vous avez initialement fixé la planification à `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` et que vous l'avez ensuite mise à jour à `"schedule" : {"time" : "2015-02-20T14:14:47"}`, le message sera désormais envoyé à l'heure spécifiée en UTC, et non à l'heure locale de l'utilisateur.

Les déclencheurs planifiés qui sont mis à jour très près de l'heure à laquelle ils étaient censés être envoyés, ou pendant cette heure, seront mis à jour au mieux afin que les changements de dernière seconde puissent être appliqués à tous, à certains ou à aucun de vos utilisateurs ciblés. Les mises à jour ne sont pas appliquées si la planification d'origine utilisait l'heure locale et que l'heure d'origine est déjà passée dans n'importe quel fuseau horaire.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `campaigns.trigger.schedule.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Requis|Chaîne de caractères| Voir [identifiant de la campagne]({{site.baseurl}}/api/identifier_types/)|
| `schedule_id` | Requis | Chaîne de caractères | Le `schedule_id` à mettre à jour (obtenu à partir de la réponse pour créer un calendrier). |
|`schedule` | Requis | Objet | Voir [objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
