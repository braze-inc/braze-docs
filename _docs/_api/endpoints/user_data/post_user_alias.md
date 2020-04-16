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

Adding a user alias for an existing user requires a valid `external_id` to be included in the new user alias object. If the `external_id` is present in the object but it is not a valid ID, the process will fail.

Creating a new alias-only user requires the `external_id` to be omitted from the new user alias object. Once the user is created, use the `/users/track` endpoint to associate the alias-only user with attributes, events and purchases, and the `/users/identify` endpoint to identify the user with an `external_id`.

You can add up to 50 user aliases per request.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/User%20Data/NewUserAliasRequestExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Request Body

```
Content-Type: application/json
```

```json
{
   "user_aliases" : (required, array of New User Alias Object)
}
```

This endpoint uses the New User Alias Object Specification.

###  Endpoint Request Body with New User Alias Object Specification

```json
{
  "external_id" : (optional, string) see External User ID below,
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

If an `external_id` is not present, a user will still be created, but will need to be identified later. You can do this using the "Identifying Users" and the `users/identify` endpoint.

## User Identification Endpoint

Use this endpoint to identify an unidentified (alias-only) user.

Identifying a user requires an `external_id` to be included in the aliases to identify the object. If the `external_id` is not a valid or known ID, it will simply be added to the aliases user's record, and the user will be considered identified.

Subsequently, you can associate multiple additional user aliases with a single `external_id`. When these subsequent associations are made, only the push tokens and message history associated with the user alias are retained; any attributes, events or purchases will be "orphaned" and not available on the identified user. One workaround is to export the aliased user's data before identification using the `/users/export/ids` endpoint, then re-associate the attributes, events, and purchases with the identified user.

You can add up to 50 user aliases per request.

Your Endpoint will correspond to your [Braze Instance][1].

Instance  | REST Endpoint
----------|----------------------------------------------
US-01  | `https://rest.iad-01.braze.com/users/identify`
US-02  | `https://rest.iad-02.braze.com/users/identify`
US-03  | `https://rest.iad-03.braze.com/users/identify`
US-04  | `https://rest.iad-04.braze.com/users/identify`
US-06  | `https://rest.iad-06.braze.com/users/identify`
EU-01  | `https://rest.fra-01.braze.eu/users/identify`
{: .reset-td-br-1 .reset-td-br-2}

### New User Identify Request

```json
POST https://YOUR_REST_API_URL/users/identify
Content-Type: application/json
{
   "aliases_to_identify" : (required, array of Aliases to Identify Object)
}
```

###  Aliases to Identify Object Specification

```json
{
  "external_id" : (required, string) see External User ID below,
  // external_ids for users that do not exist will return a non-fatal error.
  // See Server Responses for details.
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

For more information on `alias_name` and `alias_label`, check out our [User Aliases documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new?user_aliases' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "user_aliases" : 
  [
    {
      "external_id": "user_id",
      "alias_name" : "name",
      "alias_label" : "label"
    }
  ]
}'
```


{% endapi %}


[1]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/overview/#user-data-collection
[16]: #not-used-app
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1 codes"
[21]: http://docs.python-requests.org/en/latest/ "Requests"
[22]: https://rubygems.org/gems/multi_json "multiJSON"
[23]: https://rubygems.org/gems/rest-client "Rest Client"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1 codes"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: {{site.baseurl}}/developer_guide/rest_api/user_data/#braze-user-profile-fields
