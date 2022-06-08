---
nav_title: Creating Geofences
article_title: Creating Geofences
page_order: 1
page_type: reference
description: "This reference article covers what geofences are, and how to create and configure them."
tool: 
  - Location

---
# Geofences

> This reference article covers what geofences are, and how to create and configure them.

At the core of Braze's real-time location offering is the concept of a "geofence." A geofence is a virtual geographic area, represented as latitude/longitude pairs combined with a radius, forming a circle in a specific position on the globe. Geofences can vary in size from the size of a building to the size of an entire city.

You can define geofences on the Braze dashboard and trigger campaigns in real-time as users enter and exit them across the globe. Geofences are deeply integrated into Braze's segmentation and messaging capabilities. Campaigns can be delivered in real-time to users as they exit or enter geofences, or sent as followups hours or days later. As users enter or exit your geofences, they add a new layer of user data that can be used for segmentation and re-targeting.

Geofences are managed in the **Locations** page in the **Engagement** section. Geofences are organized into geofence sets—a group of geofences that can be used to segment or engage users throughout the platform. Example geofence sets include `All Northeast Regional Stores` or `September Events`. A given geofence set may only contain up to 10,000 geofences.

## Creating geofence sets manually

From the **Locations** page, click **+ Create Geofence Set**.

![Geofence set of German airports with a user drawing a radius of two thousand meters on the map for Hamburg Airport.][1]

Once you have created a geofence set, you can manually add geofences by drawing them on the map. We recommend creating geofences with a radius of at least 100 meters for optimal functionality. For more information on configurable options, refer to [Geofence configuration]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/geofence_configuration/).

## Creating geofence sets via bulk upload {#creating-geofence-sets-via-bulk-upload}

Geofences may be uploaded in bulk as a GeoJSON object of type `FeatureCollection`. Each individual geofence is a `Point` geometry type in the feature collection. The properties for each feature require a `"radius"` key, and an optional `"name"` key for each geofence. To upload your GeoJSON, click **+ Create Geofence Set** followed by **Upload GeoJSON**.

The following sample represents the correct GeoJSON for specifying two geofences: one for Braze's headquarters in NYC, and one for the Statue of Liberty south of Manhattan. We recommend uploading geofences with a radius of at least 100 meters for optimal functionality.

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
    }, ...
  ]
```

When creating your geofences, keep the following points in mind:

- The `coordinates` value in the GeoJSON is formatted as [Longitude, Latitude].
- The maximum geofence radius that may be uploaded is 10,0000 meters (about 100 kilometers or 62 miles).

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

Visit [Geofence FAQs][3] for answers to frequently asked questions about geofences.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
