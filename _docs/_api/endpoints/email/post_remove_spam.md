---
nav_title: "POST: Remove Email Addresses from Spam List"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel: Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about and using the Remove Email Addresses from the Spam List Braze endpoint."
---
{% api %}
# Remove Email Addresses from Spam List
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

This endpoint allows you to remove email addresses from your Braze spam list. We will also remove them from the spam list maintained by your email provider.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/RemovingSpamListEmailExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Body
```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Request Parameters

| Parameter | Required | Data Type | Description |
| ----------|-----------| --------|------- |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
