---
nav_title: "POST: Blacklist Emails"
page_order: 5

layout: api_page

page_type: reference
channel: Email
alias: /blacklist/

description: "User email addresses can be blacklisted via Braze using a RESTful API."
---
{% api %}
# Blacklist Emails
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/email/blacklist
{% endapimethod %}

Blacklisting an email address will unsubscribe the user from email and mark them as hard bounced.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

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
  "email": "email@address.com"
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `email` | Yes | String or Array | String email address to blacklist, or an array of up to 50 email addresses to blacklist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email": ["EMAIL_TO_BLACKLIST_1","EMAIL_TO_BLACKLIST_2"]
}'
```

{% endapi %}


