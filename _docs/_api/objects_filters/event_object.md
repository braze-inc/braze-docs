---
nav_title: "Event Object"
page_order: 6

page_type: reference

channel: Push
platform:
  - API
tool:
  - Campaigns
  - Canvas

description: "This reference article goes over the event object, what it is, and how it's a crucial part of event-based campaign strategies."
---

# Event Object Specification

> This article explains the different components of an event object, how you can use this object, and examples to draw from.

## What is the Event Object?

An Event Object is an object that gets passed through the API when a specific event occurs. Events objects are housed in an events array. Each Event Object in the events array represents a single occurrence of a Custom Event by a particular user at the designated time value. The event object has many different fields that allow you to customize by setting and using event properties in messages, data collection, and personalization.

You can check out how to set up custom events for a specific platform by reading the Platform Integration Guide within the [Developer Guide][1]. You can find this information housed within the "Tracking Custom events" page under the __analytics tab__ of the various platforms. We have linked several for you.

- Tracking Custom events: <br>[Android][2]<br>[iOS][3]<br>[Web][4]

### Event Object

```json
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string), External User ID,
  "user_alias" : (optional, User Alias Object), User Alias Object,
  "braze_id" : (optional, string) Braze User Identifier,
  "app_id" : (optional, string) see App Identifier below,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

## Event Properties Object
Custom events and purchases may have event properties. The “properties” values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs ($).

Property values can be:

- Numbers ([integers](https://en.wikipedia.org/wiki/Integer) and [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic))
- Booleans
- Datetimes (as strings in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) or `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format)
- Strings less than or equal to 255 characters

### Event Property Persistence
Event Properties are designed for filtering of, and Liquid personalization in, messages triggered by their parent Events. By default, they are not persisted on the Braze user profile. To use Event Property values in segmentation, please see our [Custom Event documentation][5] which details the various approaches to storing Event Property values long-term.

#### Event Example Request

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
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
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
      }
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
- [ISO 8601 Time Code Wiki][19]

## Event Objects

Using the example provided above, we can see that someone watched a trailer recently, and then rented a movie. While we cannot go into a campaign and segment the users based on these properties, we can use these properties strategically by using them in the form of a receipt, to send a custom message through a channel using Liquid. For example, "Hello __Beth__, Thanks for renting __The Sad Egg__ by __Dan Alexander__, here are some recommended movies based on your rental..."


[1]: {{site.baseurl}}/developer_guide/home/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"
