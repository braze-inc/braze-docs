---
nav_title: "CORRECTIF : Éditer un produit du catalogue"
article_title: "CORRECTIF : Éditer un produit du catalogue"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint de Braze Éditer un produit du catalogue."

---
{% api %}
# Éditer un produit du catalogue
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

Utilisez cet endpoint pour éditer un produit de votre catalogue. 

## Limites de débit

Cet endpoint a une limitation du débit partagée de 50 requêtes par minute entre tous les endpoints synchronisés de produits du catalogue.

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | Chaîne de caractères | Nom du catalogue. |
| `item_id` | Requis | Chaîne de caractères | L’ID du produit du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `items` | Requis | Tableau | Un tableau qui contient certains objets Produit. Les objets Produits devraient contenir les champs qui existent dans le catalogue à l’exception du champ `id`. Un seul objet Produit est autorisé par requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Réponse

Trois réponses de code de statut existent pour cet endpoint : `200`, `400` et `404`.

### Exemple de réponse réussie

Le code de statut `200` pourrait retourner le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait retourner le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

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
| `item-not-found` | Vérifiez que ce produit est dans le catalogue. |
| `item-array-invalid` | `items` doit être un tableau d’objets. |
| `request-includes-too-many-items` | Vous ne pouvez éditer qu’un produit de catalogue par requête. |
| `id-in-body` | Un ID de produit existe déjà dans le catalogue. |
| `invalid-ids` | Les caractères pris en charge pour les ID de produit sont les lettres, les nombres, les tirets et les traits de soulignement. |
| `ids-too-large` | La limite de caractères pour chaque ID de produit est de 250 caractères. |
| `items-too-large` | La limite de caractères pour chaque produit est de 5 000 caractères. |
| `invalid-fields` | Confirmez que les champs de la requête existent dans le catalogue. |
| `unable-to-coerce-value` | Les types de produits ne peuvent pas être convertis. |
| `filtered-set-field-too-long` | La valeur du champ est utilisée dans un ensemble filtré qui dépasse la limite de caractères pour un produit. |
| `arbitrary-error` | Une erreur arbitraire est survenue. Veuillez réessayer ou contacter l’[Assistance]({{site.baseurl}}/support_contact/). |
| `invalid-keys-in-value-object` | Les clés d’objet de produit ne peuvent pas inclure `.` ou `$`. |
| `too-deep-nesting-in-value-object` | Les objets de produit ne peuvent pas avoir plus de 50 niveaux d’imbrication. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}