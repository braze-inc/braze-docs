---
nav_title: Creating Geofences
article_title: Creating Geofences
page_order: 1
page_type: reference
description: "This reference article covers what geofences are, and how to create and configure geofence events."
tool: 
  - Location
search_rank: 9
---

# Geofences

> At the core of our real-time location offering is the concept of a geofence. A geofence is a virtual geographic area, represented as latitude and longitude combined with a radius, forming a circle around a specific global position. Geofences can vary from the size of a building to the size of an entire city.

You can define geofences on the Braze dashboard and use them to trigger campaigns in real-time as users enter and exit their borders, or send follow-up campaigns hours or days later. Users who enter or exit your geofences add a new layer of user data that you can use for segmentation and re-targeting.

## Overview

Manage geofences from **Audience** > **Locations**.

Geofences are organized into geofence sets—a group of geofences that can be used to segment or engage users throughout the platform. Each geofence set can hold a maximum of 10,000 geofences.

You may create or upload an unlimited amount of geofences on the dashboard, allowing your marketing team to setup geofence sets and campaigns without needing to calculate numbers of geofences. Braze will dynamically re-synchronize the geofences that it tracks for each individual user, ensuring that the most relevant geofences to them are always available.

- Android apps may only store up to 100 geofences locally at a time. Braze is configured to store only up to 20 geofences locally per app.
- iOS devices may monitor up to 20 geofences at a time per app. Braze will monitor up to 20 locations if space is available. 
- If the user is eligible to receive more than 20 geofences, Braze will download the maximum amount of locations based on proximity to the user at the point of session start/silent push refresh
- For geofences to work correctly, you should ensure that your app is not using all available geofence spots.

## Creating geofence sets

### Creating sets manually

From the **Locations** page, click **+ Create Geofence Set**.

![Geofence set of German airports with a user drawing a radius of two thousand meters on the map for Hamburg Airport.][1]

Once you have created a geofence set, you can manually add geofences by drawing them on the map. We recommend creating geofences with a radius of at least 200 meters for optimal functionality. For more information on configurable options, refer to [Geofence configuration]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/mobile_integrations/).

### Creating sets via bulk upload {#creating-geofence-sets-via-bulk-upload}

Geofences may be uploaded in bulk as a GeoJSON object of type `FeatureCollection`. Each individual geofence is a `Point` geometry type in the feature collection. The properties for each feature require a `"radius"` key, and an optional `"name"` key for each geofence. To upload your GeoJSON, click **+ Create Geofence Set** followed by **Upload GeoJSON**.

The following sample represents the correct GeoJSON for specifying two geofences: one for Braze headquarters in NYC, and one for the Statue of Liberty south of Manhattan. We recommend uploading geofences with a radius of at least 100 meters for optimal functionality.

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

When creating your geofences, keep the following points in mind:

- The `coordinates` value in the GeoJSON is formatted as [Longitude, Latitude].
- The maximum geofence radius that may be uploaded is 10,0000 meters (about 100 kilometers or 62 miles).

## Updating geofence sets

For active users, the Braze SDK will only request geofences once per day on session start. That means if changes are made to the geofence sets after session start, you'll need to wait 24 hours from the time the sets are first pulled down to receive the updated set.

For inactive users, if the user is background push enabled, Braze will also send a silent push once every 24 hours to pull down the latest locations to the device.

{% alert note %}
If the geofences aren't loaded onto the device locally, the user can't trigger the geofence even if they enter the area.
{% endalert %}

### Update for individual users

Updating geofences for individual users may be helpful when testing. To update geofence sets, navigate to the bottom of the **Locations** page and click **Re-sync Geofences**. You will then be prompted to enter `external_id` or `email` of the users you would like to update

## Using geofence events

Once geofences have been configured, you can use them to enhance and enrich how you communicate with your users.

### Triggering

To use geofence data as part of campaign and Canvas triggers, choose **Action-Based Delivery** for the delivery method. Next, add a trigger action of `Trigger a Geofence`. Finally, choose the geofence set and geofence transition event types for your message. You can also advance users through a Canvas using geofence events.

![][2]

### Personalization

To use geofence data to personalize a message, you can use the following Liquid personalization syntax:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Frequently asked questions

Visit [Geofence FAQ][3] for answers to frequently asked questions about geofences.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
