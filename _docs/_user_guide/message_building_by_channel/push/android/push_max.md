---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Max amplifies Android push notifications by tracking failed push notifications and resending the push when the user is more likely to receive it."

hidden: true
permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Learn about Push Max and how you can use this feature to potentially improve the deliverability of Android push notifications to Asia-Pacific markets.

## What is Push Max?

Push Max amplifies Android push notifications by tracking failed push notifications and resending the push when the user is more likely to receive it.

Some Android devices manufactured by Chinese Original Equipment Manufacturers (OEMs), such as Xiaomi, OPPO, and Vivo, employ a very aggressive battery optimization scheme to extend battery life. This behavior may have the unintended consequence of shutting down background app processing, which reduces the deliverability of push notifications on these devices if the app is not in the foreground. This problem is most prevalent in the Asia-Pacific (APAC) markets.

## Availability

- Available for Android push notifications only
- Not supported for action-based or API-triggered campaigns or Canvases

## Prerequisites

Push notifications sent using Push Max will only be delivered to devices that have at least the following [minimum SDK version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions android:26.3.1 %}

## Using Push Max

{% tabs %}
{% tab Campaigns %}

To use Push Max in your campaign:

1. Create a push campaign.
2. Select **Android Push** as your platform.
3. Go to the **Schedule Delivery** step.
4. Select **Send using Push Max**.

![Android Push Deliverability section of the Schedule Delivery step with the option to "Send using Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

To use Push Max in your Canvas:

1. Add a Message step to your Canvas.
2. Select **Android Push** as your platform.
3. Go to the **Delivery Settings** tab.
4. Select **Send using Push Max**.

![Delivery Settings tab of an Android Push Message step with the option to "Send using Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

The following two features, Intelligent Timing and Time to Live, can be used in tandem with Push Max to increase the deliverability of your Android push notifications.

### Intelligent Timing

Push Max works best when [Intelligent Timing]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/) is turned on. Braze can use Intelligent Timing to calculate and send the push notification at a time when the user is most likely to be using the app and the push is most likely to be delivered.

### Time to Live (TTL)

Braze will track failed push notifications to Firebase Cloud Messaging (FCM) and retry the notification when the user is likely to receive it, for up to 28 days. You can configure this retry period for failed push notifications by changing the **Time to Live** in the **Settings** tab of the Compose step.

![Time to Live field set to 28 days.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:70%"}
