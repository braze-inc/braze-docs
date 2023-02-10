---
nav_title: "POST: Identify Users"
article_title: "POST: Identify Users"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines details about the Identify Users Braze endpoint."

---
{% api %}
# Identify users
{% apimethod post %}
/users/identify
{% endapimethod %}

Use this endpoint to identify an unidentified (alias-only) user. 

Calling `/users/identify` combines the alias-only profile with the identified profile and removes the alias-only profile. To prevent unexpected loss of data when identifying users, we highly recommend that you first refer to [data collection best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) to learn about capturing user data when alias-only user info is already present.

{% alert note %}
You can add up to 50 user aliases per request.
{% endalert %}

Identifying a user requires an `external_id` to be included in the `aliases_to_identify` object. If there is no user with that `external_id`, the `external_id` will simply be added to the aliased user's record, and the user will be considered identified.

You can associate multiple additional user aliases with a single `external_id`. When any of such associations are made, the push tokens and message history associated with the user alias are retained. Any attributes, events, or purchases will be moved to the identified user if it doesn't already exist on the user. One workaround is to export the aliased user's data before identification using the [`/users/export/ids` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), then re-associate the attributes, events, and purchases with the identified user.

{% alert important %}
Request fields and their values are case sensitive. Using different cases to reference an `external_id` will result in duplicate profiles. For example, "abc123" and "ABC123" are two different `external_ids`.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects)
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `aliases_to_identify` | Required | Array of aliases to identify object | See [alias to identify object]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) and [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request example
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
        "alias_name" : "example_alias",
        "alias_label" : "example_label"
      }
    }
  ]
}'
```

For more information on `alias_name` and `alias_label`, check out our [user aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) documentation.


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}

