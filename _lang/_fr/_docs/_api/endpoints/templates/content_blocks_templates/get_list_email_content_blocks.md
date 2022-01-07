---
nav_title: "GET: Liste des blocs de contenu disponibles"
article_title: "GET: Liste des blocs de contenu disponibles"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur la liste des blocs de contenu disponibles Braze point de terminal."
---

{% api %}
# Liste des blocs de contenu disponibles
{% apimethod get %}
/fr/content_blocks/list
{% endapimethod %}

Ce point de terminaison va vous lister les [blocs de contenu existants]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) informations.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre       | Requis    | Type de données                                                     | Libellé                                                                                                                              |
| --------------- | --------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `Modifié_après` | Optionnel | Chaîne au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Récupérer uniquement les blocs de contenu mis à jour à ou après l'heure donnée.                                                      |
| `modifié_avant` | Optionnel | Chaîne au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Récupérer uniquement les blocs de contenu mis à jour à ou avant l'heure donnée.                                                      |
| `limite`        | Optionnel | Nombre positif                                                      | Nombre maximum de blocs de contenu à récupérer. Valeur par défaut à 100 si non fournie, avec une valeur maximale acceptable de 1000. |
| `décalage`      | Optionnel | Nombre positif                                                      | Nombre de blocs de contenu à sauter avant de retourner le reste des modèles qui correspondent aux critères de recherche.             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": "string",
      "name": "string",
      "content_type": "html ou texte",
      "liquid_tag": "string",
      "inclusion_count" : "integer",
      "created_at": "time-in-iso",
      "last_editeded": "time-in-iso",
      "tags" : "array of strings"
    }
  ]
}
```

### Erreurs possibles
- `Modifié après l'instant est invalide.` - La date que vous avez fournie n'est pas une date valide ou analysée. Veuillez reformater cette valeur comme une chaîne au format ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffff`).

- `Modifié avant l'instant est invalide.` - La date que vous avez fournie n'est pas une date valide ou analysée. Veuillez reformater cette valeur comme une chaîne au format ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffff`).

- `Les modifications effectuées après l'heure doivent être antérieures ou égales à celles modifiées avant l'heure.`

- `La borne numéro de bloc de contenu est invalide.` - La `limite` paramètre doit ętre un entier (nombre positif) supérieur ŕ 0.

- `La limite de nombre de bloc de contenu doit être supérieure à 0.` - La `borne` paramètre doit être un entier (nombre positif) supérieur à 0.

- `La borne numéro de bloc de contenu dépasse le maximum de 1000.` - La `limite` paramètre doit ętre un entier (nombre positif) supérieur ŕ 0.

- `Le décalage est invalide.` - Le `décalage` paramètre doit ętre un entier (nombre positif) supérieur ŕ 0.

- `Le décalage doit ętre supérieur ŕ 0.` - Le `décalage` paramètre doit ętre un entier (nombre positif) supérieur ŕ 0.

{% endapi %}
