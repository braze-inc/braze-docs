---
nav_title: Location tracking
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

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

In general, mobile apps will use the device's GPS chip and other systems (such as Wi-Fi scanning) to track a user's location. Web apps will use WPS (Wi-Fi Positioning System) to track a user's location. All of these platforms will require users to opt-in to location tracking. The accuracy of your location tracking data may be affected by whether or not your users have Wi-Fi enabled on their devices. Android users can also choose different location modes—users that are on "Battery saving" or "Device only" mode may have inaccurate data.

### SDK user location by IP address

As of November 26, 2024, Braze will detect user locations from the geolocated country using the IP address from the start of the first SDK session. 

Before this, Braze used the country code from the device locale during SDK user creation and for the duration of the first session. Only after processing the first session start would the IP address be used for setting the more reliable country on the user. This meant that user country was set with greater accuracy only from the second session onwards, only after the first session start was processed.

Now, Braze will use the IP address to set the country value on user profiles created via the SDK, and that IP-based country setting will be available during and after the first session.

## Location targeting

Using location tracking data and segments, you can set up location-based campaigns and strategies. For example, you may want to run a promotional campaign for users who live in a particular region or exclude users in a region that has stricter regulations.

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

## Partnership support for beacon and geofence

Combining existing beacon or geofence support with our targeting and messaging features gives you more information about your users' physical actions so you can message them accordingly. You can leverage location tracking with some of our partners: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Frequently asked questions

### When does Braze collect location data?

Braze only collects location when the application is open in the foreground. As a result, our `Most Recent Location` filter targets users based upon where they last opened the application (also referred to as session start).

You should also keep the following nuances in mind:

- If location is disabled, the `Most Recent Location` filter will show the last location recorded.
- If a user has ever had a location stored on their profile, they will qualify for the `Location Available` filter, even if they've opted out of location tracking since then.

### What's the difference between the Most Recent Device Locale and Most Recent Location filters?

The `Most Recent Device Locale` comes from the user's device settings. For example, this appears for iPhone users in their device at **Settings** > **General** > **Language & Region**. This filter is used to capture language and regional formatting, such as dates and addresses, and is independent of the `Most Recent Location` filter.

The `Most Recent Location` is the last known GPS location of the device. This is updated on session start and is stored on the user's profile.

### If a user opts out of location tracking, will their old location data be removed from Braze?

No. If a user has ever had a location stored on their profile, that data will not be automatically removed if they later opt out of location tracking.

