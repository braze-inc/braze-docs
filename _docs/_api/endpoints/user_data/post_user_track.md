---
nav_title: "POST: User Track"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the User Track Braze endpoint."
---
{% api %}
# User Track
{% apimethod post %}
/users/track
{% endapimethod %}

This endpoint can be used to record custom events, user attributes, and purchases for users. You can include up to 75 Attributes, Event, and Purchase Objects per request. That is, you can only post attributes for up to 75 users at a time, but in the same API call you can also provide up to 75 events and up to 75 purchases.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/User%20Data/User%20track%20%E2%80%93%20attributes%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Request Body

```
Content-Type: application/json
```

```json
{
   "api_key" : (required, string) see App Group REST API Key,
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}
```

>  Customers using the API for server-to-server calls may need to whitelist `rest.iad-01.braze.com` if they're behind a firewall.

### Objects Used
- [User Attributes Object]({{ site.baseurl }}/api/objects_filters/user_attributes_object/)
- [Events Object]({{ site.baseurl }}/api/objects_filters/event_object/)
- [Purchases Object]({{ site.baseurl }}/api/objects_filters/purchase_object/)

{% alert note %}
- When creating alias-only users through this endpoint, you must explicitly set the `_update_existing_only` flag to `false`.
<br><br>
- Updating the subscription status with this endpoint will not only update the user specified by their external_id (e.g User 123), but it will also update the subscription status of any users with the same email as that user (User 123).
{% endalert %}

### Example Request Body for Event Tracking

```json
{
  "api_key": "123a45b6-cd78-9e01-g234-hi56j7k8l9m0",
  "events": [
    {
      "external_id": "string",
      "name": "string",
      "time": "string"
    }
  ]
}
```

You can see this example in action [in our Swagger documentation]({{ site.baseurl }}/api/interactive/#/User%20Data/User%20track%20–%20events%20example).

### User Track Responses

Upon using any of the aforementioned API requests you should receive one of the following three general responses:

#### Successful Message

Successful messages will be met with the following response:

```json
{
  "message" : "success",
  "attributes_processed" : (optional, integer), if attributes are included in the request, this will return an integer of the number of attributes that were queued to be processed,
  "events_processed" : (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,,
  "purchases_processed" : (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,,
}
```

#### Successful Message with Non-Fatal Errors

If your message is successful but has non-fatal errors such as one invalid Event Object out of a longer list of events you will receive the following response:

```json
{
  "message" : "success",
  "errors" : [
    {
      <minor error message>
    }
  ]
}
```

#### Message with Fatal Errors

In the case of a success, any data that was not affected by an error in the _errors_ array will still be processed. If your message has a fatal error you will receive the following response:

```json
{
  "message" : <fatal error message>,
  "errors" : [
    {
      <fatal error message>
    }
  ]
}
```

#### Queued Responses

During times of maintenance, Braze might pause real-time processing of the API. In these situations, the server will return an HTTP Accepted 202 response code and the following body, which indicates that we have received and queued the API call but have not immediately processed it. All scheduled maintenance will be posted to [http://status.braze.com](http://status.braze.com) ahead of time.

```json
{
  "message" : "queued"
}
```

#### Fatal Error Response Codes

The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.

| Error Code | Reason / Cause |
| ---------------------| --------------- |
| `400 Bad Request` | Bad Syntax. |
| `401 Unauthorized` | Unknown or missing REST API Key. |
| `404 Not Found` | Unknown REST API Key (if provided). |
| `429 Rate Limited` | Over rate limit. |
| `5XX` | Internal server error, you should retry with exponential backoff. |


###  Importing Legacy User Data

You may submit data through the Braze API for a user who has not yet used your mobile app in order to generate a user profile. If the user subsequently uses the application all information following their identification via the SDK will be merged with the existing user profile you created via the API call. Any user behavior that is recorded anonymously by the SDK prior to identification will be lost upon merging with the existing API generated user profile.

The segmentation tool will include these users regardless of whether they have engaged with the app. If you want to exclude users uploaded via the User API whom have not yet engaged with the app you should add the filter -- `Session Count > 0`.

{% endapi %}

[1]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints
[6]: {{ site.baseurl }}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/overview/#user-data-collection
[16]: #not-used-app
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1 codes"
[21]: http://docs.python-requests.org/en/latest/ "Requests"
[22]: https://rubygems.org/gems/multi_json "multiJSON"
[23]: https://rubygems.org/gems/rest-client "Rest Client"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1 codes"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#braze-user-profile-fields
