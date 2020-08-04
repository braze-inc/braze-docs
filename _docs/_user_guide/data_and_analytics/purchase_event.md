---
nav_title: Purchase Event
title: Purchase Event
description: "This article covers how to use purchase events, how thye should be structured and how to use them within the Braze Dashboard."
---

# Purchase Events

Purchase events are purchase actions taken by your users; they are used  to record in-app purchases and establishes the Life-time Value(LTV) for each individual user profile. Logging purchase event can trigger any number/type of follow up campaigns, and enabled the following segmentation filters on the recency and frequency of that event. This data is viewable within out revenue page in time-series.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the total number of dollars spent __is greater than__ a __number__| __GREATER THAN__ | __NUMBER__ |
| Check if the total number of dollars spent __is less than__ a __number__| __LESS THAN__ | __NUMBERL__ |
| Check if total number of dollars spent __is exactly__ a __number__| __EXACTLY__ | __NUMBER__ |
| Check if the purchase last occurred __after X date__ | __AFTER__ | __TIME__ |
| Check if the purchase last occurred __before X date__ | __BEFORE__ | __TIME__ |
| Check if the purchase last occurred __more than X days ago__ | __MORE THAN__ | __TIME__ |
| Check if the purchase last occurred __less than X days ago__ | __LESS THAN__ | __TIME__ |
| Check if the purchase occurred __more than X (Max = 50) number of times__ | __MORE THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the purchase occurred __less than X (Max = 50) number of times__ | __LESS THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the purchase occurred __exactly X (Max = 50) number of times__ | __EXACTLY__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |

>  If you would like to segment on the number of times a specific purchase has occurred, you should also record that purchase individually as an [incrementing custom attribute](https://www.braze.com/docs/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).

## Purchase Event Properties

With purchase event properties, you can set properties on purchases. These properties can then be used to further qualify triger conditions, increasing personalization in messagine, and generating more sophisticated analytics through raw data export. Proerty valies can be string, numeric, boolean, or time objects. However, proerty values cannot be array objects.

For example, if an ecommerce application wanted to send a message to a user when he/she abandons their cart, it cou,d additionally improve its target audience and allow for increased campaign personalization by adding a custom event property of th e'cart value' of users carts. 






## Logging Purchases

Listed below are the methods across various platforms that are required to log purchases. Within these pages you will also be able to find documentation on how to add properties and quanitites to your purchase event. 

- [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/)
- [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [FireOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/fireos/analytics/logging_purchases/)
- React Native: [Android/FireOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/android_and_fireos/analytics/revenue_tracking/) and [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/ios/analytics/revenue_tracking/)
- [Unity](https://www.braze.com/docs/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Windows Universal](https://www.braze.com/docs/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases/)
- Xamarin: [Android/FireOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/xamarin/android_and_fireos/analytics/revenue_tracking/) and [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/xamarin/ios/analytics/logging_purchases/)
- [Roku](https://www.braze.com/docs/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)
