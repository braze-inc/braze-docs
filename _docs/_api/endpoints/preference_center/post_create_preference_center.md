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

Use this endpoint to create a preference center to allow users to manage their notification preferences for email campaigns. Check out [Creating a preference center via API]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/) for details on how to include this in your email campaigns.

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
|`preference_center_page_html`| Required | String | The HTML for the preference center page. |
|`confirmation_page_html`| Required | String | The HTML for the confirmation page. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Liquid tags

Refer to the following Liquid tags that can be included in your HTML to generate a user's subscription state on the preference center page.

{% raw %}

#### User subscription state

| Liquid | Description |
| --------- | ---------|
|`{{subscribed_state.${email_global}}}`| Get the global email subscribed state for the user (i.e. "opted_in" "subscribed" or "unsubscribed". |
|`{{subscribed_state.${}}}`| Get the subscribed state of a subscription group for the user (i.e. "subscribed" or "unsubscribed"). |
{: .reset-td-br-1 .reset-td-br-2}

#### Form inputs and action

| Liquid | Description |
| --------- | ---------|
|`{% form_field_name :email_global_state %}`| Indicates that a specific form input element corresponds to the user's global email susbcribed state. User's selection state should be "opted_in", "subscribed", or "unsubscribed" when the form is submitted with selection data for the global email subscribed state. If it's a checkbox, the user will either be "opted_in" or "unsubscribed". For a hidden input, the "subscribed" state will also be valid. |
|`{% form_field_name :subscription_group %}`| Indicates that a specific form input element corresponds to a given subscription group. User's selection state should be either "subscribed" or "unsubscribed" when the form is submitted with selection data for a specific subscription group. |
|`{{preference_center_submit_url}}`| Generates URL for form submission. |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

## Response example
{% raw %}
```
{
  "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
  "liquid_tag": "{{ preference_center.${My Preference Center 2022-09-22} }}",
  "created_at": "2022-09-22T18:28:07+00:00",
  "message": "success"
}
```
{% endraw %}

{% endapi %}