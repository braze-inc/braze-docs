---
nav_title: Email Blacklist
permalink: /blacklist/
hidden: true
---

# Email Blacklist

User email addresses can be blacklisted via Braze using a RESTful API.

{% alert important %}
Email Blacklisting via API endpoint is currently in Beta. Please reach out to your Braze Account Manager for more information. 
{% endalert %}

## Braze Instance Endpoints

Instance  | REST Endpoint
-----------|-----------------------------------------
US-01 | `https://rest.iad-01.braze.com/email/blacklist`
US-02 | `https://rest.iad-02.braze.com/email/blacklist`
US-03 | `https://rest.iad-03.braze.com/email/blacklist`
US-04 | `https://rest.iad-04.braze.com/email/blacklist`
US-06 | `https://rest.iad-06.braze.com/email/blacklist`
EU-01 | `https://rest.fra-01.braze.eu/email/blacklist`
{: .reset-td-br-1 .reset-td-br-2}

## Blacklisting Email Addresses

Blacklisting an email address will unsubscribe the user from email and mark them as hard bounced.

```json
POST https://YOUR_REST_API_URL/email/blacklist
Content-Type: application/json
```
```
{
  "email": "email@address.com"
}
```

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `email` | Yes | String or Array | String email address to blacklist, or an array of up to 50 email addresses to blacklist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Example Email Blacklist CURL

```
curl --location --request POST 'https://YOUR_REST_API_URL/email/blacklist'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["EMAIL_TO_BLACKLIST_1","EMAIL_TO_BLACKLIST_2"]}'
```
