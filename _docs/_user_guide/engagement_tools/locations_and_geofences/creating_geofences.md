---
nav_title: Creating Geofences
article_title: Creating Geofences
page_order: 1
page_type: reference
description: "This reference article covers how to create and configure Geofences."
tool: 
  - Location

---
# Geofences

> This reference article covers how to create and configure Geofences.

At the core of Braze's real-time location offering is the concept of a "geofence." A geofence is a virtual geographic area, represented as latitude/longitude pairs combined with a radius, forming a circle in a specific position on the globe. Geofences can vary in size from the size of a building to the size of an entire city.

You can define geofences on the Braze Dashboard and trigger campaigns in real-time as users enter and exit them across the globe. Geofences are deeply integrated into Braze's segmentation and messaging capabilities. Campaigns can be delivered in real-time to users as they exit or enter geofences, or sent as followups hours or days later. As users enter or exit your geofences, Braze's location analytics also add a new layer of user data that can be used for segmentation and re-targeting. Geofence-specific analytics also generate insight on the activity of particular locations of interest.

Geofences are managed in the **Locations** page in the **Engagement** section. Geofences are organized into geofence sets - a group of geofences that can be used to segment or engage users throughout the platform. Example geofence sets include `All Northeast Regional Stores` or `September Events`. A given geofence set may only contain up to 10,000 geofences.

## Creating Geofence Sets Manually

![locations_main_screen][1]

Once you have created a geofence set, you can manually add geofences by drawing them on the map. We recommend creating geofences with a radius of at least 100 meters for optimal functionality.

## Creating Geofence Sets via Bulk Upload

Geofences may be uploaded in bulk as a GeoJSON object of type `FeatureCollection`. Each individual geofence is a `Point` geometry type in the feature collection. The properties for each feature require a `"radius"` key, and an optional `"name"` key for each geofence.

The sample below represents the correct GeoJSON for specifying two geofences: one for Braze's headquarters in NYC, and one for the Statue of Liberty south of Manhattan. We recommend uploading geofences with a radius of at least 100 meters for optimal functionality.

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
>  The "coordinates" value in the GeoJSON needs to be formatted [Longitude, Latitude]

>  The maximum geofence radius that may be uploaded is 100000 meters (100km/62mi).

## Using Geofence Events

Once geofences have been configured, you can use them to enhance and enrich how you communicate with your users.

### Triggering
To use geofence data as part of campaign and Canvas triggers, choose "Action-based Delivery" for its delivery method. Next, add a trigger action of `Trigger a Geofence`. Finally, choose the geofence set and geofence transition event types for your message. You can also advance users through a Canvas using geofence events.

![action_based_geofence_trigger][2]

### Personalization

To use geofence data to personalize a message, you may use the following Liquid personalization syntax:

{% raw %}
* `{{event_properties.${geofence_name}}}`

* `{{event_properties.${geofence_set_name}}}`
{% endraw %}


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
