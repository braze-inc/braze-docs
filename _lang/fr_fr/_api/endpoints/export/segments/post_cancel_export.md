---
nav_title: "POST : Annuler les exportations par segmentation"
article_title: "POST : Annuler les exportations par segmentation"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'exportation d'annulations par segment Braze endpoint."

---
{% api %}
# Annuler les exportations par segmentation
{% apimethod post %}
/exportation/segmentation/annulation
{% endapimethod %}

> Utilisez cet endpoint pour annuler toutes les exportations en cours avec un ID de segmentation spécifié.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `segments.list`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `segment_id` | Requis | Chaîne de caractères | Le site `segment_id` pour annuler ses exportations en cours. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}

