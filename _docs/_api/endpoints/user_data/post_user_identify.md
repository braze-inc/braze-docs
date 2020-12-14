---
nav_title: "POST: Identify Users"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Identify Users Braze endpoint."
---
{% api %}
# Identify Users
{% apimethod post %}
/users/identify
{% endapimethod %}

Use this endpoint to identify an unidentified (alias-only) user.

Identifying a user requires an `external_id` to be included in the `aliases_to_identify` object. If there is no user with that `external_id`, the `external_id` will simply be added to the aliased user's record, and the user will be considered identified.

Subsequently, you can associate multiple additional user aliases with a single `external_id`. When these subsequent associations are made, only the push tokens and message history associated with the user alias are retained; any attributes, events or purchases will be "orphaned" and not available on the identified user. One workaround is to export the aliased user's data before identification using the [`/users/export/ids` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_user_identify/), then re-associate the attributes, events, and purchases with the identified user.

You can add up to 50 user aliases per request.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of Aliases to Identify Object)
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `aliases_to_identify` | Yes | Array of Aliases to Identify Objects | See Alias to Identify Object |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


### Request Components
- [Alias to Identify Object]({{site.baseurl}}/api/objects_filters/aliases_to_identify/)
- [User Alias Object]({{site.baseurl}}/api/objects_filters/user_alias_object/)

###  Request Body with Aliases to Identify Object

```json

{
   "aliases_to_identify" : (required, array of Aliases to Identify Object)
   [
     {
       "external_id" : (required, string) see External User ID below,
       // external_ids for users that do not exist will return a non-fatal error.
       // See Server Responses for details.
       "user_alias" : {
         "alias_name" : (required, string),
         "alias_label" : (required, string)
       }
     }
   ]
}
```

### Request Example
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify" : 
  [
    {
      "external_id": "user_id",
      "user_alias" : {
          "alias_name" : "user_alias123",
          "alias_label" : "label"
      }
    }
  ]
}'
```

For more information on `alias_name` and `alias_label`, check out our [User Aliases documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). You can learn more about the [Alias to Identify Object here]({{site.baseurl}}/api/objects_filters/aliases_to_identify/)

{% endapi %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
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
