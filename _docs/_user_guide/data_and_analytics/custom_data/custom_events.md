---
nav_title: Custom Events
article_title: Custom Events
page_order: 1
page_type: reference
description: "This reference article describes custom events and properties, their usage, and where to view relevant analytics."

---

# Custom Events

Custom events are actions taken by, or updates about, your users. They're best suited for tracking high-value user interactions within your application. Logging a custom event can trigger any number and type of follow-up campaigns, and enables the listed segmentation filters on the recency and frequency of that event.

> For more on using custom events in your messaging strategies, check out our LAB course on [Custom Events & Attributes](http://lab.braze.com/custom-events-and-attributes)!

## Logging Custom Events

Listed below are the methods across various platforms that are used to log custom events. Within these pages, you will also be able to find documentation on how to add properties and quantities to your custom events.

- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/fireos/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Windows Universal]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events/)
- **Xamarin**: 
    - [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/android_and_fireos/analytics/#tracking-custom-events)
    - [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/ios/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

## Custom Event Segmentation Filters

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the custom event has occurred __more than X number of times__ | __MORE THAN__ | __NUMBER__ |
| Check if the custom event has occurred __less than X number of times__ | __LESS THAN__ | __NUMBER__ |
| Check if the custom event has occurred __exactly X number of times__ | __EXACTLY__ | __NUMBER__ |
| Check if the custom event last occurred __after X date__ | __AFTER__ | __TIME__ |
| Check if the custom event last occurred __before X date__ | __BEFORE__ | __TIME__ |
| Check if the custom event last occurred __more than X days ago__ | __MORE THAN__ | __NUMBER OF DAYS AGO__ (Positive Number) |
| Check if the custom event last occurred __less than X days ago__ | __LESS THAN__ | __NUMBER OF DAYS AGO__ (Positive Number) |
| Check if the custom event occurred __more than X (Max = 50) number of times__ | __MORE THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the custom event occurred __less than X (Max = 50) number of times__ | __LESS THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the custom event occurred __exactly X (Max = 50) number of times__ | __EXACTLY__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Custom Event Analytics

Braze notes the number of times these events have occurred as well as the last time they were performed by each user for segmentation. On the [Custom Events][7] page in the Dashboard, you can view in aggregate how often each custom event occurs, as well as by segment over time for more detailed analysis. This is particularly useful to view how your campaigns have affected custom event activity by looking at the gray lines Braze overlays on the time series to indicate the last time a campaign was sent.

![custom_event_analytics_example.png][8]

{% alert tip %}
[Incrementing custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) can be used to keep a counter on a user action similar to a custom event. However, you will not be able to view custom attribute data in a time series. User actions that do not need to be analyzed in time series should be recorded using this method.
{% endalert %}

### Custom Events Analytics Not Showing?

Please note that Segments created with custom event data cannot show previous historic data from before they were created.

## Custom Event Storage

All User Profile data, including custom event metadata (first/last occurrence, total count, and X in Y over 30 days) is stored as long as each profile is active.

## Custom Event Properties

With custom event properties, you can set properties on custom events and purchases. These properties can then be used for further qualifying trigger conditions, increasing personalization in messaging, and generating more sophisticated analytics through raw data export. 

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
{: .reset-td-br-1 .reset-td-br-2}

Event property objects that contain array or object values can have an event property payload of up to 50KB.

For example, if an eCommerce application wanted to send a message to a user when they abandon their cart, it could additionally improve its target audience and allow for increased campaign personalization by adding a custom event property of the 'cart value' of users' carts.

{% alert important %}
Each custom event or purchase can have up to 256 distinct custom event properties. If a custom event or purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

![customEventProperties.png][16]

Custom event properties can also be used for personalization within the messaging template. Any campaign using [Action-Based Delivery][19] with a trigger event can use custom event properties from that event for messaging personalization. If a gaming application wanted to send a message to users who had completed a level, it could further personalize the message with a property for the time it took users to complete that level. In this example, the message is personalized for three different segments using [conditional logic][18].  The custom event property called ``time_spent``, can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% alert warning %}
Triggered in-app messages with templated custom event properties (for example, ``{event_properties.${time_spent}}}``) will fail and not display if there is no internet connectivity.
{% endalert %}

You can change the data type of your custom event property, but please be aware of [the impacts of changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) after data has been collected.

{% alert important %}
When making API calls and using the "is blank" filter, a specific custom event property is considered "blank" if excluded from the call. For example, if you were to include `"event_property": "`, then your users would be considered "not blank".
{% endalert %}

## Custom Event Property Storage

Custom event properties are designed to help you increase targeting precision and make messages feel even more personalized. Custom event properties can be stored within Braze in both the short and long term.

If you would like to segment on the values of event properties, you have two options:

1. **Within 30 days:** Braze support personnel can enable event property segmentation based on the frequency and recency of specific event property values within Braze Segments. If you’d like to leverage event properties within Segments, please contact your Braze account executive or Customer Success Manager. Note that this option will impact data usage.<br><br>
2. **Within and Beyond 30 days:** To cover both short-term and long-term event property segmentation, you can use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). This feature enables you to segment based on custom events and event properties tracked within the past year. Note that this option will not impact data usage.

Braze's Success and Support teams can help recommend the best approach depending on your specific needs. 

[7]: https://dashboard-01.braze.com/dashboard/custom_events/
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
