---
nav_title: "POST : Supprimer les adresses e-mail de la liste des courriers indésirables"
article_title: "POST : Supprimer les adresses e-mail de la liste des courriers indésirables"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Supprimer les adresses e-mail de la liste des courriers indésirables."

---
{% api %}
# Supprimer les adresses e-mail de la liste des courriers indésirables
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> Utilisez cet endpoint pour supprimer les adresses e-mail de votre liste de courriers indésirables de Braze et de la liste de courriers indésirables mise à jour par votre fournisseur d’e-mails.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `email.spam.remove`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| --------|------- |
| `email` | Requis | Chaîne de caractères ou tableau | Envoyez une adresse e-mail par chaîne de caractères ou un tableau de 50 adresses e-mail pour effectuer des modifications. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
