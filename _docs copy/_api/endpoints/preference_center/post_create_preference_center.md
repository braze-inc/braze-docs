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
# Create preference center
{% apimethod post %}
/preference_center/v1
{% endapimethod %}

> Use this endpoint to create a preference center to allow users to manage their notification preferences for your email campaigns. Refer to [Create a preference center via API]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/#create-a-preference-center-via-api) for steps on how to build an API-generated preference center.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e15d7065-2cbc-4eb3-ae16-32efe43357a6 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `preference_center.update` permission.

## Rate limit

This endpoint has a rate limit of 10 requests per minute, per workspace.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "name": "string",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "state": (optional) Choose `active` or `draft`. Defaults to `active` if not specified,
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag
  }
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`name`| Required | String | The name of the preference center that meets the following requirements: <br>- Only contains letters, numbers, hyphens, and underscores <br>- Does not have spaces |
|`preference_center_title`| Optional | String | The title for the preference center and confirmation pages. If a title is not specified, the title of the pages will default to "Preference Center". |
|`preference_center_page_html`| Required | String | The HTML for the preference center page. |
|`confirmation_page_html`| Required | String | The HTML for the confirmation page. |
|`state` | Optional | String | Choose `active` or `draft`. Defaults to `active` if not specified. |
|`options` | Optional | Object | Attributes: `meta-viewport-content`. When present, a `viewport` meta tag will be added to the page with `content= <value of attribute>`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
The preference center name can't be edited after it's created.
{% endalert %}

### Liquid tags

Refer to the following Liquid tags that can be included in your HTML to generate a user's subscription state on the preference center page.

{% raw %}

#### User subscription state

| Liquid | Description |
| --------- | ---------|
|`{{subscribed_state.${email_global}}}`| Get the global email subscribed state for the user (such as "opted_in", "subscribed", or "unsubscribed". |
|`{{subscribed_state.${<subscription_group_id>}}}`| Get the subscribed state of the specified subscription group for the user (such as "subscribed" or "unsubscribed"). |
{: .reset-td-br-1 .reset-td-br-2}

#### Form inputs and action

| Liquid | Description |
| --------- | ---------|
|`{% form_field_name :email_global_state %}`| Indicates that a specific form input element corresponds to the user's global email subscribed state. The user's selection state should be "opted_in", "subscribed", or "unsubscribed" when the form is submitted with selection data for the global email subscribed state. If it's a checkbox, the user will either be "opted_in" or "unsubscribed". For a hidden input, the "subscribed" state will also be valid. |
|`{% form_field_name :subscription_group <subscription_group_id> %}`| Indicates that a specific form input element corresponds to a given subscription group. The user's selection state should be either "subscribed" or "unsubscribed" when the form is submitted with selection data for a specific subscription group. |
|`{{preference_center_submit_url}}`| Generates URL for form submission. |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

## Example response
{% raw %}
```
{
  "preference_center_api_id": "preference_center_api_id_example",
  "liquid_tag": "{{preference_center.${MyPreferenceCenter2022-09-22}}}",
  "created_at": "2022-09-22T18:28:07+00:00",
  "message": "success"
}
```
{% endraw %}

{% endapi %}
