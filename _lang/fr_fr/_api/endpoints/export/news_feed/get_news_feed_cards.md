---
nav_title: "GET : Exporter la liste des cartes du fil d'actualité"
article_title: "GET : Exporter la liste des cartes du fil d'actualité"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter la liste des cartes de fil d’actualités."

---
{% api %}
# Exporter la liste des cartes de fil d’actualités
{% apimethod get %}
/feed/list
{% endapimethod %}

> Utilisez cet endpoint pour exporter une liste de cartes de fil d’actualité, chacune incluant son nom et son identifiant API de carte.

Les cartes sont renvoyées par groupes de 100 triées par date de création (des plus anciennes aux plus récentes par défaut).

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `feed.list`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `page` | Facultatif | Entier   | La page des cartes à renvoyer, par défaut sur 0 (renvoie le premier ensemble jusqu’à 100 éléments). |
| `include_archived` | Facultatif | Valeur booléenne   | S’il faut inclure ou non des cartes archivées, par défaut sur Faux. |
| `sort_direction` | Facultatif | Chaîne de caractères | \- Trier l’heure de création de la plus récente à la plus ancienne : indiquer la valeur `desc`.<br> \- Trier l’heure de création de la plus ancienne à la plus récente : indiquer la valeur `asc`. <br><br>Si `sort_direction` n’est pas inclus, l’ordre par défaut est de la plus ancienne à la plus récente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) the card API identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner
            "title" : (string) the title of the card,
            "tags" : (array) the tag names associated with the card
        },
        ...
    ]
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
