---
nav_title: "POST: Identify Users"
article_title: "POST: Identify Users"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Identify Users Braze endpoint."

---
{% api %}
# Identify Users
{% apimethod post %}
/users/identify
{% endapimethod %}

Use this endpoint to identify an unidentified (alias-only) user.

Identifying a user requires an `external_id` to be included in the `aliases_to_identify` object. If there is no user with that `external_id`, the `external_id` will simply be added to the aliased user's record, and the user will be considered identified.

Subsequently, you can associate multiple additional user aliases with a single `external_id`. When these subsequent associations are made, only the push tokens and message history associated with the user alias are retained; any attributes, events, or purchases will be "orphaned" and not available on the identified user. One workaround is to export the aliased user's data before identification using the [`/users/export/ids` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_user_identify/), then re-associate the attributes, events, and purchases with the identified user.

You can add up to 50 user aliases per request.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects)
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `aliases_to_identify` | Required | Array of aliases to identify object | See [alias to identify object]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) and [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request Example
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "aliases_to_identify" : 
  [
    {
      "external_id": "external_identifier",
      "user_alias" : {
          "alias_name" : "example_alias",
          "alias_label" : "example_label"
      }
    }
  ]
}'
```

For more information on `alias_name` and `alias_label`, check out our [user aliases documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% endapi %}

