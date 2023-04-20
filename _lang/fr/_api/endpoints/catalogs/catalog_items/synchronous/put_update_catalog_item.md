---
nav_title: "PUT : Créer un produit du catalogue"
article_title: "PUT : Créer un produit du catalogue"
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

Si l’`item_id` n’est pas trouvé, cet endpoint créera le produit. Cet endpoint est synchrone.

{% alert note %}
Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `catalogs.replace_item`.
{% endalert %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | String | Nom du catalogue. |
| `item_id` | Requis | String | L’ID du produit du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `items` | Requis | Tableau | Un tableau qui contient certains objets Produit. Les objets Produits devraient contenir les champs qui existent dans le catalogue à l’exception du champ `id`. Un seul objet de produit est autorisé par requête. |
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
| `id_in_body` | Enlevez n’importe quel ID de produit dans le corps de la requête. |
| `ids_too_large` | La limite de caractères pour chaque ID de produit est de 250 caractères. |
| `invalid_ids` | Les caractères pris en charge pour les ID de produits sont les lettres, les nombres, les tirets et les traits de soulignement. |
| `items_too_large` | Les valeurs de produits ne peuvent pas dépasser 5 000 caractères. |
| `invalid_fields` | Confirmez que les champs de la requête existent dans le catalogue. |
| `unable_to_coerce_value` | Les types de produits ne peuvent pas être convertis. |
| `invalid_keys_in_value_object` | Les clés d’objet de produit ne peuvent pas inclure `.` ou `$`. |
| `too_deep_nesting_in_value_object` | Les objets de produit ne peuvent pas avoir plus de 50 niveaux d’imbrication. |
| `already_reached_catalog_item_limit` | Le nombre maximum de catalogues est atteint. Contactez votre gestionnaire de compte Braze pour plus d’informations. |
| `already_reached_company_item_limit` | Le nombre maximum de produits est atteint. Contactez votre gestionnaire de compte Braze pour plus d’informations. |
| `item_already_exists` | Ce produit existe déjà dans le catalogue. | 
| `filtered-set-field-too-long` | La valeur du champ est utilisée dans un ensemble filtré qui dépasse la limite de caractères pour un produit. |
| `arbitrary_error` | Une erreur arbitraire est survenue. Veuillez réessayer ou contacter l’[Assistance]({{site.baseurl}}/support_contact/). |
| `item_array_invalid` | `items` doit être un tableau d’objets. |
| `catalog_not_found` | Vérifiez que le nom du catalogue est valide. | 
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}