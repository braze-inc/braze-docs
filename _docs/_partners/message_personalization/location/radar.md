---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "This article outlines the partnership between Braze and Radar, a geofencing platform, to add location context and tracking to your iOS and Android apps."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/) is the leading geofencing and location tracking platform. The Radar platform has three core products: [Geofences](https://radar.io/product/geofencing), [Trip Tracking](https://radar.io/product/trip-tracking), and [Geo APIs](https://radar.io/product/api). Combining Braze’s industry-leading engagement platform and Radar’s industry-leading geofencing capabilities allows you to drive revenue and loyalty through a wide range of location-based product and service experiences.

The Radar and Braze integration allows you to gain access to sophisticated location-based campaign triggers and user profile enrichment with rich, first-party location data. 

Whenever Radar geofence or trip tracking events are generated, Radar will send custom events and user attributes to Braze in real time. You can use these events and attributes to trigger location-based campaigns, power last mile pickup and delivery operations, monitor fleet and shipping logistics, or build user segments based on location patterns. 

Additionally, Radar Geo APIs can be leveraged to enrich or personalize your marketing campaigns through [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/). 

## Prerequisites

| Requirement | Description |
|---|---|---|---|
| Braze REST API key | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Group identifier | Your group identifier can be found can be found within the __Braze Dashboard -> Developer Console__ page. |
| iOS API key and Android API key | These API keys can be found within the __Braze Dashboard -> Manage Settings__ page. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

To map data between the Braze and Radar SDKs, you must set the same user IDs in both systems. This can be done using the `changeUser()` method in the Braze SDK and the `setUserId()` method in the Radar SDK.

To enable the integration on the [Radar integration page](https://www.onradar.com/integrations) under Braze:
  - Set __Enabled__ to __Yes__
  - Set your Braze endpoint
  - Paste in your group identifier and API keys
  - Input any event or event attribute filtering to ensure only relevant data is sent to Braze for engagement marketing

{% alert note %}
You can set separate API keys for the test and live environments.
{% endalert %}

Whenever Radar events are generated, Radar will send custom events and user attributes to Braze. Events from iOS devices will be sent using your iOS API keys; events and user attributes from Android devices will be sent using your Android API keys.

## Event and attribute-based use cases

You can use custom events and user attributes to build location-based segments or trigger location-based campaigns.

### Segment of traveling users

Send a push notification to the user when they’ve arrived at your store for a curbside pickup. 

![Radar Segment]({% image_buster /assets/img_archive/radar-segment.png %})

### Trigger when a user enters a location with high confidence

Send a notification as a user walks into your store

![Radar Campaign]({% image_buster /assets/img_archive/radar-campaign.png %})

## Connected Content

The following example shows how to run a promotion to drive nearby users in-store with a digital offer. 

![Connected Content Example][1]{: style="float:right;max-width:30%;border:0;"}

To get started, you'll need to have your Radar publishable API key on hand to use within your request URLs.

Next, within a `connected_content` tag, make a GET request to the [Search Places API](https://radar.io/documentation/api#search-places). The search places API returns nearby locations based on [Radar Places](https://radar.io/documentation/places): a database of locations for places, chains, and categories that provides a comprehensive view of the world.

Shown below is an example of what Radar will return as a JSON object from the API call:

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

To construct the Connected Content targeted and personalized Braze message, you can leverage the Braze `most_recent_location` attribute as an input for the `near` parameter in the API request's URL. The `most_recent_location` attribute is collected via the Radar event integration or directly through the Braze SDK.

In the example below, the Radar chain filtering is applied for Target and Walmart locations, and the search radius for nearby locations is set to 2 km.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

As you can see from the `connect_content` tag above, the JSON object is stored into the local variable `nearbyplaces` by adding `:save nearbyplaces` after the URL.
You can test what the output should be by referencing {% raw %}`{{nearbyplaces.places}}`{% endraw%}.

Bringing our use-case together, here is what the syntax of the campaign would look like. The code below iterates through the `nearbyplaces.places` object, extracting unique values and concatenating them with proper human-readable delimiters for the message.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }} 
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
Visit [Radar documentation](https://radar.io/documentation/api) for all the Radar APIs that can be leveraged in Connected Content.
{% endalert %}

[1]: {% image_buster /assets/img/radar_example.png %}
