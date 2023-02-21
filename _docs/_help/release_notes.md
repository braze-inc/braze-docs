---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: featured
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the following <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>. You can also check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK Changelogs</a>."
page_type: landing
search_rank: 1
description: "This landing page is home to Braze Release Notes. This is where you can find all updates to the Braze platform and SDKs, as well as a list of deprecated features."

guide_featured_title: "Release Notes"
guide_featured_list:
  - name: 2023
    link: /docs/help/release_notes/2023/
    fa_icon: fas fa-calendar-alt
  - name: 2022
    link: /docs/help/release_notes/2022/
    fa_icon: fas fa-calendar-alt
  - name: 2021
    link: /docs/help/release_notes/2021/
    fa_icon: fas fa-calendar-alt
  - name: 2020
    link: /docs/help/release_notes/2020/
    fa_icon: fas fa-calendar-alt
  - name: 2019
    link: /docs/help/release_notes/2019/
    fa_icon: fas fa-calendar-alt
  - name: 2018
    link: /docs/help/release_notes/2018/
    fa_icon: fas fa-calendar-alt
  - name: 2017
    link: /docs/help/release_notes/2017/
    fa_icon: fas fa-calendar-alt
  - name: 2016
    link: /docs/help/release_notes/2016/
    fa_icon: fas fa-calendar-alt
  - name: Deprecations
    link: /docs/help/release_notes/deprecations/
    fa_icon: far fa-calendar-times
  - name: SDK Changelogs
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    fa_icon: fas fa-file-code

---

# Most recent Braze release notes {#most-recent}

> Braze releases information on product updates on a monthly cadence, aligning with major Product Releases, though the product is updated with miscellaneous improvements week to week.
> <br>
> <br>
> For more information on any of the updates listed in this section, reach out to your account manager or [open a support ticket][support]. You can also check out [our SDK Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly SDK releases, updates, and improvements.

## February 7, 2023 release

### Building accessible messages

Marketing content that excludes people with disabilities, even unintentionally, can prevent millions of people from interacting with your brand. Accessibility in marketing is about making it easy for everyone to experience your marketing, receive and understand your communication, and have the opportunity to invest in or become a fan of your product, service, or brand. Refer to [Building accessible messages in Braze]({{site.baseurl}}/help/accessibility#building-accessible-messages-in-braze) for guidance.

### Query builder early access

With the [query builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder#query-builder
), you can generate reports using Braze data in Snowflake. The query builder comes with pre-built SQL query templates to get you started. Currently only the templated queries are allowed. Support for custom SQL queries will follow.

This feature is currently in early access. If you're interested in participating in the early access, reach out to your customer success manager.

### Feature flags beta

[Feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags) allow you to remotely enable or disable functionality for a selection of users. They let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence.

This feature is currently in beta. If you're interested in participating in the beta, reach out to your customer success manager.

### New Currents events

The following Currents events have recently been released and added to the [message engagement events glossary]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events):

Message abort events:
- `users_campaigns_abort`
- `users_canvas_abort`
- `users_messages_contentcard_abort`
- `users_messages_email_abort`
- `users_messages_inappmessage_abort`
- `users_messages_newsfeedcard_abort`
- `users_messages_pushnotification_abort`
- `users_messages_sms_abort`
- `users_messages_webhook_abort`

SMS short link click events:
- `users.messages.sms.ShortLinkClick`

Global state change subscription event:
- `users.behaviors.subscription.GlobalStateChange`

Subscription group state change event:
- `users.behaviors.subscriptiongroup.StateChange`

Canvas exit events:
- `users_canvas_exit_PerformedEvent`
- `users_canvas_exit_PerformedEvent_Details`
- `users_canvas_exit_MatchedAudience`
- `users_canvas_exit_MatchedAudience_Details`

### Personalized variant

When sending an A/B test, you can send users a personalized variant, sending them the variant they are most likely to engage with. Refer to [Multivariate analytics]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant) for more on how personalized variants are selected and how to leverage them in your campaigns. 

### SQL Segment Extensions early access

[Segment Extensions]({{site.baseurl}}/sql_segments/) allow you to generate a Segment Extension using Snowflake SQL queries of Snowflake data. SQL can help you unlock new segment use cases because it offers the flexibility to describe the relationships between data in ways that aren't achievable through other segmentation features.

### Pre and post-launch checklist for Canvas

Before and after you launch a Canvas, there are several details you should check:
- Ensure that your messaging and send times align with your audience's preferences
- Account for variations in time zones, entry settings, and more
- Review and adjust your Canvas in the event of discrepancies after launch based on these scenarios

Use this [checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist#pre-and-post-launch-checklist) as a guide to finetune these areas based on your use case to help contribute to the success of your Canvas. 

### New API endpoint: Update user alias

Use the [update user alias endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) to update existing user aliases.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Web SDK 4.6.0-4.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#461)
- [Android SDK 24.1.0-24.2.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2420)
- [AppboyKit iOS SDK 4.5.3](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.5.3)
- [Swift SDK 5.9.0-5.9.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#591)
  - Raises the minimum deployment target to iOS 11.0 and tvOS 11.0.
  - Raises the Xcode version to 14.1 (14B47b).
- [Flutter SDK 3.1.0](https://pub.dev/packages/braze_plugin/changelog)
  - The native Android bridge uses Braze Android SDK 24.2.0.
  - The native iOS bridge uses Braze iOS SDK 5.9.0.
  - The minimum iOS deployment target is 11.0.
- [Cordova SDK 2.33.0](https://github.com/Appboy/appboy-cordova-sdk/blob/2.33.0/CHANGELOG.md#2330)
  - Migrated the iOS plugin to use the new Braze Swift SDK (5.8.1).
  - News Feed UI is no longer supported on iOS.

## January 10, 2023 release

### User Update component for Canvas Flow

The [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) component allows you to update a user's attributes, events, and purchases in a JSON composer, so there's no need to include sensitive information like API keys.

### Setting subscription groups via API

When creating new users via the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, you can set subscription groups within the user attributes object, which allows you to create a user and set the subscription group state in one API call.

### Conversions dashboard early access

The [conversions dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard/) allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods. You can specifically track these attribution methods:

- **Open conversions:** Conversions that occurred after a user opened the message
- **Click conversions:** Conversions that occurred after a user clicked the message
- **Received conversions:** Conversions that occurred after a user received the message
- **Last-click conversions:** Conversions that occurred after a user clicked the message if the message was the most recent one the user clicked (This feature is currently being tested on a small subset of early access customers)

This feature is currently in early access. If you're interested in participating in the early access, reach out to your customer success manager.

### Canvas exit events for Braze Currents

You can now track when your users exit a Canvas by either performing an event or by matching an audience. Check out the [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) section in the Currents Event Glossary for more information.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Web SDK 4.5.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [AppboyKit iOS SDK 4.5.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.5.2)
- [Swift SDK 5.8.0-5.8.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#580)
  - Renames the `BrazeLocation` class to `BrazeLocationProvider` to avoid shadowing the module of the same name.
- [Flutter SDK 3.0.1](https://pub.dev/packages/braze_plugin/changelog)
- [Android SDK 24.0.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md)
  - Location and geofence functionality has moved to a new module called `com.braze:android-sdk-location`.
  - Appboy classes and files have been wholesale moved to Braze.
  - Changed the default behavior of `DefaultContentCardsUpdateHandler` to use the creation time instead of the last update time when sorting Content Cards.
  - Removed BrazeUser.setFacebookData() and BrazeUser.setTwitterData().

## December 13, 2022 release

### News Feed is deprecated
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.

### New API endpoints: Catalogs
Use the [Braze API Catalogs endpoints]({{site.baseurl}}/api/endpoints/catalogs) to add, edit, and manage your [catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) and catalog item details. You can use the asynchronous catalog endpoints to make bulk changes to your catalog.

### HTML attributes for links in the Drag & Drop Editor for Email
You can now [add HTML attributes]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details/) to any URL within the `Image`, `Button`, or `Text` editor blocks in the Drag & Drop Editor for Email. With custom attributes, you can easily append additional information to HTML tags in emails. This can be especially useful for message personalization, segmentation, and styling.

### Show Heatmap toggle
You can now use the [Show Heatmap toggle]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#heatmaps) to bring up a visual view of your **Message Analytics** that shows the overall frequency and location of clicks within the lifespan of the email campaign. You can also download a copy of your heatmaps for future reference.

### Updated email settings
The previous **General Email Settings** section has been split into two new sections: **Sending Configuration** and **Subscription Pages and Footers.** For more information about the individual settings, check out [Email settings]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#sending-configuration).

### Generate AI images for your Media Library
You can generate images for your Media Library using DALL·E 2, an AI system from OpenAI that can create realistic images and art from a description in natural language. Read more about [Generating an image using AI]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai).

### Enhancements to nested custom attributes
You can use nested custom attributes to send objects as a new data type for custom attributes.
- You can [trigger when a nested custom attribute object changes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#trigger-nested-custom-attribute-changes).
- You can also now [personalize your messages using a custom attribute object and Liquid]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#personalization).

### New Video block
A new content block for [Video]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/#video) has been added to the Drag & Drop Editor for Email.

### Optional Identifier for Vendor collection - Swift
In previous versions of the Braze iOS Swift SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user's device ID. Beginning in Swift SDK v5.7.0, the IDFV field can optionally be disabled, and instead, Braze will set a random UUID as the device ID. For more information, refer to [Collecting IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/swift_idfv/).

### Snowflake Reader Accounts
Snowflake Reader Accounts offer users access to the same data and functionality as [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/), all without requiring a Snowflake account or customer relationship with Snowflake. With Reader Accounts, Braze will create and share your data into an account and provide you credentials to log in and access your data. This will result in all data sharing and usage billing being handled entirely by Braze.

To learn more, reach out to your customer success manager.

### Updated Shopify integration
The [Shopify integration]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) now allows you to collect email and SMS opt-ins from your Shopify store and assign them to a subscription group in Braze.



### New Braze partnerships

#### Ada - Surveys
The [Ada]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/ada/) and Braze integration allows you to augment user profiles with data collected from your automated Ada conversations. You can set custom user attributes based on the information you collect during an Ada chat and record custom events in Braze at specified points in an Ada conversation. By connecting your Ada chatbot to Braze, you can learn more about your consumers based on what questions they ask about your brand or by proactively starting conversations with them, asking them questions that allow you to learn more about their interests and preferences.

#### B.Layer - Message templates
The [B.Layer]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/blayer) and Braze integration allows you to leverage the B.Layer in-app message builder to help you build on-brand in-app messages that can be exported as a zip file or inline HTML to Braze. This integration does not require additional developer resources, saving you time and budget.

#### Contentsquare - Analytics
The [Contentsquare]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/contentsquare/) and Braze integration allows you to send Live Signals (fraud, frustration signals, etc.) as custom events in Braze. Leverage Contentsquare experience insights to improve your campaigns' relevance and conversion rates by targeting messages based on your customers' digital experience and body language.

#### Dynamic Yield - Dynamic content
The [Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) and Braze partnership allows you to leverage Dynamic Yield's recommendation and segmentation engine to create Experience Blocks that can be embedded into Braze messages. Experience blocks can be made of:
- **Recommendations blocks**: Set algorithms and filtering to source users' personalized content that propagates when the email is opened.
- **Dynamic Content blocks**: Target different promotions and messages to different users. Targeting can be based on either affinity or audience. Dynamic Yield determines which personalized experience to serve when the email is opened.

#### Octolis - Analytics
The [Octolis]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/contentsquare/) and Braze integration acts as middleware between your raw data sources and Braze, enabling you to retrieve and unify data from various sources, both online and offline.

#### Phrasee - AB testing
[Phrasee React]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/phrasee/phrasee_react/), powered by Phrasee X, leverages Braze Currents and Connected Content to collect click tracking information from your subscribers via webhooks. Phrasee then ties those events back to your language variants for real-time language optimization.

#### Sheetlabs - Dynamic content
The [Sheetlabs]({{site.baseurl}}/partners/message_personalization/dynamic_content/sheetlabs/) and Braze integration allows you to leverage [Connected Content](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) to include Sheetlabs APIs inside your Braze marketing campaigns. This is commonly used to provide a bridge between a Google Spreadsheet (which is updated directly by the marketing team) and Braze's templates. This allows you to achieve more with Braze templates, such as translations or larger sets of custom attributes.

#### Tellius - Analytics
The [Tellius]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/tellius/) and Braze integration and Braze integration empowers users to leverage data, without relying on BI engineers, to build dashboards and generate insights to make better marketing decisions.

#### ThoughtSpot - Analytics
The [ThoughtSpot]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/thoughtspot/) and Braze integration leverages ThoughtSpot TML Blocks that allows Braze users to accelerate their user behavior analytics with prebuilt templates of worksheets and models. This integration enables users to limitlessly search across their Braze interaction data and uncover actionable insights.

#### Wunderkind - Analytics
The [Wunderkind]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/wunderkind/) and Braze integration allows you to analyze the performance lift and identify more anonymous users, significantly scaling one-to-one messages sent via Braze and contacts added directly to Braze.


### SDK updates
The following SDK updates have been released. Breaking changes are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [iOS Swift SDK 5.6.3-5.7.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Flutter SDK 3.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - The native iOS bridge now uses the [new Braze Swift SDK, version 5.6.4](https://github.com/braze-inc/braze-swift-sdk).The minimum iOS deployment target is 10.0.
    - During migration, update your project with the following changes:
        - To initialize Braze, [follow these integration steps to create a configuration object](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/a2-configure-braze). Then, add this code to complete the setup: `let braze = BrazePlugin.initBraze(configuration)`
        - To continue using `SDWebImage` as a dependency, add this line to your project's `/ios/Podfile`: `pod 'SDWebImage', :modular_headers => true`. Then, follow [these setup instructions](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
        - For guidance around other changes such as receiving in-app message and content card data, reference our sample [`AppDelegate.swift`](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift).
- [React Native SDK v1.41.0](https://github.com/Appboy/appboy-react-sdk/blob/master/CHANGELOG.md)
- [Web SDK 4.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

#### New SDK library: Segment.io Kotlin SDK
Segment.io has updated their library with a new Kotlin-first approach called Segment.io Kotlin. Braze has just released a new library of our own to work with this new library paradigm. Check out the [initial release on GitHub.](https://github.com/braze-inc/braze-segment-kotlin)

## November 15, 2022 release

### New Drag & Drop Editor for in-app messages

With the new [Drag & Drop Editor for in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop), you can create completely custom and personalized in-app messages without needing to know HTML. The Drag & Drop Editor is being rolled out to all customers over the next few months. If you'd like to request access sooner, reach out to your customer success manager.

### Updates to Drag & Drop Editor for email

#### New editor blocks

Two new editor block have been added to the Drag & Drop Editor for email: [Paragraph blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/#paragraph) and [List blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/#list).

{% alert important %}
The existing Text block is being deprecated, but any existing email that has a Text block will continue to be supported.
{% endalert %}

#### Dark Mode Preview

When [previewing and testing your emails]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-3b-preview-and-test-your-message) in the Drag & Drop Editor, you can now turn on **Dark Mode Preview** to see what your email looks like for dark mode users.

### Winning Path early access

Available as part of Experiment Paths in Canvas, [Winning Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-2-turn-on-winning-path-optional) lets you automate your A/B tests. When Winning Path is turned on, after a specified period of time, all subsequent users will be sent down the path with the highest conversion rate.

This feature is currently in early access. If you're interested in participating in the early access, reach out to your customer success manager.

### In-app messages and Content Cards on tvOS

This new article covers the nuances of integrating [in-app messages and Content Cards on tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/in-app_messaging), which are available through the Braze Swift SDK.

### New Liquid use case

We've added a new use case to the [Liquid Use Case Library]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#misc-personalize-content) on how to use a customer's subscription state to personalize content in messages. With this use case, customers are who subscribed to a specific subscription group will receive an exclusive message for both email and SMS subscription groups.

### SDK updates

The following SDK updates have been released. There are no breaking updates with these releases. All other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 23.3.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2330)
- [Web SDK 4.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#440)
- [Unity SDK 3.11.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md#3110)
- [Xamarin SDK 1.26.0](https://github.com/Appboy/appboy-xamarin-bindings/blob/master/CHANGELOG.md#1260)
- [iOS Swift SDK 5.6.0–5.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#562)
- [Flutter SDK 2.6.1](https://pub.dev/packages/braze_plugin/changelog#261)

## October 18, 2022 release

### User profile Messaging History

The **Message History** tab of the user profile shows recent messaging related events (about 40) for an individual user from the past 30 days. These events include the messages that the user was sent, received, interacted with, and more. Refer to [User profiles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#messaging-history-tab) to learn more.

### Content Blocks for Drag & Drop Editor

The [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) used exclusively in the Drag & Drop Editor are similar in functionality to the Content Blocks used across different channels. They're a centralized location for holding information that can be referenced in various email campaigns. This can include grouping together email headers, promotional callouts, and more all in one reusable row.

### Shopify ScriptTag

The [Braze and Shopify Integration]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify) now allows you to embed our Web SDK integration via ScriptTag on to your Shopify store. Embedding our Web SDK via ScriptTag supports tracking the following:
- Anonymous user tracking to track guest activity in your store
- Monthly active user tracking as the Web SDK is capable of tracking session data from your store visitors
- Option to collect Shopify on-site activity users which will count toward your data point consumption
- Option to enable in-browser messaging as a channel on your Shopify store

### SCIM endpoint

Use the following Braze SCIM endpoints to manage automated user provisioning:
- [DELETE: Remove Dashboard User Account]({{site.baseurl}}/api/endpoints/scim/delete_existing_dashboard_user/)
- [GET: Look Up an Existing Dashboard User Account]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information/)
- [POST: Create New Dashboard User Account]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/)
- [PUT: Update Dashboard User Account]({{site.baseurl}}/api/endpoints/scim/put_update_existing_user_account/)

### SMS Fuzzy opt-outs

[Fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out#fuzzy-opt-out) attempts to recognize when an inbound SMS message does not match an opt-out keyword, but indicates opt-out intent. If fuzzy opt-out is enabled and an inbound keyword response is deemed "fuzzy", Braze will automatically respond asking the user to confirm their intent.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 23.2.0-23.2.1](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2321)
- [iOS Objective-C SDK 4.5.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#451)
- [iOS Swift SDK 5.5.0S-SDK 5.5.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#550)
- [Cordova SDK 2.31.0](https://github.com/Appboy/appboy-cordova-sdk/blob/master/CHANGELOG.md#2310)
  - Updated to [Braze Android SDK 23.0.1](https://github.com/Appboy/appboy-android-sdk/releases/tag/v23.0.1).
- [Unity 3.10.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md#3100)
- [React SDK v1.39.0](https://github.com/Appboy/appboy-react-sdk/blob/master/CHANGELOG.md#1400)
  - Updated the native Android SDK to 23.2.0.
  - Renamed the `kotlin_versio`n gradle template variable to `kotlinVersion`
- [Flutter SDK 2.6.0](https://pub.dev/packages/braze_plugin/changelog#260)
  - The native Android bridge uses Braze Android SDK 23.2.0.
  - The native iOS bridge uses Braze iOS SDK 4.5.1.
  - `process(inAppMessage)` is renamed to `processInAppMessage(inAppMessage)` in the iOS layer.
- [Segment iOS 4.6.0](https://github.com/Appboy/appboy-segment-ios/blob/master/CHANGELOG.md#460)
  - Updated to Braze [iOS SDK 4.5.1+](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#451).

## September 20, 2022 release

### API guide
Check out the [Braze API Guide]({{site.baseurl}}/docs/api/home) to search for endpoints based on endpoint types, helping you narrow down the glossary.

### Personalized variants
Use [personalized variants]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#optimizations) to send each user in your target segment the variant they're most likely to engage with.

### Testing Canvases
After creating your Canvas, there are several checks you may want to perform before launching, depending on details such as your audience size or number of segmentation filters. Check out [Sending test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) for tips.

### Liquid 5
For existing Braze users, Liquid 5 is generally available. Learn more about [what's new with Liquid 5]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#whats-new-with-liquid-5).

### New Braze partnerships

#### Shopify
The Braze and [Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) allows you to update existing user profiles or create new ones in Braze for leads, sign-ups, and account registrations being captured in your Shopify store.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 23.1.0–23.12](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md)
- [React Native SDK v1.38.0–v1.38.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
  - Updated the native Android bridge to Braze Android SDK 23.0.1.
  - Updated the native iOS bridge to Braze iOS SDK 4.5.0.
  - The Braze React Native Android SDK now requires Kotlin directly for compilation.
- [Braze Expo Plugin 0.4.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
  - Renamed the prop `fcmSenderID` to `firebaseCloudMessagingSenderId`.
- [Unity 3.9.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md)
  - Updated the Android plugin to use Braze Android SDK 23.1.0.
  - Added the ability to request push notification permissions on Android 13+ devices via `Appboy.AppboyBinding.PromptUserForPushPermissions(false)`.
- [Swift SDK 5.3.0–5.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#540)

## August 23, 2022 release

### Developer portal

Connect, learn, and get inspired with other developers building with Braze. Check out our [developer portal](https://www.braze.com/dev-portal) and join the Braze developer community on Slack.

### Message archiving

[Message Archiving]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/) is an add-on feature that lets you save a copy of messages sent to users for archival or compliance purposes to your S3 bucket.

### Canvas entry properties and event properties

Though similar in name, Canvas entry properties and event properties function differently within your Canvas workflows. Learn more about when to use each property and the differences in behavior in [Canvas entry properties and event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties).

### Tracked link aliases

You can now view all the link aliases you're tracking in your emails from **Manage Settings** > **Email Settings** > **Link Aliasing Settings**. For more information, refer to [Tracking links]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#tracking-links).

### Liquid 5

Braze has updated support to Liquid up to and including **Liquid 5 from Shopify**. For new Braze users, Liquid 5 is generally available. For existing Braze users, Liquid 5 is in early access. Learn more about [what's new with Liquid 5]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#whats-new-with-liquid-5).

### Best practices for campaigns and Canvases

Creating successful campaigns and Canvases can be complex, so check out our list of best practices you should be aware of to make the most of your messaging.

- [Campaign best practices]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/best_practices/)
- [Canvas best practices]({{site.baseurl}}/user_guide/engagement_tools/canvas/best_practices/)

### Searching for campaigns

Did you know you can search for a campaign by its API identifier? Learn more about this and other ways to filter and find campaigns in [Searching for campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### New Braze partnerships

#### IAM Studio - Message templates

With the Braze and [IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/) integration, you can easily insert customizable in-app message templates into your Braze in-app messages, offering image replacement, text modification, deep link settings, custom attributes, and event settings. Using IAM Studio, you can reduce message production time and dedicate more time to content planning.

#### actionable.me - Analytics

The Braze and [actionable.me]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/actionableme/) integration allows you to deploy a service to monitor your progress in the utilization of Braze. Through a combination of tools and processes, they will rapidly benchmark your CRM performance, identify new opportunities and provide recommendations on how to perform better.

#### Storyly - Cohort import

The Braze and [Storyly]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/storyly/) integration allows you to use your segments in Braze as an audience in the Storyly platform. With this integration, you can:

- Target your segments with specific stories
- Use user attributes to personalize your story contents

#### Lokalise - Localization

The Braze and [Lokalise]({{site.baseurl}}/partners/message_personalization/localization/lokalise/) integration leverages Connected Content to allow you to easily insert translated content into your Braze campaigns based on user language settings.

#### Quikly - Retargeting

The Braze and [Quikly]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/quikly/) partnership allows you to accelerate conversions on events within a Braze customer journey. Quikly does this by using urgency psychology to motivate consumers in fun — and instant — ways. For example, brands can use Quikly to immediately acquire new email and SMS subscribers directly into Braze or to motivate other key marketing objectives like downloading your mobile app.

#### DataGrail - Data privacy and compliance

The Braze and [DataGrail]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/datagrail/) integration allows you to detect consumer data collected and stored within Braze to quickly process DSRs (access, delete, and do-not-sell requests). Braze will be added to an accurate blueprint of where consumer data lives in your organization with automated data mapping — no more surveys or spreadsheets are needed to maintain a privacy framework or produce a record of processing activities (RoPA).

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Web SDK 4.2.0–4.2.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#421)
- [iOS 4.5.0](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#450) (Objective-C)
- [iOS Swift 5.1.0–5.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#520)
- [Android 23.0.0–23.0.1](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2301)
    - `BaseContentCardView.bindViewHolder()` now takes `Card` instead of generic type.

[support]: {{site.baseurl}}/support_contact/

<br><br>
