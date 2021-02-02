---
nav_title: Mobile Integrations
page_order: 2
description: "This reference article covers the neccesary mobile integrations involved in using GeoFences."

---

# Mobile Integrations

## Cross-Platform Requirements

Geofence-triggered campaigns are available on iOS and Android. To support geofences:

1. Your integration must support background push notifications.

2. Braze geofences or location collection must be enabled.

3. For devices on iOS version 11 and up, the user must allow location access always for geofencing to work.

{% alert important %}
Starting with Braze SDK version 3.6.0 Braze location collection is disabled by default. To verify location collection is enabled on Android, ensure that `com_appboy_enable_location_collection` is set to `true` in your `appboy.xml`.
{% endalert %}

## Geofence Configuration

### Latitude/Longitude

The geographic center of the geofence.

### Radius

The radius of the geofence in meters, measured from the geographic center. We recommend setting a minimum radius of 100 meters for all geofences.

### Cooldown

Users receive geofence triggered notifications after performing enter or exit transitions on individual geofences.  After a transition occurs, there is a pre-defined period of time during which that user may not perform the same transition on that individual geofence again. This period of time is called the "cooldown" and is pre-defined by Braze. Its main purpose is to prevent unnecessary network requests.

## Frequently Asked Questions

##### How do geofences affect battery life?

Our geofencing solution uses the native geofence system service on iOS and Android and is tuned to intelligently trade off accuracy and power, ensuring best in class battery life and improvements in performance as the underlying service improves.

##### How many geofences can I upload to Braze?

You may create or upload an unlimited amount of geofences on the Dashboard, allowing your marketing team to setup geofence sets and campaigns without needing to calculate numbers of geofences. However, each geofence set can hold a maximum of 10,000 geofences. Braze dynamically re-synchronizes the geofences that it tracks for each individual user, ensuring that the most relevant geofences to them are always available.

##### Can I store more than X geofences?

Per Android's [documentation][3], Android apps may only store up to 100 geofences locally at a time. Braze is configured to store only up to 20 geofences locally per app. For geofences to work correctly, you should ensure that your App is not using all available geofence spots.

iOS devices may monitor up to 20 [geofences][4] at a time per app. Braze will monitor up to 20 locations if space is available. For geofences to work correctly, you should ensure that your App is not using all available geofence spots.

##### When are geofences active?

Braze geofences work even when your app is closed, at all hours of the day.

##### How accurate are Braze geofences?

Braze geofences use a combination of all location providers available to a device to triangulate the user's location. These include Wifi, GPS, and cellular towers.

Typical accuracy is in 20-50m range and best-case accuracy will be in the 5-10m range. In rural areas, accuracy may degrade significantly, potentially going up to several kilometers. Braze recommends creating geofences with larger radii in rural locations.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
