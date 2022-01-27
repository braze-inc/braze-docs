---
nav_title: "POST: Mettre à jour les messages de campagne programmés par l'API"
article_title: "POST: Mettre à jour les messages de campagne programmés par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "Cet article décrit les détails de la mise à jour programmée des Campagnes déclenchées par l'API Braze."
---

{% api %}
# Mettre à jour les campagnes programmées déclenchées par l'API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/campaigns/trigger/schedule/update
{% endapimethod %}

Utilisez ce point de terminaison pour mettre à jour les campagnes programmées déclenchées par l'API qui sont créées sur le tableau de bord et initiées via l'API. Vous pouvez passer `trigger_properties` qui seront tempérés dans le message lui-même.

Ce point de terminaison vous permet d'envoyer des messages de campagne via une livraison déclenchée par API, vous permettant de décider quelle action doit déclencher le message à envoyer. Veuillez noter que pour envoyer des messages avec ce terminal, vous devez avoir un ID de campagne, créé lorsque vous construisez une [Campagne déclenchée par l'API]({{site.baseurl}}/api/api_campaigns/).

Toute planification écrasera complètement celle que vous avez fournie dans la demande de création de calendrier ou dans les demandes précédentes de mise à jour. Par exemple, si vous fournissez à l'origine `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` puis dans votre mise à jour vous fournissez `"schedule" : {"time" : "2015-02-20T14:14:47"}`, votre message sera maintenant envoyé à l'heure prévue en UTC, pas à l'heure locale de l'utilisateur. Les déclencheurs programmés qui sont mis à jour très près ou pendant le temps où ils étaient censés être envoyés seront mis à jour avec le maximum d'efforts, afin que les modifications de dernière minute puissent être appliquées à tous, à certains ou à aucun de vos utilisateurs ciblés.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (requis, chaîne) voir l'identifiant de la campagne,
  "schedule_id": (requis, string) le `schedule_id` à mettre à jour (obtenu à partir de la réponse pour créer le programme),
  "schedule": {
    // requis, voir Créer la documentation du planning
  }
}
```

## Paramètres de la requête

| Paramètre        | Requis    | Type de données      | Libellé                                                                                 |
| ---------------- | --------- | -------------------- | --------------------------------------------------------------------------------------- |
| `campaign_id`    | Requis    | Chaîne de caractères | Voir l'identifiant de la campagne []({{site.baseurl}}/api/identifier_types/)            |
| `Id du planning` | Optionnel | Chaîne de caractères | Le `schedule_id` à mettre à jour (obtenu de la réponse pour créer un planning).         |
| `Horaire`        | Requis    | Objet                | Voir [l'objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/campaigns/trigger/schedule/update' \
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
