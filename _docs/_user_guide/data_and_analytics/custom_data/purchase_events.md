---
nav_title: Purchase Events
article_title: Purchase Events
page_order: 8
page_type: reference
description: "This reference article describes purchase events and properties, their usage, segmentation, where to view relevant analytics, and more."
search_rank: 3
---

# Purchase events

Purchase events are purchase actions taken by your users. These events are used to record in-app purchases and establish the Lifetime Value (LTV) for each individual user profile. These purchase events must be set up by your team. Logging purchase events gives you the option to add properties like quantity and type, helping you further target your users based on these properties.

After you have set up and begun logging purchase events, you can view this purchase data on a user's profile, in the [Overview tab]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab).

## Logging purchase events

You can log purchases by passing a [Purchase Object]({{site.baseurl}}/api/objects_filters/purchase_object/) through the [User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint.

The following lists methods across various platforms that are used to log purchases. Within these pages, you will also be able to find documentation on how to add properties and quantities to your purchase event.

- [Android and FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

## Blocklisting purchase events

In the Braze dashboard, you can manage blocklisting from **Manage Settings** > **Products**. Check out [Custom Events and Attribute Management]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/) to learn more.

## Purchase event segmentation

You can trigger any number or type of follow-up campaigns based on logged purchase events, and enable the following segmentation filters based on the recency and frequency of that event when targeting users.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the total number of dollars spent **is greater than** a **number**| **GREATER THAN** | **NUMBER** |
| Check if the total number of dollars spent **is less than** a **number**| **LESS THAN** | **NUMBER** |
| Check if total number of dollars spent **is exactly** a **number**| **EXACTLY** | **NUMBER** |
| Check if the purchase last occurred **after X date** | **AFTER** | **TIME** |
| Check if the purchase last occurred **before X date** | **BEFORE** | **TIME** |
| Check if the purchase last occurred **more than X days ago** | **MORE THAN** | **TIME** |
| Check if the purchase last occurred **less than X days ago** | **LESS THAN** | **TIME** |
| Check if the purchase occurred **more than X (Max = 50) number of times** | **MORE THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the purchase occurred **less than X (Max = 50) number of times** | **LESS THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the purchase occurred **exactly X (Max = 50) number of times** | **EXACTLY** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**Example of Filtering based on Purchase Event:**

![Filtering for users that have made more than five purchases][1]{: style="max-width:80%;margin-left:15px;"}

{% alert tip %} 
If you would like to segment on the number of times a specific purchase has occurred, you should record that purchase individually as an [incrementing custom attribute]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

## Purchase event analytics

In addition to tracking purchase metrics for segmentation, Braze also notes the number purchases for each product and the revenue generated over time. You can view this data on the [Revenue]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) page.

![Purchase graph on the Revenue page showing statistics for all purchases][4]

![Purchase breakdown table on the Revenue page listing the products in your applications, the number of times they've been purchased, and their associated revenue][3]

## Purchase event properties {#purchase-properties}

With purchase event properties, you can set properties on purchases that can be used to further qualify trigger conditions, increase personalization in messaging, and generate more sophisticated analytics through raw data export. Property value types (string, numeric, boolean, date) vary per platform, and are often assigned as key-value pairs.

For example, if an eCommerce application wanted to send a message to a user after they have made a purchase, they could additionally improve their target audience and allow for increased campaign personalization by adding a purchase event property of `brand_name`.

**Example of Triggering based on Purchase Event Properties:**

![Action-based delivery settings to send a campaign to users who purchase headphones with a brand name equal to HeadphoneMart][2]{: style="max-width:80%;margin-left:15px;"}

Refer to [Purchase Properties Object]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) for more.

### Event property segmentation

Event property segmentation allows you to target users based not just on custom events taken but the properties associated with those events. This feature adds additional filtering options when segmenting purchase and custom events.

![][6]

These segmentation filters include:
- Has done custom event with property Y with value V X times in the last Y days.
- Has made any purchases with property Y with value V X times in the last Y days.
- Adds the ability to segment within 1, 3, 7, 14, 21, and 30 days.

Unlike with [segment extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), segments used are updated in real-time, support an unlimited amount of segments, offer a look back history of at most 30 days, and incur data points. Because of the additional data point charge, you must reach out to your Braze customer success manager to get event properties turned on for your custom events. Once approved, additional properties can be added in the dashboard under **Manage Settings > Custom Events > Manage Properties** and used in the target step of the campaign or Canvas builder.

### Canvas entry properties and event properties

{% alert important %}
As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This section is available for reference when using `canvas_entry_properties` and `event_properties` for the original Canvas workflow.
{% endalert %}

You can leverage `canvas_entry_properties` and `event_properties` in your Canvas user journeys. Check out [Canvas entry properties and event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) for more information and examples.

{% alert important %}
You can't use `event_properties` in the lead Message step. Instead, you must use `canvas_entry_properties` or add an Action Paths step with the corresponding event **before** the Message step that includes `event_properties`.
{% endalert %}

{% tabs local %}
{% tab Canvas Entry Properties %}

[Canvas entry properties]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) are the properties you map for Canvases that are action-based or API-triggered. Note that the `canvas_entry_properties` object has a maximum size limit of 50 KB.

{% alert note %}
For in-app message channels specifically, `canvas_entry_properties` can only be referenced in Canvas Flow and in the original Canvas editor if you have persistent entry properties enabled in the original editor as part of the previous early access.
{% endalert %}

For Canvas Flow messaging, `canvas_entry_properties` can be used in Liquid in any Message step. Use this Liquid when referencing these properties: ``{% raw %} canvas_entry_properties${property_name} {% endraw %}``. Note that the events must be custom events or purchase events to be used this way. 

{% raw %}
For example, consider the following request: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. You could add the word "shoes" to a message with the Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

For the Canvases built with the original editor, `canvas_entry_properties` can be referenced only in the first full step of a Canvas.

{% endtab %}

{% tab Event Properties %}
Event properties refer to the properties that you set for custom events and purchases. These `event_properties` can be used in campaigns with action-based delivery as well as Canvases.

In Canvas Flow, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. For Canvas Flow, make sure to use {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} if referencing these `event_properties`. These events must be custom events or purchase events to be used this way in the Message component.

For the original Canvas editor, `event_properties` can't be used in scheduled full steps. However, you can use `event_properties` in the first full step of an action-based Canvas, even if the full step is scheduled.

In the first Message step following an Action Path, you can use `event_properties` related to the event referenced in that Action Path. These `event_properties` can only be used if the user actually took the action (didn't go to the Everyone Else group). You can have other steps (that are not another Action Paths or Message step) in between this Action Paths and the Message step.

{% endtab %}
{% endtabs %}

### Log purchases at the order level
If you would like to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

[1]: {% image_buster /assets/img/purchase1.png %}
[2]: {% image_buster /assets/img/purchase2.png %}
[3]: {% image_buster /assets/img/purchase3.png %}
[4]: {% image_buster /assets/img/purchase4.jpg %}
[5]: {% image_buster /assets/img/purchase5.png %}
[6]: {% image_buster /assets/img/nested_object3.png %}
