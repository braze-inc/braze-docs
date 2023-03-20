---
nav_title: "GET : Lister les détails du produit du catalogue"
article_title: "GET : Lister les détails du produit du catalogue"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Lister les détails du produit du catalogue."

---
{% api %}
# Lister les détails du produit du catalogue
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

Utilisez cet endpoint pour renvoyer un produit de catalogue et son contenu.

## Limite de débit

Cet endpoint a une limitation du débit partagée de 50 requêtes par minute entre tous les endpoints synchronisés de produits du catalogue.

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | String | Nom du catalogue. |
| `item_id` | Requis | String | L’ID du produit du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Paramètres de demande

Cet endpoint n’a pas de corps de demande.

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

Deux réponses de code de statut existent pour cet endpoint : `200` et `404`.

### Exemple de réponse réussie

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `404` pourrait retourner la réponse suivante. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées, le cas échéant.

| Erreur | Résolution des problèmes |
| --- | --- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `item-not-found` | Vérifiez que ce produit est dans le catalogue. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}