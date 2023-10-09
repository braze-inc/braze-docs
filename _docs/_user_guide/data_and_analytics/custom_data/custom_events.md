---
nav_title: Custom Events
article_title: Custom Events
page_order: 9
page_type: reference
description: "This reference article describes custom events and properties, segmentation, their usage, Canvas entry properties, where to view relevant analytics, and more."
search_rank: 2
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Custom events

> This article describes custom events and properties, segmentation, their usage, Canvas entry properties, where to view relevant analytics, and more. To learn more about events in Braze, refer to [Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events).

## Overview

Custom events are actions taken by, or updates about, your users. They're best suited for tracking high-value user interactions within your application. Logging a custom event can trigger any number and type of follow-up campaigns, and enables the listed segmentation filters on the recency and frequency of that event.

### Use cases

Some common custom event use cases include:
- Trigger a campaign or Canvas based on a custom event using [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).
- Segment users by how many times they performed a custom event, when the last time the event occurred, etc.
- Use dashboard [custom event analytics]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) to view an aggregate of how often each event occurred
- Find additional analytics using [funnel]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) and [retention]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/) reports.
- Leverage [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) to use metadata from your customer event for personalization in your Canvas steps.
- Generate more sophisticated analytics with [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents).
- Set up Canvas [exception events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) to define when users should not advance to the next step of your Canvas.

### Managing custom events

To create and manage custom events in the dashboard, go to **Data Settings** > **Custom Events**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Custom Events** under **Manage Settings**.
{% endalert %}

From this page, you can view, manage, or blocklist existing custom events, or create a new one. If you block a custom event, no data will be collected regarding that event, existing data will be unavailable unless reactivated, and blocklisted events will not show up in filters or graphs.

### Logging custom events

Custom events require additional setup. The following lists the methods across various platforms that are used to log custom events. Within these pages, you will also be able to find documentation on how to add properties and quantities to your custom events.

{% details Expand for documentation by platform %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

### Custom event storage

All data stored on the **User Profile**, including custom event metadata (first/last occurrence, total count, and X in Y over 30 days), is retained indefinitely as long as each profile is [active]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Segmentation filters

The following table shows the filters available for segmenting users by custom events.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the custom event has occurred **more than X number of times** | **MORE THAN** | **NUMBER** |
| Check if the custom event has occurred **less than X number of times** | **LESS THAN** | **NUMBER** |
| Check if the custom event has occurred **exactly X number of times** | **EXACTLY** | **NUMBER** |
| Check if the custom event last occurred **after X date** | **AFTER** | **TIME** |
| Check if the custom event last occurred **before X date** | **BEFORE** | **TIME** |
| Check if the custom event last occurred **more than X days ago** | **MORE THAN** | **NUMBER OF DAYS AGO** (Positive Number) |
| Check if the custom event last occurred **less than X days ago** | **LESS THAN** | **NUMBER OF DAYS AGO** (Positive Number) |
| Check if the custom event occurred **more than X (Max = 50) number of times** | **MORE THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the custom event occurred **less than X (Max = 50) number of times** | **LESS THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the custom event occurred **exactly X (Max = 50) number of times** | **EXACTLY** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Analytics

Braze notes the number of times these events have occurred as well as the last time they were performed by each user for segmentation. You can view these analytics at **Analytics** > **Custom Events Report**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find the **Custom Events** report under **Data**.
{% endalert %}

On the **Custom Events Report** page in the dashboard, you can view in aggregate how often each custom event occurs, as well as by segment over time for more detailed analysis. This is particularly useful to view how your campaigns have affected custom event activity by looking at the gray lines Braze overlays on the time series to indicate the last time a campaign was sent.

![Custom event counts graph on the Custom Events page in the dashboard showing trends for a custom event][8]

You can also use **Filters** to breakdown your custom events by hour, monthly average users (MAU), segments, or KPI formulas. 

![Custom event graph filters][9]{: style="max-width:40%;"}

{% alert tip %}
[Incrementing custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) can be used to keep a counter on a user action similar to a custom event. However, you will not be able to view custom attribute data in a time series. User actions that do not need to be analyzed in time series should be recorded using this method.
{% endalert %}

### Custom events analytics not showing?

Segments created with custom event data cannot show previous historic data from before they were created.

## Custom event properties

Custom event properties are custom event metadata or attributes that describe a specific occurrence of an event. These properties can then be used for further qualifying trigger conditions, increasing personalization in messaging, tracking conversions, and generating more sophisticated analytics through raw data export.

Custom event properties are not stored on the Braze profile and therefore do not consume data points (see [Data points](#data-points) below for exceptions).

{% alert important %}
Each custom event or purchase can have up to 256 distinct custom event properties. If a custom event or purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

### Expected format

The properties values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs (`$`).

Property values can be any of the following data types:

| Data Type | Description |
| --- | --- |
| Numbers | As either [integers](https://en.wikipedia.org/wiki/Integer) or [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleans |  |
| Datetimes | Formatted as strings in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) or `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. Not supported within arrays. |
| Strings | 255 characters or fewer. |
| Arrays | Arrays cannot include datetimes. |
| Objects | Objects will be ingested as strings. |
| Nested objects | Objects that are inside of other objects. For more, see the section in this article on [Nested objects](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2}

Event property objects that contain array or object values can have an event property payload of up to 50&nbsp;KB.

You can change the data type of your custom event property, but be aware of the impacts of [changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) after data has been collected.

### Using custom event properties

Custom event properties can be used to qualify campaign triggers, track conversions, and personalize messaging.

#### Trigger messages

You can use custom event properties to further narrow your audience for a particular campaign or Canvas. For example, if you have an eCommerce application and want to send a message to a user when they abandon their cart, you could improve your target audience and allow for increased campaign personalization by adding a custom event property of `cart value`.

![Custom event property filters for an abandoned card. Two filters are combined with an AND operator to send this campaign to users who abandoned their card with a cart value between 100 and 200 dollars][16]

Nested custom event properties are also supported in [Action-Based Delivery][19] or conversion processing.

![Custom event property filters for an abandoned card. One filter is selected if any items in the cart have a price more than 100 dollars.][20]

#### Personalize messages

You can also use custom event properties for personalization within the messaging template. Any campaign using [action-based delivery][19] with a trigger event can use custom event properties from that event for messaging personalization.

For example, if you have a gaming application and want to send a message to users who had completed a level, you could further personalize your message with a property for the time it took users to complete that level. In this example, the message is personalized for three different segments using [conditional logic][18]. The custom event property called `time_spent` can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% alert warning %}
If the user has no internet connection, triggered in-app messages with templated custom event properties (for example, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) will fail and not display.
{% endalert %}

##### Considerations with filters

- **API calls:** When making API calls and using the "is blank" filter, a custom event property is considered "blank" if excluded from the call. For example, if you were to include `"event_property": ""`, then your users would be considered "not blank".
- **Integers:** When filtering for a number custom event property and the number is very large, don't use the "exactly" filter. If a number is too large, it may be rounded at a certain length, so your filter won't work as expected.

#### Segmentation

If you'd like to create segments based on event property recency and frequency, reach out to your customer success manager to enable segmentation for specific custom event properties. When enabled, you can access additional filtering options when segmenting, such as:

- Has done custom event with property A with value B, X times in the last Y days
- Has made any purchases with property A with value B, X times in the last Y days

Data is only logged for a given event property after it has been enabled by your customer success manager—event properties are only available from that date moving forward.

##### Data points

In regards to subscription usage, custom event properties enabled for segmentation with the following filters are all counted as separate data points in addition to the data point counted by the custom event itself:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas entry properties and event properties

You can leverage `canvas_entry_properties` and `event_properties` in your Canvas user journeys. Check out [Canvas entry properties and event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) for more information and examples.

{% tabs local %}
{% tab Canvas Entry Properties %}

[Canvas entry properties]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) are the properties you map for Canvases that are action-based or API-triggered. Note that the `canvas_entry_properties` object has a maximum size limit of 50 KB.

{% alert note %}
For in-app message channels specifically, `canvas_entry_properties` can only be referenced in Canvas Flow and in the original Canvas editor if you have persistent entry properties enabled in the original editor as part of the previous early access.
{% endalert %}

For Canvas Flow messaging, `canvas_entry_properties` can be used in Liquid in any Message step. Use this Liquid when referencing these properties: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Note that the events must be custom events or purchase events to be used this way. 

{% raw %}
For example, consider the following request: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. You could add the word "shoes" to a message with the Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

{% details Expand for original Canvas editor %}

As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This section is available for reference only.

For the Canvases built with the original editor, `canvas_entry_properties` can be referenced only in the first full step of a Canvas.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

{% alert important %}
You can't use `event_properties` in the lead Message step. Instead, you must use `canvas_entry_properties` or add an Action Paths step with the corresponding event **before** the Message step that includes `event_properties`.
{% endalert %}

Event properties refer to the properties that you set for custom events and purchases. These `event_properties` can be used in campaigns with action-based delivery as well as Canvases.

In Canvas Flow, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. Make sure to use {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} if referencing these `event_properties`. These events must be custom events or purchase events to be used this way in the Message component.

In the first Message step following an Action Path, you can use `event_properties` related to the event referenced in that Action Path. These `event_properties` can only be used if the user actually took the action (didn't go to the Everyone Else group). You can have other steps (that are not another Action Paths or Message step) in between this Action Paths and the Message step.

{% details Expand for original Canvas editor %}

As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This section is available for reference only.

For the original Canvas editor, `event_properties` can't be used in scheduled full steps. However, you can use `event_properties` in the first full step of an action-based Canvas, even if the full step is scheduled.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Nested objects {#nested-objects}

You can use nested objects—objects that are inside of another object—to send nested JSON data as properties of custom events and purchases. This nested data can be used for templating personalized information in messages, for triggering message sends, and for segmentation.

#### Limitations

- Nested data is supported for both [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) and [purchase events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/), but not other event types.
- Event property objects that contain array or object values can have an event property payload of up to 50 KB.
- Event property schemas cannot be generated for purchase events.
- Event property schemas are generated through sampling custom events from the last 24 hours.
- The following SDK versions support nested objects:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

#### Schema generation

Generating a schema for events with nested event properties allows you to access the nested data. To generate a schema, follow these steps:
1. Go to **Manage Settings** > **Custom Events**.
2. Select **Manage Properties** for the events with nested properties.
3. Click the icon to generate the schema. To view the schema, click the plus button.

![][6]{: style="max-width:80%;"}

After generating a schema, you'll be able to reference the nested data during [segmentation](#segmentation) and [personalization](#personalization).

#### Usage examples

##### API request body

{% tabs %}
{% tab Music Example %}

The following is a `/users/track` example with a "Created Playlist" custom event. After a playlist has been created, to capture the properties of the playlist, we will send an API request that lists "songs" as a property, and an array of the nested properties of the songs.

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

The following is a `/users/track` example with an "Ordered" custom event. After an order has been completed, to capture properties of that order, we will send an API request that lists "r_details" as a property, and the nested properties of that order.

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
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

##### Liquid templating

The following Liquid templating examples show how to reference the nested properties saved from the preceding API request and use them in your Liquid messaging. Using Liquid and dot notation, traverse the nested data to find the specific node you would like to include in your messages.

{% tabs local %}
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

##### Message triggering

To use these properties to trigger a campaign, select your custom event or purchase, and add a **Nested Property** filter. Note that message triggering is not yet supported for in-app messages. However, you can also add nested objects after generating a schema.

{% tabs %}
{% tab Music Example %}

Triggering a campaign with nested properties from the "Created Playlist" event:

![A user choosing a nested property for property filters on a custom event]({% image_buster /assets/img/nested_object2.png %})

The trigger condition `songs[].album.yearReleased` "is" "1968" will match an event where any of the songs have an album released in 1968. We use the bracket notation `[]` for traversing through arrays, and match if **any** item in the traversed array matches the event property.<br>
{% endtab %}
{% tab Restaurant Example %}

Triggering a campaign with nested properties from the "Ordered" event:

![A user adding the property filter r_details.name is McDonalds for a custom event]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %} If your event property contains the `[]` or `.` characters, escape them by wrapping the chunk in double-quotes. For instance, `"songs[].album".yearReleased` will match an event with the literal property `"songs[].album"`.  {% endalert %}

##### Segmentation

Use [segment extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) to segment users based on nested event properties. After you've generated a schema, the nested objects explorer will display in the segmentation section. Segmentation uses the same notation as triggering (see [Message triggering](#message-triggering)). 

![][4]

##### Personalization

Using the **Add Personalization** modal, select **Advanced Event Properties** as the personalization type. This allows the option to add a nested event properties after a schema has been generated.

![][5]{: style="max-width:70%;"}

##### Event property segmentation

Event property segmentation allows you to target users based not just on custom events taken but the properties associated with those events. This feature adds more filtering options when segmenting purchase and custom events.

![][3]

These segmentation filters include:
- Has done custom event with property Y with value V X times in the last Y days.
- Has made any purchases with property Y with value V X times in the last Y days.
- Adds the ability to segment within 1, 3, 7, 14, 21, and 30 days.

Event properties with custom events are updated in real time for any segment that uses them. You can manage properties from the **Data Settings** > **Custom Events** page by clicking **Manage Properties** for your custom event. Custom event properties used in certain segment filters have a maximum look back history of 30 days. Reach out to your Braze customer success manager to discuss using event property segmentation for your custom events.

#### Frequently asked questions

##### Does this consume additional data points?

There is no change in how we charge data points as a result of adding this capability.

##### How much nested data can be sent?

If one or more of the event's properties contains nested data, the maximum payload for all combined properties on an event is 50 KB. Any request over that size limit will be rejected.

## Custom event property storage

Custom event properties are designed to help you increase targeting precision and make messages feel even more personalized. Custom event properties can be stored within Braze in both the short and long term.

If you would like to segment on the values of event properties, you have two options:

1. **Within 30 days:** Braze support personnel can enable event property segmentation based on the frequency and recency of specific event property values within Braze Segments. If you'd like to leverage event properties within Segments, contact your Braze account executive or customer success manager. Note that this option will impact data usage.<br><br>
2. **Within and beyond 30 days:** To cover both short-term and long-term event property segmentation, you can use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). This feature enables you to segment based on custom events and event properties tracked within the past two years. Note that this option will not impact data usage.

Contact your Braze customer success manager for recommendations on the best approach depending on your specific needs.


[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {% image_buster /assets/img/custom_events_report_filters.png %}
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
