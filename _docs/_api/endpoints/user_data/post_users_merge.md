---
nav_title: "POST: Users Merge"
article_title: "POST: Users Merge"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "This article outlines details about the users merge Braze endpoint."

---
{% api %}
# Merge users
{% apimethod post %}
/users/merge
{% endapimethod %}

Use this endpoint to merge one user into another user. Up to 50 merges may be specified per request. This endpoint is asynchronous.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `merge_updates` | Required | Array | An object array. Each object should contain an `identifier_to_merge` object and an `identifier_to_keep` object, which should each reference a user either by `external_id` or `user_alias`. Both users being merged must be identified using the same method. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Merge_updates behavior

This endpoint will merge any of the following fields found exclusively on the original user to the target user.

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
- Custom event and purchase event data (excluding event properties)
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

Any of the following fields found on one user to the other user:
- Custom event and purchase event count and first date and last date timestamps
  - These merged fields will update "for X events in Y days" filters. For purchase events, these filters include "number of purchases in Y days" and "money spent in last Y days".

Session data will only be merged if the app exists on both user profiles. For example, if our target user doesn't have an app summary for "ABCApp" but our original user does, the target user will have the "ABCApp" app summary on their profile after the merge. Note that message and message engagement history aren't retained after both user profiles are merged.

{% alert note %}
The endpoint does not guarantee the sequence of `merge_updates` objects being updated.
{% endalert %}

## Example request

```
curl --location --request POST 'https://rest.iad-03.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

## Response

There are two status code responses for this endpoint: `202` and `400`.

### Example success response

The status code `202` could return the following response body.

```json
{
  "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Troubleshooting

The following table lists possible error messages that may occur.

| Error | Troubleshooting |
| --- |
| `'merge_updates' must be an array of objects` | Ensure that `merge_updates` is an array of objects. |
| `a single request may not contain more than 50 merge updates` | You can only specify up to 50 merge updates in a single request. |
| `identifiers must be objects with an 'external_id' property that is a string, or 'user_alias' property that is an object` | Check the identifiers in your request. |
| `identifiers must be objects of the same type` | Ensure that the identifier object types match. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Ensure that `merge_updates` only contains the two objects `identifier_to_merge` and `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
