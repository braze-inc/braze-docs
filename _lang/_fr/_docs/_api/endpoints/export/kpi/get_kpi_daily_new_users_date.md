---
nav_title: "GET: Nouveaux utilisateurs quotidiens par date"
article_title: "GET: Nouvelles quotidiennes des utilisateurs par date"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Get Daily New Users."
---

{% api %}
# Point de terminaison quotidien des nouveaux utilisateurs
{% apimethod get %}
/fr/kpi/new_users/data_series
{% endapimethod %}

Ce point de terminaison vous permet de récupérer une série quotidienne du nombre total de nouveaux utilisateurs à chaque date.

{% apiref postman %}https://documentmenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01 {% endapiref %}

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
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/new_users/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
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
            "new_users" : (int)
        },
...
    ]
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
