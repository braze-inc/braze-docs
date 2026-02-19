---
nav_title: "POST : Créer une sélection dans le catalogue"
article_title: "POST : Créer une sélection de catalogue"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente les détails du point de terminaison Créer une sélection de catalogue Braze."

---
{% api %}
# Créer une sélection dans le catalogue
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> Utilisez cet endpoint pour créer une sélection dans votre catalogue.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `catalogs.create_selection`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Paramètres de chemin

| Paramètre      | Requis | Type de données | Description          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Requis | Chaîne de caractères    | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Paramètres de demande

| Paramètre   | Requis | Type de données | Description                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | Requis | Objet    | Un objet qui contient des critères de sélection. Les objets de sélection peuvent contenir `name`, `description`, `filters`, `results_limit`, `sort_field`, et `sort_order`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ]
  }
}'
```

### Opérateurs de filtrage

| Type de champ | Opérateurs pris en charge                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
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

| Erreur                                | Résolution des problèmes                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | Vérifiez que le nom du catalogue est valide.                                                         |
| `company-size-limit-already-reached` | La limite de taille de stockage du catalogue est atteinte.                                                    |
| `selection-limit-reached`            | La limite des sélections du catalogue est atteinte.                                                      |
| `invalid-selection`                  | Vérifiez que la sélection est valide.                                                            |
| `too-many-filters`                   | Vérifiez si la sélection comporte trop de filtres.                                                  |
| `selection-name-already-exists`      | Vérifier si le nom de la sélection existe déjà dans le catalogue.                                    |
| `selection-has-invalid-filter`       | Vérifiez que le filtre de sélection est valide.                                                       |
| `selection-invalid-results-limit`    | Vérifiez que la limite des résultats de la sélection est valide.                                                |
| `invalid-sorting`                    | Vérifier si le tri de la sélection est valide.                                                      |
| `invalid-sort-field`                 | Vérifier si le champ de tri de la sélection est valide.                                                   |
| `invalid-sort-order`                 | Vérifier si l'ordre de tri de la sélection est valide.                                                   |
| `selection-contains-too-many-arrays` | Vérifiez si la sélection contient plus d'un champ de type `array`. Un seul est pris en charge. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
