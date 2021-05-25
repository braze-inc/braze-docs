---
nav_title: FAQs
page_order: 4

page_type: reference
description: "This reference article covers some frequently asked questions surrounding the use of Geofences."
tool: Location

---

# Frequently Asked Questions

## How do geofences affect battery life?

Our geofencing solution uses the native geofence system service on iOS and Android and is tuned to intelligently trade off accuracy and power, ensuring best in class battery life and improvements in performance as the underlying service improves.

## How many geofences can I upload to Braze?

You may create or upload an unlimited amount of geofences on the Dashboard, allowing your marketing team to setup geofence sets and campaigns without needing to calculate numbers of geofences. However, each geofence set can hold a maximum of 10,000 geofences. Braze dynamically re-synchronizes the geofences that it tracks for each individual user, ensuring that the most relevant geofences to them are always available.

## Can I store more than X geofences?

Per Android's [documentation][3], Android apps may only store up to 100 geofences locally at a time. Braze is configured to store only up to 20 geofences locally per app. For geofences to work correctly, you should ensure that your App is not using all available geofence spots.

iOS devices may monitor up to 20 [geofences][4] at a time per app. Braze will monitor up to 20 locations if space is available. For geofences to work correctly, you should ensure that your App is not using all available geofence spots.

## When are geofences active?

Braze geofences work even when your app is closed, at all hours of the day.

## How accurate are Braze geofences?

Braze geofences use a combination of all location providers available to a device to triangulate the user's location. These include Wifi, GPS, and cellular towers.

Typical accuracy is in 20-50m range and best-case accuracy will be in the 5-10m range. In rural areas, accuracy may degrade significantly, potentially going up to several kilometers. Braze recommends creating geofences with larger radii in rural locations.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
