---
nav_title: Overview
article_title: In-App Message Overview for Roku
platform: Roku
channel: in-app messages
page_order: 0
page_type: reference
description: "This article covers an overview of Roku in-app messaging, including best practices and use cases."

---

# In-app messages

[In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

Check out our [case studies][6] to see examples of in-app messages.

![Three images of potential Roku in-app messages that a user could build. These examples include "full-screen takeover", "homepage banner", and "corner notifier".][3]

## In-app message types

Create an in-app message for Roku by selecting **Roku Devices** as the in-app message platform.

![][4]

## Technical documentation

Visit our [integration guide][5] for instructions on displaying in-app messages and logging impressions and click analytics.

![A "homepage banner" example showing the different components needed to build the custom banner. Components listed include the message composition component (showing the body, button text, image, assigned button behavior (deep link), and key-value pairs), the backend details (audience listed as "users who watched season 1", intended interactions (button beeplinks to app, closing the message dismisses the message, and automatic dismissal after 10 seconds), the trigger (session start), and the key-value pair (template = homepage_banner)).][2]

## Testing and QA

The test send feature is not supported for Roku in-app messages. To test a message, launch the campaign filtered to only your user ID.

[1]: {% image_buster /assets/img/roku/Roku-In-App-Messages-Flow.png %}
[2]: {% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %}
[3]: {% image_buster /assets/img/roku/Docs-Imagery.png %}
[4]: {% image_buster /assets/img/roku/1-Platform-Selector.png %}
[5]: {{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration
[6]: https://www.braze.com/customers
