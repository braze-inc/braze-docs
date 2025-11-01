---
nav_title: "POST : Mise à jour des Canvases déclenchées par l'API planifiée"
article_title: "POST : Mise à jour des canevas déclenchés par l'API planifiée"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour des Canvas planifiés déclenchés par API."

---
{% api %}
# Mise à jour des Canvases déclenchées par l'API planifiée
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour des Canvas déclenchés par API planifiés qui ont été créés dans le tableau de bord.

Ceci vous permet de décider quelle action doit déclencher l’envoi du message. Vous pouvez indiquer les `trigger_properties` qui seront modélisées dans le message lui-même.

Notez que pour envoyer des messages avec ce point de terminaison, vous devez avoir un ID Canvas, créé lorsque vous construisez un [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

Toute planification écrasera complètement celle que vous avez établie dans la demande de création de planification ou dans les demandes de mise à jour de planification précédentes.
  - Par exemple, si vous indiquez initialement `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` et, que dans votre mise à jour, vous renseignez `"schedule" : {"time" : "2015-02-20T14:14:47"}`, votre message sera envoyé à l’heure indiquée (UTC), et non à l’heure locale de l’utilisateur.
  - Les déclencheurs planifiés qui sont mis à jour peu de temps avant ou pendant la période où ils sont censés être envoyés seront mis à jour dans les meilleurs délais, de sorte que les changements de dernière minute pourraient être appliqués à tous, certains ou aucun de vos utilisateurs ciblés.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.trigger.schedule.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Requis|Chaîne de caractères| Voir [Identifiant Canvas]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Facultatif | Chaîne de caractères | Le `schedule_id` à mettre à jour (obtenu à partir de la réponse pour créer une planification). |
|`schedule` | Requis | Objet | Voir [objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
