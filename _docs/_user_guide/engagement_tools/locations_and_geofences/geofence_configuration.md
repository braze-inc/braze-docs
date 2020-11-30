---
nav_title: Geofence Configuration
page_order: 3
description: "This reference article covers various GeoFence configurations."

---

# Geofence Configuration

## Latitude/Longitude

The geographic center of the geofence.

## Radius

The radius of the geofence in meters, measured from the geographic center. We recommend setting a minimum radius of 100 meters for all geofences.

## Cooldown

Users receive geofence triggered notifications after performing enter or exit transitions on individual geofences.  After a transition occurs, there is a pre-defined period of time during which that user may not perform the same transition on that individual geofence again. This period of time is called the "cooldown" and is pre-defined by Braze. Its main purpose is to prevent unnecessary network requests.

## Technology Partners
You can also leverage geofences with some of our partners, for example: 

- [Neura][1]
- [Radar][2]
- [Foursquare][3]

[1]: {{site.baseurl}}/partners/data_augmentation/contextual_location/neura_actions/
[2]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[3]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/