---
nav_title: FAQ
article_title: Locations & Geofences FAQ
page_order: 4
page_type: FAQ
description: "This reference article covers some frequently asked questions surrounding the use of Geofences."
tool: Location

---

# Locations and geofences FAQ

> This page provides answers to frequently asked questions about localtions and geofences.

## Locations

### When does Braze collect location data?

Braze only collects location when the application is open in the foreground. As a result, our `Most Recent Location` filter targets users based upon where they last opened the application (also referred to as session start). 

You should also keep the following nuances in mind:

- If location is disabled, the `Most Recent Location` filter will show the last location recorded.
- If a user has ever had a location stored on their profile, they will qualify for the `Location Available` filter, even if they've opted out of location tracking since then.

### What's the difference between the Most Recent Device Locale and Most Recent Location filters?

The `Most Recent Device Locale` comes from the user's device settings. For example, this appears for iPhone users in their device under **Settings** > **General** > **Language & Region**. This filter is used to capture language and regional formatting, such as dates and addresses, and is independent of the `Most Recent Location` filter.

The `Most Recent Location` is the last known GPS location of the device. This is updated on session start.

### If a user opts out of location tracking, will their old location data be removed from Braze?

Nope! If a user has ever had a location stored on their profile, that data will not be automatically removed if they later opt out of location tracking.

## Geofences

### How accurate are Braze geofences?

Braze geofences use a combination of all location providers available to a device to triangulate the user's location. These include WiFi, GPS, and cellular towers.

Typical accuracy is in 20–50m range and best-case accuracy will be in the 5-10m range. In rural areas, accuracy may degrade significantly, potentially going up to several kilometers. Braze recommends creating geofences with larger radii in rural locations.

### How do geofences affect battery life?

Our geofencing solution uses the native geofence system service on iOS and Android and is tuned to intelligently trade off accuracy and power, ensuring best in class battery life and improvements in performance as the underlying service improves.

### When are geofences active?

Braze geofences work at all hours of the day, even when your app is closed.

### What's the difference between geofences versus segmenting on most recent location?

In Braze, a geofence is a different concept from segmenting based on most recent location. Geofences are only used for triggers, such as sending a message when a user enters or exits a specific area. Segments based on the `Most Recent Location` filter are used to target a specific region of your audience, such as sending a message to users located in New York.

### Can I set up a geofence within a geofence?

As a best practice, avoid setting up geofences inside each other as this may cause issues with triggering notifications.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
