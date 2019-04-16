---
nav_title: User Data
page_order: 1
search_rank: 5
---
# User Data

The User API allows you to track information on your users by logging data about your users that comes from outside your mobile app. You can also use this API to delete users for testing or other purposes.

All API endpoints have a data payload limit of 4MB. Attempts to post more data than 4MB will fail with an HTTP 413 Request Entity Too Large.

The examples below contain the URL https://rest.iad-01.braze.com, but some customers will need to use a different endpoint URL, for example if you are hosted in Braze's EU data center or have a dedicated Braze installation. Your Success Manager will inform you if you should use a different endpoint URL.

## User Track Endpoint

This endpoint can be used to record custom events, user attributes, and purchases for users. You can include up to 75 Attributes, Event, and Purchase Objects per request. That is, you can only post attributes for up to 75 users at a time, but in the same API call you can also provide up to 75 events and up to 75 purchases.

Your Endpoint will correspond to your [Braze Instance][1].

Instance  | REST Endpoint
----------|----------------------------------------------
US-01  | `https://rest.iad-01.braze.com/users/track`
US-02  | `https://rest.iad-02.braze.com/users/track`
US-03  | `https://rest.iad-03.braze.com/users/track`
US-04  | `https://rest.iad-04.braze.com/users/track`
US-06  | `https://rest.iad-06.braze.com/users/track`
EU-01  | `https://rest.fra-01.braze.eu/users/track`

### User Track Request

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
{
   "api_key" : (required, string) see App Group REST API Key,
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}
```

>  Customers using the API for server-to-server calls may need to whitelist `rest.iad-01.braze.com` if they're behind a firewall.

###  User Attributes Object Specification

An API request with any fields in the Attributes Object will create or update an attribute of that name with the given value on the specified user profile. Use Braze User Profile Field names (listed below or any listed in the [User Profile Fields chart][27]) to update those special values on the user profile in the dashboard or add your own custom attribute data to the user.

```json
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID below,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note below regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

To remove a profile attribute, set it to null. Some fields, such as `external_id` and `user_alias` cannot be removed once added to a user profile.

#### Push Token Import
When importing push tokens from other systems, an `external_id` is not always available. To maintain communication with these users during your transition to Braze, you can import the legacy tokens for anonymous users without providing `external_id` by specifying this parameter.

When specifying `push_token_import` as `true`:

* `external_id` and `braze_id` should __not__ be specified
* The attribute object must contain a push token
* If the token already exists in Braze, the request is ignored; otherwise, Braze will create a temporary, anonymous user profile for each token to enable you to continue to message these individuals

After import, as each user launches the Braze-enabled version of your app, Braze will automatically move their imported push token to their Braze user profile and clean up the temporary profile.

#### Custom Attribute Data Types

The following data types can be stored as a custom attribute:

- Dates (Must be stored in the [ISO 8601][19] format or in the `yyyy-MM-dd'T'HH:mm:ss.SSSZ` format)
  - Date attributes without a timezone will default to Midnight UTC (and will be formatted on the dashboard as the equivalent of Midnight UTC in the company's timezone)
  - Events and Attributes with timestamps in the future will default to the current time
- Strings
- Floats
- Booleans
- Integers
  - Integer custom attributes may be incremented by positive or negative integers by assigning them an object with the field "inc" and the value by which you would like to increment them.
    - Example: `"my_custom_attribute_2" : {"inc" : int_value},`
- Arrays
  - In addition to setting the values of an array by saying something like `"my_array_custom_attribute":[ "Value1", "Value2" ]` you may add to existing arrays by doing something like `"my_array_custom_attribute" : { "add" : ["Value3"] },` or remove values from an array by doing something like `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`
  - The maximum number of elements in Custom Attribute Arrays defaults to 25. The maximum for individual arrays can be increased to up to 100 in the Braze Dashboard, under "Manage App Group -> Custom Attributes". Arrays exceeding the maximum number of elements will be truncated to contain the maximum number of elements. For more information on Custom Attribute Arrays and their behavior, see our [Documentation on Arrays][6].

For information regarding when you should use a Custom Event vs a Custom Attribute, see our [Best Practices - User Data Collection][15] documentation.

#### Braze User Profile Fields

| User Profile Field | Data Type Specification |
| ---| --- |
| bio | (string) |
| country | (string) We require that country codes be passed to Braze in the [ISO-3166-1 alpha-2 standard][17]. |
| current_location | (object) Of the form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (date at which the user first used the app) String in ISO 8601 format or in `yyyy-MM-dd'T'HH:mm:ss.SSSZ` format. |
| date_of_last_session | (date at which the user last used the app) String in ISO 8601 format or in `yyyy-MM-dd'T'HH:mm:ss.SSSZ` format. |
| dob | (date of birth) String in format "YYYY-MM-DD", e.g., 1980-12-21. |
| email | (string) |
| email_subscribe | (string) Available values are "opted_in" (explicitly registered to receive email messages), "unsubscribed" (explicitly opted out of email messages), and "subscribed" (neither opted in nor out).  |
| external_id | (string) Of the unique user identifier. |
| facebook | hash containing any of `id` (string), `likes` (array of strings), `num_friends` (integer). |
| first_name | (string) |
| gender | (string) "M", "F", "O" (other), "N" (not applicable), "P" (prefer not to say) or nil (unknown). |
| home_city | (string) |
| image_url | (string) URL of image to be associated with user profile. |
| language | (string) we require that language be passed to Braze in the [ISO-639-1 standard][24]. |
| last_name | (string) |
|marked_email_as_spam_at| (string) Date at which the user's email was marked as spam. Appears in ISO 8601 format or in yyyy-MM-dd'T'HH:mm:ss.SSSZ format.|
| phone | (string) |
| push_subscribe | (string) Available values are "opted_in" (explicitly registered to receive push messages), "unsubscribed" (explicitly opted out of push messages), and "subscribed" (neither opted in nor out).  |
| push_tokens | Array of objects with `app_id` and `token` string. You may optionally provide a `device_id` for the device this token is associated with, e.g., `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. If a `device_id` is not provided, one will be randomly generated. |
| time_zone | (string) Of time zone name from [IANA Time Zone Database][26] (e.g., "America/New_York" or "Eastern Time (US & Canada)"). Only valid time zone values will be set. |
| twitter | Hash containing any of `id` (integer), `screen_name` (string, Twitter handle), `followers_count` (integer), `friends_count` (integer), `statuses_count` (integer). |

Language values that are explicitly set via this API will take precedence over the locale information Braze automatically receives from the device.

####  User Attribute Example Request

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
{
  "api_key" : "your App Group REST API Key",
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Jon",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Jill",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": App Identifier, "token": "abcd"}]
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Alice",
      "has_profile_picture" : false,
    }
  ]
}
```

This example contains two User Attribute objects of the allowed 75 per API call.

### Event Object Specification

```json
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID below,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  "app_id" : (optional, string) see App Identifier below,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss.SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

Each Event Object in the _events_ array represents a single occurrence of a Custom Event by a particular user at the designated time value.

- [ISO 8601 Time Code Wiki][19]

For information regarding when you should use a Custom Event vs a Custom Attribute, see our [Best Practices - User Data Collection][15] documentation.

#### Event Example Request

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
{
  "api_key" : "your App Group REST API Key",
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00"
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```


###  Purchase Object Specification

```json
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID below,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  "app_id" : (optional, string) see App Identifier below,
  "product_id" : (required, string) identifier for the purchase, e.g. Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  "price" : (required, float) value in the base currency unit (e.g. Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```
Each Purchase Object in the _purchases_ array represents a single purchase by a particular user at a particular time.

- [ISO 4217 Currency Code Wiki][20]


#### Purchase Example Request

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
{
  "api_key" : "your App Group REST API Key",
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### Properties Object

Custom events and purchases may have event properties. The "properties" values should be an Object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs. Property values can be integers, floats, booleans, datetimes (as strings in ISO8601 or in `yyyy-MM-dd'T'HH:mm:ss.SSSZ` format), or strings less than or equal to 255 characters.

### User Track Responses

Upon using any of the aforementioned API requests you should receive one of the following three general responses:

#### Successful Message

Successful messages will be met with the following response:

```json
{
  "message" : "success",
  "attributes_processed" : <if attributes are included in the request, this will return an integer of the number of attributes that were processed>,
  "events_processed" : <if events are included in the request, this will return an integer of the number of events that were processed>,
  "purchases_processed" : <if purchases are included in the request, this will return an integer of the number of purchases that were processed>,
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
| 400 Bad Request | Bad Syntax |
| 401 Unauthorized | Unknown or missing REST API Key |
| 404 Not Found | Unknown REST API Key (if provided) |
| 429 Rate Limited | Over rate limit |
| 5XX | Internal server error, you should retry with exponential backoff |


###  Importing Legacy User Data

You may submit data through the Braze API for a user who has not yet used your mobile app in order to generate a user profile. If the user subsequently uses the application all information following their identification via the SDK will be merged with the existing user profile you created via the API call. Any user behavior that is recorded anonymously by the SDK prior to identification will be lost upon merging with the existing API generated user profile.

The segmentation tool will include these users regardless of whether they have engaged with the app. If you want to exclude users uploaded via the User API whom have not yet engaged with the app you should add the filter -- Session Count > 0.

## User Delete Endpoint

{% alert warning %}
Deleting user profiles CANNOT be undone. It will PERMANENTLY remove users which may cause discrepancies in your data.
{% endalert %}

This endpoint allows you to delete any user profile by specifying their external identifier (User ID). Up to 50 `external_ids` or `braze_ids` can be included in a single request. Only one of `external_ids` or `braze_ids` can be included in a single request. Please note that their associated event data will still exist in the dashboard after you delete the user.

Your Endpoint will correspond to your [Braze Instance][1].

Instance  | REST Endpoint
----------|-----------------------------------------------
US-01  | `https://rest.iad-01.braze.com/users/delete`
US-02  | `https://rest.iad-02.braze.com/users/delete`
US-03  | `https://rest.iad-03.braze.com/users/delete`
US-04  | `https://rest.iad-04.braze.com/users/delete`
US-06  | `https://rest.iad-06.braze.com/users/delete`
EU-01  | `https://rest.fra-01.braze.eu/users/delete`


### User Delete Request

```json
POST https://YOUR_REST_API_URL/users/delete
Content-Type: application/json
{
  "api_key" : (required, string) App Group REST API Key,
  "external_ids" : (optional, array of string) external ids for the users to delete,
  "braze_ids" : (optional, array of string) Braze User Identifiers for the users to delete
}
```

### Users Delete Response

```json
Content-Type: application/json
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```

## New User Alias Endpoint

Use this endpoint to create new user aliases for existing identified users. You can add up to 50 user aliases per request.

Your Endpoint will correspond to your [Braze Instance][1].

Instance  | REST Endpoint
----------|----------------------------------------------
US-01  | `https://rest.iad-01.braze.com/users/alias/new`
US-02  | `https://rest.iad-02.braze.com/users/alias/new`
US-03  | `https://rest.iad-03.braze.com/users/alias/new`
US-04  | `https://rest.iad-04.braze.com/users/alias/new`
US-06  | `https://rest.iad-06.braze.com/users/alias/new`
EU-01  | `https://rest.fra-01.braze.eu/users/alias/new`

### New User Alias Request

```json
POST https://YOUR_REST_API_URL/users/alias/new
Content-Type: application/json
{
   "api_key" : (required, string) see App Group REST API Key,
   "user_aliases" : (required, array of New User Alias Object)
}
```

###  New User Alias Object Specification

```json
{
  "external_id" : (required, string) see External User ID below,
  // external_ids for users that do not exist will return a non-fatal error. See Server Responses for details.
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

For more information on `alias_name` and `alias_label`, check out our [User Aliases documentation]({{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

[1]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints
[6]: {{ site.baseurl }}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/overview/#user-data-collection
[16]: #not-used-app
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1 codes"
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"
[20]: http://en.wikipedia.org/wiki/ISO_4217 "ISO 4217 Currency Code"
[21]: http://docs.python-requests.org/en/latest/ "Requests"
[22]: https://rubygems.org/gems/multi_json "multiJSON"
[23]: https://rubygems.org/gems/rest-client "Rest Client"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1 codes"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#braze-user-profile-fields
