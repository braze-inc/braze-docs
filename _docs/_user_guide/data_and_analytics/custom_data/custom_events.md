---
nav_title: Custom Events
article_title: Custom Events
page_order: 9
page_type: reference
description: "This article describes custom events and properties, segmentation, usage, Canvas entry properties, where to view relevant analytics, and more."
search_rank: 2
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Custom events

> This article describes custom events and properties, related segmentation filters, Canvas entry properties, relevant analytics, and more. To learn about Braze events in general, refer to [Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events).

Custom events are actions taken by, or updates about, your users. When custom events are logged, they can trigger any number and type of follow-up campaigns. You can then use [segmentation filters](#segmentation-filters) to segment users based on how recently and frequently those custom events occurred. This makes custom events best suited for tracking high-value user interactions within your application.

## Use cases

Some common custom event use cases include:
- Triggering a campaign or Canvas based on a custom event using [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)
- Segmenting users by how many times they performed a custom event, when the last time the event occurred, and similar
- Using dashboard [custom event analytics]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) to view an aggregate of how often each event occurred
- Finding additional analytics using [funnel]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) and [retention]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/) reports
- Leveraging [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) to use metadata from your customer event for personalization in your Canvas steps
- Generating more sophisticated analytics with [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents)
- Setting up Canvas [exception events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) to define when users shouldn't advance to the next step of your Canvas

## Managing custom events

You can manage, create, or blocklist custom events in the dashboard by going to **Data Settings** > **Custom Events**.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), you can find **Custom Events** under **Manage Settings**.
{% endalert %}

Select the menu next to a custom event for the following actions:

### Blocklisting

You can blocklist individual custom events through the actions menu, or select and blocklist up to 10 events in bulk. 

When you block a custom event:

- Future data won't be collected for that event.
- Existing data won't be available unless that event is unblocked.
- That event won't show up in filters or graphs.

Additionally, if a blocked custom event is currently referenced by filters or triggers in other areas of Braze, a warning modal will appear explaining that all instances of the filters or triggers that reference it will be removed and archived.

### Adding descriptions

You can add a description to a custom event after it's created if you have the `Manage Events, Attributes, Purchases` [user permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/). Select **Edit description** for the custom event and input whatever you like, such as a note for your team.

## Adding tags

You can add tags to a custom event after it's created if you have the "Manage Events, Attributes, Purchases" [user permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/). The tags can then be used to filter the list of events. 

{% alert important %}
This feature is currently in early access. Contact your customer success manager if you're interested in participating in this early access.
{% endalert %}

### Viewing usage reports

The usage report lists all the Canvases, campaigns, and segments using a specific custom event. The list doesn't include uses of Liquid. 

You can view up to 10 usage reports at a time by selecting the checkboxes for multiple custom events and then selecting **View usage report**.

## Exporting data

To export the list of custom events as a CSV file, select the **Export all** button at the top of the page. The CSV file will be generated, and a download link will be emailed to you.

{% alert important %}
This feature is currently in early access. Contact your customer success manager if you're interested in participating in this early access.
{% endalert %}

## Logging custom events

Custom events require additional setup. Refer to the list below for documentation about each platform, where you'll find information about the methods used to log custom events and how to add properties and quantities to your custom events.

{% details Expand for documentation by platform %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

## Custom event storage

All data stored on the **User Profile**, including custom event metadata (first or last occurrence, total count, and X in Y over 30 days), is retained indefinitely as long as each profile is [active]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Analytics

Braze notes the number of times custom events have occurred and the last time they were performed by each user for segmentation. View these analytics by going to **Analytics** > **Custom Events Report**.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), you can find the **Custom Events** report under **Data**.
{% endalert %}

On the **Custom Events Report** page in the dashboard, you can view in aggregate how often each custom event occurs. The gray lines overlayed on the time series indicate the last time a campaign was sent, which is useful for viewing how your campaigns affected custom event activity.

![Custom event counts graph on the Custom Events page in the dashboard showing trends for a custom event][8]

You can also use **Filters** to break down your custom events by hour, monthly average users (MAU), segments, or KPI formulas. 

![Custom event graph filters][9]{: style="max-width:40%;"}

{% alert tip %}
[Increment custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) to keep a counter on a user action similar to a custom event. However, you can't view custom attribute data in a time series. User actions that don't need to be analyzed in a time series should be recorded using this method.
{% endalert %}

### Why custom events analytics aren't showing

Segments created with custom event data can't show previous historical data from before they were created.

## Custom event properties

Custom event properties are custom event metadata or attributes that describe a specific occurrence of an event. These properties can be used for further qualifying trigger conditions, increasing personalization in messaging, tracking conversions, and generating more sophisticated analytics through raw data export.

Custom event properties aren't stored on the Braze profile and therefore don't consume data points (see [Data points](#data-points) for exceptions).

{% alert important %}
Each custom event or purchase can have up to 256 distinct custom event properties. If a custom event or purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

### Expected format

The property values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs (`$`).

Property values can be any of the following data types:

| Data Type | Description |
| --- | --- |
| Numbers | As either [integers](https://en.wikipedia.org/wiki/Integer) or [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleans | Value of `true` or `false`. |
| Datetimes | Formatted as strings in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) or `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. Not supported within arrays. |
| Strings | 255 characters or fewer. |
| Arrays | Arrays cannot include datetimes. |
| Objects | Objects will be ingested as strings. |
| Nested objects | Objects that are inside of other objects. For more, see the section in this article on [Nested objects](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Event property objects that contain array or object values can have an event property payload up to 100&nbsp;KB.

You can change the data type of your custom event property, but be aware of the impacts of [changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) after data has been collected.

### Using custom event properties

Custom event properties can be used to qualify campaign triggers, track conversions, and personalize messaging.

#### Trigger messages

Use custom event properties to further narrow your audience for a particular campaign or Canvas. For example, if you have an ecommerce application and want to send a message to a user when they abandon their cart, you can add a custom event property of `cart value` to improve your target audience and allow for increased campaign personalization.

![Custom event property filters for an abandoned card. Two filters are combined with an AND operator to send this campaign to users who abandoned their card with a cart value between 100 and 200 dollars][16]

Nested custom event properties are also supported in [action-based delivery][19].

![Custom event property filters for an abandoned card. One filter is selected if any items in the cart have a price more than 100 dollars.][20]

#### Personalize messages

You can also use custom event properties for personalization within the messaging template. Any campaign using [action-based delivery][19] with a trigger event can use custom event properties from that event for messaging personalization.

For example, if you have a gaming app and want to send a message to users who completed a level, you could further personalize your message with a property for the time it took users to complete that level. In this example, the message is personalized for three different segments using [conditional logic][18]. The custom event property called `time_spent` can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
If the user doesn't have an internet connection, triggered in-app messages with templated custom event properties (for example, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) will fail and not display.
{% endalert %}

For a full list of Liquid tags that will cause in-app messages to deliver as templated in-app messages, refer to [Frequently asked questions]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Considerations with filters

- **API calls:** When making API calls and using the "is blank" filter, a custom event property is considered "blank" if excluded from the call. For example, if you were to include `"event_property": ""`, then your users would be considered "not blank".
- **Integers:** When filtering for a number custom event property and the number is very large, don't use the "exactly" filter. If a number is too large, it may be rounded at a certain length, so your filter won't work as expected.

#### Segmentation

Use event property segmentation to target users based on custom events taken and the properties associated with those events. This increases your filtering options when segmenting by purchase and custom events.

Event properties for custom events are updated in real-time for any segment that uses them. You can manage properties by going to **Data Settings** > **Custom Events** and selecting **Manage Properties** for the associated custom event. Custom event properties used in certain segment filters have a maximum look-back history of 30 days.

{% alert note %}
If you'd like to create segments based on event property recency and frequency, reach out to your customer success manager to enable segmentation for specific custom event properties. When enabled, you can access additional filtering options when segmenting.
{% endalert %}

The event property segmentation filters include:

- Has done a custom event with property A with value B, X times in the last Y days.
- Has made any purchases with property A with value B, X times in the last Y days.
- Adds the ability to segment within 1, 3, 7, 14, 21, and 30 days.

![A filter group that "has 'Abandoned Cart' with property 'number of itmes' and value '2' 'more than' 1'1 time in the last '30' calendary days (720-744 hours)."][3]

Data is only logged for a given event property after it has been enabled by your customer success manager, and event properties are only available from that date moving forward.

##### Data points

In regards to subscription usage, custom event properties enabled for segmentation with the following filters are all counted as separate data points in addition to the data point counted by the custom event itself:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas entry properties and event properties

You can use `canvas_entry_properties` and `event_properties` in your Canvas user journeys. Refer to [Canvas entry properties and event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) for more information and examples.

{% tabs local %}
{% tab Canvas Entry Properties %}

[Canvas entry properties]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) are the properties you map for Canvases that are action-based or API-triggered. Note that the `canvas_entry_properties` object has a maximum size limit of 50 KB.

{% alert note %}
For in-app message channels specifically, `canvas_entry_properties` can only be referenced in Canvas Flow and the original Canvas editor if you have persistent entry properties enabled in the original editor as part of the previous early access.
{% endalert %}

For Canvas Flow messaging, `canvas_entry_properties` can be used in any Message step with this Liquid format: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Note that the events must be custom events or purchase events to be used this way. 

#### Use case

{% raw %}
Let's say a retail store, RetailApp, has the following request: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. RetailApp can pull the product name (shoes) into a message with the Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

RetailApp can also trigger specific messages to send for different `product_name` properties in a Canvas that targets users after they've triggered a purchase event. For example, they can send different messages to users who purchased shoes and users who purchased something else by adding the following Liquid into a Message step.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
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

Event properties refer to the properties you set for custom events and purchases. These `event_properties` can be used in campaigns with action-based delivery and Canvases.

In Canvas Flow, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. Make sure to use {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} if referencing these `event_properties`. These events must be custom events or purchase events to be used this way in the Message component.

In the first Message step following an Action Path, you can use `event_properties` related to the event referenced in that Action Path. These `event_properties` can only be used if the user actually took the action (and didn't go to the Everyone Else group). You can have other steps (that are not another Action Paths or Message step) in between this Action Paths and the Message step.

{% details Expand for original Canvas editor %}

As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This section is available for reference only.

For the original Canvas editor, `event_properties` can't be used in scheduled full steps. However, you can use `event_properties` in the first full step of an action-based Canvas, even if the full step is scheduled.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Nested objects {#nested-objects}

You can use nested objects (objects inside of another object) to send nested JSON data as properties of custom events and purchases. This nested data can be used for templating personalized information in messages, triggering message sends, and segmenting users.

To learn more, refer to our dedicated page on [Nested objects]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/).

## Custom event property storage

Custom event properties are designed to help you increase targeting precision and make messages feel even more personalized. Custom event properties can be stored within Braze in both the short and long term.

You can segment based on the values of event properties in two ways:

1. **Within 30 days:** Braze support personnel can enable event property segmentation based on the frequency and recency of specific event property values within Braze segments. If you'd like to leverage event properties within segments, contact your Braze account executive or customer success manager. This option will impact data usage.<br><br>
2. **Within and beyond 30 days:** To cover both short-term and long-term event property segmentation, you can use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). This feature segments users based on custom events and event properties tracked within the past two years. This option won't impact data usage.

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
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
