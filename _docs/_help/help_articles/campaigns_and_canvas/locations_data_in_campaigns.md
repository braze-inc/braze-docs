---
nav_title: Checking Location Data
article_title: Checking Location Data
page_order: 1

page_type: solution
description: "This help article walks you through quick checks that may assist you if no users have available locations."
tool: Location
---

# Checking Location Data

Braze captures a user's most recent location by default via its SDK. This typically means that the "recent location" is the location from which your user most recently used your app. If you are sending Braze background location data, you may have more granular data available.

If no users have available locations, there are two quick checks that may help you:

* [Confirm Data Collection](#confirm-data-collection)
* [Confirm Data Transfer](#confirm-data-transfer)

## Confirm Data Collection

Confirm that your app is collecting location data:

- For iOS, this means that users opt-in to share their location data via a prompt at some point in the user journey. 
- For Android, confirm that your app asks for fine or coarse location permissions at installation.

In order to see whether user location data is being sent to Braze, use the “location available” filter. This filter will allow you to see the percentage of users for whom you have a “most recent location”.

![trouble7][25]

## Confirm Data Transfer

Confirm that your developers are passing location data to Braze. Normally, the passing of location data is handled automatically by the SDK once the user gives permissions, but it’s possible that your developers have disabled location tracking in Braze. More information on location tracking can be found for:
- [Android][26]
- [iOS][27]
- [Web][28]

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

[25]: {% image_buster /assets/img_archive/trouble7.png %}
[26]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
