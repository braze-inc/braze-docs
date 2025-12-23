---
nav_title: Create geofences
article_title: Create Geofences
page_order: 1
page_type: reference
toc_headers: h2
description: "This reference article covers what geofences are, and how to create and configure geofence events."
tool: 
  - Location
search_rank: 9
---

# Geofences

> At the core of our real-time location offering is the concept of a geofence. A geofence is a virtual geographic area, represented as latitude and longitude combined with a radius, forming a circle around a specific global position. Geofences can vary from the size of a building to the size of an entire city.

## How it works

Geofences can be used to trigger campaigns in real-time as users enter and exit their borders, or send follow-up campaigns hours or days later. Users who enter or exit your geofences add a new layer of user data that you can use for segmentation and re-targeting.

Geofences are organized into geofence sets—a group of geofences that can be used to segment or engage users throughout the platform. Each geofence set can hold a maximum of 10,000 geofences.

You can create or upload an unlimited number of geofences.

- Android apps may only store up to 100 geofences locally at a time. Braze is configured to store only up to 20 geofences locally per app.
- iOS devices may monitor up to 20 geofences at a time per app. Braze will monitor up to 20 locations if space is available. 
- If the user is eligible to receive more than 20 geofences, Braze will download the maximum amount of locations based on proximity to the user at the point of session start.
- For geofences to work correctly, you should ensure that your app is not using all available geofence spots.

Refer to the following table for common geofence terms and their descriptions.

| Term | Description |
|---|---|
| Latitude and longitude | The geographic center of the geofence. |
| Radius | The radius of the geofence in meters, measured from the geographic center. We recommend setting a minimum radius of 100–150 meters for all geofences. |
| Cooldown | Users receive geofence-triggered notifications after performing enter or exit transitions on individual geofences. After a transition occurs, there is a pre-defined time during which that user may not perform the same transition on that individual geofence again. This time is called the "cooldown" and is pre-defined by Braze, and its main purpose is to prevent unnecessary network requests. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Manually create geofences

### Step 1: Create a geofence set

To create a geofence, you'll need to create a geofence set first.

1. Go to **Audience** > **Locations** in the Braze dashboard.
2. Select **Create Geofence Set**.
3. For **Set name**, enter a name for your geofence set.
4. (Optional) Add tags to filter your set.

### Step 2: Add the geofences

Next, you can add geofences to your geofence set.

1. Select **Draw Geofence** to click and drag the circle on the map. Repeat to add more geofences to your set as needed.
2. (Optional) You can select **Edit** and replace the geofence description with a name.
3. Select **Save Geofence Set** to save.

{% alert tip %}
We recommend creating geofences with a radius of at least 200 meters for optimal functionality. For more information on configurable options, refer to [Mobile integrations](#mobile-integrations).
{% endalert %}

![A geofence set with two geofences "EastCoastGreaterNY" and "WesternRegion" with two circles on the map.]({% image_buster /assets/img/geofence_example.png %})

## Bulk upload geofences {#creating-geofence-sets-via-bulk-upload}

Geofences may be uploaded in bulk as a GeoJSON object of type `FeatureCollection`. Each geofence is a `Point` geometry type in the feature collection. The properties for each feature require a `radius` key and an optional `name` key for each geofence. 

To upload your GeoJSON, select **More** > **Upload GeoJSON**.

When creating your geofences, consider the following details:

- The `coordinates` value in the GeoJSON is formatted as `[Longitude, Latitude]`.
- The maximum geofence radius that may be uploaded is 10,000 meters (about 10 kilometers or 6.2 miles).

### Example

The following example represents the correct GeoJSON for specifying two geofences: one for Braze headquarters in NYC, and one for the Statue of Liberty south of Manhattan.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Using geofence events

After geofences have been configured, you can use them to enhance and enrich how you communicate with your users.

### Triggering campaigns and Canvases

To use geofence data as part of campaign and Canvas triggers, choose **Action-Based Delivery** for the delivery method. Next, add a trigger action of `Trigger a Geofence`. Finally, choose the geofence set and geofence transition event types for your message. You can also advance users through a Canvas using geofence events.

![An action-based campaign with a geofence that will trigger when a user enters German airports.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalizing messages

To use geofence data to personalize a message, you can use the following Liquid personalization syntax:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Updating geofence sets

For active users, the Braze SDK will only request geofences once per day on session start. That means if changes are made to the geofence sets after session start, you'll need to wait 24 hours from the time the sets are first pulled down to receive the updated set.

{% alert note %}
If the geofences aren't loaded onto the device locally, the user can't trigger the geofence even if they enter the area.
{% endalert %}

## Mobile integrations {#mobile-integrations}

### Cross-platform requirements

Geofence-triggered campaigns are available on iOS and Android. To support geofences, the following must be in place:

1. Your integration must support background push notifications.
2. Braze geofences or location collection must be enabled.
3. For devices on iOS version 11 and up, the user must allow location access always for geofencing to work.

{% alert important %}
Starting with Braze SDK version 3.6.0, Braze location collection is disabled by default. To verify that it's enabled on Android, confirm that `com_braze_enable_location_collection` is set to `true` in your `braze.xml`.
{% endalert %}

Refer to [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence) or [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5) documentation for more guidance based on your platform.

{% alert tip %}
You can also leverage geofences with our Technology Partners, such as [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) and [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)
{% endalert %}

## Frequently asked questions

### What's the difference between geofences and location tracking?

In Braze, a geofence is a different concept from location tracking. Geofences are used as triggers for certain actions. A geofence is a virtual boundary set up around a geographical location. When a user enters or exits this boundary, it can trigger a specific action, such as sending a message.

Location tracking is used to collect and store a user's most recent location data. This data can be used to segment users based on the `Most Recent Location` filter. For example, you could use the `Most Recent Location` filter to target a specific region of your audience, such as sending a message to users located in New York.

### How accurate are Braze geofences?

Braze geofences use a combination of all location providers available to a device to triangulate the user's location. These include Wi-Fi, GPS, and cellular towers.

Typical accuracy is in 20–50m range, and best-case accuracy will be in the 5-10m range. In rural areas, accuracy may degrade significantly, potentially going up to several kilometers. Braze recommends creating geofences with larger radii in rural locations.

For more information on the accuracy of geofences, refer to [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) and [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1) documentation.

### How do geofences affect battery life?

Our geofencing solution uses the native geofence system service on iOS and Android and is tuned to intelligently trade off accuracy and power, saving battery life and improving performance as the underlying service improves.

### When are geofences active?

Braze geofences work at all hours of the day, even when your app is closed. They become active as soon as they are defined and uploaded to the Braze dashboard. However, geofences can't function if a user has disabled location tracking.

For geofences to work, users must have location services enabled on their device and must have granted your app permission to access their location. If a user has disabled location tracking, your app won't be able to detect when they enter or exit a geofence.

### Is geofence data stored in user profiles?

No, Braze doesn't store geofence data on user profiles. Geofences are monitored by Apple and Google location services, and Braze only gets notified when a user triggers a geofence. At that point, we process any associated trigger campaigns.

### Can I set up a geofence within a geofence?

As a best practice, avoid setting up geofences that overlap with each other, as this may cause issues with triggering notifications.

