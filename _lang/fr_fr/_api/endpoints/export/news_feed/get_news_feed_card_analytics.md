---
nav_title: "GET :  : Exporter l’analyse des cartes de fil d’actualité"
article_title: "GET :  : Exporter l’analyse des cartes de fil d’actualité"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter l’analyse des cartes de fil d’actualité."

---
{% api %}
# Exporter l’analyse des cartes de fil d’actualité
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> Utilisez cet endpoint pour récupérer quotidiennement une série de statistiques d’engagement pour une carte au fil du temps.

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `feed.data_series`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| ----------- | -------- | --------- | ----------- |
| `card_id` | Requis | Chaîne | Voir l'[identifiant de l'API de la carte]({{site.baseurl}}/api/identifier_types/). <br><br> Le site `card_id` pour une carte donnée se trouve sur la page des [clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) et sur la page des détails de la carte dans ton tableau de bord, ou tu peux utiliser le [point de terminaison Exporter la liste des cartes du fil d'actualité]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).|
| `length` | Requis | Integer | Nombre maximum d'unités (jours ou heures) avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus).
| `unit` | Facultatif | Chaîne de caractères | Unité de temps entre les points de données. Peut être  ou , valeur par défaut .
| `ending_at` | Facultatif | Datetime <br>(Chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, l’heure de la demande.
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
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "clicks" : (int) the number of clicks,
            "impressions" : (int) the number of impressions,
            "unique_clicks" : (int) the number of unique clicks,
            "unique_impressions" : (int) the number of unique impressions
        },
        ...
    ]
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section Résolution des problèmes d’exportation[]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
