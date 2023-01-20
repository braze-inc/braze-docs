---
nav_title: "POST : [Nom de l’endpoint]"
page_order: "POST : Suivi utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: article de référence
excerpt_separator: ""

description: "Cet article présente des informations détaillées sur cet endpoint Braze POST [nom de l’endpoint] et son utilisation."

noindex: true
#ATTENTION : supprimer le noindex et l’alerte de ce modèle
---
{% api %}
# [Nom de l’endpoint]

{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

<!--
Ceci est la description de l’endpoint. Les descriptions d’API commencent généralement par « Utilisez cet endpoint pour… »–>
Cet endpoint vous permet de supprimer des numéros de téléphone « non valides » de la liste de numéros non valides de Braze. Cela peut être utilisé pour revalider les numéros de téléphone après avoir été marqués comme non valides.

<!-- Your postman link. Once you have published the endpoint to postman, you will be able get a direct link to the info in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Limites de débit

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

<!--This is where you can give more information about your endpoint request body. -->

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

### Paramètres de demande

<!--This is a place for you to describe additional details for the parameters in the request body.-->

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ---------|------ |
| `phone_number` | Requis | Tableau de chaînes de caractères au format e.164 | Un tableau de 50 numéros de téléphone à modifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande

<!--The following example demonstrates a request that will remove specific SMS numbers from Braze's invalid phone number list via the API:-->

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```
{% endapi %}
