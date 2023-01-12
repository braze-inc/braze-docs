---
nav_title: "User Attributes Object"
article_title: API User Attributes Object
page_order: 11
page_type: reference
description: "This article explains the different components of the User Alias object."

---

# User attributes object specification

An API request with any fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile. Use Braze user profile field names (listed as follows or any listed in the section for [Braze user profile fields][27]) to update those special values on the user profile in the dashboard or add your own custom attribute data to the user.

```json
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
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

To remove a profile attribute, set it to `null`. Some fields, such as `external_id` and `user_alias` cannot be removed once added to a user profile.

#### Update existing profiles only

If you wish to update only existing user profiles in Braze, you should pass the `_update_existing_only` key with a value of `true` within the body of your request. If this value is omitted, Braze will create a new user profile if the `external_id` does not already exist.

{% alert note %}
If you are creating an alias-only user profile via the users/track endpoint, `_update_existing_only` must be set to `false`. If this value is omitted, the alias-only profile will not be created.
{% endalert %}

#### Push token import

Before you import push tokens to Braze, double check if you need to. When the Braze SDKs are put in place, they handle push tokens automatically with no need to upload them via the API.

If you do find you need to upload them via the API, they can either be uploaded for identified users or anonymous users. This means that either an `external_id` needs to present, or the anonymous users must have the `push_token_import` flag set to `true`. 

{% alert note %}
When importing push tokens from other systems, an `external_id` is not always available. To maintain communication with these users during your transition to Braze, you can import the legacy tokens for anonymous users without providing `external_id` by specifying `push_token_import` as `true`.
{% endalert %}

When specifying `push_token_import` as `true`:

* `external_id` and `braze_id` should **not** be specified
* The attribute object **must** contain a push token
* If the token already exists in Braze, the request is ignored; otherwise, Braze will create a temporary, anonymous user profile for each token to enable you to continue to message these individuals

After import, as each user launches the Braze-enabled version of your app, Braze will automatically move their imported push token to their Braze user profile and clean up the temporary profile.

Braze will check once a month to find any anonymous profile with the `push_token_import` flag that doesn’t have a push token. If the anonymous profile no longer has a push token, we will delete the profile. However, if the anonymous profile still has a push token, suggesting that the actual user has yet to login to the device with said push token, we will do nothing.

For more information, refer to [Migrating push tokens][3].

#### Custom attribute data types

The following data types can be stored as a custom attribute:

| Data Type | Notes |
| --- | --- |
| Arrays | Custom attribute arrays are one-dimensional sets; multi-dimensional arrays are not supported. Adding an element to a custom attribute array appends the element to the end of the array, unless it's already present, in which case it gets moved from its current position to the end of the array.<br><br>For example, if an array `['hotdog','hotdog','hotdog','pizza']` were imported, it will show in the array attribute as `['hotdog', 'pizza']` because only unique values are supported.<br><br>In addition to setting the values of an array by saying something like `"my_array_custom_attribute":[ "Value1", "Value2" ]` you may add to existing arrays by doing something like `"my_array_custom_attribute" : { "add" : ["Value3"] },` or remove values from an array by doing something like `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>The maximum number of elements in custom attribute arrays defaults to 25, but can be increased upon request. For more information, see [Arrays][6]. |
| Booleans |  |
| Dates | Must be stored in the [ISO 8601][19] format or in any of the following formats: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Note that "T" is a time designator, not a placeholder, and should not be changed or removed. <br><br>Time attributes without a time zone will default to Midnight UTC (and will be formatted on the dashboard as the equivalent of Midnight UTC in the company's time zone). <br><br> Events with timestamps in the future will default to the current time. |
| Floats |  |
| Integers | Integer custom attributes may be incremented by positive or negative integers by assigning them an object with the field "inc" and the value by which you would like to increment them. <br><br>Example: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Strings |  |
{: .reset-td-br-1 .reset-td-br-2}

For information regarding when you should use a custom event versus a custom attribute, see our respective documentation on [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) and [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).

#### Braze user profile fields {#braze-user-profile-fields}

{% alert important %} 
The following user profile fields are case sensitive, so be sure to reference these fields in lower case.
{% endalert %}

| User Profile Field | Data Type Specification |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | (string, optional) When a user profile is recognized via the SDK, an anonymous user profile is created with an associated `braze_id`. The `braze_id` is automatically assigned by Braze, cannot be edited, and is device-specific. | 
| country | (string) We require that country codes be passed to Braze in the [ISO-3166-1 alpha-2 standard][17]. |
| current_location | (object) Of the form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (date at which the user first used the app) String in ISO 8601 format or in any of the following formats: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (date at which the user last used the app) String in ISO 8601 format or in any of the following formats: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (date of birth) String in format "YYYY-MM-DD", e.g., 1980-12-21. |
| email | (string) |
| email_subscribe | (string) Available values are "opted_in" (explicitly registered to receive email messages), "unsubscribed" (explicitly opted out of email messages), and "subscribed" (neither opted in nor out).  |
| email_open_tracking_disabled |(boolean) true or false accepted.  Set to true to disable the open tracking pixel from being added to all future emails sent to this user.|
| email_click_tracking_disabled |(boolean) true or false accepted.  Set to true to disable the click tracking for all links within a future email, sent to this user.|
| external_id | (string) A unique identifier for a user profile. Once assigned an `external_id`, the user profile is identified across a user's devices. On the first instance of assigning an external_id to an unknown user profile, all existing user profile data will be migrated to the new user profile. |
| facebook | hash containing any of `id` (string), `likes` (array of strings), `num_friends` (integer). |
| first_name | (string) |
| gender | (string) "M", "F", "O" (other), "N" (not applicable), "P" (prefer not to say) or nil (unknown). |
| home_city | (string) |
| language | (string) we require that language be passed to Braze in the [ISO-639-1 standard][24]. For supported languages, see our [list of accepted languages][2]. |
| last_name | (string) |
| marked_email_as_spam_at | (string) Date at which the user's email was marked as spam. Appears in ISO 8601 format or in any of the following formats: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (string) |
| push_subscribe | (string) Available values are "opted_in" (explicitly registered to receive push messages), "unsubscribed" (explicitly opted out of push messages), and "subscribed" (neither opted in nor out).  |
| push_tokens | Array of objects with `app_id` and `token` string. You may optionally provide a `device_id` for the device this token is associated with, e.g., `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. If a `device_id` is not provided, one will be randomly generated. |
| subscription_groups| Array of objects with `subscription_group_id` and `subscription_state` string, e.g. `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Available values for `subscription_state` are "subscribed" and "unsubscribed".|
| time_zone | (string) Of time zone name from [IANA Time Zone Database][26] (e.g., "America/New_York" or "Eastern Time (US & Canada)"). Only valid time zone values will be set. |
| twitter | Hash containing any of `id` (integer), `screen_name` (string, Twitter handle), `followers_count` (integer), `friends_count` (integer), `statuses_count` (integer). |
{: .reset-td-br-1 .reset-td-br-2}

Language values that are explicitly set via this API will take precedence over the locale information Braze automatically receives from the device.

####  User attribute example request

This example contains two user attribute objects with the allowed 75 requests per API call.

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
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
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Alice",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

[2]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[3]: {{site.baseurl}}/help/help_articles/push/push_token_migration/
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1 codes"
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1 codes"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: #braze-user-profile-fields
