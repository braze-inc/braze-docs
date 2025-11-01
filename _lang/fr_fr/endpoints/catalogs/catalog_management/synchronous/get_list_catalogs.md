---
nav_title: "GET : Lister des catalogues"
article_title: "GET : Lister des catalogues"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Lister des catalogues."

---
{% api %}
# Lister des catalogues
{% apimethod get %}
/catalogs
{% endapimethod %}

> Utilisez cet endpoint pour obtenir la liste des catalogues d'un espace de travail.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d65fb86-ccf7-423f-9eb2-f68ab36df824 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `catalogs.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Paramètres de chemin et de requête

Cet endpoint n’a pas de paramètres de chemin ni de requête.

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

### Exemple de réponse réussie

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 10,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    },
    {
      "description": "My Catalog",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "string_field",
          "type": "string"
        },
        {
          "name": "number_field",
          "type": "number"
        },
        {
          "name": "boolean_field",
          "type": "boolean"
        },
        {
          "name": "time_field",
          "type": "time"
        },
      ],
      "name": "my_catalog",
      "num_items": 3,
      "updated_at": "2022-11-02T09:03:19.967+00:00"
    },
  ],
  "message": "success"
}
```

{% endapi %}
