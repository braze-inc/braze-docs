---
nav_title: "POST: Identify Users"
permalink: /users_identify_merge/
hidden: true
layout: api_page

---
{% api %}
# Identify users
{% apimethod post %}
/users/identify
{% endapimethod %}

Use this endpoint to identify an unidentified (alias-only) user.

{% alert important %}
Support for the `merge_behavior` field is currently in early access. Please contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

Identifying a user requires an `external_id` to be included in the `aliases_to_identify` object. If there is no user with that `external_id`, the `external_id` will simply be added to the aliased user's record, and the user will be considered identified. You can add up to 50 user aliases per request. 

Subsequently, you can associate multiple additional user aliases with a single `external_id`. 
- When these subsequent associations are made with the `merge_behavior` field set to `none`, only the push tokens and message history associated with the user alias are retained; any attributes, events, or purchases will be "orphaned" and not available on the identified user. One workaround is to export the aliased user's data before identification using the [`/users/export/ids` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_user_identify/), then re-associate the attributes, events, and purchases with the identified user.
- When associations are made with the `merge_behavior` field set to `merge`, this endpoint will merge [specific fields](#merge) found exclusively on the anonymous user to the identified user.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

{% alert note %}
A rate limit is applied to requests made to this endpoint for customers who onboarded with Braze on or after September 16, 2021. For more information, see [API Limits]({{site.baseurl}}/api/basics/#api-limits).
{% endalert %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects), 
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `aliases_to_identify` | Required | Array of aliases to identify object | See [alias to identify object]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) and [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `merge_behavior` | Optional | String | One of `none` or `merge` is expected.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Merge_behavior field {#merge}

Setting the `merge_behavior` field to `merge` sets the endpoint to merge any of the following fields found exclusively on the anonymous user to the identified user:
- First name
- Last name
- Email
- Gender
- Date of birth
- Phone number
- Time zone
- Home city
- Country
- Language
- Custom event data (excluding event properties)
- Purchase event data (excluding purchase properties)

{% alert warning %}
The following attributes are not yet supported:
- Session data 
- Custom event or purchase properties for segmentation
{% endalert %}

Setting the field to `none` will maintain the current functionality detailed above. 

## Request example
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
  ],
  "merge_behavior": "merge"
}'
```

For more information on `alias_name` and `alias_label`, check out our [user aliases documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% endapi %}