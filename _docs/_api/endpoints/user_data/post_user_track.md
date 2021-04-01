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
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/track
{% endapimethod %}

Use this endpoint to record Custom events, Purchases, and update user profile attributes.

User Track has a base speed limit of 50,000 requests per minute for all customers. Each request can contain up to 75 events, 75 attribute updates, and 75 purchases. Each component (event, attribute, and purchase arrays), can update up to 75 users each (max of 225 individual users). Each update can also belong to the same user for a max of 225 updates to a single user in a request. Please see our page on API limits for details, and reach out to your Customer Success Manager if you need your limit increased.

Please note that Braze processes the data passed via API at face value and customers should only pass deltas (changing data) to minimize unnecessary data point consumption. To read more, check out our data point [documentation]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#data-points). 

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/User%20Data/User%20track%20%E2%80%93%20attributes%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

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
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object),
}
```

Customers using the API for server-to-server calls may need to whitelist `rest.iad-01.braze.com` if they're behind a firewall.

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array of Attributes Object | See User Attributes Object |
| `events` | Optional | Array of Event Object | See Events Objects |
| `purchases` | Optional | Array of Purchase Object | See Purchase Object |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
Note that for each of the request components listed below, one of `external_id`, `user_alias`, or `braze_id` is __required__.
- [User Attributes Object]({{site.baseurl}}/api/objects_filters/user_attributes_object/)
- [Events Object]({{site.baseurl}}/api/objects_filters/event_object/)
- [Purchases Object]({{site.baseurl}}/api/objects_filters/purchase_object/)

{% alert note %}
- When creating alias-only users through this endpoint, you must explicitly set the `_update_existing_only` flag to `false`.
<br><br>
- Updating the subscription status with this endpoint will not only update the user specified by their external_id (e.g User 123), but it will also update the subscription status of any users with the same email as that user (User 123).
{% endalert %}

### Example Request Body for Event Tracking

```json
{
  "events": [
    {
      "external_id": "string",
      "name": "string",
      "time": "string"
    }
  ]
}
```

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [ 
    {
      "external_id": "user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
  ],
  "events": [
    {
      "external_id": "user_id",
      "app_id" : "app_identifier",
      "name": "watched_trailer",
      "time": "2013-07-16T19:20:30+1:00"
    }  
  ],
  "purchases": [
    {
      "external_id": "user_id",
      "app_id": "app_identifier",
      "product_id": "product_name",
      "currency": "USD",
      "price": 12.12,
      "quantity": 6,
      "time": "2017-05-12T18:47:12Z",
      "properties": {
         "integer_property": 3,
         "string_property": "Russell",
         "date_property": "2014-02-02T00:00:00Z"
       } 
     }
  ],
}'
```

### User Track Responses

Upon using any of the aforementioned API requests you should receive one of the following three general responses:

#### Successful Message

Successful messages will be met with the following response:

```json
{
  "message" : "success",
  "attributes_processed" : (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed" : (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,,
  "purchases_processed" : (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,,
}
```

#### Successful Message with Non-Fatal Errors

If your message is successful but has non-fatal errors such as one invalid Event Object out of a long list of events you will receive the following response:

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

During times of maintenance, Braze might pause the real-time processing of the API. In these situations, the server will return an HTTP Accepted 202 response code and the following body, which indicates that we have received and queued the API call but have not immediately processed it. All scheduled maintenance will be posted to [http://status.braze.com](http://status.braze.com) ahead of time.

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
{: .reset-td-br-1 .reset-td-br-2}


###  Importing Legacy User Data

You may submit data through the Braze API for a user who has not yet used your mobile app in order to generate a user profile. If the user subsequently uses the application all information following their identification via the SDK will be merged with the existing user profile you created via the API call. Any user behavior that is recorded anonymously by the SDK prior to identification will be lost upon merging with the existing API generated user profile.

The segmentation tool will include these users regardless of whether they have engaged with the app. If you want to exclude users uploaded via the User API who have not yet engaged with the app you should add the filter -- `Session Count > 0`.

{% endapi %}

