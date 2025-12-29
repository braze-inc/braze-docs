---
nav_title: "POST: Identify users"
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

> Use this endpoint to identify an unidentified (alias-only, email-only, or phone number-only) user using the provided external ID.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## How it works

Calling `/users/identify` combines a user profile that is identified by an alias (alias-only profile), email address (email-only profile), or phone number (phone number-only profile) with a user profile that has an `external_id` (identified profile), then removes the alias-only profile.

Identifying a user requires an `external_id` to be included in the following objects:

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

If there isn't a user with that `external_id`, the `external_id` is added to the aliased user's record, and the user is considered identified. Users can have only one alias for a specific label. If a user already exists with the `external_id` and has an existing alias with the same label as the alias-only profile, then the user profiles are not combined.

{% alert tip %}
To prevent unexpected loss of data when identifying users, we highly recommend that you first refer to [data collection best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) to learn about capturing user data when alias-only user information is already present.
{% endalert %}

### Merging behavior

By default, this endpoint merges the following list of fields found **exclusively** on the anonymous user to the identified user.

{% details List of fields that are merged %}
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
- Date of first session (Braze picks the earlier date of the two dates)
- Date of last session (Braze picks the later date of the two dates)
- Custom attributes
- Custom event and purchase event data
- Custom event and purchase event properties for "X times in Y days" segmentation (where X<=50 and Y<=30)
- Segmentable custom events summary
  - Event count (the sum from both profiles)
  - Event first occurred (Braze picks the earlier date of the two dates)
  - Event last occurred (Braze picks the later date of the two dates)
- In-app purchase total in cents (the sum from both profiles)
- Total number of purchases (the sum from both profiles)
- Date of first purchase (Braze picks the earlier date of the two dates)
- Date of last purchase (Braze picks the later date of the two dates)
- App summaries
- Last_X_at fields (Braze updates the fields if the orphaned profile fields are more recent)
- Campaign summaries (Braze picks the most recent date fields)
- Workflow summaries (Braze picks the most recent date fields)
- Message and message engagement history
- Custom event and purchase event count and first date and last date timestamps
  - These merged fields update "for X events in Y days" filters. For purchase events, these filters include "number of purchases in Y days" and "money spent in last Y days".
- Session data if the app exists on both user profiles
  - For example, if our target user doesn't have an app summary for "ABCApp" but our original user does, the target user has the "ABCApp" app summary on their profile after the merge.
{% enddetails %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `users.identify` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
   "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},
```

### Request parameters

You can add up to 50 user aliases per request. You can associate multiple additional user aliases with a single `external_id`.

{% alert important %}
One of the following is required: `aliases_to_identify`, `emails_to_identify`, or `phone_numbers_to_identify` per request. For example, you can use this endpoint to identify users by email by using `emails_to_identify` in your request.
{% endalert %}

| Parameter                   | Required | Data Type                           | Description                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | Required | Array of aliases to identify object | See [alias to identify object]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) and [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`        | Required | Array of aliases to identify object | Required if `email` is specified as the identifier. Email addresses to identify users. See [Identifying users by email](#identifying-users-by-email).                                                                                                              |
| `phone_numbers_to_identify` | Required | Array of aliases to identify object | Phone numbers to identify users.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Identifying users by email addresses and phone numbers

If an email address or phone number is specified as an identifier, you must also include `prioritization` in the identifier.

The `prioritization` must be an array specifying which user to merge if there are multiple users found. `prioritization` is an ordered array, meaning if more than one user matches from a prioritization, then merging does not occur.

The allowed values for the array are:

- `identified`
- `unidentified`
- `most_recently_updated` (refers to prioritizing the most recently updated user)
- `least_recently_updated` (refers to prioritizing the least recently updated user)

Only one of the following options may exist in the prioritization array at a time:

- `identified` refers to prioritizing a user with an `external_id`
- `unidentified` refers to prioritizing a user without an `external_id`

If you specify `identified` in the array, this would mean the user **must** have an `external_id` to be entered into the Canvas. If you want users with email addresses to enter the message, regardless of whether they're identified or not, only use the `most_recently_updated` or `least_recently_updated` parameter instead.

## Request example

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

{% alert tip %}
For more information on `alias_name` and `alias_label`, check out our [user aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) documentation.
{% endalert %}

## Response

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}
