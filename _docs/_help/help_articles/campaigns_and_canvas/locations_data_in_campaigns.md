---
nav_title: Checking location data
article_title: Checking Location Data
page_order: 1
page_type: solution
description: "This help article walks you through quick checks that may assist you if no users have available locations."
tool: Location
---

# Checking location data

Braze captures a user's most recent location by default via its SDK. This typically means that the "recent location" is the location from which your user most recently used your app. If you send Braze background location data, you may have more granular data available.

If no users have available locations, two quick checks can help you confirm data collection and date transfer.

## Data collection

Confirm that your app is collecting location data:

- For iOS, this means that users opt-in to share their location data via a prompt at some point in the user journey. 
- For Android, confirm that your app asks for fine or coarse location permissions at installation.

To see whether user location data is being sent to Braze, use the **Location Available** filter. This filter allows you to see the percentage of users with a "most recent location".

![]({% image_buster /assets/img_archive/trouble7.png %})

## Data transfer

Confirm that your developers are passing location data to Braze. Normally, the passing of location data is handled automatically by the SDK after the user gives permissions, but your developers may have disabled location tracking in Braze. More information on location tracking can be found for:
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/)

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on November 16, 2022_

