---
nav_title: Custom Events
article_title: Custom Events
page_order: 1
page_type: reference
description: "This reference article describes custom events and properties, their usage, and where to view relevant analytics."

---

# Custom events

Custom events are actions taken by, or updates about, your users. They're best suited for tracking high-value user interactions within your application. Logging a custom event can trigger any number and type of follow-up campaigns, and enables the listed segmentation filters on the recency and frequency of that event.

{% alert tip %}
For more on using custom events in your messaging strategies, check out our [Custom Events and Attributes](http://lab.braze.com/custom-events-and-attributes) LAB course!
{% endalert %}

## Managing custom events

To create and manage custom events in the dashboard, go to **Manage Settings** > **Custom Events**. From this page, you can view, manage, or blocklist existing custom events, or create a new one. If you block a custom event, no data will be collected regarding that event, existing data will be unavailable unless reactivated, and blocklisted events will not show up in filters or graphs.

## Logging custom events

Listed below are the methods across various platforms that are used to log custom events. Within these pages, you will also be able to find documentation on how to add properties and quantities to your custom events.

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

Braze notes the number of times these events have occurred as well as the last time they were performed by each user for segmentation. On the [Custom Events][7] page in the dashboard, you can view in aggregate how often each custom event occurs, as well as by segment over time for more detailed analysis. This is particularly useful to view how your campaigns have affected custom event activity by looking at the gray lines Braze overlays on the time series to indicate the last time a campaign was sent.

![Custom event counts graph on the Custom Events page in the dashboard showing trends for two different custom events][8]

{% alert tip %}
[Incrementing custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) can be used to keep a counter on a user action similar to a custom event. However, you will not be able to view custom attribute data in a time series. User actions that do not need to be analyzed in time series should be recorded using this method.
{% endalert %}

### Custom events analytics not showing?

Please note that Segments created with custom event data cannot show previous historic data from before they were created.

## Custom event properties

With custom event properties, you can set properties on custom events and purchases. These properties can then be used for further qualifying trigger conditions, increasing personalization in messaging, track conversions, and generating more sophisticated analytics through raw data export.

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

For example, if an eCommerce application wanted to send a message to a user when they abandon their cart, it could additionally improve its target audience and allow for increased campaign personalization by adding a custom event property of the 'cart value' of users' carts.

{% alert important %}
Each custom event or purchase can have up to 256 distinct custom event properties. If a custom event or purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

![Custom event property filters for an abandoned card. Two filters are combined with an AND operator to send this campaign to users who abandoned their card with a cart value between 100 and 200 dollars][16]

Custom event properties can also be used for personalization within the messaging template. Any campaign using [Action-Based Delivery][19] with a trigger event can use custom event properties from that event for messaging personalization. If a gaming application wanted to send a message to users who had completed a level, it could further personalize the message with a property for the time it took users to complete that level. In this example, the message is personalized for three different segments using [conditional logic][18].  The custom event property called ``time_spent``, can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% alert warning %}
Triggered in-app messages with templated custom event properties (for example, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) will fail and not display if there is no internet connectivity.
{% endalert %}

You can change the data type of your custom event property, but please be aware of the impacts of [changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) after data has been collected.

{% alert important %}
When making API calls and using the "is blank" filter, a specific custom event property is considered "blank" if excluded from the call. For example, if you were to include `"event_property": "`, then your users would be considered "not blank".
{% endalert %}

In regards to subscription usage, custom event properties enabled for segmentation with the filters `X Custom Event Property in Y Days` or `X Purchase Property in Y Days` are all counted as separate data points in addition to the data point counted by the custom event itself.

### Nested objects {#nested-objects}

You can use nested objects—objects that are inside of another object—to send nested JSON data as properties of custom events and purchases. This nested data can be used for templating personalized information in messages, for triggering message sends, and for segmentation.

{% alert important %}
This feature is generally available. However, triggering messages and segmenting users based on this data is in early access. For more information, please reach out to your Braze account manager.
{% endalert %}

#### Limitations

- Nested data can only be sent with [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) and [purchase events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/).
- Sending nested custom attributes (objects as a custom attribute data type) is limited to customers participating in the early access. For more information, refer to [Nested custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).
- Event property objects that contain array or object values can have an event property payload of up to 50KB.
- The following SDK versions support nested objects:

{% sdk_min_versions web:3.3.0 ios:4.3.1 android:1.0.0 %}

#### Usage examples

##### API request body

{% tabs %}
{% tab Music Example %}

Shown below is a `/users/track` example with a "Created Playlist" custom event. Once a playlist has been created, to capture the properties of the playlist, we will send an API request that lists "songs" as a property, and an array of the nested properties of the songs.

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

Shown below is a `/users/track` example with an "Ordered" custom event. Once an order has been completed, to capture properties of that order, we will send an API request that lists "r_details" as a property, and the nested properties of that order.

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

The Liquid templating examples below show how to reference the nested properties saved from the above API request and use them in your Liquid messaging. Using Liquid and dot notation, traverse the nested data to find the specific node you would like to include in your messages.

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

{% alert important %}
Nested objects is generally available. However, triggering messages and segmenting users based on this data is in early access. For more information, please reach out to your Braze account manager.
{% endalert %}

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

Use [segment extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) to segment users based on nested event properties. Segmentation uses the same notation as triggering (described above).

{% alert important %}
Nested objects is generally available. However, triggering messages and segmenting users based on this data is in early access. For more information, please reach out to your Braze account manager.
{% endalert %}

#### Frequently asked questions

##### Does this consume additional data points?

There is no change in how we charge data points as a result of adding this capability.

##### How much nested data can be sent?

If one or more of the event's properties contains nested data, the maximum payload for all combined properties on an event is 50 KB. Any request over that size limit will be rejected.

## Custom event property storage

Custom event properties are designed to help you increase targeting precision and make messages feel even more personalized. Custom event properties can be stored within Braze in both the short and long term.

If you would like to segment on the values of event properties, you have two options:

1. **Within 30 days:** Braze support personnel can enable event property segmentation based on the frequency and recency of specific event property values within Braze Segments. If you’d like to leverage event properties within Segments, please contact your Braze account executive or Customer Success Manager. Note that this option will impact data usage.<br><br>
2. **Within and Beyond 30 days:** To cover both short-term and long-term event property segmentation, you can use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). This feature enables you to segment based on custom events and event properties tracked within the past year. Note that this option will not impact data usage.

Braze's Success and Support teams can help recommend the best approach depending on your specific needs. 


[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[7]: https://dashboard-01.braze.com/dashboard/custom_events/
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
