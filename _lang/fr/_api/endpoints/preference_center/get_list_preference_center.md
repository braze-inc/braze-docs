---
nav_title: "GET : Répertorier les centres de préférences"
article_title: "GET : Répertorier les centres de préférences"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article précise des détails concernant l’endpoint de Braze Répertorier les centres de préférences."

---
{% api %}
# Répertorier les centres de préférences
{% apimethod get %}
/preference_center/v1/list
{% endapimethod %}

> Utilisez cet endpoint pour répertorier vos centres de préférences disponibles.

## Limite de débit

Cet endpoint a une limitation du débit de 1 000 demandes par minute, par groupe d’apps.

## Paramètres de chemin et de requête

Cet endpoint n’a pas de paramètres de chemin ni de requête.

## Exemple de demande

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
{
  "preference_centers": [
    {
      "name": "My Preference Center 1",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-17T15:46:10Z",
      "updated_at": "2022-08-17T15:46:10Z"
    },
    {
      "name": "My Preference Center 2",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:13:06Z",
      "updated_at": "2022-08-19T11:13:06Z"
    },
    {
      "name": "My Preference Center 3",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:30:50Z",
      "updated_at": "2022-08-19T11:30:50Z"
    },
    {
      "name": "My Preference Center 4",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-09-13T20:41:34Z",
      "updated_at": "2022-09-13T20:41:34Z"
    }
  ]
}
```

{% endapi %}
