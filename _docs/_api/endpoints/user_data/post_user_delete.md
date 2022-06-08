---
nav_title: "POST: User Delete"
article_title: "POST: User Delete"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the delete User Information Braze endpoint."

---
{% api %}
# User delete endpoint
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/delete
{% endapimethod %}


This endpoint allows you to delete any user profile by specifying a known user identifier. Up to 50 `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request. Only one of `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

{% alert warning %}
Deleting user profiles cannot be undone. It will permanently remove users which may cause discrepancies in your data. Learn more about what happens when you [delete a user profile via API]({{site.baseurl}}/help/help_articles/api/delete_user/) in our Help documentation.
{% endalert %}

## Rate limit

{% include rate_limits.md endpoint='users delete' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (optional, array of string) External ids for the users to delete,
  "user_aliases" : (optional, array of user alias objects) User aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze user identifiers for the users to delete
}
```
### Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Optional | Array of strings | External identifiers for the users to delete. |
| `user_aliases` | Optional | Array of user alias object | [User aliases]({{site.baseurl}}/api/objects_filters/user_alias_object/) for the users to delete. |
| `braze_ids` | Optional | Array of strings | Braze user identifiers for the users to delete. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"].
  "user_aliases": [
    {"alias_name": "user_alias1", "alias_label": "alias_label1"},
    {"alias_name": "user_alias2", "alias_label": "alias_label2"}
  ]
}'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```
{% endapi %}


