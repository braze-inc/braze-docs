---
nav_title: "User attributes object"
article_title: API User Attributes Object
page_order: 11
page_type: reference
description: "This reference article explains the different components of the user attributes object."

---

# User attributes object

> An API request with any fields in the attributes object creates or updates an attribute of that name with the given value on the specified user profile.

Use Braze user profile field names (listed as follows or any listed in the section for [Braze user profile fields](#braze-user-profile-fields)) to update those special values on the user profile in the dashboard or add your own custom attribute data to the user.

## Object body

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
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

- [External user ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [User aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

To remove a profile attribute, set it to `null`. Some fields, such as `external_id` and `user_alias` cannot be removed after they're added to a user profile.

#### Update existing profiles only

If you wish to update only existing user profiles in Braze, you should pass the `_update_existing_only` key with a value of `true` within the body of your request. If this value is omitted, Braze creates a new user profile if the `external_id` does not already exist.

{% alert note %}
If you are creating an alias-only user profile through the `/users/track` endpoint, you must set `_update_existing_only` to `false`. If you omit this value, Braze does not create the alias-only profile.
{% endalert %}

#### Push token import

Before you import push tokens to Braze, double check if you need to. When the Braze SDKs are put in place, they handle push tokens automatically with no need to upload them through the API.

If you do find you need to upload them through the API, they can either be uploaded for identified users or anonymous users. This means that either an `external_id` needs to present, or the anonymous users must have the `push_token_import` flag set to `true`.

{% alert note %}
When importing push tokens from other systems, an `external_id` is not always available. To maintain communication with these users during your transition to Braze, you can import the legacy tokens for anonymous users without providing `external_id` by specifying `push_token_import` as `true`.
{% endalert %}

When specifying `push_token_import` as `true`:

* `external_id` and `braze_id` should **not** be specified
* The attribute object **must** contain a push token
* If the token already exists in Braze, the request is ignored; otherwise, Braze creates a temporary, anonymous user profile for each token to enable you to continue to message these individuals

After import, as each user launches the Braze-enabled version of your app, Braze automatically moves their imported push token to their Braze user profile and cleans up the temporary profile.

Braze checks once a month to find any anonymous profile with the `push_token_import` flag that doesn't have a push token. If the anonymous profile no longer has a push token, Braze deletes the profile. However, if the anonymous profile still has a push token, suggesting that the actual user has yet to login to the device with said push token, Braze does nothing.

For more information, refer to [Migrating push tokens](#migrating-push-tokens).

#### Custom attribute data types

The following data types can be stored as a custom attribute:

| Data Type | Notes |
| --- | --- |
| Arrays | Custom attribute arrays are supported. Adding an element to a custom attribute array appends the element to the end of the array, unless it's already present, in which case it gets moved from its current position to the end of the array.<br><br>For example, if the array `['hotdog','hotdog','hotdog','pizza']` was imported, it shows in the array attribute as `['hotdog', 'pizza']` because only unique values are supported.<br><br>In addition to setting the values of an array by saying something like `"my_array_custom_attribute":[ "Value1", "Value2" ]`, you may add to existing arrays by doing something like `"my_array_custom_attribute" : { "add" : ["Value3"] },` or remove values from an array by doing something like `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>The maximum number of elements in custom attribute arrays defaults to 25, but can be increased up to 100 for an individual array. For more information, see [Arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays). |
| Array of objects | Array of objects allows you to define a list of objects where each object contains a set of attributes. This can be useful if you need to store multiple sets of related data for a user, such as hotel stays, purchase history, or preferences. <br><br> For example, you can define a custom attribute on a user profile named `hotel_stays`. This custom attribute can be defined as an array where each object represents a separate stay, with attributes such as `hotel_name`, `check_in_date`, `nights_stayed`. For more details, see [this example](#array-of-objects-example). |
| Booleans | `true` or `false` |
| Dates | Must be stored in the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format or in any of the following formats: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Note that "T" is a time designator, not a placeholder, and should not be changed or removed. <br><br>Time attributes without a time zone default to Midnight UTC (and are formatted on the dashboard as the equivalent of Midnight UTC in the company's time zone). <br><br> Events with timestamps in the future default to the current time. <br><br> For regular custom attributes, if the year is less than 0 or greater than 3000, Braze stores these values as strings on the user. |
| Floats | Float custom attributes are positive or negative numbers with a decimal point. For example, you can use floats to store account balances or user ratings for products or services. |
| Integers | Integer custom attributes may be incremented by positive or negative integers by assigning them an object with the field "inc" and the value by which you want to increment them. <br><br>Example: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Nested custom attributes | Nested custom attributes define a set of attributes as a property of another attribute. When you define a custom attribute object, you define a set of additional attributes for that object. For more information, refer to [Nested custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/). |
| Strings | String custom attributes are sequences of characters used to store text data. For example, you can use strings to store first and last names, email addresses, or preferences. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
For information on when you should use a custom event versus a custom attribute, see our respective documentation on [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) and [custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).
{% endalert %}

##### Array of objects example

This array of objects allows you to create segments based on specific criteria within the stays, and personalize your messages using the data from each stay with Liquid templates.

```json
"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
  ]
```

#### Braze user profile fields {#braze-user-profile-fields}

{% alert important %}
The following user profile fields are case sensitive, so be sure to reference these fields in lower case.
{% endalert %}

| User Profile Field | Data Type Specification |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | (string, optional) When a user profile is recognized by the SDK, an anonymous user profile is created with an associated `braze_id`. The `braze_id` is automatically assigned by Braze, cannot be edited, and is device-specific. |
| country | (string) We require that country codes be passed to Braze in the [ISO-3166-1 alpha-2 standard](http://en.wikipedia.org/wiki/ISO_3166-1). Our API makes a best effort to map countries received in different formats. For example, "Australia" may map to "AU". However, if the input doesn't match a given [ISO-3166-1 alpha-2 standard](http://en.wikipedia.org/wiki/ISO_3166-1), the country value is set to `NULL`. <br><br>Setting `country` on a user by CSV import or API prevents Braze from automatically capturing this information through the SDK. |
| current_location | (object) Of the form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (date at which the user first used the app) String in ISO 8601 format or in any of the following formats: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (date at which the user last used the app) String in ISO 8601 format or in any of the following formats: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (date of birth) String in format "YYYY-MM-DD", for example, 1980-12-21. |
| email | (string) |
| email_subscribe | (string) Available values are "opted_in" (explicitly registered to receive email messages), "unsubscribed" (explicitly opted out of email messages), and "subscribed" (neither opted in nor out).  |
| email_open_tracking_disabled |(boolean) `true` or `false` accepted. Set to `true` to disable the open tracking pixel from being added to all future emails sent to this user. Available for SparkPost and SendGrid only.|
| email_click_tracking_disabled |(boolean) `true` or `false` accepted. Set to `true` to disable the click tracking for all links within a future email, sent to this user. Available for SparkPost and SendGrid only.|
| external_id | (string) A unique identifier for a user profile. After assigned an `external_id`, Braze identifies the user profile across a user's devices. On the first instance of assigning an external_id to an unknown user profile, Braze migrates all existing user profile data to the new user profile. |
| facebook | hash containing any of `id` (string), `likes` (array of strings), `num_friends` (integer). |
| first_name | (string) |
| gender | (string) "M", "F", "O" (other), "N" (not applicable), "P" (prefer not to say) or nil (unknown). |
| home_city | (string) |
| language | (string) we require that language be passed to Braze in the [ISO-639-1 standard](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). For supported languages, see our [list of accepted languages]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/).<br><br>Setting `language` on a user by CSV import or API prevents Braze from automatically capturing this information through the SDK. |
| last_name | (string) |
| marked_email_as_spam_at | (string) Date at which the user's email was marked as spam. Appears in ISO 8601 format or in any of the following formats: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (string) We recommend providing phone numbers in the [E.164](https://en.wikipedia.org/wiki/E.164) format. For details, refer to [User phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | (string) Available values are "opted_in" (explicitly registered to receive push messages), "unsubscribed" (explicitly opted out of push messages), and "subscribed" (neither opted in nor out).  |
| push_tokens | Array of objects with `app_id` and `token` string. You may optionally provide a `device_id` for the device this token is associated with, for example, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. If a `device_id` is not provided, one is randomly generated. |
| subscription_groups| Array of objects with `subscription_group_id` and `subscription_state` string, for example, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Available values for `subscription_state` are "subscribed" and "unsubscribed".|
| time_zone | (string) Of time zone name from [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (for example, "America/New_York" or "Eastern Time (US & Canada)"). Only valid time zone values are set. |
| twitter | Hash containing any of `id` (integer), `screen_name` (string, X (formerly Twitter) handle), `followers_count` (integer), `friends_count` (integer), `statuses_count` (integer). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Language values that are explicitly set through this API take precedence over the locale information Braze automatically receives from the device.

####  User attribute example request

This example contains four user attribute objects, out of a total of 75 allowed attribute objects per API call.

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

## Migrating push tokens

If you were sending push notifications prior to integrating Braze, either on your own or through another provider, push token migration allows you to continue sending push notifications to your users with registered push tokens.

### Automatic migration through SDK

After you [integrate the Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/), push tokens for your opted-in users are automatically migrated the next time they open your app. Until then, you can't send those users push notifications through Braze.

Alternatively, you can [migrate your push tokens manually](#manual-migration-via-api), allowing you to re-engage your users more promptly.

#### Web token considerations

Due to the nature of web push tokens, be sure you consider the following when implementing push for web:

|Consideration|Details|
|----------------------|------------|
| **Service workers**  | By default, the Web SDK looks for a service worker at `./service-worker` unless another option is specified, such as `manageServiceWorkerExternally` or `serviceWorkerLocation`. If your service worker isn't set up properly, it may lead to expired push tokens for your users. |
| **Expired tokens**   | If a user hasn't started a web session within 60 days, their push token expires. Because Braze can't migrate expired push tokens, you must send a [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) to re-engage them. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Manual migration through API

Manual push token migration is the process of importing these previously-created keys into your Braze platform through the API.

Programmatically migrate iOS (APNs) and Android (FCM) tokens to your platform by using the [`users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). You can migrate both identified users (users with an associated external ID) and anonymous users (users without an external ID).

Specify your app's `app_id` during push token migration to associate the appropriate push token with the appropriate app. Each app (iOS, Android, etc.) has its own `app_id`, which can be found in the **Identification** section of the [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) page. Be sure to use the correct platform's `app_id`.

{% alert important %}
It is not possible to migrate web push tokens through the API. This is because web push tokens do not conform to the same schema as other platforms.

<br>If you are attempting to migrate web push tokens programmatically, you might see an error like the following: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
As an alternative to API migration, we recommend that you integrate the SDK and allow your token base to repopulate naturally.
{% endalert %}

{% tabs local %}
{% tab External ID present %}
For identified users, set the `push_token_import` flag to `false` (or omit the parameter) and specify the `external_id`, `app_id`, and `token` values in the user `attributes` object.

For example:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab External ID missing %}
When importing push tokens from other systems, an `external_id` is not always available. In this circumstance, set your `push_token_import` flag as `true` and specify the `app_id` and `token` values. Braze creates a temporary, anonymous user profile for each token to enable you to continue to message these individuals. If the token already exists in Braze, the request is ignored.

For example:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

After import, when the anonymous user launches the Braze-enabled version of your app, Braze automatically moves their imported push token to their Braze user profile and cleans up the temporary profile.

Braze checks once a month to find any anonymous profile with the `push_token_import` flag that doesn't have a push token. If the anonymous profile no longer has a push token, Braze deletes the profile. However, if the anonymous profile still has a push token, suggesting that the actual user has yet to log in to the device with said push token, Braze does nothing.
{% endtab %}
{% endtabs %}

### Importing Android push tokens

{% alert important %}
The following consideration applies only for Android apps. iOS apps do not require these steps because that platform has only one framework for displaying push, and push notifications render immediately as long as Braze has the necessary push tokens and certificates.
{% endalert %}

If you must send Android push notifications to your users before the Braze SDK integration is complete, use key-value pairs to validate push notifications.

You must have a receiver to handle and display push payloads. To notify the receiver of the push payload, add the necessary key-value pairs to the push campaign. The values of these pairs are contingent on the specific push partner you used before Braze.

{% alert note %}
For some push notification providers, Braze needs to flatten the key-value pairs so that they can be properly interpreted. To flatten key-value pairs for a specific Android app, contact your customer success manager.
{% endalert %}