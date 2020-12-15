---
nav_title: "POST: User Delete"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the delete User Information Braze endpoint."
---
{% api %}
# User Delete Endpoint
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/delete
{% endapimethod %}
<br>
{% alert warning %}
Deleting user profiles CANNOT be undone. It will PERMANENTLY remove users which may cause discrepancies in your data. Learn more about [what happens when you delete a user profile via API]({{site.baseurl}}/help/help_articles/api/delete_user/) in our Help documentation.
{% endalert %}

This endpoint allows you to delete any user profile by specifying a known user identifier. Up to 50 `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request. Only one of `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/User%20Data/UserDeleteExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

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
  "external_ids" : (optional, array of string) external ids for the users to delete,
  "user_aliases" : (optional, array of User Alias objects) User Aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze User Identifiers for the users to delete
}
```
### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Optional | Array of Strings | External ids for the users to delete |
| `user_aliases` | Optional | Array of User Alias Objects | User Aliases for the users to delete |
| `braze_ids` | Optional | Array of Strings | Braze User Identifiers for the users to delete |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [User Alias Object here]({{site.baseurl}}/api/objects_filters/user_alias_object/)

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["user_id1", "user_id2"],
  "user_aliases": ["user_alias1", "user_alias2"],
  "braze_ids": ["braze_id1", "braze_id2"]
}'
```

### Response

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```
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
