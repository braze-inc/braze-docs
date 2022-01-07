---
nav_title: "GET: Utilisateurs actifs mensuels pour les 30 derniers jours"
article_title: "GET: Utilisateurs actifs mensuels pour les 30 derniers jours"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Get Monthly Active Users ."
---

{% api %}
# Fin des utilisateurs actifs mensuels
{% apimethod get %}
/fr_FR/kpi/mau/data_series
{% endapimethod %}

Ce point de terminaison vous permet de récupérer une série quotidienne du nombre total d'utilisateurs actifs uniques sur une fenêtre roulante de 30 jours.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre        | Requis    | Type de données                                                                | Libellé                                                                                                                                                                   |
| ---------------- | --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Longueur`       | Requis    | Nombre entier                                                                  | Nombre maximum de jours avant `ending_at` pour inclure dans la série retournée. Doit être compris entre 1 et 100 (inclus).                                                |
| `finalisation_à` | Optionnel | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle la série de données doit se terminer. Par défaut, l'heure de la requête.                                                                                  |
| `app_id`         | Optionnel | Chaîne de caractères                                                           | Identifiant API de l'application récupéré de la **console développeur**. Si exclue, les résultats pour toutes les applications du groupe d'applications seront retournés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne 'success' lorsqu'il est terminé sans erreurs,
    "données" : [
        {
            "temps" : (chaîne) date comme date ISO 8601,
            "mau" : (int)
        },
...
    ]
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
