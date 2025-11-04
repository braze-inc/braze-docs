---
nav_title: "POST : Créer des champs de catalogue"
article_title: "POST : Créer des champs de catalogue"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente les détails du point de terminaison Créer des champs de catalogue Braze."

---
{% api %}
# Créer des champs de catalogue
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> Utilisez cet endpoint pour créer plusieurs champs dans votre catalogue.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `catalogs.create_fields`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Paramètres de chemin

| Paramètre      | Requis | Type de données | Description          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Requis | Chaîne de caractères    | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Paramètres de demande

| Paramètre | Requis | Type de données | Description                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | Requis | Tableau     | Un tableau qui contient des objets de champ. Les objets champs doivent contenir le nom et le type des nouveaux champs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
      "type": "number"
    },
    {
      "name": "Loyalty_Program",
      "type": "boolean"
    },
    {
      "name": "Created_At",
      "type": "time"
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

| Erreur                                | Résolution des problèmes                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | Une erreur arbitraire est survenue. Veuillez réessayer ou contacter l'[assistance.]({{site.baseurl}}/support_contact/) |
| `catalog-not-found`                  | Vérifiez que le nom du catalogue est valide.                                                                  |
| `company-size-limit-already-reached` | La limite de taille de stockage du catalogue est atteinte.                                                             |
| `request-includes-too-many-fields`   | Chaque demande peut contenir jusqu'à 50 nouveaux champs.                                                          |
| `catalog-exceeds-fields-limit`       | Le catalogue ne peut pas comporter plus de 500 champs.                                                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
