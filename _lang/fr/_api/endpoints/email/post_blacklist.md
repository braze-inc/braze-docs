---
nav_title: "POST : ajouter des e-mails à la liste noire"
article_title: "POST : ajouter des e-mails à la liste noire"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "Cet article décrit l’utilisation et les paramètres pour ajouter à la liste noire des adresses e-mail d’utilisateur à l’aide de l’endpoint Braze Ajouter des e-mails à la liste noire."

---
{% api %}
# Ajouter des e-mails à la liste noire
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/email/blacklist
{% endapimethod %}

{% alert important %}

Braze a publié l’[endpoint `/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/) avec la même fonctionnalité que l’endpoint `/email/blacklist`. Il est recommandé d’utiliser l’endpoint `/email/blocklist` à la place.

{% endalert %}

Utilisez cet endpoint pour désinscrire un utilisateur des e-mails et le marquer comme rejeté définitivement.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| -----------|----------| --------|------- |
| `email` | Requis | Chaîne de caractères ou tableau | Envoyez une adresse e-mail par chaîne de caractères ou un tableau de 50 adresses e-mail à la liste noire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}


