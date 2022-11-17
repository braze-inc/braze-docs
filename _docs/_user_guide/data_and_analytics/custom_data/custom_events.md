---
nav_title: Custom Events
article_title: Custom Events
page_order: 1
page_type: reference
description: "This reference article describes custom events and properties, their usage, and where to view relevant analytics."

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Custom events

Custom events are actions taken by, or updates about, your users. They're best suited for tracking high-value user interactions within your application. Logging a custom event can trigger any number and type of follow-up campaigns, and enables the listed segmentation filters on the recency and frequency of that event.

## Use cases

Some common custom event use cases include:
- Trigger a campaign or Canvas based on a custom event using [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).
- Segment users by how many times they performed a custom event, when the last time the event occurred, etc.
- Use dashboard [custom event analytics]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) to view an aggregate of how often each event occurred
- Find additional analytics using [funnel]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/funnel_reports/#step-2-select-events-for-funnel-steps) and [retention]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/retention_reports/) reports.
- Leverage [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) to use metadata from your customer event for personalization in your Canvas steps.
- Generate more sophisticated analytics with [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents).
- Set up Canvas [exception events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) to define when users should not advance to the next step of your Canvas.
- And more!

## Managing custom events

To create and manage custom events in the dashboard, go to **Manage Settings** > **Custom Events**. From this page, you can view, manage, or blocklist existing custom events, or create a new one. If you block a custom event, no data will be collected regarding that event, existing data will be unavailable unless reactivated, and blocklisted events will not show up in filters or graphs.

## Logging custom events

The following lists the methods across various platforms that are used to log custom events. Within these pages, you will also be able to find documentation on how to add properties and quantities to your custom events.

{% details Expand for documentation by platform %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Windows Universal]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

## Custom event storage

All data stored on the **User Profile**, including custom event metadata (first/last occurrence, total count, and X in Y over 30 days), is retained indefinitely as long as each profile is [active]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Custom event segmentation filters

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

## Custom event analytics

Braze notes the number of times these events have occurred as well as the last time they were performed by each user for segmentation. On the **Custom Events** reporting page in the dashboard, you can view in aggregate how often each custom event occurs, as well as by segment over time for more detailed analysis. This is particularly useful to view how your campaigns have affected custom event activity by looking at the gray lines Braze overlays on the time series to indicate the last time a campaign was sent.

![Custom event counts graph on the Custom Events page in the dashboard showing trends for two different custom events][8]

{% alert tip %}
[Incrementing custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) can be used to keep a counter on a user action similar to a custom event. However, you will not be able to view custom attribute data in a time series. User actions that do not need to be analyzed in time series should be recorded using this method.
{% endalert %}

### Custom events analytics not showing?

Note that Segments created with custom event data cannot show previous historic data from before they were created.

## Custom event properties

With custom event properties, you can set properties on custom events and purchases. These properties can then be used for further qualifying trigger conditions, increasing personalization in messaging, track conversions, and generating more sophisticated analytics through raw data export.

{% alert important %}
Each custom event or purchase can have up to 256 distinct custom event properties. If a custom event or purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

### Expected format

The properties values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs ($).

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

Event property objects that contain array or object values can have an event property payload of up to 50KB.

You can change the data type of your custom event property, but be aware of the impacts of [changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) after data has been collected.

### Using custom event properties

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

#### Considerations with filters

- **API calls:** When making API calls and using the "is blank" filter, a custom event property is considered "blank" if excluded from the call. For example, if you were to include `"event_property": ""`, then your users would be considered "not blank".
- **Integers:** When filtering for a number custom event property and the number is very large, don't use the "exactly" filter. If a number is too large, it may be rounded at a certain length, so your filter won't work as expected. 
 
#### Data points

In regards to subscription usage, custom event properties enabled for segmentation with the following filters are all counted as separate data points in addition to the data point counted by the custom event itself:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas entry properties and event properties

You can leverage `canvas_entry_properties` and `event_properties` in your Canvas user journeys. Check out [Canvas entry properties and event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) for more information and examples.

{% alert important %}

For the original Canvas editor and Canvas Flow, you can't use `event_properties` in the lead Message step. Instead, you must use `canvas_entry_properties` or add an Action Paths step with the corresponding event **before** the Message step that includes `event_properties`.

{% endalert %}

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

For the Canvases built with the original editor, `canvas_entry_properties` can be referenced only in the first full step of a Canvas.

{% endtab %}

{% tab Event Properties %}
Event properties refer to the properties that you set for custom events and purchases. These `event_properties` can be used in campaigns with action-based delivery as well as Canvases.

In Canvas Flow, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. For Canvas Flow, make sure to use {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} if referencing these `event_properties`. These events must be custom events or purchase events to be used this way in the Message component.

For the original Canvas editor, `event_properties` can't be used in scheduled full steps. However, you can use `event_properties` in the first full step of an action-based Canvas, even if the full step is scheduled.

In the first Message step following an Action Path, you can use `event_properties` related to the event referenced in that Action Path. These `event_properties` can only be used if the user actually took the action (didn’t go to the Everyone Else group). You can have other steps (that are not another Action Paths or Message step) in between this Action Paths and the Message step.

{% endtab %}
{% endtabs %}

### Nested objects {#nested-objects}

You can use nested objects—objects that are inside of another object—to send nested JSON data as properties of custom events and purchases. This nested data can be used for templating personalized information in messages, for triggering message sends, and for segmentation.

#### Limitations

- Nested data can only be sent with [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) and [purchase events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/).
- Event property objects that contain array or object values can have an event property payload of up to 50KB.
- The following SDK versions support nested objects:

{% sdk_min_versions web:3.3.0 ios:4.3.1 android:1.0.0 %}

#### Usage examples

##### API request body

{% tabs %}
{% tab Music Example %}

The following is a `/users/track` example with a "Created Playlist" custom event. Once a playlist has been created, to capture the properties of the playlist, we will send an API request that lists "songs" as a property, and an array of the nested properties of the songs.

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

The following is a `/users/track` example with an "Ordered" custom event. Once an order has been completed, to capture properties of that order, we will send an API request that lists "r_details" as a property, and the nested properties of that order.

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifier": "12345678",
    "location" ; {
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

To use these properties to trigger a campaign, select your custom event or purchase, and add a **Nested Property** filter. Note that message triggering is not yet supported for in-app messages.

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

Use [segment extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) to segment users based on nested event properties. Segmentation uses the same notation as triggering (see [Message triggering](#message-triggering)).

##### Event property segmentation

Event property segmentation allows you to target users based not just on custom events taken but the properties associated with those events. This feature adds additional filtering options when segmenting purchase and custom events.

![][3]

These segmentation filters include:
- Has done custom event with property Y with value V X times in the last Y days.
- Has made any purchases with property Y with value V X times in the last Y days.
- Adds the ability to segment within 1, 3, 7, 14, 21, and 30 days.

Unlike with [segment extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), segments used are updated in real-time, support an unlimited amount of segments, offer a look back history of at most 30 days, and incur data points. Because of the additional data point charge, you must reach out to your CSM to get event properties turned on for your custom events. Once approved, additional properties can be added in the dashboard under **Manage Settings > Custom Events > Mangage Properties** and used in the target step of the campaign or Canvas builder.

#### Frequently asked questions

##### Does this consume additional data points?

There is no change in how we charge data points as a result of adding this capability.

##### How much nested data can be sent?

If one or more of the event's properties contains nested data, the maximum payload for all combined properties on an event is 50 KB. Any request over that size limit will be rejected.

## Custom event property storage

Custom event properties are designed to help you increase targeting precision and make messages feel even more personalized. Custom event properties can be stored within Braze in both the short and long term.

If you would like to segment on the values of event properties, you have two options:

1. **Within 30 days:** Braze support personnel can enable event property segmentation based on the frequency and recency of specific event property values within Braze Segments. If you’d like to leverage event properties within Segments, contact your Braze account executive or customer success manager. Note that this option will impact data usage.<br><br>
2. **Within and Beyond 30 days:** To cover both short-term and long-term event property segmentation, you can use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). This feature enables you to segment based on custom events and event properties tracked within the past two years. Note that this option will not impact data usage.

Braze's Success and Support teams can help recommend the best approach depending on your specific needs.


[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
