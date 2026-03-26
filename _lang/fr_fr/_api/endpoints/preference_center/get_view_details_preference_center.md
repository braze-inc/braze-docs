---
nav_title: "GET : Afficher les détails du centre de préférences"
article_title: "GET : Afficher les détails du centre de préférences"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente l'endpoint Braze Afficher les détails du centre de préférences."

---
{% api %}
# Afficher les détails du centre de préférences
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Utilisez cet endpoint pour consulter les détails de vos centres de préférences, y compris les dates de création et de mise à jour.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `preference_center.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='get preference center' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Requis | Chaîne de caractères | L'ID de votre centre de préférences. |
{: role="presentation" }

## Paramètres de requête

Cet endpoint ne comporte aucun paramètre de requête.

## Exemple de requête

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse
```json
{
  "name": "My Preference Center",
  "preference_center_api_id": "preference_center_api_id",
  "created_at": "example_time_created",
  "updated_at": "example_time_updated",
  "preference_center_title": "Example preference center title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML for confirmation page here",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=2"
  },
  "state": "active"
}
```

{% endapi %}