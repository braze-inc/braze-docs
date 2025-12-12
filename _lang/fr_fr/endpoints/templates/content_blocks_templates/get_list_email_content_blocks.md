---
nav_title: "GET : Liste des blocs de contenu disponibles"
article_title: "GET : Répertorier les blocs de contenu disponibles"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Répertorier les blocs de contenu disponibles."

---
{% api %}
# Répertorier les blocs de contenu disponibles
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> Utilisez cet endpoint pour dresser la liste des informations relatives à vos [blocs contenus]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) existants.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Conditions préalables
Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `content_blocks.list`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `modified_after`  | Facultatif | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Récupérer uniquement les blocs de contenu mis à jour à partir de l'heure donnée. |
| `modified_before`  |  Facultatif | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Récupérer uniquement les blocs de contenu mis à jour au plus tard à l'heure donnée. |
| `limit` | Facultatif | Nombre positif | Nombre maximum de blocs de contenu à récupérer. Par défaut à 100 si non renseigné, avec une valeur maximale acceptable de 1 000. |
| `offset`  |  Facultatif | Nombre positif | Nombre de blocs de contenu à ignorer avant de renvoyer le reste des modèles correspondant aux critères de recherche. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings,
    }
  ]
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Modified after time is invalid` | La date fournie n’est pas une date valide ou analysable. Reformater cette valeur en tant que chaîne de caractères au format ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified before time is invalid` | La date fournie n’est pas une date valide ou analysable. Reformater cette valeur en tant que chaîne de caractères au format ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified after time must be earlier than or the same as modified before time.` | Modifier la valeur `modified_after` à une heure antérieure à l’heure `modified_before`. |
| `Content Block number limit is invalid` | Le paramètre `limit` doit être un entier (nombre positif) supérieur à 0. |
| `Content Block number limit must be greater than 0` | Modifier le paramètre `limit` à un entier supérieur à 0. |
| `Content Block number limit exceeds maximum of 1000` | Modifier le paramètre `limit` à un entier inférieur à 1 000. |
| `Offset is invalid` | Le paramètre `offset` doit être un entier supérieur à 0. |
| Le décalage doit être supérieur à 0 | Modifier le paramètre `offset` à un entier supérieur à 0. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
