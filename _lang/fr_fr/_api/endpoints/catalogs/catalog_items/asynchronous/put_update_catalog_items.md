---
nav_title: "PUT : mettre à jour plusieurs produits du catalogue"
article_title: "PUT : mettre à jour plusieurs produits du catalogue"
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

Si un élément de catalogue n’existe pas, ce point de terminaison créera l’élément dans votre catalogue. Chaque requête peut prendre en charge jusqu’à 50 produits du catalogue. Cet endpoint est asynchrone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `catalogs.replace_items`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Paramètres de chemin

| Paramètre | Obligatoire | Type de données | Descriptif |
|---|---|---|---|
| `catalog_name` | Obligatoire | Chaîne | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Paramètres de demande

| Paramètre | Obligatoire | Type de données | Descriptif |
|---|---|---|---|
| `items` | Obligatoire | Matrice | Tableau contenant des objets d’élément. Chaque produit doit avoir un ID. Les objets Produits devraient contenir des champs qui existent dans le catalogue. Jusqu’à 50 objets sont autorisés par requête.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
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

| Erreur | Dépannage |
| --- | --- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `ids-not-string` | Vérifiez que chaque ID d’élément est une chaîne. |
| `ids-not-unique` | Vérifiez que chaque ID d’élément est unique. |
| `ids-too-large` | La limite de caractères pour chaque ID d’objet est de 250 caractères. |
| `item-array-invalid` `items` | doit être un tableau d’objets. |
| `items-missing-ids` | Vérifiez que chaque élément a un ID. |
| `items-too-large` | Les valeurs des objets ne peuvent pas dépasser 5 000 caractères. |
| `invalid-ids` | Les caractères pris en charge pour les noms d’ID d’élément sont les lettres, les chiffres, les traits d’union et les traits de soulignement. |
| `invalid-fields` | Vérifiez que tous les champs que vous envoyez dans la requête d’API existent déjà dans le catalogue. Cela n’est pas lié au champ ID mentionné dans l’erreur. |
| `invalid-keys-in-value-object` | Les clés d’objet d’élément ne peuvent pas inclure `.` ou `$`. |
| `too-deep-nesting-in-value-object` | Les objets d’élément ne peuvent pas avoir plus de 50 niveaux d’imbrication. |
| `request-includes-too-many-items` | Votre demande comporte trop d’éléments. La limite de produit par requête est de 50.
| `unable-to-coerce-value` | Les types d’objets ne peuvent pas être convertis. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
