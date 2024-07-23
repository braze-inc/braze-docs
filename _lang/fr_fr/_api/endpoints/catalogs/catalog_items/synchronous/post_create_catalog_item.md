---
nav_title: "POST : Créer un produit du catalogue"
article_title: "POST : Créer un produit du catalogue"
search_tag: Endpoint
page_order: 5

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer un produit du catalogue."

---
{% api %}
# Créer un produit du catalogue
{% apimethod post %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Utilisez cet endpoint pour créer un produit dans votre catalogue.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#820c305b-ea6a-4b71-811a-55003a212a40 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `catalogs.create_item`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Paramètres de chemin

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
|---|---|---|---|
| `catalog_name` | Obligatoire | Chaîne | Nom du catalogue. |
| `item_id` | Requis | Chaîne | L'identifiant de l'article du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
|---|---|---|---|
| `items` | Obligatoire | Tableau | Un tableau qui contient des objets Produit. Les objets de produits devraient contenir tous les champs qui existent dans le catalogue à l’exception du champ `id`. Un seul objet de produit est autorisé par requête.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    }
  ]
}'
```

## Réponse

Trois réponses de code de statut existent pour cet endpoint : `201`, `400` et `404`.

### Exemple de réponse réussie

Le code de statut `201` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la `400`résolution des problèmes[](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

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
Une erreur arbitraire est survenue. Veuillez réessayer ou contacter l’Assistance[]({{site.baseurl}}/support_contact/).
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `filtered-set-field-too-long` | La valeur du champ est utilisée dans un ensemble filtré qui dépasse la limite de caractères pour un élément. |
| `id-in-body` | Supprimez tous les ID de produit dans le corps de la requête. |
| `ids-too-large` | La limite de caractères pour chaque ID de produit est de 250 caractères. |
| `invalid-ids` | Les caractères pris en charge pour les noms d'identifiants d'articles sont les lettres, les chiffres, les traits d'union et les traits de soulignement. |
| `invalid-fields` | Vérifiez que tous les champs que vous envoyez dans la requête d’API existent déjà dans le catalogue. Cela n'a rien à voir avec le champ d'identification mentionné dans l'erreur. |
Les clés d’objet de produit ne peuvent pas inclure  ou .
| `item-already-exists` | L'article existe déjà dans le catalogue. |
| `item-array-invalid` | `items` doit être un tableau d'objets. |
| `items-too-large` | La limite de caractères pour chaque élément est de 5 000 caractères. |
| `request-includes-too-many-items` | Vous ne pouvez créer qu'un seul produit de catalogue par requête. |
| `too-deep-nesting-in-value-object` | Les objets de type article ne peuvent pas avoir plus de 50 niveaux d'imbrication. |
| `unable-to-coerce-value` | Les types d'articles ne peuvent pas être convertis. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}