---
nav_title: Tracking Push Unsubscribes
article_title: Tracking Push Unsubscribes
page_type: solution
description: "This help article provides some tips to track push unsubscribes."
channel: push
---

# Tracking push unsubscribes

Push unsubscribes depend on updates to a user’s push status from providers like Apple or Google. These updates can be infrequent and unpredictable. As a result, push unsubscribes are not included as a metric in push campaign analytics. 

However, manually tracking push unsubscribes can still provide valuable insights into user responses to your notification frequency and content relevance. Here are two options for tracking push unsubscribes.

## Option 1: Use segment filters

As a workaround, you can create a segment to identify users who aren't push enabled, meaning they're not subscribed or opted-in and don't have a [foreground push token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens). For example, to see the number of unsubscribes in your Android app, you would use the combination of the following segments: 

- `Background or Foreground Push Enabled for App "TEST (Android)" is false`
- `Has Uninstalled`

![The Segment Builder section with the filter "Background or Foreground Push Enabled for App" for the TEST (Android) app is false, and the filter "Has Uninstalled" are selected to show 2,393 reachable users.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Note the segmentation filters will be approximate and cannot be specifically tied to a date and campaign.

## Option 2: Use a custom event

{% alert important %}
Be aware that logging a custom event for subscription change will log [data points]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Alternatively, use segment filters to identify and target users who aren't push enabled.
{% endalert %}

For a different workaround, we also recommend creating a custom event for push unsubscribes based on whether a user's push enabled status is `true` or `false` in order to track this metric.

_Last updated on June 13, 2024_
