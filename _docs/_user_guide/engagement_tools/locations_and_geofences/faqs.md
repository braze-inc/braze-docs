---
nav_title: FAQs
article_title: Locations & Geofences FAQs
page_order: 4
page_type: FAQ
description: "This reference article covers some frequently asked questions surrounding the use of Geofences."
tool: Location

---

# Locations and geofences FAQs

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

### How many geofences can I store?

Per Android's [documentation][3], Android apps may only store up to 100 geofences locally at a time. Braze is configured to store only up to 20 geofences locally per app. For geofences to work correctly, you should ensure that your App is not using all available geofence spots.

iOS devices may monitor up to 20 [geofences][4] at a time per app. Braze will monitor up to 20 locations if space is available. For geofences to work correctly, you should ensure that your App is not using all available geofence spots.

### How many geofences can I upload to Braze?

You may create or upload an unlimited amount of geofences on the dashboard, allowing your marketing team to setup geofence sets and campaigns without needing to calculate numbers of geofences. However, each geofence set can hold a maximum of 10,000 geofences. Braze dynamically re-synchronizes the geofences that it tracks for each individual user, ensuring that the most relevant geofences to them are always available.

### How accurate are Braze geofences?

Braze geofences use a combination of all location providers available to a device to triangulate the user's location. These include WiFi, GPS, and cellular towers.

Typical accuracy is in 20-50m range and best-case accuracy will be in the 5-10m range. In rural areas, accuracy may degrade significantly, potentially going up to several kilometers. Braze recommends creating geofences with larger radii in rural locations.

### How do geofences affect battery life?

Our geofencing solution uses the native geofence system service on iOS and Android and is tuned to intelligently trade off accuracy and power, ensuring best in class battery life and improvements in performance as the underlying service improves.

### When are geofences active?

Braze geofences work even when your app is closed, at all hours of the day.

### How often are geofences refreshed for users?

For active users, the Braze SDK will only request geofences once per day on session start. That means if changes are made to the geofence sets after session start, you'll need to wait 24 hours from the time the sets are first pulled down to receive the updated set.

For inactive users, if the user is background push enabled, Braze will also send a silent push once every 24 hours to pull down the latest locations to the device.

You can manually update geofence sets for individual users at any time by clicking **Re-sync Geofences** on the bottom corner of the **Locations** page.

{% alert note %}
If the geofences aren't loaded onto the device locally, the user can't trigger the geofence even if they enter the area.
{% endalert %}

### What's the difference between geofences versus segmenting on most recent location?

In Braze, a geofence is a different concept from segmenting based on most recent location. Geofences are only used for triggers, such as sending a message when a user enters or exits a specific area. Segments based on the `Most Recent Location` filter are used to target a specific region of your audience, such as sending a message to users located in New York.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
