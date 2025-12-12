---
nav_title: "POST: Delete users"
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

Up to 50 `external_ids`, `user_aliases`, `braze_ids`, `email_addresses`, or `phone_numbers` can be included in a single request. Only one of `external_ids`, `user_aliases`, `braze_ids`, `email_addresses`, or `phone_numbers` can be included in a single request.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

If you have a use case that can't be solved with bulk user deletion through the API, contact the [Braze Support team]({{site.baseurl}}/user_guide/administrative/access_braze/support/) for assistance.

## What data is deleted (nulled) {#data-deleted}

{% alert warning %}
Deleting user profiles cannot be undone. It will permanently remove users which may cause discrepancies in your data.
{% endalert %}

When you use this endpoint to remove a user, the following data is deleted (nulled):

- Any attributes that the user had
- Email address
- Phone number
- External user ID
- Gender
- Country
- Language

The following events will also occur:

- The user profile is deleted (nulled).
- The Lifetime Users count will be updated to account for the newly removed users.
- The removed user will still count toward the aggregated conversion percentage. Custom event counts and purchase counts will not be updated for removed users.

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
  "external_ids" : (optional, array of string) External IDs to be deleted,
  "user_aliases" : (optional, array of user alias objects) User aliases to be deleted,
  "braze_ids" : (optional, array of string) Braze user identifiers to be deleted,
  "email_addresses": (optional, array of string) User emails to be deleted,
  "phone_numbers": (optional, array of string) User phone numbers to be deleted
}
```
### Request parameters

| Parameter         | Required | Data Type                  | Description                                                                                      |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids`    | Optional | Array of strings           | External identifiers to be deleted.                                                    |
| `user_aliases`    | Optional | Array of user alias object | [User aliases]({{site.baseurl}}/api/objects_filters/user_alias_object/) to be deleted. |
| `braze_ids`       | Optional | Array of strings           | Braze user identifiers to be deleted.                                                  |
| `email_addresses` | Optional | Array of strings           | User emails to be deleted. Refer to [Deleting users by email](#deleting-users-by-email) for more information.                                                             |
| `phone_numbers` | Optional | Array of strings | User phone numbers to be deleted. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Deleting users by email addresses and phone numbers

If an email address or phone number is specified as an identifier, an additional `prioritization` value is required in the identifier. `prioritization` must be an ordered array and should specify which user to delete if there are multiple users. This means deleting users will not occur if more than one user matches a prioritization.

The allowed values for the array are:

- `identified`
- `unidentified`
- `most_recently_updated` (refers to prioritizing the most recently updated user)

Only one of the following options may exist in the `prioritization` array at a time:

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
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```
{% endapi %}


