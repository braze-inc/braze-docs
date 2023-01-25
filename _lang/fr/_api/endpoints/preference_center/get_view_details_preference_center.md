---
nav_title: "GET : Afficher les détails du centre de préférences"
article_title: "GET : Afficher les détails du centre de préférences"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article précise des détails concernant l’endpoint de Braze Afficher les détails du centre de préférences."

---
{% api %}
# Afficher les détails du centre de préférences
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalId}
{% endapimethod %}

Utilisez cet endpoint pour afficher les détails de vos centres de préférences, y compris la date de leur création et de leurs mises à jour.

{% alert important %}
La prise en charge de cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Limites de débit

Cet endpoint a une limitation du débit de 1 000 demandes par minute, par groupe d’apps.

## Exemple de demande

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse 
```json 
{
  "name": "Mon centre de préférences",
  "preference_center_api_id": "preference_center_api_id",
  "created_at": "example_time_created",
  "updated_at": "example_time_updated",
  "preference_center_title": "Exemple de titre du centre de préférences",
  "preference_center_page_html": "HTML du centre de préférences ici",
  "confirmation_page_html": "HTML de la page de confirmation ici",
  "redirect_page_html": null
}
```

{% endapi %}
