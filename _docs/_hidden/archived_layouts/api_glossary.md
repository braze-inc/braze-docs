---
title: API or Code Glossary
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "This is the Google Search description. Characters past 160 get truncated, keep it brief."
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 Create Email Template
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Post,Email,Create,Template,REST,API
{% endapitags %}

Use the email Template REST APIs to programmatically manager the email templates that you stored on the Braze dashboards, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

The response from this endpoint includes a field for `email_template_id`, which can be used to update the template in subsequent API calls.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### REQUEST BODY
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### EXAMPLE RESPONSE
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### PARAMETER DETAILS

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `modified_after`  | No | String in ISO 8601 | Retrieve only templates updated at or after the given time. |
| `modified_before`  |  No | String in ISO 8601 | Retrieve only templates updated at or before the given time. |
| `limit` | No | Positive Number | Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000. |
| `offset`  |  No | Positive Number | Number of templates to skip before returning rest of the templates that fit the search criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


{% endapi %}
{% api %}
## 2 List Available Email Template
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
Get,Email,Template,List,REST
{% endapitags %}

Use the following endpoints to get a list of available templates.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### REQUEST BODY
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### EXAMPLE RESPONSE
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### PARAMETER DETAILS

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `email_template_id`  | Yes | String | Your email template's API Identifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 3 Campaigns Trigger Send
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}Post, Campaigns, Trigger,Send{% endapitags %}

API-Triggered Delivery allows you to house message content inside of the Braze dashboard, while dictating when a message is sent, and to whom via your API. 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### REQUEST BODY
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### EXAMPLE RESPONSE
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "context": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "context": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent context)
    },
    ...
  ]
}
```


#### PARAMETER DETAILS

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `email_template_id`  | Yes | String | Your email template's API Identifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 4 Campaigns Trigger Send
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, Campaigns, Trigger, Send{% endapitags %}

This endpoint can be used to record custom events, user attributes, and purchases for users. You can include up to 75 Attributes, Event, and Purchase Objects per request. That is, you can only post attributes for up to 75 users at a time, but in the same API call you can also provide up to 75 events and up to 75 purchases.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### REQUEST BODY
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### EXAMPLE RESPONSE
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
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

#### PARAMETER DETAILS

| User Profile Field | Data Type Specification |
| ---| --- |
| country | (string) We require that country codes be passed to Braze in the [ISO-3166-1 alpha-2 standard][17]. |
| current_location | (object) Of the form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (date at which the user first used the app) String in ISO 8601 format or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. |
| date_of_last_session | (date at which the user last used the app) String in ISO 8601 format or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. |
| dob | (date of birth) String in format "YYYY-MM-DD", for example, 1980-12-21. |
| email | (string) |
| email_subscribe | (string) Available values are "opted_in" (explicitly registered to receive email messages), "unsubscribed" (explicitly opted out of email messages), and "subscribed" (neither opted in nor out).  |
| external_id | (string) Of the unique user identifier. |
| facebook | hash containing any of `id` (string), `likes` (array of strings), `num_friends` (integer). |
| first_name | (string) |
| gender | (string) "M", "F", "O" (other), "N" (not applicable), "P" (prefer not to say) or nil (unknown). |
| home_city | (string) |
| image_url | (string) URL of image to be associated with user profile. |
| language | (string) we require that language be passed to Braze in the [ISO-639-1 standard][24]. <br>[List of accepted Languages](/docs/user_guide/data_and_analytics/user_data_collection/language_codes/)|
| last_name | (string) |
|marked_email_as_spam_at| (string) Date at which the user's email was marked as spam. Appears in ISO 8601 format or in yyyy-MM-dd'T'HH:mm:ss:SSSZ format.|
| phone | (string) |
| push_subscribe | (string) Available values are "opted_in" (explicitly registered to receive push messages), "unsubscribed" (explicitly opted out of push messages), and "subscribed" (neither opted in nor out).  |
| push_tokens | Array of objects with `app_id` and `token` string. You may optionally provide a `device_id` for the device this token is associated with, for example, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. If a `device_id` is not provided, one will be randomly generated. |
| time_zone | (string) Of time zone name from [IANA Time Zone Database][26] (for example, "America/New_York" or "Eastern Time (US & Canada)"). Only valid time zone values will be set. |
| twitter | Hash containing any of `id` (integer), `screen_name` (string, X (formerly Twitter) handle), `followers_count` (integer), `friends_count` (integer), `statuses_count` (integer). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
