---
nav_title: "GET: Sessions de l'application par heure"
article_title: "Obtenir : Sessions de l'application par Temps"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur les sessions d'application par point de terminaison temporelle."
---

{% api %}
# Point de terminaison d'analyse de session
{% apimethod get %}
/fr/sessions/data_series
{% endapimethod %}

Ce point de terminaison vous permet de récupérer une série de sessions pour votre application sur une période déterminée.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## Paramètres de la requête

| Paramètre             | Requis    | Type de données                                                                | Libellé                                                                                                                                                               |
| --------------------- | --------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Longueur`            | Requis    | Nombre entier                                                                  | Nombre maximal d'unités (jours ou heures) avant `ending_at` pour inclure dans la série retournée. Doit être compris entre 1 et 100 (inclus).                          |
| `unité`               | Optionnel | Chaîne de caractères                                                           | Unité de temps entre les points de données. Peut être `jour` ou `heure`, par défaut à `jour`.                                                                         |
| `finalisation_à`      | Optionnel | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle la série de données doit se terminer. Par défaut, l'heure de la requête.                                                                              |
| `app_id`              | Optionnel | Chaîne de caractères                                                           | Identifiant API de l'application récupéré de la **console développeur** pour limiter les analyses à une application spécifique.                                       |
| `identifiant_segment` | Optionnel | Chaîne de caractères                                                           | See [Segment API identifier]({{site.baseurl}}/api/identifier_types/). ID de segment indiquant le segment analytique pour lequel les sessions doivent être retournées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne 'success' lorsqu'il est terminé sans erreurs,
    "data" : [
        {
            "time" : (string) point dans le temps - comme ISO 8601 étendu lorsque l'unité est "hour" et comme la date ISO 8601 lorsque l'unité est "day",
            "sessions" : (int)
        },
...
    ]
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
