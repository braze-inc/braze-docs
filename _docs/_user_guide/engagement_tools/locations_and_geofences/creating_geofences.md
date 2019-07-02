---
nav_title: Creating Geofences
page_order: 1
---

# Creating Geofence Sets Manually

![locations_main_screen][1]

Once you have created a geofence set, you can manually add geofences by drawing them on the map. We recommend creating geofences with a radius of at least 100 meters for optimal functionality.

# Creating Geofence Sets via Bulk Upload

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

>  The maximum geofence radius that may be uploaded is 100000 meters (100km/62mi).

# Using Geofence Events

Once geofences have been configured, you can use them to enhance and enrich how you communicate with your users.

## Triggering
To use geofence data as part of campaign and canvas triggers, choose "Action-based Delivery" for its delivery method. Next, add a trigger action of `Trigger a Geofence`. Finally, choose the geofence set and geofence transition event types for your message. You can also advance users through a Canvas using geofence events.

![action_based_geofence_trigger][2]

## Personalization

To use geofence data to personalize a message, you may use the following Liquid personalization syntax:

{% raw %}
* `{{event_properties.${geofence_name}}}`

* `{{event_properties.${geofence_set_name}}}`
{% endraw %}


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
