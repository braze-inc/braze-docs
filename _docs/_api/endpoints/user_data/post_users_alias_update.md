---
nav_title: "POST: Update user alias"
article_title: "POST: Update User Alias"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the Update user aliases Braze endpoint."
---
{% api %}
# Update user alias
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> Use this endpoint to update existing user aliases.

Up to 50 user aliases may be specified per request.

Updating a user alias requires `alias_label`, `old_alias_name`, and `new_alias_name` to be included in the update user alias object. If there is no user alias associated with the `alias_label` and `old_alias_name`, no alias will be updated. If the given `alias_label` and `old_alias_name` is found, then the `old_alias_name` will be updated to the `new_alias_name`.

{% alert note %}
This endpoint does not guarantee the sequence of `alias_updates` objects being updated.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `users.alias.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Required | Array of update user alias objects | See [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> For more information on `old_alias_name`, `new_alias_name`, and `alias_label`, refer to [User aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Endpoint request body with update user alias object specification

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}

