---
nav_title: "POST: Liste noire des E-mails"
article_title: "POST: Liste noire des E-mails"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: Référence
alias: /blacklist/
description: "Cet article décrit l'utilisation et les paramètres pour mettre en liste noire les adresses e-mail des utilisateurs avec le point de terminaison Post Blacklist Emails Braze."
---

{% api %}
# Liste noire des e-mails
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/email/blacklist
{% endapimethod %}

La mise en liste noire d'une adresse e-mail désabonnera l'utilisateur de l'e-mail et le marquera comme étant rebondi dur.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "exemple@braze.com"
}
```

## Paramètres de la requête

| Paramètre | Requis | Type de données   | Libellé                                                                                                |
| --------- | ------ | ----------------- | ------------------------------------------------------------------------------------------------------ |
| `Email`   | Requis | Chaîne ou tableau | Chaîne l'adresse e-mail à la liste noire, ou un tableau de 50 adresses e-mail à mettre en liste noire. |
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


