---
nav_title: Platform Features
article_title: Platform Features
page_order: 0
description: "This reference article covers specific platform features including SDK sizes, dashboard UI, multichannel messaging, and more."
platform:
  - iOS
  - Android
  - Web
  
---

# Platform features

Braze provides a comprehensive user engagement solution for your mobile and web applications. The Braze platform has three primary components - the SDK, the dashboard, and the data API.

## SDK

The Braze SDKs can be integrated into your mobile and web applications to provide powerful marketing, customer support, and analytics tools.

| Platform | Approximate SDK Size |
|---|---|
| Android | 800 KB |
| iOS | (IPA - Addition to App File) 1MB - 2MB; (Framework) 30MB |
| Web | 35 KB |
{: .reset-td-br-1 .reset-td-br-2}

## Dashboard/UI

The dashboard controls all of the data and interactions at the heart of the Braze platform. Marketers can use the site to manage notifications, setup targeted messaging campaigns, and view analytics. Developers can use the dashboard to manage settings for integrating apps, such as API keys and push notification credentials.

## Data API

The Braze Data API provides a web service where you can record actions taken by your users directly via HTTP, rather than through the mobile and web SDKs. This allows you to add custom events for segmentation purposes directly from a web-based application.

## Granular targeting and analysis

### App Analytics
The Braze dashboard displays graphs that are updated in real-time based upon a number of analytics metrics as well as custom events that you instrument in your application.

### User segmentation

Segmentation allows you to create groups of users based on powerful filters of their in-app behavior, demographic data, social data, etc. Braze also allows you to define any in-app user action as a "custom event" if the desired action is not captured by default. The same is true of user characteristics via "custom attributes". Once a user segment is created on the dashboard, your users will move in and out of the segment as they meet (or fail to meet) the defined criteria. For example, the below image shows a segment that includes all users who have spent money in-app and last used the app more than two weeks ago.

![Segmentation Example][2]

## Multichannel messaging

Once you have defined a segment, Braze's messaging tools allow for multichannel communication with your users. For example, send a push notification and email to the example segment defined in the previous section. Messaging channels are best used in concert and with regularity to re-engage lost users, retain active users, and energize your brand ambassadors. Moreover, you can use our advanced scheduling options to automate campaigns to specific groups of those users going forward.

### Content Cards {#platform-features-content-cards}

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, Connected Content, custom card expiration times, card analytics, and easy coordination with push notifications.

![Content Cards Feed]({% image_buster /assets/img/cc_feed_new.png %}){: style="max-width:60%"}

### Push notifications {#platform-features-push}

Braze supports the Apple Push Notification Service (APNs) for iOS and Firebase Cloud Messaging (FCM) for Android. Push notifications can be triggered by the publication of messaging campaigns and news items.

![Example Push Dashboard][8]

### In-app messaging {#platform-features-in-app-messaging}

Braze provides unobtrusive in-app notifications via our custom-built native user interface. Messages can be presented at any time of your choosing (e.g., when users start a new session or complete a specific action) ensuring that your message arrives at the most effective time to engage the user. Learn more about [creating an in-app message][13].

![IAM Example][9]

### Email {#platform-features-email}

Send your users rich HTML messages by adding your existing HTML templates, using our rich text editor, or our drag and drop editor. Braze makes it easy to include email as part of your mobile engagement strategy.

![Email Dashboard][10]

### SMS and MMS {#platform-features-sms-mms}

Use SMS with Braze to send transactional notifications, share promotions, send reminders, and more. With over 23 billion text messages sent every day worldwide, SMS is the most direct way to reach users and customers.

![SMS preview example]({% image_buster /assets/img_archive/sms_preview.png %})

### Webhooks {#platform-features-webhooks}

Braze's webhooks allow you to trigger non-app actions provide other systems and applications with real-time information. The flexibility of this feature allows you to send information to any endpoint.

![Webhooks][22]

[2]: {% image_buster /assets/img_archive/dashboard_segment_example.png %} "Segmentation Example"
[4]: http://en.wikipedia.org/wiki/Dayparting
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[6]: {% image_buster /assets/img_archive/news_feed_dashboard_example.png %} "News Feed Dashboard"
[8]: {% image_buster /assets/img_archive/UOiOSPush.png %} "Example Push Dashboard"
[9]: {% image_buster /assets/img_archive/In-App_Modal.png %} "Slideup Example"
[10]: {% image_buster /assets/img_archive/EmailTemplateEditor.png %} "Email Template Editor"
[22]: {% image_buster /assets/img_archive/Webhook_Body_Edit.png %}
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
