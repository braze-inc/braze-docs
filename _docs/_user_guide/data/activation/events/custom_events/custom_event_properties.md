---
nav_title: Custom event properties
article_title: Custom Event Properties
page_order: 0
page_type: reference
description: "This article describes custom event properties, their expected format, how to use them, and custom event property storage."
---

# Custom event properties

> This article describes custom event properties, their expected format, how to use them for messaging and segmentation, and custom event property storage.

Custom event properties are custom event metadata or attributes that describe a specific occurrence of an event. These properties can be used for further qualifying trigger conditions, increasing personalization in messaging, tracking conversions, and generating more sophisticated analytics through raw data export.

Custom event properties aren't stored on the Braze profile and therefore don't log data points (see [Data points](#data-points) for exceptions).

{% alert important %}
Each custom event or purchase can have up to 256 distinct custom event properties. If a custom event or purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

## Expected format

The property values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs (`$`).

Property values can be any of the following data types:

| Data Type | Description |
| --- | --- |
| Numbers | As either [integers](https://en.wikipedia.org/wiki/Integer) or [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleans | Value of `true` or `false`. |
| Datetimes | Formatted as strings in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) or `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. Not supported within arrays. |
| Strings | 255 characters or fewer. |
| Arrays | Arrays cannot include datetimes. |
| Nested objects | Objects that are inside of other objects. For more, see the section in this article on [Nested objects](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Event property objects that contain array or object values can have an event property payload up to 100&nbsp;KB.

You can change the data type of your custom event property, but be aware of the impacts of [changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) after data has been collected.

## Using custom event properties

Custom event properties can be used to qualify campaign triggers, track conversions, and personalize messaging.

### Trigger messages

Use custom event properties to further narrow your audience for a particular campaign or Canvas. For example, if you have an eCommerce application and want to send a message to a user when they abandon their cart, you can add a custom event property of `item price` to improve your target audience and allow for increased campaign personalization.

![Custom event property filters for an abandoned card. Two filters are combined with an AND operator to send this campaign to users who abandoned their card with a item price between 100 and 200 dollars]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Nested custom event properties are also supported in [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

![Custom event property filters for an abandoned card. One filter is selected if any items in the cart have a price more than 100 dollars.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png")

### Personalize messages

You can also use custom event properties for personalization within the messaging template. Any campaign using [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) with a trigger event can use custom event properties from that event for messaging personalization.

For example, if you have a gaming app and want to send a message to users who completed a level, you could further personalize your message with a property for the time it took users to complete that level. In this example, the message is personalized for three different segments using [conditional logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/). The custom event property called `time_spent` can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

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

#### Considerations with filters

- **API calls:** When making API calls and using the "is blank" filter, a custom event property is considered "blank" if excluded from the call. For example, if you were to include `"event_property": ""`, then your users would be considered "not blank".
- **Integers:** When filtering for a number custom event property and the number is very large, don't use the "exactly" filter. If a number is too large, it may be rounded at a certain length, so your filter won't work as expected.

### Segmentation

Use event property segmentation to target users based on custom events taken and the properties associated with those events. This increases your filtering options when segmenting by purchase and custom events.

Event properties for custom events are updated in real-time for any segment that uses them. You can manage properties by going to **Data Settings** > **Custom Events** and selecting **Manage properties** for the associated custom event. Custom event properties used in certain segment filters have a maximum look-back history of 30 days.

#### Adding event properties for segmentation

You need the "Edit Custom Event Property Segmentation" [user permission]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage) to create segments based on event property recency and frequency.

{% multi_lang_include deprecations/user_permissions.md %}

By default, you can have 20 segmentable event properties per workspace. Contact your Braze account manager to increase this limit.

To add event properties for segmentation, do the following:

1. Go to your custom event and select **Manage properties**.
2. Select the **Enable segmentation** toggle to add the event property for segmentation. You can access additional filtering options when segmenting.

The event property segmentation filters include:

- Has done a custom event with property A with value B, X times in the last Y days.
- Has made any purchases with property A with value B, X times in the last Y days.
- Adds the ability to segment within 1 to 30 days.

![A filter group that has 'Abandoned Cart' with property 'number of items' and value 2 more than 1 time in the last 30 calendar days.]({% image_buster /assets/img/nested_object3.png %})

Data is logged only for a given event property after you enable it, and event properties are available only from that date moving forward.

#### Data points

In regards to subscription usage, custom event properties enabled for segmentation with the following filters are all counted as separate data points in addition to the data point counted by the custom event itself:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas entry properties and event properties

{% multi_lang_include canvas_entry_event_properties.md %}

### Nested objects {#nested-objects}

You can use nested objects (objects inside of another object) to send nested JSON data as properties of custom events and purchases. This nested data can be used for templating personalized information in messages, triggering message sends, and segmenting users.

To learn more, refer to our dedicated page on [Nested objects]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/).

## Custom event property storage

Custom event properties are designed to help you increase targeting precision and make messages feel even more personalized. Custom event properties can be stored within Braze in both the short and long term.

You can segment based on the values of event properties in two ways:

1. **Within 30 days:** You can use event property segmentation based on the frequency and recency of specific event property values within Braze segments. This option impacts data usage.<br><br>
2. **Within and beyond 30 days:** To cover both short-term and long-term event property segmentation, you can use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). This feature segments users based on custom events and event properties tracked within the past two years. This option does not impact data usage.

Contact your Braze customer success manager for recommendations on the best approach depending on your specific needs.
