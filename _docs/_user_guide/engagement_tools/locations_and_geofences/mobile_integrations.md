---
nav_title: Mobile Integrations
article_title: Geofence Mobile Integrations
page_order: 2
page_type: reference
description: "This reference article covers the necessary mobile integrations involved in using geofences."
tool: Location

---

# Mobile integrations

> This reference article covers the necessary mobile integrations involved in using geofences.

## Cross-platform requirements

Geofence-triggered campaigns are available on iOS and Android. To support geofences, the following must be in place:

1. Your integration must support background push notifications.
2. Braze geofences or location collection must be enabled.
3. For devices on iOS version 11 and up, the user must allow location access always for geofencing to work.

{% alert important %}
Starting with Braze SDK version 3.6.0, Braze location collection is disabled by default. To verify that it's enabled on Android, confirm that `com_braze_enable_location_collection` is set to `true` in your `braze.xml`.
{% endalert %}

## Geofence configuration

### Latitude and longitude

The geographic center of the geofence.

### Radius

The radius of the geofence in meters, measured from the geographic center. We recommend setting a minimum radius of 100–150 meters for all geofences.

Refer to these guides for more guidance based on your platform:
- [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence)
- [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5)

### Cooldown

Users receive geofence-triggered notifications after performing enter or exit transitions on individual geofences. After a transition occurs, there is a pre-defined time during which that user may not perform the same transition on that individual geofence again. This time is called the "cooldown" and is pre-defined by Braze. Its main purpose is to prevent unnecessary network requests.

### Technology partners

You can also leverage geofences with some of our partners, for example: 

- [Radar][12]
- [Foursquare][13]

## Frequently asked questions

Visit our [Geofence FAQ][5] for answers to frequently asked questions about geofences.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
[12]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[13]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/

