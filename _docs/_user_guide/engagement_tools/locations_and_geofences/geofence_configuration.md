---
nav_title: Geofence Configuration
page_order: 3
---

# Geofence Configuration

## Latitude/Longitude

The geographic center of the geofence.

## Radius

The radius of the geofence in meters, measured from the geographic center. We recommend setting a minimum radius of 100 meters for all geofences.

## Cooldown

Users receive geofence triggered notifications after performing enter or exit transitions on individual geofences.  After a transition occurs, there is a pre-defined period of time during which that user may not perform the same transition on that individual geofence again. This period of time is called the "cooldown" and is pre-defined by Braze. Its main purpose is to prevent unnecessary network requests.
