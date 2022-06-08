---
nav_title: Purchase Events
article_title: Purchase Events
page_order: 0.5
page_type: reference
description: "This reference article describes purchase events and properties, their usage, and where to view relevant analytics."

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
- [Windows Universal]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases/)
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

Unlike with [segment extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), segments used are updated in real-time, support an unlimited amount of segments, offer a look back history of at most 30 days, and incur data points. Because of the additional data point charge, you must reach out to your CSM to get event properties turned on for your custom events. Once approved, additional properties can be added in the dashboard under **Manage Settings > Custom Events > Mangage Properties** and used in the target step of the campaign or Canvas builder.

### Referencing purchase event properties with Liquid

When you send through purchase data that includes purchase properties, you can use the `event_properties` tag to reference the purchase properties in your channel messaging.

{% raw %}

```liquid
{{event_properties.${your_custom_event_property}}}
```

{% endraw %}

For example, to reference the name of a product, replace `your_custom_event_property` with the `product_id`.

[1]: {% image_buster /assets/img/purchase1.png %}
[2]: {% image_buster /assets/img/purchase2.png %}
[3]: {% image_buster /assets/img/purchase3.png %}
[4]: {% image_buster /assets/img/purchase4.jpg %}
[5]: {% image_buster /assets/img/purchase5.png %}
[6]: {% image_buster /assets/img/nested_object3.png %}
