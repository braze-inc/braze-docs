---
nav_title: Nested Object Support
page_title: Nested Object Support for Custom Event Properties
page_order: 4
alias: /nested_object_support/
page_type: reference
description: "This reference article describes nested object support for custom event properties, and includes example use cases, limitations, and frequently asked questions."
---

# Nested Object Support for Custom Event Properties

Nested Object Support allows you to send arrays of data as properties of custom events and purchases. This nested data can be used for templating personalized information in API-triggered messages through the use of Liquid and dot notation.

## Limitations

- Nested data can only be sent with [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) and [purchase events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/). This is not yet supported with user attributes.
- Array data cannot be used for segmentation or in any other way on the platform outside of Liquid templating and triggering.
- Datetimes are not supported within the array.
- Object data types will be ingested as strings.
- Event property objects that contain array or object values can have an event property payload of up to 50KB.

## Usage Examples

### API Request Body

{% tabs %}
{% tab Music Example %}

Shown below is a `/users/track` example with a "Played Song" custom event. Once a song has been played, to capture the properties of the song, we will send an API request that lists "songs" as a property, and an array of the nested properties of the songs.

```
...
properties: {
  ...
  "songs" :[{
    "title" : "Smells Like Teen Spirit",
    "artist" : "Nirvana",
    "album" : {
      "name" : "Nevermind",
      "yearReleased" : "1991"
    }
  }],
  ...
}
...
```
{% endtab %}
{% tab Restaurant Example%}

Shown below is a `/users/track` example with an "Ordered" custom event. Once an order has been completed, to capture properties of that order, we will send an API request that lists "r_details" as a property, and the nested properties of that order.

```
...
properties:{
  ...
  "r_details" : {
    "name" : "McDonalds",
    "identifier" : "12345678",
    "location" : {
      "city" : "Montclair",
      "state" : "NJ"
    }
  },
  ...
}
...
```
{% endtab %}
{% endtabs %}

### Liquid Templating

The Liquid templating example below shows how to reference the nested properties saved from the above API request and use them in your API-triggered Liquid messaging. Using Liquid and dot notation, traverse the nested data array to find the specific node you would like to include in your API-triggered messages.

{% tabs local %}
{% tab Music Example %}
Templating in Liquid in a message triggered by the "Liked Song" event:

{% raw %}
`{{event_properties.${songs}[0].album.name}}` - "Nevermind"<br>
`{{event_properties.${songs}[0].title}}` - "Smells Like Teen Spirit"
{% endraw %}

{% endtab %}
{% endtabs %}

### Campaign Triggering

Campaign triggering is supported for object custom event properties only. To use these properties to trigger a campaign, select your custom event, and add a __Nested Object Property__ filter. 

{% tabs %}
{% tab Music Example %}

Triggering a campaign with nested properties from the "Liked Song" event:

![Triggering Campaign]({% image_buster /assets/img/nested_object2.png %})

{% endtab %}
{% tab Restaurant Example %}

Triggering a campaign with nested properties from the "Ordered" event:

![Triggering Campaign]({% image_buster /assets/img/nested_object1.png %})

`r_details.name` - "Mcdonalds"<br>
`r_details.location.city` - "Montclair"
{% endtab %}
{% endtabs %}

## Frequently Asked Questions

### Does this consume additional data points?

Array properties are treated the same as other event type properties, so there is no change in how we charge data points as a result of adding this capability.

### How much data can be sent in the array?

If one or more of the event's properties contains nested data, the maximum payload for all combined properties on an event is 50 KB. Any request over that size limit will be rejected.

[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}

