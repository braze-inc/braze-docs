---
nav_title: "POST: Blacklist Emails"
article_title: "POST: Blacklist Emails"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
alias: /blacklist/
description: "This article outlines the usage of and parameters for blacklisting user email addresses with the Post Blacklist Emails Braze endpoint."

---
{% api %}
# Blacklist emails
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/email/blacklist
{% endapimethod %}

Blacklisting an email address will unsubscribe the user from email and mark them as hard bounced.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `email` | Required | String or Array | String email address to blacklist, or an array of up to 50 email addresses to blacklist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}


