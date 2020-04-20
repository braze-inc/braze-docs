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
{% apimethod post %}
/users/delete
{% endapimethod %}

{% alert warning %}
Deleting user profiles CANNOT be undone. It will PERMANENTLY remove users which may cause discrepancies in your data. Learn more about [what happens when you delete a user profile via API]({{site.baseurl}}/help/help_articles/api/delete_user/) in our Help documentation.
{% endalert %}

This endpoint allows you to delete any user profile by specifying a known user identifier. Up to 50 `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request. Only one of `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request. Please note that users' associated event data will still exist in the dashboard after you delete the user(s).

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/User%20Data/UserDeleteExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Request Body

```
Content-Type: application/json
```

```json
{
  "api_key" : (required, string) App Group REST API Key,
  "external_ids" : (optional, array of string) external ids for the users to delete,
  "user_aliases" : (optional, array of User Alias objects) User Aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze User Identifiers for the users to delete
}
```
Learn more about the [User Alias Object here]({{site.baseurl}}/api/objects_filters/user_alias_object/).

### Response

```json
Content-Type: application/json
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
