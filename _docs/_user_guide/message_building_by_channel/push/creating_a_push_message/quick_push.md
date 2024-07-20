---
nav_title: Quick Push Campaigns
article_title: Quick Push Campaigns
alias: "/quick_push/"
description: "This article describes things to know when creating a push campaign using the quick push editing experience."
---

# Quick push campaigns

When creating a push campaign in Braze, you can select multiple platforms and devices to craft one message for all platforms in a single editing experience called quick push.

{% alert important %}
This functionality is only available for campaigns.
{% endalert %}

## Use cases

This editing experience is best for the following use cases:

- Mobile push campaigns that need to be sent to multiple device types (such as both iOS and Android).
- Time-sensitive push notifications that need to target multiple platforms quickly and accurately, where content is the same across platforms (such as breaking news or live game updates).

## Creating a quick push campaign

To create a campaign targeting multiple platforms and devices:

1. Go to **Campaigns** and click **Create Campaign**.
2. Select **Push Notification**.
3. Select your desired platforms (Mobile, Web, Kindle) and mobile devices (iOS, Android). If you select multiple devices, multivariate testing will not be available for your campaign.

![Options to select multiple platforms for a push campaign, such as Mobile, Web, and Kindle, and multiple devices, such as iOS and Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

{:start="4"}
4. Click **Next**. After clicking **Next**, you will be unable to change your selected platforms or devices.
5. Continue setting up your push campaign.

Your composer will look slightly different from usual. Keep reading to see what's different.

### What's different

On the **Compose** tab, you can specify one title, message, and on-click behavior for all of your chosen platforms and devices.

The preview pane shows an approximation of what your message will look like for each platform. While it can give you a good indicator of where you might reach character limits, remember to always test your messages on a real device before sending your campaign.

![Single editing view with one title, message, and on-click behavior field for three push types: iOS, Android, and Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

In the **Assets** section, select or upload the images you want to appear for each platform. Keep in mind that different devices have different specifications for images and character counts. Refer to [Push message and image formats]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) for help.

![Assets section of the single editing view with fields for Push Icon Image, iOS notification image, Android notification image, and Web notification image.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Then, finish setting up your push campaign as normal. See [Creating a push campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) for more details.

## Things to know

### Notification type

The notification type defaults to "Standard Push" and cannot be changed. If you want to create a different push, such as Push Stories or Inline Image (Android), create separate campaigns for each device type.

### Multivariate testing

If you select multiple devices for mobile platforms, such as both iOS and Android, multivariate testing will not be available for your campaign. If you want to perform multivariate testing, create separate campaigns for each device type.

### Device-specific settings

Settings specific to iOS and Android are not supported when multiple platforms or devices are selected. This includes settings like [push action buttons]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), notification channels and groups, TTL, display priority, sounds, and more.

For more information on device-specific settings, refer to the following article collections:

- [iOS options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios)
- [Android options]({{site.baseurl}}/user_guide/message_building_by_channel/push/android)



