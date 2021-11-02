---
nav_title: Purchase Events
article_title: Purchase Events
page_order: 0.5
page_type: reference
description: "This reference article describes purchase events and properties, their usage, and where to view relevant analytics."

---

# Purchase events

Purchase events are purchase actions taken by your users. These events are used to record in-app purchases and establish the Lifetime Value (LTV) for each individual user profile. These purchase events must be set up by your team. Logging purchase events gives you the option to add properties like quantity and type, helping you further target your users based on these properties.

Once you have set up and begun logging purchase events, you can view this purchase data on the User Profile.

![Purchase 5][5]{: style="max-width:80%;margin-left:15px;"}

## Logging purchase events

You can log purchases by passing a [Purchase Object]({{site.baseurl}}/api/objects_filters/purchase_object/) through the [User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint.

Listed below are the methods across various platforms that are used to log purchases. Within these pages, you will also be able to find documentation on how to add properties and quantities to your purchase event.

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
| Check if the total number of dollars spent __is greater than__ a __number__| __GREATER THAN__ | __NUMBER__ |
| Check if the total number of dollars spent __is less than__ a __number__| __LESS THAN__ | __NUMBER__ |
| Check if total number of dollars spent __is exactly__ a __number__| __EXACTLY__ | __NUMBER__ |
| Check if the purchase last occurred __after X date__ | __AFTER__ | __TIME__ |
| Check if the purchase last occurred __before X date__ | __BEFORE__ | __TIME__ |
| Check if the purchase last occurred __more than X days ago__ | __MORE THAN__ | __TIME__ |
| Check if the purchase last occurred __less than X days ago__ | __LESS THAN__ | __TIME__ |
| Check if the purchase occurred __more than X (Max = 50) number of times__ | __MORE THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the purchase occurred __less than X (Max = 50) number of times__ | __LESS THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the purchase occurred __exactly X (Max = 50) number of times__ | __EXACTLY__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**Example of Filtering based on Purchase Event:**

![Purchase 1][1]{: style="max-width:80%;margin-left:15px;"}

{% alert tip %} 
If you would like to segment on the number of times a specific purchase has occurred, you should record that purchase individually as an [incrementing custom attribute]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

## Purchase event analytics

In addition to tracking purchase metrics for segmentation, Braze also notes the number purchases for each product and the revenue generated over time. You can view this data on the [Revenue]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) page.

![Purchase 4][4]

![Purchase 3][3]

## Purchase event properties {#purchase-properties}

With purchase event properties, you can set properties on purchases that can be used to further qualify trigger conditions, increase personalization in messaging, and generate more sophisticated analytics through raw data export. Property value types (string, numeric, boolean, date) vary per platform, and are often assigned as key-value pairs.

For example, if an eCommerce application wanted to send a message to a user after they have made a purchase, they could additionally improve their target audience and allow for increased campaign personalization by adding a purchase event property of `brand_name`.

**Example of Triggering based on Purchase Event Properties:**

![Purchase 2][2]{: style="max-width:80%;margin-left:15px;"}

Refer to [Purchase Properties Object]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) for more.

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
[4]: {% image_buster /assets/img/purchase4.png %}
[5]: {% image_buster /assets/img/purchase5.png %}