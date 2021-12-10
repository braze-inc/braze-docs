---
nav_title: Beacon and Geofence Support
article_title: Beacon and Geofence Support
page_order: 7
page_type: reference
tool:
  - Segments
  - Location
description: "This article briefly discusses Beacon and Geofence support and how to use your location partner account to begin location tracking."
---

# Beacon and geofence support

> This article briefly discusses Beacon and Geofence support and how to use your location partner account to begin location tracking.

Combining existing beacon or geofence support with Braze's targeting and messaging features allows you to learn more about your user's physical actions and message them accordingly.

## Radar support

Radar has full support for unlimited custom geofences, pre-built POI geofences, beacon detection, region detection, trip tracking, and more. When you enable the Radar and Braze integration, Radar forwards real time location events and user attributes which can be used to trigger real time campaigns, power last mile pickup and delivery operations, optimize fleet tracking and shipping logistics, or build user segments based on location patterns. Additionally, Radar Geo APIs can be leveraged to enrich or personalize your marketing campaigns through Connected Content. Visit our [Radar integrations page](https://www.braze.com/docs/partners/message_personalization/location/radar/#radar) to learn more.

## Gimbal places support

Connecting your Gimbal Account to Braze lets you track when your users enter or leave your defined places and trigger events off of these entries and exits. In addition, you can track extra information like the Place name or the Dwell visit as an event property so that you can personalize your messaging even further. Please reference Gimbal's documentation along with our instructions for [iOS][1] and [Android][2] integration.

{% alert note %}
Note that this will work the same for Gimbal's beacons as well as their geofence solutions.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#beacon-integration
