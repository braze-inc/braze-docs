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

Vous pouvez ainsi décider de l'action qui déclenche l'envoi du message. Vous pouvez intégrer `trigger_properties` que Braze modélise dans le message lui-même.

Notez que pour envoyer des messages avec ce point de terminaison, vous devez avoir un ID Canvas, créé lorsque vous construisez un [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

Toute planification écrasera complètement celle que vous avez établie dans la demande de création de planification ou dans les demandes de mise à jour de planification précédentes.
  - Par exemple, si vous indiquez initialement `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` puis `"schedule" : {"time" : "2015-02-20T14:14:47"}` dans votre mise à jour, Braze envoie votre message à l'heure indiquée en UTC, et non à l'heure locale de l'utilisateur.
  - Les déclencheurs planifiés que vous mettez à jour à proximité ou pendant l'heure à laquelle ils étaient censés être envoyés sont mis à jour dans la mesure du possible, de sorte que Braze peut appliquer des modifications de dernière seconde à tous les utilisateurs ciblés, à certains d'entre eux ou à aucun d'entre eux.

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
