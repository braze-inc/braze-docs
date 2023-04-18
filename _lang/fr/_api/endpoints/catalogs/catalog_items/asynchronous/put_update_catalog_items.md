---
nav_title: "PUT : créer plusieurs produits du catalogue"
article_title: "PUT : créer plusieurs produits du catalogue"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour plusieurs produits du catalogue."

---
{% api %}
# Mettre à jour les produits du catalogue
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour plusieurs produits de votre catalogue. 

Chaque requête peut prendre en charge jusqu’à 50 produits du catalogue. Cet endpoint est asynchrone.

{% alert note %}
Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `catalogs.replace_items`.
{% endalert %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | String | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `items` | Requis | Tableau | Un tableau qui contient certains objets Produit. Chaque produit doit avoir un ID. Les objets Produits devraient contenir des champs qui existent dans le catalogue. Jusqu’à 50 objets sont autorisés par requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2
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
| `request_includes_too_many_items` | Votre requête contient trop de produits. La limite de produit par requête est de 50. |
| `ids_not_unique` | Vérifiez que chaque ID de produit est unique. |
| `ids_too_large` | La limite de caractères pour chaque ID de produit est de 250 caractères. |
| `ids_not_string` | Confirmez que chaque ID de produit est une chaîne de caractères. |
| `invalid_ids` | Les caractères pris en charge pour les ID de produits sont les lettres, les nombres, les tirets et les traits de soulignement. |
| `items_missing_ids` | Confirmez que chaque produit a un ID. |
| `items_too_large` | Les valeurs de produits ne peuvent pas dépasser 5 000 caractères. |
| `invalid_fields` | Confirmez que les champs de la requête existent dans le catalogue. |
| `unable_to_coerce_value` | Les types de produits ne peuvent pas être convertis. |
| `invalid_keys_in_value_object` | Les clés d’objet de produit ne peuvent pas inclure `.` ou `$`. |
| `too_deep_nesting_in_value_object` | Les objets de produit ne peuvent pas avoir plus de 50 niveaux d’imbrication. |
| `item_array_invalid` | `items` doit être un tableau d’objets. |
| `catalog_not_found` | Vérifiez que le nom du catalogue est valide. | 
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}