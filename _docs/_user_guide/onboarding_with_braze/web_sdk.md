---
nav_title: Web SDK
article_title: Web SDK Overview
page_order: 3

page_type: reference
description: "This onboarding reference article covers implementing Braze's Web SDK."

---

# Web SDK

![List of apps in the Settings tab of the Manage Settings page][7]{: style="float:right;max-width:30%;max-height:30vw;margin-left:15px;"}

With Braze’s Web SDK, you can collect session data, identify users (with the same set of attributes that we support across our other platforms), and record purchases and custom events via a web/mobile browser. Implementing Braze's Web SDK enables you to create a more complete view of your users across web and mobile channels. You can also use the Web SDK to engage with your users by sending in-app web messages and web push notifications.

## Implementation

For information on integrating the Braze Web SDK, see [Initial SDK Setup for Web][6]. After implementing the Web SDK, your website will appear as an app in your app group and will be grouped with your mobile apps.

## In-app web messaging

You can send web messages to engage with users directly in their web/mobile browser. Web messages are sent as in-app messages, and can also be sent as slideup, modal, or fullscreen types. For more information on composing an in-app message, see our page on [creating an in-app message][8].

## Web push

![Push displayed on a web browser versus mobile device][12]{: style="float:right;max-width:60%;margin-left:15px;border:0;"}

Web push is another great way to engage with users of your web application. Customers visiting your website via Chrome, Safari, Firefox, and Opera can opt-in to receive web push from your web application whether or not the web page is loaded. 

This feature is also supported on Android Chrome and Firefox Mobile on Android allowing for mobile web notifications. Web push works the same way app push notifications operate on your phone. For more information on composing a web push, see our page on [creating a push notification][11].

Users of your web application need to opt-in to receive web push. 

![System notification requesting push notification permissions][13]

For more information on the push protocol standards and browser support, you can review resources from [Apple][3] [Mozilla][1] and [Microsoft][2]

{% alert important %}
Private browsing windows do not currently support web push.
{% endalert %}

## Delivery rules

By default, a campaign containing an in-app message will send an in-app web message as well as an in-app mobile message. To send an in-app message exclusively to web or mobile, you will need to segment your campaign accordingly.

## Segmenting for web users

You can create a segment of your web users by selecting only your website’s app icon in the **Apps Used** section of a segment.

![Segment Details page with web app selected][10]

This will allow you to target users based on their behavior on the web only. If you wanted to target web users to encourage them to download your mobile app, you’d create this segment as your target audience. If you wanted to send a messaging campaign that included a mobile in-app message but not a web message, you would simply uncheck your website’s icon in your segment.

[1]: https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Mozilla Push API browser compatibility"
[2]: https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Microsoft Push API"
[3]: https://developer.apple.com/notifications/safari-push-notifications/ "Safari Push Notifications"
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[7]: {% image_buster /assets/img_archive/app_group_list.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[10]: {% image_buster /assets/img_archive/web-users-segment.png %}
[11]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[12]: {% image_buster /assets/img_archive/Macbook_Push.png %}
[13]: {% image_buster /assets/img_archive/WebPush_Prompt.png %}
