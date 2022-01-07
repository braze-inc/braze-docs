---
nav_title: "GET: Liste des segments"
article_title: "GET: Segment List"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article présente des détails sur et l'utilisation du point de terminaison de la liste des segments pour exporter une liste des segments disponibles."
---

{% api %}
# Point de terminaison de la liste des segments
{% apimethod get %}
/fr/segments/list
{% endapimethod %}

Ce point de terminaison vous permet d'exporter une liste de segments, dont chacun inclura son nom, Identificateur d'API de segment, et si le suivi d'analyse est activé. Les segments sont retournés en groupes de 100 triés par date de création (du plus ancien au plus récent par défaut). Les segments archivés ne sont pas inclus.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre       | Requis    | Type de données      | Libellé                                                                                                                                                                                                                                                                                                                  |
| --------------- | --------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `page`          | Optionnel | Nombre entier        | La page des segments à retourner, par défaut à 0 (retourne le premier ensemble jusqu'à 100).                                                                                                                                                                                                                             |
| `direction_tri` | Optionnel | Chaîne de caractères | - Trier le temps de création du plus récent au plus ancien : passer dans la valeur `desc`.<br> - Trier le temps de création de la plus ancienne à la plus récente : passer dans la valeur `asc`. <br><br>Si `sort_direction` n'est pas incluse, l'ordre par défaut est plus ancien que le plus récent. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne « success» quand terminé sans erreurs,
    "segments" : [
        {
            "id" : (string) Segment API Identifier,
            "nome" : (chaîne) nom de segment,
            "analytics_tracking_enabled" : (boolean) si le segment a activé le suivi analytique,
            "tags" : (tableau) noms de balises associés au segment
        },
...
    ]
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
