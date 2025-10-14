---
nav_title: Home
article_title: Release Notes
description: "Stay up-to-date on major product releases, ongoing product improvements, Braze partnerships, breaking SDK changes, and feature deprecations."
page_order: 0
search_rank: 1
page_type: landing
layout: dev_guide

guide_top_header: "Release notes"
guide_top_text: "> Braze release notes are published monthly so you can stay up-to-date on major product releases, ongoing product improvements, Braze partnerships, breaking SDK changes, and feature deprecations."

guide_featured_list:
  - name: 2025
    link: /docs/releases/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2024
    link: /docs/releases/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/releases/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/releases/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/releases/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/releases/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/releases/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/releases/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/releases/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/releases/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Deprecations
    link: /docs/releases/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: SDK Changelogs
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

{% alert tip %}
For more information on any of the updates listed on this page, reach out to your account manager or [open a support ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). You can also check out our [SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs) for more information about our monthly SDK releases, improvements, and breaking changes.
{% endalert %}

## October 14, 2025 release

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) replaces A/B testing with AI decisioning that personalizes everything, and maximizes any metric: drive dollars, not clicks. With BrazeAI Decisioning Studio™, you can optimize any business KPI. Refer to our dedicated section [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) for sample use cases and key features.

### Data flexibility

#### New Currents events

These new events were added to the [Currents glossary]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events):

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`.
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`

#### Suppression lists

{% multi_lang_include release_type.md release="General availability" %}

[Suppression lists]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) are groups of users who automatically do not receive any campaigns or Canvases. Suppression lists are defined by segment filters, and users will enter and exit suppression lists as they meet filter criteria.

#### Zero-copy personalization

{% multi_lang_include release_type.md release="Early access" %}

Sync Canvas triggers using Cloud Data Ingestion for [zero-copy personalization]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). This feature accesses user-specific information from your data storage solution and passes it to a destination Canvas. Canvas steps can optionally include personalization fields that are not persisted on Braze user profiles.

#### Canvas Context variables for Audience Paths and Decision Split steps

{% multi_lang_include release_type.md release="Early access" %}

You can [create context variable filters]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-filters) that use previously declared context variables in [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) and [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) steps.

### Unlocking creativity

#### Deal Cards for emails

Use [Deal Cards]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) to provide key deal information directly at the top of email bodies. This allows recipients to quickly understand the offer details and take action.

#### Templates for Banners

When you [compose your Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns), you can now either start with a blank template, use a Braze template, or select a saved Banner template.

### Robust channels

#### SMS and RCS bot click filtering

{% multi_lang_include release_type.md release="General availability" %}

[SMS and RCS bot click filtering]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) enhances campaign analytics and workflows by excluding suspected bot clicks. A “bot click” refers to automated clicks on shortened links in SMS and RCS messages, such as those from web crawlers, Android and iOS link previews, or CPaaS security software. This feature facilitates accurate reporting, segmentation, and orchestration to engage real users.

#### Transfer WhatsApp phone numbers

Transfer a WhatsApp Business Account (WABA) phone number and its associated subscription group [from one workspace to another]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) within Braze.

#### WhatsApp Flows response messages and preview

In a Canvas, you can create a WhatsApp message step that uses a [response message]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) and flow message. You can also select **Preview Flow** to preview the Flow directly in Braze to confirm it behaves as expected

### WhatsApp product messages

[Product messages]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/) empower you to send interactive WhatsApp messages that showcase products directly from your Meta catalog.

### Integrating Braze and WhatsApp with an external system

[Leverage the power of AI chatbots and live agent hand-offs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) on the WhatsApp channel to streamline your customer support operations. By automating routine inquiries and seamlessly transitioning to human agents when needed, you can significantly improve response times and enhance the overall customer experience.

### AI and ML automation

#### Braze Agents

{% multi_lang_include release_type.md release="Beta" %}

[Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences.

### New Braze partnerships

#### Jasper - Templates

The [Jasper]({{site.baseurl}}/partners/jasper/) and Braze integration empowers you to streamline content creation and campaign execution. With Jasper, your marketing teams can generate high-quality, on-brand copy in minutes. Braze will then facilitate the delivery of these messages to the right audience at the optimal time. This integration fosters seamless workflows, reduces manual effort, and drives stronger engagement outcomes.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Updated the native Android bridge [from Braze Android SDK 37.0.0 to 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The minimum required GradlePluginKotlinVersion is now 2.1.0.
    - Updated the native iOS bridge [from Braze Swift SDK 12.0.0 to 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). This includes Xcode 26 support.
    - Removes support for News Feed. The following APIs have been removed:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Updates the native Android SDK version bindings [from Braze Android SDK 37.0.0 to 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Removes support for News Feed. The following APIs have been removed:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Updated the native iOS bridge [from Braze Swift SDK 12.0.0 to 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). This includes Xcode 26 support.

## September 16, 2025 release

### Data flexibility

#### Braze Data Platform

Braze Data Platform is a set of comprehensive, composable set of data capabilities and partner integrations that empowers you to create personalized, impactful experiences across the customer lifecycle. Learn more about the three data related jobs to be done: 

- [Data unification]({{site.baseurl}}/user_guide/data/unification)
- [Data activation]({{site.baseurl}}/user_guide/data/activation)
- [Data distribution]({{site.baseurl}}/user_guide/data/distribution)

#### Deleting user profiles

{% multi_lang_include release_type.md release="Early access" %}

Now you can delete individual users or a segment of users directly through the Braze dashboard&#8212;instead of only relying on the Braze REST API.  You'll need to contact your customer success manager if you'd like to participate in the early access. To get started, see [Deleting users]({{site.baseurl}}/user_guide/data/unification/user_data/delete_users/).

#### Custom Banner properties

{% multi_lang_include release_type.md release="Early access" %}

You can use custom properties from your Banner campaign to retrieve key–value data through the SDK and modify your app’s behavior or appearance. To learn more, see [Custom Banner properties]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Token authentication

{% multi_lang_include release_type.md release="General availability" %}

When using Braze Connected Content, you may find that certain APIs require a token instead of a username and password. Braze can store credentials that hold [token authentication header values]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication).

#### Promotion codes

You can save promotion codes to a user’s profile through a User Update step. For more information, refer to [Saving promotion codes to user profiles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Unlocking creativity

#### Braze Pilot

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) is a publicly available app for Android and iOS that allows you to launch messages from your Braze dashboard to your phone. Check out [Getting started with Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) for a walkthrough of downloading the app, initializing the connection to your Braze dashboard, and completing the setup.

### New Braze partnerships

#### Blings - Visual and interactive content

[Blings]({{site.baseurl}}/partners/blings/) is a next-generation personalized video platform that enables you to deliver real-time, interactive, and data-driven video experiences across channels at scale.

#### Shopify standard integration with third-party tool

For Shopify online stores, we recommend using Braze’s standard integration method to support the Braze SDKs on your site.

However, we understand that you may prefer using a third-party tool, like Google Tag Manager, so we put together a guide on how you can. To get started, see [Shopify: Third-party tagging]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Updates the native Android bridge from Braze Android SDK `36.0.0` to `39.0.0`.
    - Updates the native iOS bridge from Braze Swift SDK `12.0.0` to `13.2.0`. This includes Xcode 26 support.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Updates the Braze Swift SDK bindings to require releases from the `13.0.0+` SemVer denomination. This allows compatibility with any version of the Braze SDK from `13.0.0` up to, but not including, `14.0.0`.

## August 19, 2025 release

### Time zone consistency standardization to Canvas Context

{% multi_lang_include release_type.md release="Early access" %}

If you're participating in the [Canvas Context step early access]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), all timestamps with a datetime type from trigger event properties in action-based Canvases will always be normalized to [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). To learn more about this, refer to [Time zone consistency standardization]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Data flexibility

#### Self-serve custom domains

{% multi_lang_include release_type.md release="General access" %}

[Self-serve custom domains]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) empower you to configure and manage your own custom domains for SMS, RCS, and WhatsApp—directly from your Braze dashboard. You can easily add, monitor, and manage up to 10 custom domains in one place.

#### Segment funnel statistics

Select [View funnel statistics]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) to display the statistics for that filter group and see how each added filter impacts your segment statistics. You’ll see an estimated count and percentage for users who are targeted by all filters up to that point. Once the statistics are displayed for a filter group, they will update automatically whenever you change the filters. 

#### New response fields for `/campaigns/details` endpoint for push notifications

The `messages` response for push notifications now includes two new fields:

- `image_url`: An image URL for an Android notification image, an iOS notification image, or a web push icon image.
- `large_image_url`: A web notification image URL for Android Chrome and Windows web push actions.

#### Defining PII fields

Selecting and [defining certain fields as PII fields]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) only affects what Users can view on the Braze dashboard and does not impact how the End User data in such PII fields is handled.

Consult your legal team to align your dashboard’s settings with any privacy regulations and policies applicable to your company, including those related to [data retention]({{site.baseurl}}/api/data_retention/).

#### Sharing a Report Builder download link

You can [share a dashboard link]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) to the report by selecting **Share** and then **Share a link** or **Send or schedule an email**.

### Unlocking creativity

#### Custom head tags for drag-and-drop emails

Use `<head>` tags to add CSS and metadata in your email message. For example, you can use these tags to add a stylesheet or favicon. Liquid is supported in `<head>` tags.

### Robust channels

#### Fuzzy out-out best practices

We've added a [best practices section]({{site.baseurl}}) to help you thoughtfully configure your fuzzy opt-out message and create a clear, compliant, and positive experience for your subscribers.

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) is an enhancement to the existing WhatsApp channel, allowing you to create interactive and dynamic messaging experiences. 

#### WhatsApp inbound product questions

Users can respond to your product or catalog message with [product questions]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions). These arrive as inbound messages, which can then be sorted with an Action Path.

Additionally, Braze extracts the product ID and catalog ID from these questions, so if you wish to automate responses or send questions to another team (such as customer support), you can include those details.

### AI and ML automation

#### New BrazeAI™ use case articles

We’ve added new use case articles to help you get the most out of BrazeAI™. These guides highlight practical ways to apply AI to your engagement strategies, including:

- [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/use_case): Identify customers at risk of churning and take action early.
- [Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_events/use_case): Anticipate key user actions and shape experiences in real time.
- [Recommendations]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Deliver more relevant content and products based on customer behavior.

#### MCP server

{% multi_lang_include release_type.md release="Beta" %}

The [Braze MCP server]({{site.baseurl}}/user_guide/brazeai/mcp_server/), a secure and read-only connection, lets AI tools like Claude and Cursor access non-PII Braze data to answer questions, analyze trends, and provide insights without altering data.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Extends the functionality of `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` to be triggered for "Optional" authentication errors.
        - The delegate method `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` will now be triggered for both "Required" and "Optional" authentication errors.
        - If you want to only handle "Required" SDK authentication errors, add a check ensuring that `BrazeSDKAuthError.optional` is false inside your implementation of this delegate method.
    - Fixes the usage of `Braze.Configuration.sdkAuthentication` to take effect when enabled.
        - Previously, the value of this configuration was not consumed by the SDK and the token was always attached to requests if it was present.
        - Now, the SDK will only attach the SDK authentication token to outgoing network requests when this configuration is enabled.
    - The setters for all properties of `Braze.FeatureFlag` and all properties of `Braze.Banner` have been made `private`. The properties of these classes are now read-only.
    - Removes the `Braze.Banner.id` property, which was deprecated in version `11.4.0`.
        - Instead, use `Braze.Banner.trackingId` to read a banner's campaign tracking ID.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Updates the native Android SDK version bindings from [Braze Android SDK 36.0.0 to 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updates the native Swift SDK version bindings from [Braze Swift SDK 12.0.0 to 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The `sdkAuthenticationError` event will now trigger for both "Required" and "Optional" authentication errors.
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Added support for .NET 9.0 for the iOS and Android bindings.
        - This removes support for .NET 8.0.
        - This requires a [minimum version of iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Updated the Android binding from [Braze Android 32.0.0 to 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the iOS binding from [Braze Swift SDK 10.0.0 to 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - This release contains APIs for the Banners feature but is not currently fully supported by this SDK. If you wish to use Banners in your .NET MAUI app, contact your customer support manager before integrating into your application.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Updated the internal iOS implementation of `enableSdk` method to use `setEnabled`: instead of `_requestEnableSDKOnNextAppRun`, which was deprecated in the Swift SDK.
    - Calling this method no longer requires the app to be re-launched to take effect. The SDK will now become enabled as soon as this method is executed.
    - Updated the native Android bridge from [Braze Android SDK `36.0.0` to `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

## July 22, 2025 release

### Security events export with Amazon S3

You can automatically [export Security Events to Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/), a cloud storage provider, with a daily job that runs at midnight UTC. Once set up, you don't need to manually export Security Events from the dashboard.

### Data flexibility

#### CSV import

{% multi_lang_include release_type.md release="General availability" %}

You can use CSV import to record and update user attributes and custom events in Braze like `first_name`, `last_destination_searched`, and `trip_booked`. To get started, see [CSV Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### API usage alerts

{% multi_lang_include release_type.md release="General availability" %}

API usage alerts provide critical visibility into your API usage, allowing you to proactively detect unexpected traffic. By setting up these alerts to track key API request volumes, you can receive real-time notifications and address problems before they impact your marketing campaigns.

#### Workspace API rate limits

With workspace API rate limits, you can set a maximum number of API requests a workspace can make to a specific ingestion endpoint, such as `/users/track` or SDK data. You can also apply rate limits to a group of workspaces, meaning the limit is shared across all the workspaces in that group.

#### New Currents events

These new events were added to the Currents glossary:

- [Banner Abort events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Banner Click events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Banner Impression events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Banner Viewed events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Webhook Failure events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Default time range for campaign analytics

By default, the time range for [**Campaign Analytics**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) will display the last 90 days from the current time. This means that if the campaign was launched more than 90 days ago, the analytics will display as "0" for the given time range. To view all analytics for older campaigns, adjust the reporting time range.

#### Updated behavior for Canvas Experiment Paths step

If your Canvas has an active or in-progress [experiment]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) and you update the active Canvas (even if it's not to the Experiment Path step), the in-progress experiment will end. To restart the experiment, you can disconnect the existing Experiment Path and launch a new one, or duplicate the Canvas and launch a new Canvas. 

For more information, refer to [Editing Canvases after launch]({{site.baseurl}}/post-launch_edits/).

#### Faster rate limit available for `/users/export/ids` endpoint

You can also increase the [rate limit for the /users/export/ids endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) to 40 requests per second by meeting the following requirements:

- Your workspace has the default rate limit (250 requests per minute) enabled. Contact your Braze account manager for further assistance with removing any pre-existing rate limit you may have.
- Your request includes the fields_to_export parameter to list out all the fields you want to receive.

#### New translation for email templates endpoints

{% multi_lang_include release_type.md release="Early access" %}

Use these endpoints to view and make updates to translations and locales for email templates:

- [GET: View the source translations]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET: View a specific translation and locale for email template endpoint]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [GET: View all translations and locales for an email template]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [PUT: Update translations for an email template]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### Unlocking creativity

#### Landing pages

You can make your landing page [responsive to the size of a user's device]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) by vertically stacking columns on smaller screens. To enable this, add a column into the row you want to make responsive, and then toggle on **Vertically stack on smaller screens** in the **Customize columns** section.

### Robust channels

#### Bot filtering for emails

{% multi_lang_include release_type.md release="General availability" %}

Set up bot filtering in your [Email Preferences]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) to exclude all suspected machine or bot clicks. A "bot click" in email refers to a click on hyperlinks within an email that's generated by an automated program. By filtering these bot clicks, you can intentionally trigger and deliver messages to recipients who are engaged.

#### Drag-and-drop product blocks

{% multi_lang_include release_type.md release="Early access" %}

The [drag-and-drop editor]({{site.baseurl}}/dnd_product_blocks/) empowers you to quickly add and configure product blocks to your messages for seamless product showcases, without the need to create custom Liquid code. The drag-and-drop product block feature is currently only available for email.

#### Span text for landing pages and in-app messages

Span text allows you to apply specific styling to text blocks without custom code for your [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) and [in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks). To do so, highlight the text you want to style and then select **Wrap with span for style**. 

#### Ad Click to WhatsApp

[Ads That Click to WhatsApp]({{site.baseurl}}/whatsapp_use_cases/) are an efficient way to bring both new and existing customers from Meta ads on Facebook, Instagram, or other platforms. Use these ads to promote your products and services while making users aware of your WhatsApp presence. 

### New Braze partnerships

#### Shopify Visitory API — eCommerce

Braze collects visitor information, such as email addresses and phone numbers, through in-browser messages. This information is then sent to Shopify. This data helps merchants recognize visitors to their store and create a more personalized shopping experience.

#### Okendo — eCommerce

The Braze and [Okendo]({{site.baseurl}}/partners/okendo/) integration works across multiple products in Okendo's platform, including Reviews, Loyalty, Referrals, Surveys, and Quizzes. Okendo sends custom events and user attributes to Braze, which can be used to personalize and trigger messages.

#### Lemnisk — Customer Data Platform

The Braze and [Lemnisk]({{site.baseurl}}/partners/lemnisk/) integration allows brands and enterprises to unlock the full potential of Braze by acting as a CDP-led intelligence layer that unifies user data across platforms in real time, and sending the user's information and behaviors collected to Braze in real-time.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Web SDK 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Removed the `Banner.html` property, `logBannerClick`, and `logBannerImpressions` methods. Instead, use [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) which automatically handles impression and click tracking.
    - Removed support for the legacy News Feed feature. This includes removal of the Feed class, and its associated methods.
    - The created and categories fields that were used by legacy News Feed cards have been removed from [`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) subclasses.
    - The linkText field was also removed from the [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) Card subclass and its constructor.
    - Clarified definitions and updated types to note that certain SDK methods explicitly return undefined when the SDK is not initialized, aligning the typings with actual runtime behavior. This could introduce new TypeScript errors in projects that relied on the previous (incomplete) typings.
    - The images of in-app messages with `cropType` of `CENTER_CROP` (such as `FullScreenMessage` by default) are now rendered via an `<img>` tag instead of `<span>` for improved accessibility. This may break existing CSS customizations for the `.ab-center-cropped-img` class or its children.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Updated the internal iOS implementation of `enableSdk` method to use setEnabled: instead of `_requestEnableSDKOnNextAppRun`, which was deprecated in the Swift SDK.
        - Calling this method no longer requires the app to be re-launched to take effect. The SDK will now become enabled as soon as this method is executed.
    - Updated the native Android bridge [from Braze Android SDK 36.0.0 to 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Android SDK 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

## June 24, 2025 release

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) replaces A/B testing with AI decisioning that personalizes everything, and maximizes any metric: drive dollars, not clicks—with BrazeAI Decisioning Studio™, you can optimize any business KPI. Refer to our dedicated section [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) for sample use cases and key features.

### New SDK tutorials

Each Braze SDK tutorial offers step-by-step instructions along with full sample code. Choose a tutorial below to get started:

- [Displaying Banners]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Customizing in-app message styling]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Conditionally displaying in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Deferring triggered in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Data flexibility

#### SAML just-in-time provisioning

{% multi_lang_include release_type.md release="General availability" %}

Use [SAML just-in-time provisioning]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) to allow new dashboard users to create a Braze account on their first sign in. This eliminates the need for administrators to manually create an account for a new dashboard user, choose their permissions, assign them to a workspace, and wait for them to activate their account.

#### Filters per selection

You can now add up to 10 filters per [selection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections).

#### Catalog storage

The storage size for the free version of [catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#catalog-storage) is up to 100&nbsp;MB. You can have unlimited items as long as they're under 100&nbsp;MB.

#### Number of rows synced with Cloud Data Ingestion

By default, for Cloud Data Ingestion, each run can sync up to 500 million rows. Any syncs with more than 500 million new rows will be stopped.

Refer to [Cloud Data Ingestion product limitations]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations) for more details.

### Robust channels

#### Accessibility testing in Inbox Vision

{% multi_lang_include release_type.md release="General availability" %}

Use [Accessibility testing]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) in Inbox Vision to highlight accessibility issues that may exist with your email. 

Accessibility testing analyzes your email content against some [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA requirements. This can provide insights into which elements aren't meeting accessibility standards.

#### Click tracking for WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

You can turn on [click tracking]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) in both response and template messages to see click data in your WhatsApp performance reports and be able to segment users based on who clicked what.

#### Videos for WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

You can [embed videos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) within the body text for outbound WhatsApp messages. These files must be hosted through URL or in the [Braze media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library).

### New Braze partnerships

#### Stripe - eCommerce

The Braze and [Stripe]({{site.baseurl}}/partners/stripe) intergation allows you to trigger messaging in Braze based on Stripe events such as trial started, subscription activated, subscription cancellation, and more.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Updated the native Android bridge [from Braze Android SDK 35.0.0 to 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native iOS bridge [from Braze Swift SDK 11.6.1 to 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Segment Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Updated Braze Android SDK [from 35.0.0 to 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

## May 27, 2025 release

### Data flexibility

#### Copying Canvases across workspaces

{% multi_lang_include release_type.md release="General availability" %}

You can now copy Canvases across workspaces. This lets you jumpstart your message composition by starting with a copy of a Canvas in a different workspace. For more information on what's copied over, refer to [Copying campaigns and Canvases across workspaces]({{site.baseurl}}/copying_to_workspaces/).

#### Messaging rules for approval workflow 

{% multi_lang_include release_type.md release="General availability" %}

Use [messaging rules]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules) in your approval workflow to limit the number of reachable users before an additional approval is required—this way, you can review your campaigns and Canvases before you target a larger audience.

#### Entity relationship diagrams for Snowflake and Braze

Earlier this year, we created entity relationship tables for data shared between Snowflake and Braze. This month, we added [new interactive diagrams]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/) where you can pan, grab, and zoom into the details of each table, giving you a better idea of how your data interacts with Braze.

### Unlocking creativity

#### Recommended events

{% multi_lang_include release_type.md release="Early access" %}

[Recommended events]({{site.baseurl}}/user_guide/data/custom_data/recommended_events) map to the most common eCommerce use cases. By using recommended events, you can unlock pre-built Canvas templates, reporting dashboards that map to the customer lifecycle, and more.

### Robust channels

#### Banners channel

{% multi_lang_include release_type.md release="General availability" %}

With [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners), you can create personalized messaging for your users, all while extending the reach of your other channels, such as email or push notifications. You can embed Banners directly in your app or website, which lets you engage with users through an experience that feels natural.

#### Rich Communication Services (RCS) channel

{% multi_lang_include release_type.md release="General availability" %}

[Rich Communication Services (RCS)]({{site.baseurl}}/about_rcs/) enhances traditional SMS by enabling brands to deliver messages that are not only informative but also far more engaging. Now supported on both Android and iOS, RCS brings features like high-quality media, interactive buttons, and branded sender profiles directly into users’ pre-installed messaging apps, eliminating the need to download a separate app.

#### Push Settings page

{% multi_lang_include release_type.md release="General availability" %}

Use the [**Push Settings** page]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings) to configure key settings for your push notifications, including the Push Time to Live (TTL) and the default FCM priority for Android campaigns. These settings help optimize the delivery and effectiveness of your push notifications, ensuring a better experience for your users.

#### Promotion codes for in-app message campaigns

{% multi_lang_include release_type.md release="Early access" %}

You can use [promotion codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) in in-app message campaigns by inserting a [promotion code list snippet]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) into the message body of your in-app message campaign.

#### Handling webhook errors and rate limiting

[About webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#webhook-error-handling-and-rate-limiting) has a new section that describes how Braze handles webhook errors and rate limiting.

#### In-app message locales

After [adding locales]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/using_locales) to your workspace, you can target users in different languages all within a single in-app message.

#### Amazon SES as an Email Sending Provider (ESP)

You can now use Amazon SES as an ESP, similar to how you would use SendGrid and SparkPost. Refer to [SSL at Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) and [Universal Links and App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) for nuances in SSL set up and click-tracking on a link-to-link basis.

### New Braze partnerships

#### Eagle Eye - Loyalty

The Braze and [Eagle Eye]({{site.baseurl}}/partners/eagle_eye/) bi-directional integration allows you to activate loyalty and promotional data directly in Braze, allowing marketers to personalize customer engagement using real-time data such as point balances, promotions, and reward activities.

#### Eppo - A/B Testing

The Braze and [Eppo]({{site.baseurl}}/partners/eppo/) integration allows you to set up A/B tests in Braze and analyze results in Eppo to uncover insights and tie message performance to long-term business metrics like revenue or retention.

#### Mention Me - Referrals

Together, [Mention Me](https://www.mention-me.com/) and Braze can be your gateway to attracting premium customers and fostering unwavering brand loyalty. By seamlessly integrating first-party referral data into Braze, you can deliver highly-personalized omnichannel experiences targeted at your brand fans. To get started, see [Technology Partners: Mention Me]({{site.baseurl}}/partners/mention_me).

#### Shopify - eCommerce

[Connect multiple Shopify store domains]({{site.baseurl}}/shopify_connecting_multiple_stores/) to a single workspace to have a holistic view of your customers across all markets. Build and launch automation programs and journeys in a single workspace without duplicating efforts across regional stores.

### Other

#### Update to Building accessible messages in Braze

We’ve updated our [Building accessible messages in Braze]({{site.baseurl}}/help/accessibility/) article with clearer, more prescriptive guidance on creating accessible messages. This article now includes expanded best practices for content structure, alt text, buttons, and color contrast, along with a new section on ARIA handling for custom HTML messages. 

This update is part of our broader effort to support more accessible messaging experiences in Braze. We know accessibility is an evolving area, and we’ll keep sharing what we learn.

{% multi_lang_include accessibility/feedback.md %}

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 36.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. Note that while we are re-introducing the ability to compile, we are not reintroducing formal support for < API 25, and cannot guarantee that the SDK will work as intended on devices running those versions.
    - If your app supports those versions, you should:
        - Validate your integration of the SDK works as intended on physical devices (not just emulators) for those API versions.
        - If you cannot validate expected behavior, you must either call [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html), or not initialize the SDK on those versions. Otherwise, you may cause unintended side effects or degraded performance on your end users' devices.
    - Fixed an issue where in-app messages would cause a read on the main thread.
    `BrazeInAppMessageManager.displayInAppMessage` is now a Kotlin suspend function.
        - If you do not call this function directly, you do not need to make any changes.
    - AndroidX Compose BOM updated to 2025.04.01 to handle updates in the Jetpack Compose APIs.
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Updates the native Android bridge from Braze Android SDK 35.0.0 to 36.0.0.
    - Updates the native iOS version bindings from Braze Swift SDK 11.9.0 to 12.0.0.
    - Updates the unit representation of PushNotificationEvent.timestamp to milliseconds on iOS.
        - Previously, this value would be represented in seconds on iOS. This will now match the existing Android implementation.
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. However, we are not reintroducing formal support for < API 25. Read more [here](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600).
    - Updates the native Android bridge from Braze Android SDK 35.0.0 to 36.0.0.
    - Updates the native iOS bridge from Braze Swift SDK 11.9.0 to 12.0.0.

## April 29, 2025 release

### Troubleshooting Braze access

[Troubleshooting Braze Access]({{site.baseurl}}/user_guide/administrative/access_braze/troubleshooting/) helps you navigate issues you may have when trying to access Braze, such as getting locked out of your account or working with a Braze dashboard that won’t perform as expected.

### Data flexibility

#### Currents frequently asked questions

You can find answers to some frequently asked questions about Currents on the new [Frequently asked questions]({{site.baseurl}}/user_guide/data/braze_currents/faq/) page.

#### Anonymous users

Check out the following sections in [Anonymous users]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) for new details about how anonymous users work and why you might want to assign them user aliases:
- [How it works]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#how-it-works) 
- [Assigning user aliases]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#assigning-user-aliases)

#### Campaign drafts

[Saving drafts]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#campaign-drafts) can help you make large-scale changes to active campaigns. By creating a draft, you’re able to pilot planned changes before your next launch.

#### Identifying and merging users

When [identifying]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) or [merging users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/), you can now use the `least_recently_updated` parameter in the `prioritization` array to prioritize the least recently updated user.

#### Scheduled user merging

[Scheduled merging]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#scheduled-merging) allows you to automate the merging of user profiles on a daily basis using preconfigured rules. Braze will notify the admins of your workspace 24 hours before the scheduled merge occurs, providing a reminder and time to review the configuration.

#### Recipient object

You can now include `braze_id` in the [recipient object]({{site.baseurl}}/api/objects_filters/recipient_object/), which allows you to request or write information in our endpoints.

#### New data centers

Braze has launched two new [data centers]({{site.baseurl}}/user_guide/data/data_centers/): US-10 and ID-01. You can sign up for region-specific data centers when setting up your Braze account. 

### Unlocking creativity

#### Landing page templates

Use [landing page templates]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#using-landing-page-templates) to create templates for your next campaigns. These templates can be accessed and managed in both the landing page editor and the **Templates** section of the dashboard.

#### Landing page form field

When customizing your landing page, you can choose whether a form field is [required or optional]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page). Required fields must be filled out before the form can be submitted. Optional fields can be left blank or unselected by a user.

#### Canvas pre-built templates

Braze Canvas offers several [pre-built templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) tailored specifically for eCommerce marketers, making it easier to implement essential strategies. This page offers some key templates you can use to enhance your customer journeys.

### Robust channels

#### WhatsApp videos

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp video files]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages) can now be hosted through either a URL or in the Braze media library.

#### WhatsApp list messages

[List messages]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages#list-messages/) appear as a body message with a list of clickable options. Each list can have multiple sections, and each list can have up to 10 rows.

#### Copy preview link

Use **Copy preview link** in your HTML and drag-and-drop [email messages]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#step-3-add-your-sending-information), [email templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/#step-5-preview-and-test-your-message), and [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) to generate a shareable link that shows how your content will look like for a random user.

#### Push registration diagram

We revamped our push notification documentation in the User Guide and added a new diagram to help visualize [what push registration looks like on a larger scale]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#what-does-this-look-like-on-a-broader-scale).

### New Braze partnerships

#### Updated partner categories

We updated the [Technology Partners section]({{site.baseurl}}/partners/home/) with new categories and subcategories to improve your navigation experience.

#### Shopify (new version) - eCommerce

A new version of the Shopify integration will be released in phases starting April, based on the type of Shopify store and the external ID used to set up the initial integration.

**The older version of the integration will be deprecated on August 28, 2025. You must update to the newer version of the integration before August 28, 2025.**

New Braze customers: Starting April 2025, Braze will be gradually rolling out the new Shopify connector for new onboardings and upgrading existing customers. To learn more about the new standard integration, refer to [Shopify standard integration]({{site.baseurl}}/shopify_standard_integration/).

#### Just Words - Dynamic Content

[Just Words]({{site.baseurl}}/partners/just_words/) hyper-personalizes messaging at scale on lifecycle marketing channels, empowering you to dynamically test hundreds of variations and auto-refresh underperforming content.

#### Tapcart - eCommerce

[Tapcart]({{site.baseurl}}/partners/ecommerce/tapcart/) is a leading mobile commerce platform for Shopify-powered brands, enabling merchants to create custom mobile apps that deliver personalized, engaging shopping experiences their customers love.

### SDKs

#### Braze SDK version management

You can now learn about [version management]({{site.baseurl}}/developer_guide/sdk_integration/version_management/) for the Braze SDK, so your app can stay up-to-date with the latest features and quality improvements.

#### SDK docs audit

We're currently auditing all our [SDK content for developers]({{site.baseurl}}/developer_guide/) to ensure all of our code samples are helpful and accurate. So far, we've made a variety of updates to our Android and Swift docs, and more are on the way.

### Contributing to Braze Docs

#### Offline support for Braze contributors

If you’re a Braze Docs contributor, you can now generate your local docs site completely offline. To get started, see [Contributing to Braze Docs]({{site.baseurl}}/contributing/home/).

#### Troubleshooting your Braze Docs fork

For Braze Docs contributors having trouble targeting our repository from their fork, we've created [troubleshooting steps]({{site.baseurl}}/contributing/troubleshooting/#missing-base-repository) to help get you back on track.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Braze Unity SDK 8.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
    - Updated the native iOS bridge from [Braze Swift SDK 10.3.0 to 11.9.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native Android bridge from [Braze Android SDK 32.1.0 to 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The minimum required Android SDK version is 25. See more details [here](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Braze Segment Kotlin 3.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
    - Updated Braze Android SDK [from 32.1.0 to 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The minimum required Android SDK version is 25. See more details [here](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200)
    - The distributed static XCFrameworks now include their resources directly instead of relying on external resources bundles.
        - When manually integrating the static XCFrameworks, you must select the *Embed & Sign* option for each XCFramework in the *Frameworks, Libraries, and Embedded Content* section of your target’s *General settings*.
        - No changes are required for Swift Package Manager or CocoaPods integrations.
- [Braze Segment Swift 6.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Updates the Braze Swift SDK bindings to require releases from the `12.0.0`+ SemVer denomination.
        - This allows compatibility with any version of the Braze SDK from `12.0.0` up to, but not including, `13.0.0`.
        - Refer to the changelog entry for [`12.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200) for more information on potential breaking changes.

## April 1, 2025 release

### Updates to Braze navigation

The updated navigation in Braze is designed to help you efficiently access features and content across devices. Note that the option to switch between navigation versions is no longer available. Learn more at our dedicated [Navigating Braze]({{site.baseurl}}/user_guide/administrative/access_braze/navigation) article.

### Developer Guide detangle

Previously, many platform-level tasks were split across multiple pages, such as integrating the Swift SDK being split across six pages. Additionally, shared features were individually documented for each platform, meaning searching for a topic like “Setting Up Push Notifications” would return 10 different pages.

**Before:**

![The previous Swift documentation located in the Platform Integration Guides section.]({% image_buster /assets/img/before_swift.png %})

Now, platform-level tasks have been merged into single pages and shared SDK features now exist on the same page (with the help of our new SDK-tabbing feature). For example, now there’s  only one page for Integrating the Braze SDK, where you can switch between platforms by selecting a tab at the top of the page. When you do, even the in-page table of contents will update to reflect the currently-selected tab.

**After:**

![The updated Swift documentation located in the Swift tab of the Integrating the SDK article.]({% image_buster /assets/img/after_swift.png %})

![The updated Android documentation located in the Android tab of the Integrating the SDK article.]({% image_buster /assets/img/after_android.png %})

### Contributing to Braze Docs

If you didn’t know, our docs are fully open-source! You can learn how in our [Contributing Guide]({{site.baseurl}}/contributing/home). This month, we documented some site functionality, like [forcing sections to auto-expand]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand) and [rendering API-generated content]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server).

### Data flexibility

#### Update to Canvas entry properties

Canvas entry properties are now part of [Canvas context variables]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Each context variable includes a name, data type, and a value that can include Liquid. For more information, refer to the [Context component]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

#### Updates to segmentation filters for phone number filters

Segmentation filters have been updated to reflect changes to two phone number filters:

- [Unformatted Phone Number]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (formerly **Phone Number**): Segments your users by their unformatted phone number.
- [Phone Number]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (formerly **Sending Phone Number**): Segments your users by the E.164 formatted phone number field.

#### Delete custom data

As you build targeted campaigns and segments, you may find that you no longer need a custom event or custom attribute. You can now [delete this custom data]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data) and remove its references from your app.

#### Import users with email addresses and phone numbers

You can now use an email address or phone number to [import users]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers) and omit an external ID or user alias.

#### Service Provider initiated login troubleshooting

Service Provider (SP) initiated login now has a [troubleshooting section]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting) to help you work through issues with SAML and single-sign on issues.

#### User import troubleshooting

The [User Import troubleshooting section]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting) has new and updated entries, including how to troubleshoot missing rows in your imported CSV files.

#### Frequently asked questions for Segment Extensions

Check out our [frequently asked questions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions) for Segment Extensions, including how you can create a Segment Extension that uses multiple custom events.

#### Personalized and extended delays

{% multi_lang_include release_type.md release="Early access" %}

You can set up a [personalized delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays) for your users and use this with a Context step to select the context variable to delay by.

You can also now extend Delay steps up to two years. For example, if you’re onboarding new users for your app, you can add an extended delay for two months before sending a Message step to nudge the users who haven’t started a session.

#### Default user profile attributes for Snowflake

{% multi_lang_include release_type.md release="Beta" %}

There are now three [default user profile attributes]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes/) in Snowflake. Each view is designed for a specific use case with its own performance considerations. For example, you can be provided a periodic snapchat of a user profile's default attributes.

### Robust channels

#### Messaging fundamentals

[Messaging Fundamentals]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals) is a new section in Engagement Tools that houses the shared concepts and terms for campaigns and Canvases, such as archiving and localizing messages.

#### WhatsApp custom domains

You can now assign [custom domains]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/) to one or multiple WhatsApp subscription groups.

#### Triggered in-app messages for Canvas

You can now select a [trigger for your in-app messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) to be triggered on session start, or by custom events and purchases. After any delays pass and the audience options are checked, in-app messages are set to live when a user reaches the Message step. If a user starts a session and performs the trigger event for the in-app message, the user will see the in-app message. 

#### Limit entrance volume for Canvas

You can limit the number of people who would potentially enter this Canvas by a selected cadence (daily, lifetime of the Canvas, or every time the Canvas is scheduled). For example, you can [set the entry controls]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience) to allow the Canvas to only send to 5,000 users per day.

#### New use case: Booking reminder email system

Learn how you can use Braze features to [build a booking reminder email messaging service]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case). The service will allow users to book appointments and will message users with reminders of their upcoming appointments. Though this use case uses email messages, you can send messages in any, or multiple, channels based on a single update to a user profile.

#### Click tracking for specific links

You can [turn off click tracking]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) for specific links by adding HTML code to your email message in the HTML editor or to components in the drag-and-drop editor.

#### Dynamic Apple Push Notification Service gateway management

[Dynamic APNs gateway management]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management) enhances the reliability and efficiency of iOS push notifications by automatically detecting the correct APNs environment. Previously, you would manually select APNs environments (development or production) for your push notifications, which sometimes led to incorrect gateway configurations, delivery failures, and BadDeviceToken errors.

#### Flutter support for Banners

{% multi_lang_include release_type.md release="Early access" %}

Banners now support Flutter. Additionally, all Banner documentation has been overhauled for easier usability. Check out the following articles to get started:

- [About Banners]({{site.baseurl}}/developer_guide/banners/)
- [Creating Banner campaigns]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
- [Embedding Banners into your app]({{site.baseurl}}/developer_guide/banners/placements/)

#### WhatsApp click tracking

{% multi_lang_include release_type.md release="Early access" %}

[Click tracking]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/) lets you measure when someone taps a link in your WhatsApp message—giving you a clear view into what content is driving engagement. Braze shortens your URLs, adds tracking behind the scenes, and logs click events as they happen.

#### Frequently asked questions for push

Check out our new [Push FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq) article that addresses some of the most frequently asked questions that arise when setting up push campaigns.

#### Push troubleshooting

[Push troubleshooting]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting) provides a number of steps to help you navigate delivery challenges with push notifications. For example, if you're experiencing delivery challenges with push notifications, we've compiled steps you can take to troubleshoot the issue.

### New Braze partnerships

#### Movable Ink Da Vinci - Dynamic Content

The Braze and Movable Ink [Da Vinci]({{site.baseurl}}/partners/movable_ink_da_vinci) integration empowers brands to deliver highly personalized messaging by leveraging Da Vinci’s AI-driven content decisioning engine. Da Vinci curates the most relevant content for each user and seamlessly deploys messages through Braze.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Updates the native Android bridge from [Braze Android SDK 33.0.0 to 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The minimum required Android SDK version is 25. See more details [here](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

