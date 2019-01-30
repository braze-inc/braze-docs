---
nav_title: Radar
alias: /partners/radar/
---

# Radar Integration

[Radar](https://www.onradar.com/) is a location platform for mobile apps. You can use Radar to add location context and tracking to your iOS and Android apps in <10 lines of code, allowing you to easily identify or retarget users and augment your marketing with rich location data.

The Radar platform has three products: Geofences, Insights, and Places.

* [Geofences](https://www.onradar.com/documentation/geofences): Radar geofencing supports many powerful features, including cross-platform support for unlimited geofences, polygon geofences, stop detection, and accuracy down to 30 meters. Create geofences to receive the `entered_geofence` and `exited_geofence` events.
* [Insights](https://www.onradar.com/documentation/insights): Radar can learn a user’s approximate home and work locations and tell you when a user is at home, at work, or traveling. Turn on Insights on the Radar dashboard to receive the `entered_home`, `exited_home`, `entered_office`, `exited_office`, `started_traveling`, and `stopped_traveling` events.
* [Places](https://www.onradar.com/documentation/places): Radar can tell you when a user visits a place, even if you haven’t set up a geofence for that location. Places have category and chain information. Radar is integrated with Facebook Places, the same place database that powers Facebook and Instagram, with over 140M places worldwide. Turn on Places to receive the `entered_place` and `exited_place` events.

Whenever Radar events are generated, Radar will send custom events and user attributes to Braze. You can use events and user attributes to build location-based segments or trigger location-based campaigns.

## Integration Details
In order to properly map data between the Braze and Radar SDKs, you will need to set the same user ID in both systems, using the `changeUser` method in the Braze SDK and the `setUserId` method in the Radar SDK.

To enable the integration, on the Braze Developer Console page, copy your group identifier. Then, on the Braze Manage App Group page, copy your iOS API keys and Android API keys.

Finally, on the Radar [Integrations page](https://www.onradar.com/integrations) under Braze:

* Set "Enabled" to "Yes"
* Paste in your group identifier and API keys. Note that you can set separate API keys for the Test and Live environments.

Whenever Radar events are generated, Radar will send custom events and user attributes to Braze. Events from iOS devices will be sent using your iOS API keys, and events and user attributes from Android devices will be sent using your Android API keys.

## Use Cases

You can use custom events and user attributes to build location-based segments or trigger location-based campaigns.

For example, to build a segment of users who are currently traveling:

![Radar Segment]({% image_buster /assets/img_archive/radar-segment.png %})

Or, to trigger a campaign when a user enters a Starbucks with high confidence:

![Radar Campaign]({% image_buster /assets/img_archive/radar-campaign.png %})
