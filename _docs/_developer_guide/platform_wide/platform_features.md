---
nav_title: Platform Features
page_order: 0
---
# Platform Features

Braze provides a comprehensive user engagement solution for your mobile and web applications. The Braze platform has three primary components - the SDK, the dashboard, and the data API.

## SDK

The Braze SDKs can be integrated into your mobile and web applications to provide powerful marketing, customer support, and analytics tools.

| Platform | Approximate SDK Size |
|---|---|
| Android | 800 KB |
| iOS | (IPA - Addition to App File) 1MB - 2MB; (Framework) 30MB |
| Web | 35 KB |

## Dashboard/UI

The dashboard controls all of the data and interactions at the heart of the Braze platform. Marketers can use the site to manage notifications, setup targeted messaging campaigns, and view analytics or feedback. Developers can use the dashboard to manage settings for integrating apps, such as API keys and push notification credentials.

## Data API

The Braze Data API provides a web service where you can record actions taken by your users directly via HTTP, rather than through the mobile and web SDKs. This allows you to add custom events for segmentation purposes directly from a web-based application.

## Granular Targeting and Analysis

### App Analytics
The Braze dashboard displays graphs that are updated in real-time based upon a number of analytics metrics as well as custom events which you instrument in your application.

### User Segmentation

Segmentation allows you to create groups of users based on powerful filters of their in-app behavior, demographic data, social data, etc. Braze also allows you to define any in-app user action as a "custom event" if the desired action is not captured by default. The same is true of user characteristics via "custom attributes". Once a user segment is created on the dashboard, your users will move in and out of the segment as they meet (or fail to meet) the defined criteria. For example, the below image shows a segment which includes all users who have spent money in-app and last used the app more than two weeks ago.

![Segmentation Example][2]

## Multi-Channel Messaging

Once you have defined a segment, Braze's messaging tools allow for multi-channel communication with your users. For example, send a push notification and email to the example segment defined in the previous section. Messaging channels are best used in concert and with regularity to re-engage lost users, retain active users, and energize your brand ambassadors. Moreover, you can use our advanced scheduling options to automate campaigns to specific groups of those users going forward.

### News Feed {#platform-features-news-feed}

When your app opens, the Braze SDK automatically pulls down the user's News Feed -- a set of News Items and Cross-Promotions cards that are controlled on the Braze dashboard. By making a call to the Braze library, you can display the News Feed when a button or action is triggered in your app, providing an in-app notification center that can be updated by non-technical team members without having to change your code or database.

- Braze will track how many clicks and impressions each card in the News Feed receives
- You can schedule a specific time-frame when cards will display, allowing for deep [dayparting][4]
- Cards within the News Feed may be targeted at user segments just like any other message
- In-app messages will automatically appear when a user has new items in their News Feed
- News Feed Items can ["Deeply Link"][5] to in-app content enabling the marketer to provide individualized content navigation for each user. Every process from onboarding, to the surfacing of rich in-app content can be behaviorially targeted and customized using the News Feed and ["Deep Links"][5]

![News Feed Dashboard][6]

#### Cross Promotion Cards

Cross-Promotions are a type of News Feed card which display content from the App Store or Google Play that you have recommended to users.  Cross-promotions are a wonderful way to leverage your user data to accelerate the adoption of other content within your network by moving audiences from one of your apps to another.

- Touching a Cross-Promotion will bring users to the relevant store so that they can download the content
- Users will only see Cross-Promotions for their device's platform in the News Feed
- In iOS, you may recommend books, music, or other content available in the App Store in addition to apps

### Push Notifications {#platform-features-push}

Braze supports the Apple Push Notification Service (APNs) for iOS and Firebase Cloud Messaging (FCM) for Android. Push notifications can be triggered by the publication of messaging campaigns, news items, and replying to user feedback.

![Example Push Dashboard][8]

### In-App Messaging {#platform-features-in-app-messaging}

Braze provides unobtrusive in-app notifications via our custom-built native user interface. Messages can be presented at any time of your choosing (e.g., when users start a new session or complete a specific action) ensuring that your message arrives at the most effective time to engage the user. See our academy section on [creating an in-app message][13] for more details.

![IAM Example][9]

### Email {#platform-features-email}

Send your users rich HTML messages by adding your existing HTML templates or or using our rich text editor. Braze makes it easy to include email as part of your mobile engagement strategy.

![Email Dashboard][10]

### Webhooks {#platform-features-webhooks}

Braze's webhooks allow you to trigger non-app actions such as SMS text message delivery. You can use webhooks to provide other systems and applications with real-time information. The flexibility of this feature allows you to send information to any endpoint.

![Webhooks][22]

### Feedback {#platform-features-feedback}

 The Braze SDK provides a feedback widget that can be added to your app to allow users to leave feedback. Feedback is managed on the dashboard, where you can add internal notes and respond to users via multiple messaging channels. We show the user's Braze profile side-by-side with their feedback so you can easily see the user's device, OS version, app version, and behavioral data. This minimizes the work your support team has to do to understand technical issues.

 {% alert warning %}
This feature is [set to be deprecated]({{ site.baseurl }}/help/release_notes/deprecations/#feedback) on July 1, 2019.
  {% endalert %}




[2]: {% image_buster /assets/img_archive/dashboard_segment_example.png %} "Segmentation Example"
[4]: http://en.wikipedia.org/wiki/Dayparting
[5]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[6]: {% image_buster /assets/img_archive/news_feed_dashboard_example.png %} "News Feed Dashboard"
[7]: {% image_buster /assets/img_archive/News_Feed_Ad2.png %} "News Feed User Interface"
[8]: {% image_buster /assets/img_archive/UOiOSPush.png %} "Example Push Dashboard"
[9]: {% image_buster /assets/img_archive/In-App_Modal.png %} "Slideup Example"
[10]: {% image_buster /assets/img_archive/EmailTemplateEditor.png %} "Email Template Editor"
[22]: {% image_buster /assets/img_archive/Webhook_Body_Edit.png %}
[13]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message/#creating-an-in-app-message
