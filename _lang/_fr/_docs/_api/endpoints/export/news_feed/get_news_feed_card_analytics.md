---
nav_title: "GET: Analyses de la carte des actualités"
article_title: "GET: Analyses de la carte des actualités"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article présente des détails sur et l'utilisation du point de terminaison de la liste des segments pour exporter une liste des segments disponibles."
---

{% api %}
# Point de terminaison de l'analyse des fiches d'actualités
{% apimethod get %}
/fr/feed/data_series
{% endapimethod %}

Ce point de terminaison vous permet de récupérer une série quotidienne de statistiques d'engagement pour une carte au fil du temps.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04e9d4d4d8 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre        | Requis    | Type de données                                                                | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------- | --------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id de la carte` | Requis    | Chaîne de caractères                                                           | Voir [Identifiant API de la carte]({{site.baseurl}}/api/identifier_types/). <br><br> La `card_id` pour une carte donnée peut être trouvée dans la page **Console développeur** et sur la page de détails de la carte dans votre tableau de bord, ou vous pouvez utiliser le [Point de terminaison de la liste des fils d'actualités]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/). |
| `Longueur`       | Requis    | Nombre entier                                                                  | Nombre maximal d'unités (jours ou heures) avant `ending_at` pour inclure dans la série retournée. Doit être compris entre 1 et 100 (inclus).                                                                                                                                                                                                                                                                            |
| `unité`          | Optionnel | Chaîne de caractères                                                           | Unité de temps entre les points de données. Peut être `jour` ou `heure`, par défaut à `jour`.                                                                                                                                                                                                                                                                                                                           |
| `finalisation_à` | Optionnel | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle la série de données doit se terminer. Par défaut, l'heure de la requête.                                                                                                                                                                                                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/data_series?card_id={{card_identifier}}&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00' \
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
            "clics" : (int) ,
            "impressions" : (int),
            "unique_clicks" : (int),
            "unique_impressions" : (int)
        },
...
    ]
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
