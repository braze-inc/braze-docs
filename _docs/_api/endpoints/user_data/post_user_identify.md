---
nav_title: "POST: Identify Users"
article_title: "POST: Identify Users"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "This article outlines details about the Identify users Braze endpoint."

---
{% api %}
# Identify users
{% apimethod post %}
/users/identify
{% endapimethod %}

> Use this endpoint to identify an unidentified (alias-only) user. 

{% alert important %}
Starting August 7, 2023, this endpoint will merge data for all calls. This means [`merge_behavior`](#merge) will be set to `merge` for all calls.
{% endalert %}

Calling `/users/identify` combines the alias-only profile with the identified profile and removes the alias-only profile.

Identifying a user requires an `external_id` to be included in the `aliases_to_identify` object. If there is no user with that `external_id`, the `external_id` will simply be added to the aliased user's record, and the user will be considered identified. You can add up to 50 user aliases per request. 

Subsequently, you can associate multiple additional user aliases with a single `external_id`. 
- When these subsequent associations are made with the `merge_behavior` field set to `none`, only the push tokens and message history associated with the user alias are retained; any attributes, events, or purchases will be "orphaned" and not available on the identified user. One workaround is to export the aliased user's data before identification using the [`/users/export/ids` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), then re-associate the attributes, events, and purchases with the identified user.
- When associations are made with the `merge_behavior` field set to `merge`, this endpoint will merge [specific fields](#merge) found on the anonymous user to the identified user.

{% alert tip %}
To prevent unexpected loss of data when identifying users, we highly recommend that you first refer to [data collection best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) to learn about capturing user data when alias-only user information is already present.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

{% alert note %}
To use this endpoint, you'll need to generate an API key with the `users.identify` permission.
{% endalert %}

## Rate limit 

A rate limit is applied to requests made to this endpoint for customers who onboarded with Braze on or after September 16, 2021. For more information, see [API limits]({{site.baseurl}}/api/basics/#api-limits).

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

Setting the `merge_behavior` field to `merge` sets the endpoint to merge any of the following fields found **exclusively** on the anonymous user to the identified user. 
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
- Session count (the sum of sessions from both profiles)
- Date of first session (Braze will pick the earlier date of the two dates)
- Date of last session (Braze will pick the later date of the two dates)
- Custom attributes
- Custom event and purchase event data
- Custom event and purchase event properties for "X times in Y days" segmentation (where X<=50 and Y<=30)
- Segmentable custom events summary
  - Event count (the sum from both profiles)
  - Event first occurred (Braze will pick the earlier date of the two dates)
  - Event last occurred (Braze will pick the later date of the two dates)
- In-app purchase total in cents (the sum from both profiles)
- Total number of purchases (the sum from both profiles)
- Date of first purchase (Braze will pick the earlier date of the two dates)
- Date of last purchase (Braze will pick the later date of the two dates)
- App summaries
- Last_X_at fields (Braze will update the fields if the orphaned profile fields are more recent)
- Campaign summaries (Braze will pick the most recent date fields)
- Workflow summaries (Braze will pick the most recent date fields)
- Message and message engagement history

Any of the following fields found on the anonymous user to the identified user:
- Custom event and purchase event count and first date and last date timestamps 
  - These merged fields will update "for X events in Y days" filters. For purchase events, these filters include "number of purchases in Y days" and "money spent in last Y days".

Session data will only be merged if the app exists on both user profiles. For example, if our target user doesn't have an app summary for "ABCApp" but our original user does, the target user will have the "ABCApp" app summary on their profile after the merge. 

Setting the field to `none` will not merge any user data to the identified user profile.

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
