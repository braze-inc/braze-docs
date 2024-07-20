---
nav_title: Location Tracking
article_title: Location Tracking
page_order: 0
page_type: reference
description: "This reference article explains how to use location tracking and location targeting in your apps and which partners support location tracking."
tool: Location
search_rank: 2
---

# Location tracking

> Location collection captures a user's most recent location when the app was opened using GPS location data. You can use this information to segment data based on users who were in a defined location. 

## Enabling location tracking

To enable location collection on your app, refer to the developer guide for the platform you're using:

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/)

In general, mobile apps will use the device's GPS chip and other systems (such as Wi-Fi scanning) to track a user's location. Web apps will use WPS (Wi-Fi Positioning System) to track a user's locations. All of these platforms will require users opt-in to location tracking.

Note that the accuracy of your location tracking data may be affected by whether or not your users have Wi-Fi enabled on their device. Android users can also choose different location modes—users that are on "Battery saving" or "Device only" mode may have inaccurate data. 

## Location targeting

Using location tracking data and segments, you can set up location-based campaigns and strategies. For example, you may want to run a promotional campaign for users that live in a particular region, or exclude users in a region that has stricter regulations.

Refer to [Location targeting]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) for more information on creating a location segment.

## Hard setting the default location attribute

You can also use the [`users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) in our API to update the [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) standard attribute. An example is: 
```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Technology partners

You can also leverage location tracking with some of our partners: 

- [Radar]({{site.baseurl}}/partners/data_augmentation/contextual_location/radar/)
- [Foursquare]({{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/)
- [Gimbal]({{site.baseurl}}/partners/data_augmentation/contextual_location/gimbal/)

## Frequently asked questions

Check out our [Locations FAQ]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations) for answers to frequently asked questions about locations.

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/data_augmentation/contextual_location/gimbal/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations
