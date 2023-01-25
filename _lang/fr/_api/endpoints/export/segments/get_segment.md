---
nav_title: "GET : Liste des segments"
article_title: "GET : Liste des segments"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Liste de segments pour exporter une liste de segments disponibles et son utilisation."

---
{% api %}
# Endpoint Liste des segments
{% apimethod get %}
/segments/list
{% endapimethod %}

Utilisez cet endpoint pour exporter une liste de segments, chacun incluant son nom, l’identifiant API du segment et s’il a un suivi analytique activé. Les segments sont renvoyés par groupes de 100 triés par date de création (des plus anciens aux plus récents par défaut). Les segments archivés ne sont pas inclus.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre| Requis | Type de données | Description |
| -------- | -------- | --------- | ----------- |
| `page` | Facultatif | Integer | La page des segments à renvoyer, par défaut sur 0 (renvoie le premier ensemble jusqu’à 100 éléments). |
| `sort_direction` | Facultatif | String | - Trier l'heure de création de la plus récente à la plus ancienne : indiquer la valeur `desc`.<br> - Trier l'heure de création de la plus ancienne à la plus récente : indiquer la valeur `asc`. <br><br>Si `sort_direction` n’est pas inclus, l’ordre par défaut est du plus ancien au plus récent. |
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
    "message": (required, string) le statut de l’exportation, renvoie « réussite » lorsqu’elle s’achève sans erreur,
    "segments" : [
        {
            "id" : (string) l’identifiant API de segment,
            "name" : (string) nom du segment,
            "analytics_tracking_enabled" : (boolean) si le suivi d’analytique est activé ou non pour ce segment,
            "tags" : (array) les noms de balise associés au segment formatés en tant que chaînes de caractères
        },
        ...
    ]
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et de l'API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
