---
nav_title: Platform Overview
article_title: Platform Overview
page_order: 1
description: "This article covers the basic parts and capabilities of the Braze platform. Links from this article connect to essential Braze topics."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
  
---

# Getting started: Platform overview

> This article covers the basic parts and capabilities of the Braze platform. Links from this article connect to essential Braze topics.

Braze is a customer engagement platform. This simply means that Braze helps you listen to your users, understand your users’ actions and behaviors, and then act on them. The Braze platform has three primary components: the SDK, the dashboard, and the REST API.

![Braze has different layers. In total, it consists of the SDK, the API, and partner integrations. These each contribute parts of a data ingestion layer, a classification layer, an orchestration layer, a personalization layer, action layer, and an export layer. The action layer has various channels, including push, in-app messages, Connected Catalog, webhook, SMS, and email.][17]{: style="max-width:55%;float:right;margin-left:15px;"} 

## SDK
The Braze SDKs can be integrated into your mobile and web applications to provide powerful marketing, user management, and analytics tools. The Braze SDK provides two critical pieces of functionality: it collects and syncs user data into a consolidated user profile, and powers messaging channels such as push notifications, in-app messages, and Content Cards.

## Dashboard user interface
The dashboard is the UI that controls all of the data and interactions at the heart of the Braze platform. Marketers will use the dashboard to do their job and create content. Developers use the dashboard to manage settings for integrating apps, such as API keys and push notification credentials. 

If you're just getting started, your team administrator should add you (and all other team members who need access to Braze) as [users on your dashboard][1].

## REST API
The Braze API provides a web service where you can record actions taken by your users directly via HTTP, rather than through the mobile and web SDKs. This allows you to add custom events for segmentation purposes directly from a web-based application. The [API guide][2] lists available Braze API endpoints and their uses.

For more on the parts and pieces of Braze, check out: [Getting Started: Architecture overview]({{site.baseurl}}/developer_guide/platform_wide/getting_started/architecture_overview).

## Data analysis and action
Data stored in Braze is retained and usable for segmentation, personalization, and targeting as long as you’re a Braze customer. That allows you to act on user profile data (for example, session activity or purchases) until you choose to deprecate that information. For instance, a streaming service could track each subscriber’s viewed content from their first day on the service (even if that was many years ago) and use that data to  power relevant messaging.

![A segment in the Braze dashboard called "Recent purchasers" juxtaposed next to a phone screen showing a "Top Recommendations for Linda" email.][3]{: style="max-width:80%;center;"} 

### App analytics
The Braze dashboard displays graphs that are updated in real-time based upon a number of analytics metrics as well as custom events that you instrument in your application. Consistently measuring and optimizing your campaigns with A/B testing, custom reporting and analytics, and automated intelligence helps you keep customers engaged and stand out from competitors in your space.

### User segmentation
Segmentation allows you to create groups of users based on powerful filters of their in-app behavior, demographic data, etc. Braze also allows you to define any in-app user action as a "custom event" if the desired action is not captured by default. The same is true of user characteristics via "custom attributes." After a user segment is created on the dashboard, your users will move in and out of the segment as they meet (or fail to meet) the defined criteria. For example, you can create segment that includes all users who have spent money in-app and last used the app more than two weeks ago.

For more on our data models, check out: [Getting Started: Analytics overview]({{site.baseurl}}/developer_guide/platform_wide/getting_started/architecture_overview).

## Multichannel messaging
Braze was designed to handle an evolving technological landscape with its channel-agnostic, user-centric data model. Messaging is done inside your app or site (such as sending in-app messages or through graphic elements like Content Card carousels and banners) or outside your app experience (such as sending push notifications or emails).  

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/messaging-channel-graphic.png <br> Once you have defined a segment, Braze's messaging tools allow for multichannel communication with your users. For example, send a push notification and email to the example segment defined in the previous section. Messaging channels are best used in concert and with regularity to re-engage lost users, retain active users, and energize your brand ambassadors. Moreover, you can use our advanced scheduling options to automate campaigns to specific groups of those users going forward.
{{site.baseurl}}/assets/img_archive/cc_usecase_onboarding.png <br> **Content Cards** <br> With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, Connected Content, custom card expiration times, card analytics, and easy coordination with push notifications. [Learn more about integrating and customizing Content Cards.]({{site.baseurl}}/developer_guide/customization_guides/content_cards)
{{site.baseurl}}/assets/img_archive/Macbook_Push.png  <br>**Push notifications** <br> Braze supports the Apple Push Notification Service (APNs) for iOS and Firebase Cloud Messaging (FCM) for Android. Push notifications can be triggered by the publication of messaging campaigns and news items. [Learn more about using Braze to trigger push notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push).
{{site.baseurl}}/assets/img_archive/dnd_iam_save_as_template.png <br>**In-app messaging** <br> Braze provides unobtrusive in-app notifications via our custom-built native user interface. Messages can be presented at any time of your choosing (for example, when users start a new session or complete a specific action) ensuring that your message arrives at the most effective time to engage the user. [Learn more about how marketers create and customize in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).
{{site.baseurl}}/assets/img/dnd/dnd_emailvariant.png <br>**Email** <br> Send your users rich HTML messages by adding your existing HTML templates, using our rich text editor, or our drag and drop editor. Braze makes it easy to include email as part of your mobile engagement strategy. [Learn more about how marketers create emails from the Braze dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/email).
{{site.baseurl}}/assets/img/link_shortening/shortening1.png  <br>**SMS and MMS** <br> Use SMS with Braze to send transactional notifications, share promotions, send reminders, and more. With over 23 billion text messages sent every day worldwide, SMS is the most direct way to reach users and customers. [Learn more about setting up SMS, managing users and phone numbers, subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/sms).<br><br>SMS and MMS are only available in select Braze packages. Reach out to your account manager or customer success manager to get started.
{{site.baseurl}}/assets/img/whatsapp/whatsapp8.png <br>**WhatsApp** <br> WhatsApp is a popular peer-to-peer messaging platform used across the world offering conversation-based messaging for businesses. Braze offers a direct way to reach users and customers on the WhatsApp platform. [Learn more about integrating WhatsApp with Braze]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp).<br><br>WhatsApp access is only available in select Braze packages. Reach out to your account manager or customer success manager to get started.
{{site.baseurl}}/assets/img_archive/Webhook_template_test.png <br>**Webhooks** <br>Braze's webhooks allow you to trigger non-app actions, providing other systems and applications with real-time information. The flexibility of this feature allows you to send information to any endpoint. [Learn more about setting up webhooks in Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks).
{% endgallery %}

For more on customizing messaging channels, check out: [Getting Started: Customization overview]({{site.baseurl}}/developer_guide/customization_guides/customization_overview).

## Integrating Braze
Braze is designed to get up and running quickly and easily. Our average time-to-value is six weeks across our customer base of hundreds of brands.

For more on the integration process, check out: [Getting Started: Integration overview]({{site.baseurl}}/developer_guide/platform_wide/getting_started/integration_overview/).

> Explore the different SDKs Braze offers:

<style>
table th:nth-child(1) {
width: 33%;
}
table th:nth-child(2) {
width: 33%;
}
table th:nth-child(3) {
width: 33%;
}
table td {
word-break: break-word;
text-align: center;
}
</style>
Featured integrations   | &nbsp;  |  &nbsp;
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/android.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) |[<i class="fa-brands fa-apple" style="font-size:60px;vertical-align: middle;"></i>]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/){: style="max-width:30%;margin-right:15px;border:0"} [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/) | [<i class="fas fa-globe" style="font-size:60px;vertical-align: middle;"></i>]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0"} [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)  

All integrations   | &nbsp;  |  &nbsp;
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/) | [![Flutter Android and iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android and iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/)

[1]: {{site.baseurl}}/user_guide/administrative/access_braze
[2]: {{site.baseurl}}/api/home
[3]: {% image_buster /assets/img/getting-started/getting-started-segment.png %} 
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/email
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms
[8]: {% image_buster /assets/img_archive/UOiOSPush.png %} "Example Push dashboard"
[9]: {% image_buster /assets/img_archive/In-App_Modal.png %} "Slideup Example"
[10]: {% image_buster /assets/img_archive/EmailTemplateEditor.png %} "Email Template Editor"
[11]: {{site.baseurl}}/user_guide/message_building_by_channel/whatsapp
[12]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/
[14]: {% image_buster /assets/img_archive/Webhook_Body_Edit.png %}
[15]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[16]: {{site.baseurl}}/developer_guide/home
[17]: {% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %} 