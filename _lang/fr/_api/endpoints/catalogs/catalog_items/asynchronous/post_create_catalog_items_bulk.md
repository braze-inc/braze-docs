---
nav_title: "POST : Créer plusieurs produits du catalogue"
article_title: "POST : Créer plusieurs produits du catalogue"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: référence
description: "Cet article présente en détail l’endpoint de Braze Créer plusieurs produits du catalogue."

---
{% api %}
# Créer plusieurs produits du catalogue
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

Utilisez cet endpoint pour créer plusieurs produits dans votre catalogue. Chaque requête peut prendre en charge jusqu’à 50 objets. Cet endpoint est asynchrone.

## Limites de débit

Cet endpoint a une limitation du débit partagée de 100 requêtes par minute entre tous les endpoints asynchrones de produits du catalogue.

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | String | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `items` | Requis | Array | Un tableau qui contient certains objets de produit. Les objets de produits devraient contenir tous les champs qui existent dans le catalogue. Jusqu’à 50 objets sont autorisés par requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

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
      "Cuisine": "Américain",
      "Rating": 5,
      "Loyalty_Program": true,
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "Américain",
      "Rating": 10,
      "Loyalty_Program": true,
      "Created_At": "2022-11-02T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "Américain",
      "Rating": 3,
      "Loyalty_Program": false,
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Réponse

Trois réponses de code d’état existent pour cet endpoint : `202`, `400` et `404`..

### Exemple de réponse réussie

Le code de statut `202` pourrait retourner le corps de réponse suivant.

```json
{
  "message": "réussite"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait retourner le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "fields-do-not-match",
      "message": "Les champs ne correspondent pas aux champs du catalogue.",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant2"
      ]
    }
  ],
  "message": "Requête invalide"
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `item-array-invalid` | `items` doit être un tableau d’objets. |
| `request-includes-too-many-items` | Votre requête contient trop de produits. La limite de produit par requête est de 50. |
| `invalid-ids` | Ces ID de produit peuvent uniquement inclure des lettres, des chiffres, des traits d’union et des traits de soulignement. |
| `ids-too-large` | Les ID de produit ne peuvent pas contenir plus de 250 caractères. |
| `ids-not-unique` | Les ID de produits doivent être uniques au sein de la requête. |
| `ids-not-strings` | Les ID de produits doivent être de type chaîne de caractères. |
| `items-missing-ids` | Il y a des produits qui n’ont pas d’ID de produit. Vérifiez que chaque produit possède un ID de produit. |
| `items-too-large` | Les valeurs de produits ne peuvent pas dépasser 5 000 caractères. |
| `invalid-fields` | Confirmez que les champs de la requête existent dans le catalogue. |
| `fields-do-not-match` | Les champs mis à jour doivent correspondre aux champs du catalogue. |
| `unable-to-coerce-value` | Les types de produits ne peuvent pas être convertis. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}