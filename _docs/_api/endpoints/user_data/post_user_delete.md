---
nav_title: "POST: Delete Users"
article_title: "POST: Delete Users"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "This article outlines details about the Delete users Braze endpoint."

---
{% api %}
# Delete users
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/delete
{% endapimethod %}

> Use this endpoint to delete any user profile by specifying a known user identifier.

Up to 50 `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request. Only one of `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request.

{% alert warning %}
Deleting user profiles cannot be undone. It will permanently remove users which may cause discrepancies in your data. Learn more about what happens when you [delete a user profile via API]({{site.baseurl}}/help/help_articles/api/delete_user/) in our Help documentation.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `users.delete` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External ids for the users to delete,
  "user_aliases" : (optional, array of user alias objects) User aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze user identifiers for the users to delete
}
```
### Request parameters

| Parameter      | Required | Data Type                  | Description                                                                                      |
| -------------- | -------- | -------------------------- | ------------------------------------------------------------------------------------------------ |
| `external_ids` | Optional | Array of strings           | External identifiers for the users to delete.                                                    |
| `user_aliases` | Optional | Array of user alias object | [User aliases]({{site.baseurl}}/api/objects_filters/user_alias_object/) for the users to delete. |
| `braze_ids`    | Optional | Array of strings           | Braze user identifiers for the users to delete.                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Deleting users by email
If an `email` is specified as an identifier, an additional `prioritization` value is required in the identifier. The `prioritization` should be an array specifying which user to merge if there are multiple users found. `prioritization` is an ordered array, meaning if more than one user matches from a prioritization, then merging will not occur.

The allowed values for the array are: `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` refers to prioritizing the most recently updated user.

Only one of the following options may exist in the prioritization array at a time:
- `identified` refers to prioritizing a user with an `external_id`
- `unidentified` refers to prioritizing a user without an `external_id`

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ],
  "email_addresses": [
    {
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```
{% endapi %}


