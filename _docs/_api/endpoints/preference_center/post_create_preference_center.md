---
nav_title: "POST: Create Preference Center"
article_title: "POST: Create Preference Center"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Create a preference center Braze endpoint."

---
{% api %}
# Create a preference center
{% apimethod post %}
/preference_center/v1
{% endapimethod %}

Use this endpoint to create a preference center to allow users to manage their notification preferences for email campaigns.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Rate limit

This endpoint has a rate limit of 10 requests per minute, per app group.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "name": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string"
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`name`| Required | String | The name of the preference center. |
|`preference_center_page_html`| Optional | String | The HTML for the preference center page. |
|`confirmation_page_html`| Optional | String | The HTML for the confirmation page. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request example
```json
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example Preference Center",
  "preference_center_page_html": "<html>
  <head></head>
    <body>
    Email Subscription Group A (Marketing) Status: {% subscribed_state :email_subscription_group XXX %}
    <br />
    Email Subscription Group B (Math Games) Status: {% subscribed_state :email_subscription_group XXX %}
    <br />
    Global email subscription state: {% subscribed_state :email_global_state %}
    <br />
    <form method=\"post\" action=\"{{ preference_center_submit_url }}\">
      <select id=\"sg-a\" name = \"{% form_field_name :email_subscription_group XXX %}\" >
        <option value=\"subscribed\">Subscribed</option>
        <option value=\"unsubscribed\">Unsubscribed</option>
      </select>
      <label for=\"sg-a\">Subscription Group A</label>
      <br />
      <select id=\"sg-b\" name = \"{% form_field_name :email_subscription_group XXX %}\" >
        <option value=\"subscribed\">Subscribed</option>
        <option value=\"unsubscribed\">Unsubscribed</option>
      </select>
      <label for=\"sg-b\">Subscription Group B</label>
      <br />
      <select id=\"global\" name = \"{% form_field_name :email_global_state %}\" >
        <option value=\"subscribed\">Subscribed</option>
        <option value=\"unsubscribed\">Unsubscribed</option>
        <option value=\"opted_in\">Opted In</option>
      </select>
      <label for=\"global\">Global Subscription State</label>
      <br />
      <input type=\"submit\" value=\"Submit\">
    </form>
  </body>
</html>",
  "confirmation_page_html":"<html>
    <head>
    </head>
    <body>Thanks for updating your preferences!
      </body>
</html>",
}'
```

{% endapi %}