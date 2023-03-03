---
nav_title: Geofence Configuration
article_title: Geofence Configuration
page_order: 3
page_type: reference
description: "This reference article covers various Geofence configurations."
tool: Location

---

# Geofence configuration

> This reference article covers various Geofence configuration options available when creating geofence sets.

## Latitude and longitude

The geographic center of the geofence.

## Radius

The radius of the geofence in meters, measured from the geographic center. we recommend setting a minimum radius of 200 meters for all geofences. Only geofences that are within 2,000 kilometer radius are sent down to the users device.

## Cooldown

Users receive geofence-triggered notifications after entering or exiting individual geofences. After a transition occurs, there is a period of time during which that user may not perform the same transition on that individual geofence again. This period of time is called the "cooldown" and is pre-defined by Braze as six hours.

If the app is re-installed, the cooldown will reset. Cooldowns are per geofence and separate for entry and exit, so a user can trigger on entry and exit within 6 hours on the same geofence, but not twice for entry or twice for exit.

The main purpose of cooldown is to prevent unnecessary network requests.

## Technology partners

You can also leverage geofences with some of our partners, for example: 

- [Radar][2]
- [Foursquare][3]

[2]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[3]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/