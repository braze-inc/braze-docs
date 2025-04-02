---
nav_title: Push TTL Settings
article_title: Push TTL Settings
page_order: 16
page_type: reference
description: "This reference article covers the Push Time to Live settings page in the Braze dashboard."
channel: push

---

# Push TTL settings

> Learn about the Push Time to Live settings page in the Braze dashboard.

## What is Push TTL?

Push Time to Live (TTL) controls how long Braze will attempt to deliver a push notification to devices that are offline at the time the campaign is sent. If a device reconnects after the TTL expires, the message won’t be delivered. This setting will not remove a notification if it has already been received by the user's device—it only controls how long the push provider attempts to deliver a notification.

## Setting default Push TTL values

By default, Braze sets the Push TTL to the maximum for each push messaging service. 

| Push messaging service | Maximum TTL |
| --- | --- |
| Web (through FCM or Web Push services) | 28 days |
| Firebase Cloud Messaging (FCM) | 28 days |
| Kindle (ADM) | 31 days |
| Huawei (HMS) | 15 days |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

These settings apply globally to all push campaigns unless a different TTL is set for a specific message. To adjust a message's TTL, see [Advanced campaign settings]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl).

To set a different default Push TTL:

1. Go to **Settings** > **Manage Settings** > **Push TTL Settings**.
2. For each Android platform, define a default time to live value. You can set smaller increments like hours or seconds for more precise control.
3. Select **Save** to apply your changes.

![Push Time to Live Settings tab under Manage Settings][1]


[1]: {% image_buster /assets/img/push_ttl.png %}
