---
nav_title: "POST : Créer un catalogue"
article_title: "POST : Créer un catalogue"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer un catalogue."

---
{% api %}
# Créer un catalogue
{% apimethod post %}
/catalogs
{% endapimethod %}

Utilisez cet endpoint pour créer un catalogue.

## Limite de débit

Cet endpoint a une limitation du débit partagée de 5 requêtes par minute entre tous les endpoints synchronisés du catalogue.

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalogs` | Requis | Tableau | Un tableau qui contient des objets Catalogue. Un seul objet Catalogue est autorisé pour cette requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Paramètres de l’objet Catalogue

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `name` | Requis | String | Le nom du catalogue que vous voulez créer. |
| `description` | Requis | String | La description du catalogue que vous voulez créer. |
| `fields` | Requis | Tableau | Un tableau d’objets dans lequel l’objet contient les clés `name` et `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
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
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

## Réponse

Deux réponses de code de statut existent pour cet endpoint : `201` et `400`.

### Exemple de réponse réussie

Le code de statut `201` pourrait renvoyer le corps de réponse suivant.

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
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    }
  ],
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
      ],
      "parameter_values": [
        "restaurants"
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
| `catalog-array-invalid` | `catalogs` doit être un tableau d’objets. |
| `too-many-catalog-atoms` | Vous ne pouvez créer qu’un catalogue par requête. |
| `invalid_catalog_name` | Le nom de catalogue peut uniquement inclure des chiffres, des lettres, des traits d’union et des traits de soulignement. |
| `catalog-name-too-large`  | La limite de caractères d’un nom de catalogue est de 250. |
| `catalog-name-already-exists` | Un catalogue avec ce nom existe déjà. |
| `id-not-first-column` | Le champ `id` doit être le premier champ dans le tableau. Vérifiez que le type est une chaîne de caractères. |
| `invalid-fields` | `fields` n’est pas formaté correctement. |
| `too-many-fields` | La limite du nombre de champs est de 30. |
| `invalid-field-names` | Les champs peuvent uniquement inclure des chiffres, des lettres, des traits d’union et des traits de soulignement. |
| `invalid-field-types` | Assurez-vous que les types des champs sont valides. |
| `field-names-too-large` | La limite de caractères d’un nom de champ est de 250. |
| `field-names-not-unique` | Le même nom de champ est référencé deux fois. |
| `reached-company-catalogs-limit` | Le nombre maximum de catalogues est atteint. Contactez votre gestionnaire de compte Braze pour plus d’informations. |
| `description-too-long` | La limite de caractères pour la description est de 250. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}