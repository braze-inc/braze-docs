---
nav_title: "DELETE : Supprimer la sélection du catalogue"
article_title: "DELETE : Supprimer la sélection du catalogue"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente les détails du point de terminaison Supprimer la sélection de catalogue de Braze."

---
{% api %}
# Supprimer la sélection du catalogue
{% apimethod delete %}
/catalogs/{catalog_name}/selections/{selection_name}
{% endapimethod %}

> Utilisez cet endpoint pour supprimer une sélection de catalogue.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `catalogs.delete_selection`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Paramètres de chemin

| Paramètre        | Requis | Type de données | Description                    |
| ---------------- | -------- | --------- | ------------------------------ |
| `catalog_name`   | Requis | Chaîne de caractères    | Nom du catalogue.           |
| `selection_name` | Requis | Chaîne de caractères    | Nom de la sélection du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/selections/favorite_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Réponse

Deux réponses de code de statut existent pour cet endpoint : `202` et `404`.

### Exemple de réponse réussie

Le code de statut `202` pourrait renvoyer le corps de réponse suivant :

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `404` pourrait renvoyer le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

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

| Erreur                | Résolution des problèmes                                          |
| -------------------- | -------------------------------------------------------- |
| `catalog-not-found`  | Vérifiez que le nom du catalogue est valide.                    |
| `invalid-selection`  | Vérifiez que le nom de la sélection est valide.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
