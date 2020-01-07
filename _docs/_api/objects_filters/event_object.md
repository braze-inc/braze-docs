---
nav_title: "Event Object"
page_order: 5
page_layout: reference
description: "This reference article goes over the event object, what it is, and how it's a crucial part of event-based campaign strategies."
tool: docs
platform: API
---

# Event Object Specification

> This article explains the different components of an event object, how you can use this object, and examples to draw from. 

## What is an Event Object?

An Event Object is an object that gets passed through the API when a specific event occurs. Events objects are housed in an events array. Each Event Object in the events array represents a single occurrence of a Custom Event by a particular user at the designated time value. The event object has many different fields that allow you to customize by setting and using event properties in messages, data collection, and personalization. 

You can check out how to set up custom events for a specific platform by reading the Platform Integration Guide within the [Developer Guide][1]. You can find this information housed within the "Tracking Custom Events" page under the __analytics tab__ of the various platforms. We have linked several for you.

- Tracking Custom Events: <br>[Android][2]<br>[iOS][3]<br>[Web][4]

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
Custom events and purchases may have event properties. The “properties” values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs. Property values can be integers, floats, booleans, datetimes (as strings in ISO8601 or yyyy-MM-dd'T'HH:mm:ss:SSSZ format), or strings less than or equal to 255 characters.

### Event Properties
Event properties __do not__ persist and aren't saved on a user's profile. These properties can, however, be used to trigger messages and for personalization using Liquid, but __does not__ allow you to segment based on these properties. However, Braze does allow you to "save" these properties for 30 days by turning on this feature flipper to keep these properties alive and useable for message personalization. To turn on this feature in your own app group, contact your customer service manager. 

While uncommon, if you require these properties to persist past the 30-day limit, contact your Customer Success Manager, or, see our webhooks suggestion below to see how you can incorporate webhooks to save these properties as custom attributes. 

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


[1]: https://www.braze.com/docs/developer_guide/home/
[2]: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/
[3]: https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[4]: https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"
