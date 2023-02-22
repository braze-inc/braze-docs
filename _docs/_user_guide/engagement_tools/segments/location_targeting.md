---
nav_title: Location Targeting
article_title: Location Targeting
page_order: 6.5
page_type: tutorial
tool: 
- Segments
- Location
description: "This how-to article will walk you through how to set up Location targeting, allowing you to segment users by location."

---

# Location targeting

> This article will walk you through how to set up Location Targeting, allowing you to segment users by their most recent location. This is perfect for if you are looking into location-based campaigns and strategies.

## Step 1: Create your segment

Navigate to the **Segments** page, under **Engagement**, to view all of your current user segments. On this page, you can create and name new segments. To get started, click **Create Segment** and give your segment a name.

![][1]{: style="max-width:70%;"}

## Step 2: Customize your location

Once you have created your segment, add a **Most Recent Location** filter to target users by the last place that they used your app. You have the option of either highlighting users in a standard circular region or a customizable polygonal region.

![][2]

### Circular regions

For circular regions, you can move the origin and adjust the location radius for your segmentation.

![A circular outline of cities between New Jersey and New York.][3]{: style="max-width:70%;"}

### Polygonal regions

For polygonal regions, you can more specifically designate which areas you wish to be included in your segment.

![An outline of New York state as the selected polygonal region.][4]{: style="max-width:70%;"}

## Technology partners 

Interested in taking advantage of location targeting with the help of a Braze partner? Check out our available Braze [contextual location partners]({{site.baseurl}}/partners/message_personalization/location/). Some examples are listed below.

### Radar support

Radar has full support for unlimited custom geofences, pre-built POI geofences, beacon detection, region detection, trip tracking, and more. When you enable the Radar and Braze integration, Radar forwards real time location events and user attributes which can be used to trigger real time campaigns, power last mile pickup and delivery operations, optimize fleet tracking and shipping logistics, or build user segments based on location patterns. Additionally, Radar Geo APIs can be leveraged to enrich or personalize your marketing campaigns through Connected Content. Visit [Radar integrations]({{site.baseurl}}/partners/message_personalization/location/radar/#radar) to learn more.

### Gimbal support

Connecting your Gimbal account to Braze lets you track when your users enter or leave your defined places and trigger events off of these entries and exits. In addition, you can track extra information like the place name or the dwell visit as an event property so that you can personalize your messaging even further. Visit [Gimbal integrations]({{site.baseurl}}/partners/message_personalization/location/gimbal/) for more information.

{% alert note %}
Note that this will work the same for Gimbal's beacons as well as their geofence solutions.
{% endalert %}

[1]: {% image_buster /assets/img_archive/createsegment2.png %}
[2]: {% image_buster /assets/img_archive/filter_recent_location.png %}
[3]: {% image_buster /assets/img_archive/location_circle.png %}
[4]: {% image_buster /assets/img_archive/create_polygon.png %}
