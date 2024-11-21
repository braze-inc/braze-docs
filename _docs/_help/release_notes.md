---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: dev_guide
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the following <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>."
page_type: landing
search_rank: 1
description: "This landing page is home to Braze release notes. This is where you can find all updates to the Braze platform and SDKs, as well as a list of deprecated features."

guide_featured_title: "Release notes"
guide_featured_list:
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Deprecations
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: SDK Changelogs
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Most recent Braze release notes {#most-recent}

> Braze releases information on product updates on a monthly cadence, aligning with major Product Releases, though the product is updated with miscellaneous improvements week to week.
> <br>
> <br>
> For more information on any of the updates listed in this section, reach out to your account manager or [open a support ticket]({{site.baseurl}}/help/support/). You can also check out [our SDK Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly SDK releases, updates, and improvements.

## November 12, 2024 release
 
### Data flexibility
 
#### Speed limit for `/users/track`

The speed limit for the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) has been updated to 3,000 per 3 seconds.
 
### Unlocking creativity

#### Canvas Use Cases

We've put together some use cases showcasing the different ways you can leverage a Braze Canvas. If you're looking for inspiration, choose a use case below to get started.

- [Abandoned Cart]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [Back In Stock]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Feature Adoption]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Lapsed User]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Onboarding]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Post-Purchase Feedback]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Robust channels

#### LINE

{% multi_lang_include release_type.md release="General availability" %}

Braze's LINE integration is now generally available! LINE  is the most popular messaging app in Japan, with over 95 million monthly active users. In addition to messaging, LINE offers its users an “all-in-one” platform for social media, gaming, shopping, and payments.

To get started, see our [LINE documentation]({{site.baseurl}}/user_guide/message_building_by_channel/line/).
 
#### LinkedIn Audience Sync

{% multi_lang_include release_type.md release="Beta" %}

You can now use LinkedIn with [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/), a tool that helps you extend the reach of your campaigns to many of the top social and advertising technologies. To join the beta, reach out to your Braze Success Manager.
 
### Improving the developer guide
 
We're in the process of making major improvements to the [Braze Developer Guide]({{site.baseurl}}/developer_guide/home/). As a first step, we simplified the navigation and reduced the number of nested sections. 

|Before|After|
|------|-----|
|!["The old navigation for the Braze Developer Guide."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["The new navigation for the Braze Developer Guide."]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### New Braze partnerships
 
#### MyPostcard

[MyPostcard](https://www.mypostcard.com/), a leading global postcard app, empowers you to execute direct mail campaigns with ease, providing a seamless and profitable way to connect with your customers. To get started, see [Integrating MyPostcard with Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Expo Plugin 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - This version requires 13.1.0 of the Braze React Native SDK.
    - Replaces the iOS BrazeAppDelegate method call of BrazeReactUtils.populateInitialUrl with BrazeReactUtils.populateInitialPayload.
        - This update resolves an issue where push opened events would not be triggered when clicking on a notification while the application is in a terminated state.
        - To fully leverage this update, replace all calls of Braze.getInitialURL with Braze.getInitialPushPayload in your JavaScript code. The initial URL can now be accessed via the url property of the initial push payload.
- [Braze Segment Swift Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Updates the Braze Swift SDK bindings to require releases from the 11.1.1+ SemVer denomination.
    - This allows compatibility with any version of the Braze SDK from 11.1.1 up to, but not including, 12.0.0.
    - Refer to the changelog entry for 11.1.1 for more information on potential breaking changes.

## October 15, 2024 release

### Data flexibility

#### Campaigns and Canvases

While creating campaigns and Canvases, you can calculate the exact number of reachable users in your target audience instead of the default estimation by selecting [Calculate exact statistics]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size).

#### API Android objects

The [`android_priority` parameter]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) will accept values either “normal” or “high” to specify the FCM sender priority. By default, notification messages are sent with high priority, and data messages are sent with normal priority.

For more information on how different values impact delivery, see [Android message priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Use the [Braze SDK's built-in debugger]({{site.baseurl}}/developer_guide/platform_wide/debugging/) to troubleshoot issues for your SDK-powered channels without needing to enable verbose logging in your app.

#### Live Activities

We updated the [frequently asked questions]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) for Swift Live Activities with a few new questions and answers.

#### Custom events

[Event property objects]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) that contain array or object values can now have an event property payload of up to 100&nbsp;KB.

#### Random bucket numbers

Use [random audience re-entry with random bucket numbers]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) for A/B testing or targeting specific user groups in your campaigns.

#### Segment Extensions

You can [refresh segment extensions on a recurring schedule]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh) by selecting the frequency at which the extensions will refresh (daily, weekly, or monthly) and the specific time the refresh will occur.

### Robust channels

#### SMS

We added [Adding UTM parameters]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) to demonstrate how you can use UTM parameters in an SMS message, so you track the performance of campaigns in third-party analytics tools, such as Google Analytics.

#### Landing pages

[Connect your own domain]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/connect_domain/) to your Braze workspace to customize your landing page URLs with your brand.

#### LINE and Braze

{% multi_lang_include release_type.md release="Beta" %}

We added new documentation:

- [LINE message types]({{site.baseurl}}/line/create/message_types/) covers the LINE message types you can compose, including aspects and limitations, and is part of the LINE beta collection.
- [User account linking]({{site.baseurl}}/line/line_setup/#user-account-linking) allows users to link their LINE account to your app’s user account. You can then use Liquid in Braze, such as {% raw %}`{{line_id}}`{% endraw %}, to create a personalized URL for the user that passes the user's LINE ID back to your website or app, which can then be associated with a known user.

#### WhatsApp and Braze

[WhatsApp Business Accounts (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) can now be shared with multiple Business Solution Providers.

### New Braze partnerships

#### Future Anthem - Dynamic Content

The Braze and [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) partnership leverages Amplifier AI to deliver content personalization, real-time experiences, and dynamic audiences. Amplifier AI works across sports, casinos, and lottery, allowing you to enhance Braze player profiles with industry-specific player attributes, such as a favorite game, engagement score, expected next bet, and more.

### Settings

#### Indentifier field-level encryption

{% multi_lang_include release_type.md release="General availability" %}

Using [identifier field-level encryption]({{site.baseurl}}/user_guide/data_and_analytics/field_level_encryption/), you can seamlessly encrypt email addresses with AWS Key Management Service (KMS) to minimize personally identifiable information (PII) shared in Braze. Encryption replaces sensitive data with ciphertext, which is unreadable encrypted information.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Swift SDK 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Swift SDK 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Adds support for [Swift 6 strict concurrency checking](https://developer.apple.com/documentation/swift/adoptingswift6)
        - Relevant public Braze classes and data types now conform to the `Sendable` protocol and can be safely used across concurrency contexts.
        - Main thread-only APIs are now marked with the `@MainActor` attribute.
        - We recommend using Xcode 16.0 or later to take advantage of these features while minimizing the number of warnings generated by the compiler. Previous versions of Xcode may still be used, but some features may generate warnings.
    - When integrating push notification support manually, you may need to update the `UNUserNotificationCenterDelegate` conformance to use the `@preconcurrency` attribute to prevent warnings.
        - Applying the `@preconcurrency` attribute on protocol conformance is only available in Xcode 16.0 or later. Reference our sample integration code [here](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual).
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Updates the native Android version bindings from [Braze Android SDK 31.1.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updates the native iOS version bindings from [Braze Swift SDK 10.3.0 to 11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [Swift SDK 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Updated Kotlin from 1.8 to Kotlin 2.0.
- [Web SDK 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## September 17, 2024 release

### Data flexibility

#### Braze Cloud Data Ingestion for S3

You can use [Cloud Data Ingestion (CDI) for S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) to directly integrate one or more S3 buckets in your AWS account with Braze. When new files are published to S3, a message is posted to SQS, and Braze Cloud Data Ingestion takes in those new files.

#### Increased rate limit

The rate limit for the [/users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) request type has increased to 2,500 requests per minute.

#### Monthly active users CY 24-25

For customers who have purchased Monthly Active Users - CY 24-25, Braze manages different rate limits on its `/users/track` endpoint. For details, refer to [POST: Track Users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Unlocking creativity

#### Templating catalog items including Liquid

{% multi_lang_include release_type.md release="Early access" %}

Use the `:rerender` flag in a Liquid tag to [render a catalog item's Liquid content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). For example, if you render the following Liquid content:

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

This will display as the following:

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### Robust channels

#### WhatsApp response messages

{% multi_lang_include release_type.md release="General availability" %}

You can use [response messages]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) to reply to inbound WhatsApp messages from your users. These messages are built in-app on Braze during your composition experience and can be edited at any time. You can use Liquid to match the response message language to the appropriate users.

#### Canvas templates

{% multi_lang_include release_type.md release="General availability" %}

Create [Canvas templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/) to refine your messaging by creating a consistent framework that can be easily customized to fit your specific goals across your Canvases.

#### Landing pages

{% multi_lang_include release_type.md release="Beta" %}

Braze [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) are standalone webpages that can drive your user acquisition and engagement strategy.

#### Changes since last viewed

You can view the number of updates to your [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), campaigns, and [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) by other members of your team by referring to the *Changes Since Last Viewed* metric on the respective overview pages (such as the overview page for an [email campaign]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)). 

#### Troubleshooting webhook and Connected Content requests 

[This article]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) covers how to troubleshoot webhook and Connected Content error codes, including what the errors are and steps to resolve them.

### New Braze partnerships

#### Inbox Monster - Analytics

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) is an inbox signals platform that helps enterprise brands land every send. It's an integrated suite of solutions for deliverability, creative rendering, and SMS monitoring, that empowers modern customer relationship managment (CRM) teams and ends the sending scaries.

#### SessionM - Loyalty

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) is a customer engagement and loyalty platform that provides campaign management features and loyalty management solutions to help marketers drive targeted outreach to increase engagement and profitability.

### AI and ML automation

#### Trending item recommendations

In addition to the "AI Personalized" model, the [AI item recommendations]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) feature also includes a recommendation model for "Trending", which features items that had the most positive momentum when it comes to recent user interactions.

### Settings

#### Roles

{% multi_lang_include release_type.md release="General availability" %}

[Roles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) allow for more structure by bundling together your individual custom permissions with workspace access controls. This is especially useful if you have many brands or regional workspaces in one dashboard. With roles, you can add dashboard users to the right workspaces and directly grant them the associated permissions. 

#### Security event report

We added a complete list of the [security events]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) that may appear in your downloaded security report event.

#### Message usage report

{% multi_lang_include release_type.md release="Early access" %}

The [message usage dashboard]({{site.baseurl}}/message_usage/) provides self-service insights into your SMS and WhatsApp credit usage for a comprehensive view of historical and current usage compared against contract allotments. These insights can reduce your confusion and help you make adjustments to prevent overage risks.

### SDK

#### Delayed initialization for the Braze Swift SDK

Set up [delayed initialization]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/) to initialize your Braze Swift SDK asynchronously while ensuring push notification handling is preserved. This can be useful when you need to set up other services before initializing the SDK, such as fetching configuration data from a server, or waiting for user consent.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segment Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [Swift SDK 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - This version now requires Cordova Android 13.0.0.
    - Refer to the [Cordova release announcement](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html) for a full list of project dependency requirements.- Updated the native Android bridge [from Braze Android SDK 30.3.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native iOS bridge [from Braze Swift SDK 9.2.0 to 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Updated the native Android bridge [from Braze Android SDK 30.3.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native iOS bridge [from Braze Swift SDK 9.0.0 to 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Segment Swift Plugin 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Updates the Braze Swift SDK bindings to require releases from the `10.2.0+` SemVer denomination.
        - This allows compatibility with any version of the Braze SDK from `10.2.0` up to, but not including, `11.0.0`.
        - Refer to the changelog entry for [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) for more information on potential breaking changes.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Updates the native Android bridge [from Braze Android SDK 30.4.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Changes the behavior of `wipeData()` on Android to retain external subscriptions (like `subscribeToContentCards()`) after being called.
    - Updates the native iOS bridge [from Braze Swift SDK 9.0.0 to 10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

## August 20, 2024 release

### New use cases

#### Catalogs

You can bring in any type of data into a catalog. Typically, the data is metadata about offerings, such as products, discounts, promotions, events, and similar. Read our [use cases]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) and learn how you can use this data to target users with highly relevant messaging.

#### Intelligence Suite

The Intelligence Suite provides powerful features to analyze user history and campaign and Canvas performance, then make automatic adjustments to increase engagement, viewership, and conversions. For a few examples of how these features can benefit different industries, check out our [use cases]({{site.baseurl}}/user_guide/brazeai/intelligence).

### Home dashboard update

You can [pick up where you left off]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off) in the Braze dashboard with easy access to files you've recently edited or created. This section appears at the top of the **Home** page of the Braze dashboard.

### Data flexibility

#### Data Transformation templates and new destination

{% multi_lang_include release_type.md release="General availability" %}

Build your Data Transformation using our dedicated [template library]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation) to help you get started with certain external platforms, instead of default code. You can now select **POST: Send messages immediately via API Only** as your destination to transform webhooks from a source platform to send immediate messages to your users.

#### Merge users in bulk

{% multi_lang_include release_type.md release="General availability" %}

If you encounter duplicate user profiles, you can [bulk merge]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) these users to help streamline your data.

#### Export custom attributes

{% multi_lang_include release_type.md release="General availability" %}

You can [export the list of custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data) as a CSV file by selecting **Export all** on the **Custom Attributes** page. The CSV file will be generated, and a download link will be emailed to you.

#### Currents IP allowlisting

Braze will send Currents data from the listed IPs, which are automatically and dynamically added to any API keys that have been opted-in for [allowlisting]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents).

### Robust channels

#### New segment builder experience

{% multi_lang_include release_type.md release="General availability" %}

Build a segment using our [updated experience]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). Segments update in real-time as data changes, and you can create as many segments as needed for your targeting and messaging purposes.

#### Metrics by segments

Use [Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) report templates to break down performance metrics for campaigns, Canvas, variants, and steps by segments.

#### Phone number acquisition

To use the WhatsApp messaging channel, you'll need a phone number that meets WhatsApp’s requirements for its [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) or [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers). 

You must acquire your phone number yourself, as Braze won't provision the number for you. You can either purchase a physical phone with a SIM card through your business phone provider or use one of our partners: Twilio or Infoblip. **You must have your own Twilio or Infobip account because this cannot be done through Braze.**

### New Braze partnerships

#### Zendesk Chat - Instant Chat

The Braze and [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) integration uses webhooks from each platform to set up a two-way SMS conversation. When a user requests support, a ticket is created in Zendesk. Agent responses are forwarded to Braze through an API-triggered SMS campaign, and user replies are sent back to Zendesk.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - The following changes have been made when subscribing to Push events with [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)):
        - The `update` closure will now be triggered by both "Push Opened" and "Push Received" events by default. Previously, it would only be triggered by "Push Opened" events.
            - To continue subscribing only to "Push Opened" events, pass in `[.opened]` for the parameter `payloadTypes`. Alternatively, implement your `update` closure to check that the `type` from the `Braze.Notifications.Payload` is `.opened`.
        - When receiving a push notification with `content-available: true`, the [`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type) will now be `.received` instead of `.opened`.
    - Marks the following deprecated APIs as unavailable:
        - `Braze.Configuration.Api.Flavor`
        - `Braze.Configuration.Api.flavor`
        - `Braze.Configuration.Api.SdkMetadata`
        - `Braze.Configuration.Api.addSdkMetadata(_:)`
        - `Braze.ContentCard.ClickAction.uri(_:useWebview:)`
        - `Braze.ContentCard.ClickAction.uri`
        - `Braze.InAppMessage.ClickAction.uri(_:useWebview:)`
        - `Braze.InAppMessage.ClickAction.uri`
        - `Braze.InAppMessage.ModalImage.imageUri`
        - `Braze.InAppMessage.Full.imageUri`
        - `Braze.InAppMessage.FullImage.imageUri`
        - `Braze.InAppMessage.Themes.default`
        - `Braze.deviceId(queue:completion:)`
        - `Braze._objc_deviceId(completion:)`
        - `Braze.deviceId()`
        - `Braze.User.setCustomAttributeArray(key:array:fileID:line:)`
        - `Braze.User.addToCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User._objc_addToCustomAttributeArray(key:value:)`
        - `Braze.User._objc_removeFromCustomAttributeArray(key:value:)`
        - `gifViewProvider`
        - `GifViewProvider.default`
    - Removes the deprecated APIs:
        - `Braze.Configuration.DeviceProperty.pushDisplayOptions`
        - `Braze.InAppMessageRaw.Context.Error.extraProcessClickAction`
    - Removes the deprecated `BrazeLocation` class in favor of `BrazeLocationProvider`.
- [Xamarin SDK Version 6.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Added support for .NET 8.0 for the iOS and Android bindings as .NET 7.0 has reached end of life support.
        - This removes support for .NET 7.0.
    - Updated the Android binding from [Braze Android 30.4.0 to 32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the iOS binding from [Braze Swift SDK 9.0.0 to 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - When subscribing to push notification events, the subscription will be triggered on iOS for both "Push Received" and "Push Opened", instead of only for "Push Opened" events.
- [React Native SDK 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - Updates the native iOS version bindings from [Braze Swift SDK 9.0.0 to 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - When subscribing to push notification events, the subscription will be triggered on iOS for both `push_received` and `push_opened`, instead of only for `push_opened` events.

## July 23, 2024 release

### Braze Docs updates

#### Diátaxis and Braze Docs

We're in the process of standardizing our documentation using a framework called [Diátaxis](https://diataxis.fr/). To help our writers and contributors create content that fits into this new framework, we've created [templates for each content type]({{site.baseurl}}/contributing/content_types).

#### New pull-request template for Braze Docs

We took the time to improve our pull-request (PR) template so it's easier and less confusing to [contribute to Braze Docs]({{site.baseurl}}/contributing/home/). If you still think there's room for improvement, open up a PR or [submit an issue](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=). Whatever's easier!
 
### Data flexibility

#### Export custom events and attributes

{% multi_lang_include release_type.md release="General availability" %}

You can now export custom event and custom attributes using the [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) and [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) endpoints.

#### New Currents permissions for users

There are two new permission settings for users: **View Currents Integrations** and **Edit Currents Integrations**. Learn more about [user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions). 

#### Update to Snowflake data retention policy
 
Beginning August 27, 2024, personally identifiable information (PII) will be removed from all Snowflake Secure Data Sharing events data that is older than two years old. If you use Snowflake, you may choose to retain the full events data in your environment by storing a copy in your Snowflake account before the retention policy is applied. Learn more about [Snowflake data retention]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/).
 
### Unlocking creativity

#### Multi-page in-app messages

{% multi_lang_include release_type.md release="General availability" %}

Adding pages to your in-app message lets you guide users through a sequential flow, like an onboarding flow or welcome journey. To learn more, see [Creating an in-app message with drag-and-drop]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page).

#### Link shortening with Liquid

{% multi_lang_include release_type.md release="General availability" %}

Use [Liquid to personalize URLs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening) to automatically shorten URLs contained in SMS messages and collect click-through-rate analytics. To try it out, see [Link shortening]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/).

#### API examples for catalogs

We've added examples for the `/catalogs` endpoint using array fields. To see the examples, check out the following:

- [Edit multiple catalog items]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [Create multiple catalog items]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [Update catalog items]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [Edit catalog item]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [Create catalog item]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [Update catalog item]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [Create catalog]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### Robust channels

### Multiple WhatsApp Business accounts

{% multi_lang_include release_type.md release="General availability" %}

You can now add multiple WhatsApp Business accounts and subscription groups (and phone numbers) to each workspace. For details, see [Multiple WhatsApp Business accounts]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups). 

#### SMS Geographic Permissions

SMS Geographic Permissions enhance security and protect against fraudulent SMS traffic by enforcing controls on the countries to which you can send SMS messages. To learn how to specify an allowlist of countries so you can make sure SMS messages are only sent to approved regions, see [Configuring your SMS country allowlist]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist).

#### LINE and Braze

{% multi_lang_include release_type.md release="Beta" %}

[LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf) is the most popular messaging app in Japan, with over 95 million monthly active users. You can integrate your LINE accounts with Braze to leverage your zero- and first-party customer data to send compelling LINE messages to the right customers based on their preferences, behaviors, and cross-channel interactions. To get started, see [LINE]({{site.baseurl}}/line).

#### Shopify: Price drops and back-in-stock

{% multi_lang_include release_type.md release="Early access" %}

Now with Shopify, you can create custom notifications for [price drops]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) and [back-in-stock items]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications).
 
### AI and ML automation
 
#### Rules-based merging for duplicate users

Previoulsy, you could find and merge duplicate users in Braze individually or in bulk. Now you can create rules to control how duplicates are resolved, so the most relevant user is kept. To learn more, see [Rules-based merging]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

#### AI Liquid assistant

{% multi_lang_include release_type.md release="Beta" %}

The AI Liquid Assistant is a chat assistant powered by BrazeAI<sup>TM</sup> that helps generate the Liquid you need to personalize message content. You can generate Liquid from templates, receive personalized Liquid suggestions, and optimize existing Liquid with the support of BrazeAI<sup>TM</sup>. The AI Liquid Assistant also provides annotations explaining the Liquid used, so you can increase your understanding of Liquid and learn to write your own.

To get started, see [AI Liquid assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_liquid).
 
### SDK
 
#### Android SDK logs

We overhauled the [logging docs for the Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging), so it's easier to read and use in your app. We also added descriptions for each log level.

#### iOS SDK foreground push notifications

The `subscribeToUpdates` method in the Braze iOS SDK can now detect if a foreground push notification is received. To learn more, see [iOS push notification integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration).
 
#### Updating the Xamarin docs
 
Since [version 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0), the Braze Xamarin SDK uses the Swift SDK binding, so we updated the code snippets and reference material. We also restructured the section to make it easier to read and understand. To check it out, see [the Xamarin docs]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup).

#### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Swift SDK 9.3.1](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.1)
- [Web SDK 5.3.2](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#532)
    - Fixed a regression introduced in 5.2.0 that could cause HTML In-App Messages to render incorrectly when an external script is loaded synchronously.
- [Web SDK 5.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#540)

## June 25, 2024 release

### Japanese docs

We now support the Japanese language for Braze Docs!

![The Braze Docs site displaying the Japanese interface]({% image_buster /assets/img/braze-docs-japan.png %}){: style="max-width:70%;"}
 
### Data flexibility

#### Attachments for API-triggered campaigns

{% multi_lang_include release_type.md release="General availability" %}

The [`/campaigns/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) now supports attachments (just like the `/messages/send` endpoint supports attachments for emails). 

#### Additional data warehouse support

{% multi_lang_include release_type.md release="Early access" %}

Braze [Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources) now supports BigQuery, Databricks, Redshift, and Snowflake.

#### WhatsApp phone number migration

Migrate your WhatsApp phone number between WhatsApp Business Accounts by using Meta's Embedded Signup. Read more about [WhatsApp phone number migration]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration).
 
### Unlocking creativity

#### Engagement by Device

{% multi_lang_include release_type.md release="General availability" %}

The new **Engagement by Device** report provides a breakdown of what devices your users are using to engage with your email. This data tracks email engagement across mobile, desktop, tablet, and other device types. Learn more about [the report and the Email Performance Dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard).

#### WhatsApp and SMS Liquid properties in Canvas flow

{% multi_lang_include release_type.md release="General availability" %}

We added support for [WhatsApp and SMS Liquid properties in Canvas flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Now, when an Action Path step contains a "Sent an SMS Inbound Message" or "Sent a WhatsApp Inbound Message" trigger, the subsequent Canvas steps can include an SMS or WhatsApp Liquid property. This mirrors how event properties work in Canvas Flow. This way you can leverage your messages to save and reference first-party data on user profiles and conversational messaging.
 
#### Personalized Paths in recurring Canvases

{% multi_lang_include release_type.md release="Early access" %}

Personalized Paths in Canvases let you personalize any point of a Canvas journey for individual users based on conversion likelihood. Now, Personalized Paths are available for recurring Canvases. Learn more about [Personalized Variants]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths).

#### Segments troubleshooting

Working with segments? Here are some [troubleshooting steps and considerations]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting) to keep in mind.

#### Liquid highlighting

We improved the [color-coding that Liquid uses]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) to better support accessibility guidelines.

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### Robust channels

#### SMS geographic permissions

{% multi_lang_include release_type.md release="Early access" %}

SMS geographic permissions enhance security and protect against fraudulent SMS traffic by enforcing controls on the countries to which you can send SMS messages. Admins can now specify an allowlist of countries to make sure that SMS messages are only sent to approved regions. For more information, see [SMS Geographic Permissions]({{site.baseurl}}/sms_geographic_permissions). 

![The "Country allowlist" dropdown with the most common countries displaying at the top.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### Best practices for SMS/MMS

Learn more about [best practices for SMS/MMS with Braze]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices), including our recommendations for opt-out monitoring and traffic pumping. 

#### Tracking push unsubscribes

Check out our new [help article]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) for some tips to track push unsubscribes.

#### Shopify `checkout.liquid` deprecation

Please note that support for Shopify `checkout.liquid` will begin deprecation in August 2024 and finish in August 2025. Read more about how Braze will [handle this transition]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout). 

### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Swift SDK 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - Deprecates the existing Feature Flag APIs, to be removed in a future version:
        - `Braze.FeatureFlag.jsonStringProperty(key:)` has been deprecated.
        - `Braze.FeatureFlag.jsonObjectProperty(key:)` has been deprecated in favor of `Braze.FeatureFlag.jsonProperty(key:)`.
- [Roku SDK 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Braze Expo Plugin 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### tvOS documentation

A few months ago, the articles for [tvOS Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos) and [in-app messaging]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos) were deprecated by mistake. These docs have now been republished under the Swift section in Braze Docs.

{% alert note %}
[Contributors]({{site.baseurl}}/contributing/home) to Braze Docs should note that the site now runs on Ruby 3.3.0. Please upgrade your Ruby version as necessary.
{% endalert %}

## May 28, 2024 release

### Visual updates to documentation site

You may have noticed our documentation website has a snazzy new look! We've revamped it to reflect the new vibrant Braze brand identity. For a behind-the-scenes look at our new brand, read more at [Unveiling Our New Brand: A Conversation with Braze Executive Creative Director Greg Erdelyi](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi).

### Support for Portuguese and Spanish

{% multi_lang_include release_type.md release="General availability" %}

Braze is now available in both Portuguese and Spanish. To change the language the Braze dashboard appears in, refer to [Language settings]({{site.baseurl}}/user_guide/administrative/access_braze/language/).

### Robust channels

#### Multi-language settings

{% multi_lang_include release_type.md release="General availability" %}

By adjusting [multi-language settings]({{site.baseurl}}/multi_language_support/), you can target users in different languages and locations with different messages all within a single email message. To edit and manage multi-language support, you must have the "Manage Multi-Language Settings" user permission. To add the locale to a message, you'll need permissions for editing campaigns.

#### Message-level one-click list-unsubscribe header

{% multi_lang_include release_type.md release="General availability" %}

The one-click unsubscribe for the list-unsubscribe header ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) provides an easy way for recipients to opt-out from emails. You can adjust this header setting to be applied at a message level in your emails. For more information on this setting, refer to [Email unsubscribe header in workspaces]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces).

#### About email sanitization

Visit our new [sanitization]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization) article to learn more about the process that occurs when Braze detects a specific type of JavaScript in your email message. Its main purpose is to prevent bad actors from accessing other Braze dashboard users' session data.

#### Inclusion count for Content Blocks

After adding a Content Block in an active campaign or Canvas, you can [preview this Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) from the Content Blocks Library by hovering over the Content Block and selecting the <i class="fa fa-eye preview-icon"></i> **Preview** icon.

#### Canvas statuses

On the Braze dashboard, your Canvases are grouped by their status. Check out the different [Canvas statuses and descriptions]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) for what they mean.

### AI and ML automation

#### Brand guidelines for AI copywriting assistant

{% multi_lang_include release_type.md release="General availability" %}

You can now create and apply [brand guidelines]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/) to customize the style of copy generated by the AI copywriting assistant to fit your brand's voice. Set up multiple guidelines for different scenarios to ensure your tone always matches the context.
 
### New Braze partnerships

#### Adikteev - Analytics

The Braze and [Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) integration allows you to boost user retention by leveraging Adikteev’s churn prediction technology within Braze CRM campaigns to target high-risk user segments in priority.
 
#### Celebrus - Analytics
 
The Braze and [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) integration seamlessly integrates with the Braze SDK across web and mobile app channels, facilitating the population of Braze with channel activity data. This includes comprehensive insights into visitor traffic across digital assets over specified periods.
 
#### IAM Studio - Message Templates
 
With the Braze and [IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/) integration, you can easily insert customizable in-app message templates into your Braze in-app messages, offering image replacement, text modification, deep link settings, custom attributes, and event settings. Using IAM Studio, you can reduce message production time and dedicate more time to content planning.
 
#### Regal - Instant Chat

By integrating Braze and [Regal]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/), you can create a more consistent and personalized experience across all your customer touchpoints.

#### Treasure Data - Cohort Import
 
With the Braze and [Treasure Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/) integration, you can import user cohorts from Treasure Data to Braze so you can send targeted campaigns based on data that may only exist in your warehouse.
 
#### Zapier - Workflow Automation
 
The Braze and [Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/) partnership leverages the Braze API and Braze webhooks to connect with third-party applications to automate various actions.

### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift Plugin 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Updates the Braze Swift SDK bindings to require releases from the 9.2.0+ SemVer denomination.
        - This allows compatibility with any version of the Braze SDK from 9.2.0 up to, but not including, 10.0.0.
        - Refer to the changelog entries for [7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700), [8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), and [9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900) for more information on potential breaking changes.
    - Push notification support now requires a call to the static method `BrazeDestination.prepareForDelayedInitialization()` as early as possible in the app lifecycle, in your application’s `AppDelegate.application(_:didFinishLaunchingWithOptions:)` method.
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Updated the native iOS bridge [from Braze Swift SDK 7.7.0 to 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Expo Plugin 2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - Updated the native iOS bridge [from Braze Swift SDK 7.7.0 to 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native Android bridge [from Braze Android SDK 29.0.1 to 30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Web SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDK Version 5.0.0
    - Updated the iOS binding [from Braze Swift SDK 8.4.0 to 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

## April 30, 2024 release

### Permissions to create or update promotion code lists

As of April 2024, users will need the “Access Campaigns, Canvases, Cards, Segments, Media Library” permission to create or update promotion code lists. Refer to [Managing limited and team role permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) for a list of permission names and their descriptions.

### Data flexibility

#### SAML just-in-time provisioning

{% multi_lang_include release_type.md release="Early access" %}

[Just-in-time provisioning]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) works with SAML SSO to allow new dashboard users to create a Braze account on their first sign in. This eliminates the need for administrators to manually create an account for a new dashboard user, choose their permissions, assign them to a workspace, and wait for them to activate their account.

#### Permission sets and roles

Use [permission sets]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets-and-roles) to bundle permissions related to specific subject areas or actions. These permission sets can be applied to dashboard users who need the same access across different workspaces.

#### Cloud Data Ingestion Segments

Braze [Cloud Data Ingestion segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) allow you to write SQL that directly queries your own data warehouse by using data made available via your CDI connections, and create a group of users that can be targeted within Braze.

### Unlocking creativity

### Query Builder templates

{% multi_lang_include release_type.md release="General availability" %}

Using Query Builder templates, you can create reports using Braze data from Snowflake. To access [Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) templates, select **Query Template** when creating a report. All templates surface data from up to the last 60 days, but you can directly edit that and other values in the editor.

### Performance data by segment

{% multi_lang_include release_type.md release="General availability" %}

You can break down [performance data by segment]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment) in Query Builder report templates for campaigns, variants, and Canvases and Canvas steps by segments.

### Robust channels

#### Automatic link shortening for SMS messaging

{% multi_lang_include release_type.md release="General availability" %}

Use [automatic link shortening]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/?tab=manage%20responses#managing-keywords-and-auto-responses) to automatically shorten static URLs in your response. This can help shape your response as the character counter will update to show the expected length of the shortened URL.

### New Braze partnerships

#### Friendbuy - Loyalty

Leverage the integration between Braze and [Friendbuy]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/friendbuy/) to expand your email and SMS capabilities while effortlessly automating your referral and loyalty program communications. Braze will generate customer profiles for all the opted-in phone numbers collected via Friendbuy.

### NiftyImages - Dynamic Content

The Braze and [NiftyImages]({{site.baseurl}}/partners/message_personalization/dynamic_content/niftyimages/) partnership allows you to create dynamic and personalized images for your email campaigns by mapping your existing Braze personalization tags to your NiftyImages URLs.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 30.4.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift Plugin 2.4.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#240)
- [Flutter SDK 9.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Updates the native iOS bridge from [Braze Swift SDK 7.7.0 to 8.4.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The minimum iOS deployment target has been updated to 12.0.
    - Updates the native Android bridge from [Braze Android SDK 29.0.1 to 30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - The minimum supported Dart version is 2.15.0.
- [React Native SDK 9.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 8.3.0-8.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Swift SDK 9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Removes the default privacy tracking domains from the BrazeKit privacy manifest.
        - If you are using the Braze [data tracking features]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/), you will need to manually add your tracking endpoint to your app-level privacy manifest.
        - Refer to the updated [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking) for integration guidance.
    - Removes the deprecated `BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method in favor of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError)`.
        - This method was originally deprecated in [release 5.14.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.14.0).
        - Failing to switch to the new delegate method will not trigger a compiler error; instead, the `BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)` method you define will simply not be called.
- [Xamarin SDK Version 4.0.3](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#403)
