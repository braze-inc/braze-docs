---
nav_title: Location Tracking
article_title: Location Tracking
page_order: 0
page_type: reference
description: "This reference article explains how to use location tracking and location targeting in your apps."
tool: Location
---

# Location tracking

Location collection captures a user's most recent location when the app was opened using GPS location data. You can use this information to segment data based on users who were in a defined location.

## Enabling location tracking

To enable location collection on your app, take a look at the appropriate developer guide for the platform you are using:

- [iOS][2]
- [Android][3]
- [Web][4]

In general, mobile apps will use the device's GPS chip and other systems (such as Wi-Fi scanning) to track a user's location. Web apps will use WPS (Wi-Fi Positioning System) to track a user's locations.

Note that the accuracy of your location tracking data may be affected by whether or not your users have wi-fi enabled on their device. Android users can also choose different location modes—users that are on "Battery saving" or "Device only" mode may have inaccurate data.

## Location targeting

Using location tracking data, you can set up location-based campaigns and strategies. For example, you may want to run a promotional campaign for users that live in a particular region, or exclude users in a region that has stricter regulations.

See [this article][1] for more information on location targeting.

## Hard setting the default location attribute

You can also use the [`users/track`][8] endpoint in our API to update the [`current_location`][9] default attribute—for example:
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

You can also leverage location tracking with some of our partners, for example:

- [Neura][5]
- [Radar][6]
- [Foursquare][7]
- [Gimbal][10]

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.trackLocation
[5]: {{site.baseurl}}/partners/data_augmentation/contextual_location/neura_actions/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/data_augmentation/contextual_location/gimbal/