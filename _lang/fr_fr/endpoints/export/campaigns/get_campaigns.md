---
nav_title: "GET : Exporter la liste des campagnes"
article_title: "GET : Exporter la liste des campagnes"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter la liste des campagnes."

---
{% api %}
# Exporter la liste des campagnes
{% apimethod get %}
/campaigns/list
{% endapimethod %}

> Utilisez cet endpoint pour exporter une liste de campagnes, chacune incluant son nom, l’identifiant API de la campagne, s’il s’agit d’une campagne par API, et les balises associées à la campagne.

Les campagnes sont renvoyées par groupes de 100 triés par date de création (des plus anciens aux plus récents par défaut).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `campaigns.list`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `page` | Facultatif | Entier | La page des campagnes à renvoyer, par défaut sur 0 (renvoie le premier ensemble jusqu’à 100 éléments). |
| `include_archived` | Facultatif | Valeur booléenne | S’il faut inclure ou non des campagnes archivées, par défaut sur Faux. |
| `sort_direction` | Facultatif | Chaîne de caractères | \- Trier l’heure de création de la plus récente à la plus ancienne : indiquer la valeur `desc`.<br> \- Trier l’heure de création de la plus ancienne à la plus récente : indiquer la valeur `asc`. <br><br>Si `sort_direction` n’est pas inclus, l’ordre par défaut est de la plus ancienne à la plus récente. |
| `last_edit.time[gt]` | Facultatif | Date | Filtre les résultats et renvoie uniquement les campagnes qui ont été modifiées au-delà de l’heure indiquée jusqu’à maintenant. Le format est `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "campaigns" : [
        {
            "id" : (string) the Campaign API identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message
            "name" : (string) the campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
            "tags" : (array) the tag names associated with the campaign formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
