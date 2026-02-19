---
nav_title: "POST : Créer plusieurs produits du catalogue"
article_title: "POST : Créer plusieurs produits du catalogue"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer plusieurs produits du catalogue."

---
{% api %}
# Créer plusieurs produits du catalogue
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utilisez cet endpoint pour créer plusieurs produits dans votre catalogue.

Chaque requête peut prendre en charge jusqu’à 50 objets. Cet endpoint est asynchrone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cea18bb3-b83a-4160-81fe-8cd42aa6e7cc {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `catalogs.add_items`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | Chaîne de caractères | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `items` | Requis | Tableau | Un tableau qui contient certains objets Produit. Les objets Produits devraient contenir tous les champs qui existent dans le catalogue. Jusqu’à 50 objets sont autorisés par requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 40.7413,
        "Longitude": -73.9764
      },
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ],
      "Created_At": "2022-11-02T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 3,
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 40.7489,
        "Longitude": -73.9972
      },
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ],
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Réponse

Trois réponses de code de statut existent pour cet endpoint : `202`, `400` et `404`.

### Exemple de réponse réussie

Le code de statut `202` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `ids-not-strings` | Les ID de produit doivent être de type chaîne de caractères. |
| `ids-not-unique` | Les ID de produit doivent être uniques au sein de la requête. |
| `ids-too-large` | Les ID de produit ne peuvent pas contenir plus de 250 caractères. |
| `invalid-ids` | Ces ID de produit peuvent uniquement inclure des lettres, des chiffres, des traits d’union et des traits de soulignement. |
| `invalid-fields` | Confirmez que tous les champs que vous envoyez dans la requête API existent déjà dans le catalogue. Cela n'a rien à voir avec le champ ID mentionné dans l'erreur. |
| `invalid-keys-in-value-object` | Les clés d’objet de produit ne peuvent pas inclure `.` ou `$`. |
| `item-array-invalid` | `items` doit être un tableau d’objets. |
| `items-missing-ids` | Certains articles n'ont pas d'ID. Vérifiez que chaque produit possède un ID de produit. |
| `items-too-large` | Les valeurs de produits ne peuvent pas dépasser 5 000 caractères. |
| `request-includes-too-many-items` | Votre requête contient trop de produits. La limite de produit par requête est de 50. |
| `too-deep-nesting-in-value-object` | Les objets de produit ne peuvent pas avoir plus de 50 niveaux d’imbrication. |
| `unable-to-coerce-value` | Les types de produits ne peuvent pas être convertis. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
