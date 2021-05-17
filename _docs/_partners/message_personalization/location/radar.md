---
nav_title: Radar
alias: /partners/radar/

description: "This article outlines the partnership between Braze and Radar to add location context and tracking to your iOS and Android apps."
page_type: partner

---

# Radar Integration

> [Radar](https://www.onradar.com/) is a location platform for mobile apps.

You can use Radar to add location context and tracking to your iOS and Android apps in less than 10 lines of code, allowing you to easily retarget to your customers and augment your marketing with rich location data.

The Radar platform has three products: [Geofences](https://radar.io/product/geofencing), [Trip Tracking](https://radar.io/product/trip-tracking), and [Geo APIs](https://radar.io/product/api).

Whenever Radar events are generated, Radar will send __custom events__ and __user attributes__ to Braze. You can use events and user attributes to build location-based segments or trigger location-based campaigns.

## Integration Details
In order to properly map data between the Braze and Radar SDKs, you will need to set the same user ID in both systems, using the `changeUser` method in the Braze SDK and the `setUserId` method in the Radar SDK.

To enable the integration, go to the Braze `Developer Console` page and copy your group identifier. Then, on the Braze `Manage Settings` page, copy your iOS API keys and Android API keys.

Finally, on the Radar [Integrations page](https://www.onradar.com/integrations) under Braze:

* Set "Enabled" to "Yes".
* Paste in your group identifier and API keys.

{% alert note %}
  You are able to set separate API keys for the Test and Live environments.
{% endalert %}

Whenever Radar events are generated, Radar will send custom events and user attributes to Braze. Events from iOS devices will be sent using your iOS API keys; events and user attributes from Android devices will be sent using your Android API keys.

## Use Cases

You can use custom events and user attributes to build location-based segments or trigger location-based campaigns.

For example, to build a segment of users who are currently traveling:

![Radar Segment]({% image_buster /assets/img_archive/radar-segment.png %})

Or, to trigger a campaign when a user enters a Starbucks with high confidence:

![Radar Campaign]({% image_buster /assets/img_archive/radar-campaign.png %})
