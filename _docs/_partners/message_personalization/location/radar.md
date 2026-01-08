---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "This reference article outlines the partnership between Braze and Radar, a geofencing platform, to add location context and tracking to your iOS and Android apps."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.radar.com/) is the leading geofencing and location tracking platform. The Radar platform has three core products: [Geofences](https://radar.com/product/geofencing), [Trip Tracking](https://radar.com/product/trip-tracking), and [Geo APIs](https://radar.com/product/api). Combining the Braze industry-leading engagement platform and Radar's industry-leading geofencing capabilities allows you to drive revenue and loyalty through a wide range of location-based product and service experiences. These include pickup and delivery tracking, location-triggered notifications, contextual personalization, location verification, store locators, address autocomplete, and more.

_This integration is maintained by Radar._

## About the integration

The Braze and Radar integration allows you to access sophisticated location-based campaign triggers and user profile enrichment with rich, first-party location data. When Radar geofence or trip tracking events are generated, custom events and user attributes are sent to Braze in real-time. These events and attributes can then be used to trigger location-based campaigns, power last-mile pickup and delivery operations, monitor fleet and shipping logistics, or build user segments based on location patterns. 

Additionally, Radar Geo APIs can be used to enrich or personalize your marketing campaigns through [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/). 

## Prerequisites

| Requirement | Description |
|---|---|
| Radar account | A Radar account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| App identifier | Your [app identifier]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) can be found can be found within the Braze dashboard from **Settings** > **API Keys**. |
| iOS API key<br>Android API key | These API keys can be found within the Braze dashboard from **Settings** > **App Settings**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

To map data between the Braze and Radar SDKs, you must set the same user IDs or user aliases in both systems. This can be done using the `changeUser()` method in the Braze SDK and the `setUserId()` method in the Radar SDK.

To enable the integration:

1. In Radar on the [Integrations](https://radar.com/documentation/integrations) page, locate Braze.
1. Set **Enabled** to **Yes**.
3. Paste in your app identifier and API keys.

{% alert note %}
You can set separate API keys for test and live environments.
{% endalert %}

{:start="4"}
4. Select your Braze endpoint.
5. Input any event or event attribute filtering to ensure only relevant data is sent to Braze for engagement marketing. Whenever Radar events are generated, Radar will send custom events and user attributes to Braze. Events from iOS devices will be sent using your iOS API keys; events and user attributes from Android devices will be sent using your Android API keys.

{% alert note %}
By default, Radar `userId` maps to Braze `external_id` for logged in users. However, you can track logged out users or specify custom mappings by setting Radar `metadata.brazeAlias` or `metadata.brazeExternalId`. If you set `metadata.brazeAlias`, you must also add a matching alias in Braze with label `radarAlias`.
{% endalert %}

## Event and attribute-based use cases

You can use custom events and user attributes to build location-based segments or trigger location-based campaigns.

### Trigger a store arrival notification for curbside pickup 

Send a push notification to the user with arrival instructions as they arrive at your store for a curbside pickup.

![An action-based delivery campaign showing that the campaign will be delivered when the "arrived_at_trip_destination" custom event occurs, and the "trip_metadata" equals "curbside".]({% image_buster /assets/img_archive/radar-campaign.png %})

### Build an audience segment of recent store visitors

For example, target any users who have visited your store within the past 7 days, whether they made a purchase or not.

![A segment where "radar_geofence_tags" includes value my_store and "radar_updated_at" was less than 7 days ago.]({% image_buster /assets/img_archive/radar-segment.png %})

## Connected Content

The following example shows how to run a promotion to drive nearby users in-store with a digital offer. 

![An Android image of a Connected Content push message that displays "New In Store Deals, Walmart and target near you".]({% image_buster /assets/img/radar_example.png %}){: style="float:right;max-width:30%;border:0;"}

To get started, you'll need to have your Radar publishable API key on hand to use within your request URLs.

Next, within a `connected_content` tag, make a GET request to the [Search Places API](https://radar.com/documentation/api#search-places). The search places API returns nearby locations based on [Radar Places](https://radar.com/documentation/places): a database of locations for places, chains, and categories that provides a comprehensive view of the world.

The following code snippet is an example of what Radar will return as a JSON object from the API call:

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

To construct the Connected Content targeted and personalized Braze message, you can use the Braze `most_recent_location` attribute as an input for the `near` parameter in the API request's URL. The `most_recent_location` attribute is collected via the Radar event integration or directly through the Braze SDK.

In the following example, the Radar chain filtering is applied for Target and Walmart locations, and the search radius for nearby locations is set to 2 km.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

As you can see from the `connect_content` tag, the JSON object is stored into the local variable `nearbyplaces` by adding `:save nearbyplaces` after the URL.
You can test what the output should be by referencing {% raw %}`{{nearbyplaces.places}}`{% endraw%}.

Bringing our use-case together, here is what the syntax of the campaign would look like. The following code iterates through the `nearbyplaces.places` object, extracting unique values and concatenating them with proper human-readable delimiters for the message.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
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
Visit [Radar documentation](https://radar.com/documentation/api) for all the Radar APIs that can be used in Connected Content.
{% endalert %}


