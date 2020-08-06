---
nav_title: Purchase Event
title: Purchase Event
description: "This article covers purchase events, how they should be structured, and how to use them within the Braze Dashboard."
---

# Purchase Events

> Purchase events are purchase actions taken by your users; these events are used to record in-app purchases and establish the Lifetime Value (LTV) for each individual user profile. These purchase events must be set up by your team. Logging purchase events also give you the option to add properties like quantity and type, helping you further target your users based on these properties.

## Purchase Event Segmentation

Logging purchase event can trigger any number/type of follow up campaigns, and enable the following segmentation filters on the recency and frequency of that event when targeting users. This data is viewable within our revenue page in time-series.

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

![Purchase 1][1]{: style="max-width:80%;margin-left:15px;"}

>  If you would like to segment on the number of times a specific purchase has occurred, you should record that purchase individually as an [incrementing custom attribute](https://www.braze.com/docs/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).

## Purchase Event Properties

With Purchase Event Properties, you can set properties on purchases. These properties can then be used to further qualify trigger conditions, increase personalization in messaging, and generate more sophisticated analytics through raw data export. Property values types (string, numeric, boolean, date, etc.) vary per platform and are often assigned as key-value pairs. Check out the logging purchase methods shown below for further information on how to assign purchase event properties and quantity. 

For example, if an eCommerce application wanted to send a message to a user after they have made a purchase, it could additionally improve its target audience and allow for increased campaign personalization by adding a purchase event property of 'brand_name'.

__Example of Triggering based on Purchase Event Properties__

![Purchase 2][2]{: style="max-width:80%;margin-left:15px;"}

### Purchase Event Storage
All User Profile data (Custom Events, Custom Attribute, Custom Data) is stored as long as those profiles are active. Custom Event Properties are stored and available for Segmentation for thirty (30) days. If you’d like to leverage Event Properties for Segmentation, please contact your Braze account or customer success manager.

## Logging Purchases

Listed below are the methods across various platforms that are used to log purchases. Within these pages, you will also be able to find documentation on how to add properties and quantities to your purchase event. 

- [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/)
- [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [FireOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/fireos/analytics/logging_purchases/)
- __React Native__: [Android/FireOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/android_and_fireos/analytics/revenue_tracking/) and [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/ios/analytics/revenue_tracking/)
- [Unity](https://www.braze.com/docs/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Windows Universal](https://www.braze.com/docs/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases/)
- __Xamarin__: [Android/FireOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/xamarin/android_and_fireos/analytics/revenue_tracking/) and [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/xamarin/ios/analytics/logging_purchases/)
- [Roku](https://www.braze.com/docs/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

[1]: {% image_buster /assets/img/purchase_event/purchase1.png %}
[2]: {% image_buster /assets/img/purchase_event/purchase2.png %}
