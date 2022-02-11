---
nav_title: Mobile Integrations
article_title: Geofence Mobile Integrations
page_order: 2
page_type: reference
description: "This reference article covers the neccesary mobile integrations involved in using Geofences."
tool: Location

---

# Mobile integrations

## Cross-platform requirements

Geofence-triggered campaigns are available on iOS and Android. To support geofences, the following must be in place:

1. Your integration must support background push notifications.
2. Braze geofences or location collection must be enabled.
3. For devices on iOS version 11 and up, the user must allow location access always for geofencing to work.

{% alert important %}
Starting with Braze SDK version 3.6.0 Braze location collection is disabled by default. To verify location collection is enabled on Android, ensure that `com_braze_enable_location_collection` is set to `true` in your `braze.xml`.
{% endalert %}

## Geofence configuration

### Latitude and longitude

The geographic center of the geofence.

### Radius

The radius of the geofence in meters, measured from the geographic center. We recommend setting a minimum radius of 100 meters for all geofences.

### Cooldown

Users receive geofence triggered notifications after performing enter or exit transitions on individual geofences. After a transition occurs, there is a pre-defined period of time during which that user may not perform the same transition on that individual geofence again. This period of time is called the "cooldown" and is pre-defined by Braze. Its main purpose is to prevent unnecessary network requests.

## Frequently asked questions

Visit our [Geofence FAQs][5] page for answers to frequently asked questions about geofences.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
