---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: dev_guide
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

## April 4, 2023 release

### Documentation breadcrumbs 
You might notice that the Braze Docs site now has breadcrumbs on the top of each article to show you where you are in the site. These are just another option to help you navigate!

![A series of breadcrumbs navigating from User Guide > Message Building by Channel > In-App Messages > Templates > Simple Survey][1]{: style="max-width:55%"}

### Creating catalogs in browser
You can use catalogs to reference non-user data in your Braze campaigns through Liquid. Braze now allows you to create a catalog directly in your browser instead of importing a CSV. Refer to [Creating a catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) for more for more information.

### Custom SQL in query builder
With the query builder, you can generate reports using Braze data in Snowflake. Now, you can [use custom SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/custom_sql) to unlock new insights.

{% alert important %}
The SQL editor is in early access. If you're interested in participating in the early access, reach out to your customer success manager.
{% endalert %}

### Feature flag FAQ
We've answered some [frequently asked questions for feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/faq).

### Message extras Liquid tag for Currents
Using the [`message_extras` Liquid tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras), you can annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. This Liquid tag appends key-value pairs to the corresponding send event in Currents.

{% alert important %}
This Liquid tag is currently in beta for email, SMS, and push send events. Contact your Braze customer success manager if you're interested in participating in the beta.
{% endalert %}

### New Currents events: users_campaigns_abort and users_canvas_abort
Two new events were added to the Currents glossary: [Canvas abort message events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#canvas-abort-message-events) and [campaign abort message events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#campaign-abort-message-events).

### New API endpoints: Catalogs
Use the [Update catalog item]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) and [Update catalog items]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) endpoints to update an item or multiple items in your catalog.

### Shopify Historical Backfill
[Shopify Historical Backfill](https://www.braze.com/docs/partners/additional_channels_and_extensions/ecommerce/shopify/shopify_backfill/) allows Braze to import all customers, orders, and purchase events from the last 90 days prior to your Shopify integration connection.

### WhatsApp
WhatsApp is a popular peer-to-peer messaging platform used across the world offering conversation-based messaging for businesses. The [WhatsApp messaging channel]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp) offers a direct way to engage users on the WhatsApp platform through campaigns, opt-ins and opt-outs, quick replies, and more.

#### WhatsApp API object
As part of Braze's WhatsApp support, the `whats_app` object allows you to modify or create WhatsApp messages via our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging). See the [`whats_app` object documentation]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object) for the full spec.

### New Braze partnerships

#### Merkury - Analytics
The Braze and [Merkury]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/merkury) integration allows you to leverage the `MerkuryID` to increase site visitor recognition rates for Braze customers.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Cordova SDK 3.0.0](https://github.com/Appboy/appboy-cordova-sdk/blob/3.0.0/CHANGELOG.md)
- [Swift SDK 5.11.1-5.13.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Android SDK 24.3.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md)
- [React Native SDK v3.0.0-v4.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 4.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Expo Plugin v1.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Web SDK v4.7.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## March 7, 2023 release

### Removing support for duplicating original experience Canvases

As of February 28, 2023, you can no longer create or duplicate Canvases using the original Canvas experience. Braze recommends that customers who use the original Canvas experience move to Canvas Flow. It’s an improved editing experience to better build and manage Canvases. Learn more about [cloning your Canvases to Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).

### Live Activities for iOS (early access)

[Live Activities]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/) are persistent, interactive notifications displayed on your lock screen, allowing you to keep an eye on things in real-time. Because they appear on the lock screen, Live Activities ensure that your notifications won’t be missed. Because they’re persistent, you can display up-to-date content to your users without even having them unlock their phone.

{% alert important %}
Live Activities are currently in early access. Contact your Braze account manager if you’re interested in participating.
{% endalert %}

### Card creation for Content Cards

You can now choose when Braze evaluates audience eligibility and personalization for new Content Card campaigns by specifying when the card is created.

The following options are available:

- **At campaign launch:** The previous default behavior for Content Cards. Braze calculates audience eligibility and personalization when the campaign launches, then creates the card and stores it until the user opens your app.
- **At first impression:** When the user next opens your app (that is, starts a new session), Braze determines which Content Cards the user is eligible for, templates any personalization like Liquid or Connected Content, then creates the card.

For more information, refer to [card creation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).

### Reset styles for in-app message Drag & Drop Editor

In the Drag & Drop Editor for in-app messages, you can now quickly reset styles to their default styling after making changes. For more, refer to [resetting styles to default]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#resetting-styles-to-default).

### Custom domains for link shortening

Link shortening also allows you to use your own domain to personalize the look and feel of your shortened URLs, helping portray a consistent brand image. Once configured, [custom domains]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#custom-domains) can be assigned to one or multiple SMS subscription groups.

### Safari mobile web push

Safari v16.4 supports mobile web push, which means you can now re-engage mobile users with push notifications on iOS and iPadOS. Follow our dedicated guide for steps on how to support [web push on Safari for iOS and iPadOS]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/).

### User Update component use cases

The User Update component in Canvas allows you to update a user’s attributes, events, and purchases in a JSON composer—but are you not quite sure how to make the most of this feature? We've added [three example use cases]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#use-cases) to give you some ideas.

### User lookup

This new article describes how to use [user lookup]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup) to search for a specific user directly from the composer to test if your filters and segments are set up correctly. This can also be helpful when troubleshooting a campaign or Canvas that isn’t sending as expected—for example, if users aren’t receiving a message when they should be.

User lookup is available when:

- Creating a segment
- Setting up a campaign or Canvas audience
- Setting up an Audience Paths step

### Blocklisting or deleting custom data

This new article describes how to retire a custom data object by [blocklisting or deleting custom data]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/blocklist_delete_custom_data/).

You may occasionally identify custom attributes, custom events, or purchase events that are either consuming too many data points, are no longer useful to your marketing strategy, or were recorded in error. To stop this data from being sent to Braze, you can blocklist a custom data object while your engineering team works to remove it from the backend of your app or website.

### New Braze partnerships

#### Sisu Data - Business intelligence

The [Sisu Data]({{site.baseurl}}/partners/data_and_analytics/business_intelligence/sisu_data/) and Braze integration allows you to understand across all campaigns or at a campaign level why metrics (e.g., open rate, click-through rate, conversion rate, etc.) are changing and what drives the most optimal outcomes. Once these segments are identified, Braze users can materialize the outputs in their data warehouse or send them directly from Sisu to Braze to retarget and reengage users.

#### Loplat - Contextual location

The Braze and [loplat]({{site.baseurl}}/partners/message_personalization/location/loplat/) integration allows you to use loplat’s location services (store POI and custom geofence) to trigger geo-contextual marketing campaigns and create custom events using offline segmentation. When users visit the targeted location you set in loplat X, the campaign and location information are sent immediately to Braze.

#### ActionIQ - Customer data platform

The Braze and [ActionIQ]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/actioniq/) integration allows brands to sync and map their ActionIQ data directly to Braze, empowering the delivery of extraordinary customer experiences based on the entire breadth of their customer data. The integration enables the users to:

- Map audience segments or custom attributes to Braze directly from ActionIQ
- Forward the events tracked by ActionIQ to Braze in real time to trigger personalized and targeted campaigns

#### Komo - Dynamic content

The Braze and [Komo]({{site.baseurl}}/partners/message_personalization/dynamic_content/komo/) integration allows you to gather first and zero-party data through Komo Engagement Hubs. These hubs are dynamic microsites that offer interactive content and gamification features. The user data collected from these hubs are then transmitted to the Braze API.

- Ingest first and zero-party user data gather from Komo to Braze in real-time
- Ingest market research and user preference data when they answer surveys, polls, and quiz questions
- Progressively build user profiles in Braze over time as the user continues to engage and share more data about themselves
- Standardize the look and feel of transactional emails sent through Braze

#### Phrase - Localization

The [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase/) and Braze integration allow you to translate email templates and content blocks without leaving the Braze interface. With the Phrase TMS integration for Braze, you can increase customer engagement and drive growth into new markets with seamless localization.

#### Nift - Loyalty

The Braze and [Nift]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/nift/) integration allows you to automatically trigger “thank-yous” containing Nift gifts at key moments in the customer lifecycle and identify which customers used their gift. Nift gift cards can be used to access products and services supplied by brands relying on Nift’s matchmaking technology to acquire new customers cost-effectively at scale.

#### Sageflo - Message templates

The Braze and [Sageflo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/sageflo/) integration empowers local teams to easily send their own emails using marketing-approved templates, images, and audience segments through API integrations with Braze.

#### Airbyte - Workflow automation

The Braze and [Airbyte]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/airbyte/) integration allows users to create a data pipeline to collect and analyze Braze data by connecting all of your applications and databases to a central warehouse. Once data has been collected in the central warehouse, data teams can explore Braze data effectively using their preferred business intelligence tools.

#### Flywheel - Workflow automation

The Braze and [Flywheel]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/flywheel/) integration allows you to segment customer data directly from data warehouse and send it to Braze–ensuring that users can optimize the deep feature set of Braze in tandem with their single source of truth. Streamline marketing efforts for customer segmentation and activation, reducing the time it takes to segment, launch, test, and measure the results of targeted campaigns sent to Braze.

#### Mozart Data - Workflow automation

The Braze and [Mozart Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/mozart_data/) integration allows you to:

- Use Fivetran to import Braze data into Snowflake
- Create transforms by combining Braze data with other applications data and effectively analyze user behaviors
- Import data from Snowflake into Braze to create new customer engagement opportunities
- Combine Braze data with other applications data to gain a more holistic understanding of user behaviors
- Integrate with a business intelligence tool to further explore the data that is stored in Snowflake

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Swift SDK 5.10.0-5.11.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 4.6.2-4.6.3](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Segment iOS SDK 4.6.1](https://github.com/Appboy/appboy-segment-ios/releases)
- [AppboyKit iOS SDK 4.5.4](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.5.4)
- [React Native SDK 2.0.0-2.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Xamarin SDK 1.27.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [ExpoPlugin 1.0.0-1.1.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
   - Now requires Braze React Native SDK v2.1.0+.
   - Updates the default Kotlin version to 1.8.10 for Expo 48 compatibility. This value is overridden by the `android.kotlinVersion` property in `app.json`.
- [Roku SDK 0.1.3](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)

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

The following Currents events have recently been released and added to the [message engagement event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) and [customer behavior and user event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events) glossaries:

Message abort events:
- `users.messages.contentcard.abort`
- `users.messages.email.abort`
- `users.messages.inappmessage.abort`
- `users.messages.newsfeedcard.abort`
- `users.messages.pushnotification.abort`
- `users.messages.sms.abort`
- `users.messages.webhook.abort`

SMS short link click events:
- `users.messages.sms.ShortLinkClick`

Global state change subscription event:
- `users.behaviors.subscription.GlobalStateChange`

Subscription group state change event:
- `users.behaviors.subscriptiongroup.StateChange`

Canvas exit events:
- `users.canvas.exit.PerformedEvent`
- `users.canvas.exit.MatchedAudience`

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
- [Android SDK 24.1.0-24.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2420)
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
- [Android SDK 24.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
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
In previous versions of the Braze iOS Swift SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user's device ID. Beginning in Swift SDK v5.7.0, the IDFV field can optionally be disabled, and instead, Braze will set a random UUID as the device ID. For more information, refer to [Collecting IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/).

### Snowflake Reader Accounts
Snowflake Reader Accounts offer users access to the same data and functionality as [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/), all without requiring a Snowflake account or customer relationship with Snowflake. With Reader Accounts, Braze will create and share your data into an account and provide you credentials to log in and access your data. This will result in all data sharing and usage billing being handled entirely by Braze.

To learn more, reach out to your customer success manager.

### Updated Shopify integration
The [Shopify integration]({{site.baseurl}}/partners/additional_channels_and_extensions/ecommerce/shopify/shopify/) now allows you to collect email and SMS opt-ins from your Shopify store and assign them to a subscription group in Braze.



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
[Phrasee React]({{site.baseurl}}/partners/message_orchestration/ab_testing/phrasee/phrasee_react/), powered by Phrasee X, leverages Braze Currents and Connected Content to collect click tracking information from your subscribers via webhooks. Phrasee then ties those events back to your language variants for real-time language optimization.

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
- [React Native SDK v1.41.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
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

- [Android SDK 23.3.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2330)
- [Web SDK 4.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#440)
- [Unity SDK 3.11.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md#3110)
- [Xamarin SDK 1.26.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#1260)
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

- [Android SDK 23.2.0-23.2.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2321)
- [iOS Objective-C SDK 4.5.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#451)
- [iOS Swift SDK 5.5.0S-SDK 5.5.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#550)
- [Cordova SDK 2.31.0](https://github.com/Appboy/appboy-cordova-sdk/blob/master/CHANGELOG.md#2310)
  - Updated to [Braze Android SDK 23.0.1](https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.0.1).
- [Unity 3.10.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md#3100)
- [React SDK v1.39.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1400)
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
The Braze and [Shopify]({{site.baseurl}}/partners/additional_channels_and_extensions/ecommerce/shopify/shopify/) allows you to update existing user profiles or create new ones in Braze for leads, sign-ups, and account registrations being captured in your Shopify store.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 23.1.0–23.12](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
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

[support]: {{site.baseurl}}/support_contact/

[1]: {% image_buster /assets/img/doc-breadcrumbs.png %} 

<br><br>
