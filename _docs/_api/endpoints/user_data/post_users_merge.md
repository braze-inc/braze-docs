---
nav_title: "POST: Merge users"
article_title: "POST: Merge Users"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "This article outlines details about the Merge users Braze endpoint."

---
{% api %}
# Merge users
{% apimethod post %}
/users/merge
{% endapimethod %}

> Use this endpoint to merge one user into another user. 

Up to 50 merges may be specified per request. This endpoint is asynchronous.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `users.merge` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `merge_updates` | Required | Array | An object array. Each object should contain an `identifier_to_merge` object and an `identifier_to_keep` object, which should each reference a user either by `external_id`,  `user_alias`, `phone`, or `email`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Merge behavior

The behavior documented below is true for all Braze features that **are not** powered by Snowflake. User merges won't be reflected for the **Messaging History** tab, Segment Extensions, Query Builder, and Currents.

{% alert important %}
The endpoint does not guarantee the sequence of `merge_updates` objects being updated.
{% endalert %}

This endpoint will merge the following fields if they're not found on the target user.

- First name
- Last name
- Email addresses (unless they are [encrypted]({{site.baseurl}}/user_guide/data/field_level_encryption/))
- Gender
- Date of birth
- Phone number
- Time zone
- Home city
- Country
- Language
- Device information
- Session count (the sum of sessions from both profiles)
- Date of first session (Braze will pick the earlier date of the two dates)
- Date of last session (Braze will pick the later date of the two dates)
- Custom attributes (existing custom attributes on the target profile are retained and will include custom attributes that didn't exist on the target profile)
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
- Campaign interaction data (Braze will pick the most recent date fields)
- Workflow summaries (Braze will pick the most recent date fields)
- Message and message engagement history
- Session data will only be merged if the app exists on both user profiles.

{% alert note %}
When merging users, using the `/users/merge` endpoint works the same way as using the [`changeUser()` method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

#### Custom event date and purchase event date behavior

These merged fields will update "for X events in Y days" filters. For purchase events, these filters include "number of purchases in Y days" and "money spent in last Y days".

### Merging users by email or phone number

If an `email` or `phone` is specified as an identifier, an additional `prioritization` value is required in the identifier. The `prioritization` should be an ordered array specifying which user to merge if multiple users are found. This means if more than one user matches from a prioritization, then merging will not occur.

The allowed values for the array are:

- `identified`
- `unidentified`
- `most_recently_updated` (refers to prioritizing the most recently updated user)
- `least_recently_updated` (refers to prioritizing the least recently updated user)

Only one of the following options may exist in the prioritization array at a time:

- `identified` refers to prioritizing a user with an `external_id`
- `unidentified` refers to prioritizing a user without an `external_id`

## Example requests

### Basic request

This is a basic request body to show the pattern of the request.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
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
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
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

### Merging unidentified user

The following request would merge the most recently updated unidentified user with email address `john.smith@braze.com` into the user with an external ID `john`. In this example, using `most_recently_updated` will filter the query to just one unidentified user. So, if there were two unidentified users with this email address, only one would get merged into the user who has an external ID `john`.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Merging unidentified user into identified user

This next example merges the most recently updated unidentified user with email address `john.smith@braze.com` into the most recently updated identified user with email address `john.smith@braze.com`. 

Using `most_recently_updated` will filter the queries to just one user (one unidentified user for `identifier_to_merge`, and one identified user for the `identifier_to_keep`).

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### Merging an unidentified user without including the most_recently_updated prioritization

If there are two unidentified users with ethe mail address `john.smith@braze.com`, this example request doesn't merge any users since there are two unidentified users with that email address. This request only works if there is only one unidentified user with the email address `john.smith@braze.com`.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
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
| `'merge_updates' must be an array of objects` | Check that `merge_updates` is an array of objects. |
| `a single request may not contain more than 50 merge updates` | You can only specify up to 50 merge updates in a single request. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Check the identifiers in your request. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Check that `merge_updates` only contains the two objects `identifier_to_merge` and `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
