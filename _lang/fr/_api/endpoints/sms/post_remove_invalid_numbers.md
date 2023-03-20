---
nav_title: "POST : Supprimer les numéros de téléphone non valides"
article_title: "POST : Supprimer les numéros de téléphone non valides"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article donne des détails sur la suppression de numéros de téléphone non valides de l’endpoint Braze."

---
{% api %}
# Supprimer les numéros de téléphone non valides
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

Cet endpoint vous permet de supprimer des numéros de téléphone « non valides » de la liste de numéros non valides de Braze. Cela peut être utilisé pour revalider les numéros de téléphone après avoir été marqués comme non valides.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ---------|------ |
| `phone_number` | Requis | Tableau de chaînes de caractères au format e.164 | Un tableau de 50 numéros de téléphone à modifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}
