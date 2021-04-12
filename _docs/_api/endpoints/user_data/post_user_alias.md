---
nav_title: "POST: Create New User Alias"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the create new User Aliases Braze endpoint."
---
{% api %}
# Create New User Alias
{% apimethod post %}
/users/alias/new
{% endapimethod %}

Use this endpoint to add new user aliases for existing identified users, or to create new unidentified users.

__Adding a user alias for an existing user__ requires an `external_id` to be included in the new user alias object. If the `external_id` is present in the object but there is no user with that `external_id`, the alias will not be added to any users. If an `external_id` is not present, a user will still be created but will need to be identified later. You can do this using the "Identifying Users" and the `users/identify` endpoint.

__Creating a new alias-only user__ requires the `external_id` to be omitted from the new user alias object. Once the user is created, use the `/users/track` endpoint to associate the alias-only user with attributes, events, and purchases, and the `/users/identify` endpoint to identify the user with an `external_id`.

You can add up to 50 user aliases per request.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "user_aliases" : (required, array of new user alias object)
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Yes | Array of new user alias objects | See user alias object |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [User Alias Object]({{site.baseurl}}/api/objects_filters/user_alias_object/)
<br><br>
For more information on `alias_name` and `alias_label`, check out our [User Aliases documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

###  Endpoint Request Body with New User Alias Object Specification

```json
{
  "external_id" : (optional, string) see external user id below,
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "user_aliases" : 
  [
    {
      "external_id": "user_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

{% endapi %}

