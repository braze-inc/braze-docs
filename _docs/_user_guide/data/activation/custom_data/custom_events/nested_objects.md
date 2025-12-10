---
nav_title: Nested objects
article_title: Nested Objects in Custom Events
page_order: 1
page_type: reference
description: "This article describes how to send nested JSON data as properties of custom events and purchases, and how to use those nested objects in your messaging."
---

# Nested objects in custom events

> This page covers how to send nested JSON data as properties of custom events and purchases, and how to use those nested objects in your messaging.

You can use nested objects—objects that are inside of another object—to send nested JSON data as properties of custom events and purchases. This nested data can be used for templating personalized information in messages, triggering message sends, and segmenting users.

## Limitations

- Nested data is supported for both [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) and [purchase events]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), but not other event types.
- Event property objects that contain array or object values can have an event property payload of up to 100 KB.
- Event property schemas cannot be generated for purchase events.
- Event property schemas are generated through sampling custom events from the last 24 hours.

### Minimum SDK versions

The following SDK versions support nested objects:

{% sdk_min_versions swift:5.0.0 android:20.0.0 web:3.3.0 %}

## Step 1: Generate a schema

You can access the nested data in your custom event by generating a schema for each event with nested event properties. To generate a schema:

1. Go to **Data Settings** > **Custom Events**.
2. Select **Manage Properties** for the events with nested properties.
3. Select the <i class="fas fa-arrows-rotate"></i> button to generate the schema. To view the schema, select the <i class="fas fa-plus"></i> plus button.

![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

If new properties are sent in the future, they won't be in the schema until it is regenerated. Schemas can be regenerated every 24 hours.

## Step 2: Use the nested object

You can reference the nested data during segmentation and personalization. Note that a schema is not required. Refer to the following sections for usage examples:

- [API request body](#api-request-body)
- [Liquid templating](#liquid-templating)
- [Message triggering](#message-triggering)
- [Segmentation](#segmentation)
- [Personalization](#personalization)

### API request body

{% tabs %}
{% tab Music Example %}

The following is a `/users/track` example with a "Created Playlist" custom event. After a playlist has been created, capture the properties of the playlist by sending:
- An API request that lists "songs" as a property
- An array of the nested properties of the songs

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

The following is a `/users/track` example with an "Ordered" custom event. After an order has been completed, capture properties of that order by sending:
- An API request that lists `r_details` as a property
- The nested properties of that order

```
...
"properties": {
  "r_details": {
    "name": "SandwichEmperor",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
For nested custom event properties, if the year is less than 0 or greater than 3000, Braze doesn't store these values on the user.
{% endalert %}

### Liquid templating

The following shows how to create a Liquid template that references the nested properties requested from the [previous API request](#api-request-body).

{% tabs %}
{% tab Music Example %}
Templating in Liquid in a message triggered by the "Created Playlist" event:

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br>
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Templating in Liquid in a message triggered by the "Ordered" event:

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Message triggering

To use these properties to trigger a campaign, select your custom event or purchase, then add a **Nested Property** filter. Note that message triggering is not yet supported for in-app messages, but nested properties in Liquid personalization in the messages will still display.

{% tabs %}
{% tab Music Example %}

Triggering a campaign with nested properties from the "Created Playlist" event:

![A user choosing a nested property for property filters on a custom event.]({% image_buster /assets/img/nested_object2.png %})

The trigger condition `songs[].album.yearReleased` "is" "1968" will match an event where any of the songs have an album released in 1968. We use the bracket notation `[]` for traversing through arrays, and match if **any** item in the traversed array matches the event property.

{% alert important %}
The **does not equal** filter only matches if none of the properties in your array equal the provided value. <br><br>For example, let's say Canvas A has the action-based custom event nested property filter **equals** "smartwatch", and Canvas B has the action-based custom event nested property filter **does not equal** "simphone". If you have "smartwatch" and "simphone" in your properties, both Canvases will trigger. But if you have "simphone" or "sim only" in any property, neither Canvas will trigger.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Triggering a campaign with nested properties from the "Ordered" event:

![A user adding the property filter r_details.name is SandwichEmperor for a custom event.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "SandwichEmperor"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
If your event property contains the `[]` or `.` characters, escape them by wrapping the chunk in double-quotes. For example, `"songs[].album".yearReleased` will match an event with the literal property `"songs[].album"`.
{% endalert %}

### Segmentation

To segment users based on nested event properties, you must use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). After you've generated a schema, the nested objects explorer will display in the segmentation section. 

![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

Segmentation uses the same notation as triggering (see [Message triggering](#message-triggering)).

To edit or create Segment Extensions, you'll need "Edit Segments" permission.

### Personalization

Using the **Add Personalization** modal, select **Advanced Event Properties** as the personalization type. This allows the option to add a nested event properties after a schema has been generated.

![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Frequently asked questions

### Does using nested objects log additional data points?

There is no change in how we log data points as a result of adding this capability. Segmenting based on nested objects uses Segment Extensions, which doesn't use additional data points.

### How much nested data can be sent?

If one or more of the event's properties contains nested data, the maximum payload for all combined properties on an event is 100 KB. Any request over that size capacity will be rejected.

