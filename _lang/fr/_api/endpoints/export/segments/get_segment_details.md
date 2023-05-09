---
nav_title: "GET : Exporter les informations relatives au segment"
article_title: "GET : Exporter les informations relatives au segment"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter les informations relatives au segment."

---
{% api %}
# Exporter les informations relatives au segment
{% apimethod get %}
/segments/details
{% endapimethod %}

> Utilisez cet endpoint pour récupérer des informations pertinentes sur un segment, qui peuvent être identifiées par le `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre    | Requis | Type de données | Description            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Requis | String | Voir [Identifiant API de segment]({{site.baseurl}}/api/identifier_types/).<br><br> Le `segment_id` pour un segment donné se trouve dans votre **Developer Console (Console du développeur)** sur votre compte Braze, sinon vous pouvez utiliser l’[endpoint Liste des segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description, 
      "tags" : (array) the tag names associated with the segment formatted as strings
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
