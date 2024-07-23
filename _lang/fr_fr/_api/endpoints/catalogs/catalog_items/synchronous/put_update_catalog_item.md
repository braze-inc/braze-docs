---
nav_title: "PUT : Mettre à jour un produit du catalogue"
article_title: "PUT : Mettre à jour un produit du catalogue"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour un produit du catalogue."

---
{% api %}
# Mettre à jour un produit du catalogue
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour un produit dans votre catalogue. 

Si l’`item_id` n'est pas trouvé, cet endpoint créera le produit dans votre catalogue. Cet endpoint est synchrone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `catalogs.replace_item`.

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
| `items` | Obligatoire | Tableau | Un tableau qui contient des objets Produit. Les objets Produits devraient contenir les champs qui existent dans le catalogue à l’exception du champ `id`. Un seul objet de produit est autorisé par requête.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
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

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Reporte-toi à la rubrique [Dépannage](#troubleshooting) pour plus d'informations sur les erreurs que tu peux rencontrer.

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
| `arbitrary-error` | Une erreur arbitraire s'est produite. Essaie à nouveau ou contacte l'[assistance]({{site.baseurl}}/support_contact/). |
| `catalog-not-found` | Vérifie que le nom du catalogue est valide. |
| `filtered-set-field-too-long` | La valeur du champ est utilisée dans un ensemble filtré qui dépasse la limite de caractères pour un élément. |
| `id-in-body` | Supprimez tous les ID de produit dans le corps de la requête. |
| `ids-too-large` | La limite de caractères pour chaque ID de produit est de 250 caractères. |
| `invalid-ids` | Les caractères pris en charge pour les noms d'identifiants d'articles sont les lettres, les chiffres, les traits d'union et les traits de soulignement. |
| `invalid-fields` | Vérifiez que tous les champs que vous envoyez dans la requête d’API existent déjà dans le catalogue. Cela n'a rien à voir avec le champ d'identification mentionné dans l'erreur. |
| `invalid-keys-in-value-object` | Les clés de l'objet de l'article ne peuvent pas inclure `.` ou `$`. |
| `item-already-exists` | L'article existe déjà dans le catalogue. |
| `item-array-invalid` | `items` doit être un tableau d'objets. |
| `items-too-large` | La limite de caractères pour chaque élément est de 5 000 caractères. |
| `request-includes-too-many-items` | Vous ne pouvez créer qu’un produit de catalogue par requête. |
| `too-deep-nesting-in-value-object` | Les objets de type article ne peuvent pas avoir plus de 50 niveaux d'imbrication. |
| `unable-to-coerce-value` | Les types d'articles ne peuvent pas être convertis. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}