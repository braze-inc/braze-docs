---
nav_title: "POST : Ajouter des e-mails à la liste de blocage"
article_title: "POST : Ajouter des e-mails à la liste de blocage"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre des e-mails en liste de blocage."

---
{% api %}
# Ajouter des e-mails à la liste de blocage
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> Utilisez cet endpoint pour désinscrire un utilisateur des e-mails et le marquer comme rejeté définitivement.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `email.blacklist`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blocklist_email1","blocklist_email2"]
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| -----------|----------| --------|------- |
| `email` | Requis | Chaîne de caractères ou tableau | Adresse e-mail par chaîne de caractères ou un tableau de 50 adresses e-mail à ajouter à la liste de blocage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}
