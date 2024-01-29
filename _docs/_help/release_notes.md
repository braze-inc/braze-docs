---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: dev_guide
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the following <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>. You can also check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK changelogs</a>."
page_type: landing
search_rank: 1
description: "This landing page is home to Braze release notes. This is where you can find all updates to the Braze platform and SDKs, as well as a list of deprecated features."

guide_featured_title: "Release notes"
guide_featured_list:
  - name: 2024
    link: /docs/help/release_notes/2024/
    fa_icon: fas fa-calendar-alt
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
> For more information on any of the updates listed in this section, reach out to your account manager or [open a support ticket]({{site.baseurl}}/help/support/). You can also check out [our SDK Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly SDK releases, updates, and improvements.

## January 9, 2024 release

### Updated Shopify integration documentation

We've updated sections of our Braze and Shopify integration documentation, including:

- [Getting started with Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)
- [Setting up Shopify in Braze]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)
- [Shopify user identity management]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/Shopify_Features/shopify_user_identity/)

### Data flexibility

#### Back-in-stock notifications for catalogs

{% multi_lang_include release_type.md release="Early access" %}

Using a combination of [back-in-stock notifications]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/) through catalogs and a Canvas, you can notify customers when an item is back-in-stock. Any time a customer performs a selected custom event, they can be automatically subscribed to be notified when the item is replenished.

#### Catalog segments

{% multi_lang_include release_type.md release="Early access" %}

[Catalog segments]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/catalog_segments/) are an audience of users based on catalog data in SQL Segment Extensions. These SQL Segment Extensions can be referenced in a segment and then targeted by campaigns and Canvases. Catalog segments use SQL to join data from catalogs and data from custom events or purchases. To do so, you must have a common identifier field across your catalogs and your custom events or purchases.

#### Migrating to the Firebase Cloud Messaging API

{% multi_lang_include release_type.md release="Early access" %}

Learn [how to migrate]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/) from Google’s deprecated Cloud Messaging API to their fully-supported Firebase Cloud Messaging (FCM) API.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Swift SDK 7.5.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Adds privacy manifests for `BrazeKit` and `BrazeLocation` to describe Braze's data collection policies. For more details, refer to Apple's [documentation](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests) on privacy manifests. More configurations to manage your data collection practices will be made available in a future release.
    - Fixes an issue with the code signatures of XCFrameworks introduced in 7.1.0.
- [Web SDK v5.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Unity SDK 5.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Updated the native iOS bridge from Braze Swift SDK 6.1.0 to 7.4.0.
        - The iOS repository link now points to the prebuilt dynamic XCFrameworks from this [repository](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic).
    - Updated the native Android bridge from Braze Android SDK 27.0.1 to 29.0.1.
    - `AppboyBinding.GetFeatureFlag(string id)` will now return `null` if the feature flag does not exist.
    - `FEATURE_FLAGS_UPDATED` will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.


## December 12, 2023 release

### Updates to Android push integration

On June 20, 2023, Google deprecated their Cloud Messaging API for sending push notifications to Android apps. The [Standard Android push integration](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) now shows you how to set up Google's Firebase Cloud Messaging API instead.

For more information about Google's Cloud Messaging API depreciation, see [Firebase FAQ](https://firebase.google.com/support/faq#fcm-23-deprecation).

### Robust channels

#### WhatsApp response messaging

{% multi_lang_include release_type.md release="General availability" %}

When [creating a WhatsApp message]({{site.baseurl}}/whatsapp_response_messaging/) in a campaign or Canvas, you can create response messages to reply to user's WhatsApp messages within a 24-hour window. Response messaging can be particularly helpful in Canvases that encourage interactions between your brand and its users, such as opt-in campaigns.

#### WhatsApp frequency capping

{% multi_lang_include release_type.md release="General availability" %}

You can now set up [frequency capping rules]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) for WhatsApp. Frequency capping is applied at the campaign or Canvas component send level, and can be set up for each workspace from **Settings** > **Frequency Capping Rules**.  

### Data flexibility

#### Conversions dashboard

{% multi_lang_include release_type.md release="General availability" %}

The [conversions dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard/) allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods. When measuring your conversions, you can specify the time frame, conversion event, and conversion window.

#### Email Insights reports

{% multi_lang_include release_type.md release="General availability" %}

There's a new tab, Email Insights, located within the [Email Performance dashboard]({{site.baseurl}}/email_engagement_dashboard/) that contains two new reports:

- **Engagement by Mailbox Providers:** Shows the number of clicks and opens by mailbox provider. You can select a mailbox provider and drilldown into specific receiving domains.
- **Engagement by Day of Week:** Shows when users are engaging with their emails.

#### Update to subscription group timeseries graph

{% multi_lang_include release_type.md release="General availability" %}

The **Subscription Group Timeseries** graph that appears on the **Subscription Groups** page now shows the subscription count per user rather than per email or phone number. This better aligns with how Braze calculates statistics in other areas of the dashboard.

### AI & ML automation

#### AI item recommendations

{% multi_lang_include release_type.md release="General availability" %}

[AI item recommendations]({{site.baseurl}}/user_guide/sage_ai/recommendations/) is a deep learning-based product recommendation engine that uses collective user purchasing behavior to recommend items. You can use AI item recommendations to calculate the most popular products or create personalized AI recommendations for a specific catalog. After you create your recommendation, you can use personalization to insert those products into your messages.

### New Braze partnerships

#### Facebook Lead Ads via Zapier – Leads Capture

With the [Facebook Lead Ads integration via Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/leads_capture/facebook_via_zapier/), you can import your leads from Facebook into Braze and track a custom event when leads are captured.

#### SmarterSends – Message Templates

The Braze and [SmarterSends]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/smartersends/) partnership allows you to combine the power of Braze with the hyper-localized content owned by your distributed users to elevate your marketing campaigns.

#### Recurly – Payments

The [Recurly]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/recurly/) and Braze integration simplifies the process of sharing subscription data with Braze, enabling targeted communication with customers.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Flutter SDK 8.0.0-8.1.0](https://pub.dev/packages/braze_plugin/changelog)
  - Updates the native Android bridge from Braze Android SDK 27.0.1 to 29.0.1.
  - Updates the native iOS bridge from Braze Swift SDK 6.6.1 to 7.2.0.
  - Modifies the behavior for Feature Flags methods.
    - `BrazePlugin.getFeatureFlagByID(String id)` will now return `null` if the feature flag does not exist.
    - `BrazePlugin.subscribeToFeatureFlags(void Function(List<BrazeFeatureFlag>) onEvent))` will only trigger in the following situations:
      - When a refresh request completes with success or failure.
      - Upon initial subscription if there was previously cached data from the current session.
  - The minimum supported Android SDK version is 21.
- [React Native SDK 8.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.2.0/CHANGELOG.md)
- [Swift SDK 7.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Braze Segment Swift Plugin 2.2.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
- [Braze Expo Plugin 1.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.2.0/CHANGELOG.md)

## November 14, 2023 release

### Getting started with Braze

Exciting news! We're introducing two Getting Started sections tailored specifically for our Braze [marketers]({{site.baseurl}}/user_guide/getting_started) and [developers]({{site.baseurl}}/developer_guide/platform_wide/getting_started). These sections are designed to help you hit the ground running with Braze, providing you with all the necessary tools and guidance. Dive in and start exploring.

### New Braze dashboard instance

Braze manages a number of different instances for our dashboard and REST endpoints. We have added a new dashboard instance `US-07`. For more information, refer to [API overview]({{site.baseurl}}/api/basics/).

### Robust channels

#### Custom drag-and-drop templates for in-app messages

{% multi_lang_include release_type.md release="General availability" %}

You can now use [custom drag-and-drop templates for in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) to begin designing your in-app message in the drag-and-drop editor.

#### SMS double opt-in

{% multi_lang_include release_type.md release="General availability" %}

[SMS double opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/sms_double_opt_in/) allows you to require users to explicitly confirm their opt-in intent before they can receive SMS messages. This helps you tailor your focus to users who are likely to be engaged or are engaged with SMS.

#### Estimated real open rate for email reporting

{% multi_lang_include release_type.md release="General availability" %}

[Estimated real open rate]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#estimated-real-open-rate) uses a proprietary analytical model created by Braze to reconstruct an estimate of the campaign's unique open rate as if machine opens did not exist. Braze uses click data from each campaign to infer the rate at which actual humans opened the message. This compensates for various machine opening mechanisms, including Apple’s MPP. 

#### Personalized Paths for Canvas

{% multi_lang_include release_type.md release="Beta" %}

With [Personalized Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/), you can personalize entire Canvas journeys for individual users based on conversion likelihood, similar to Personalized Variants in campaigns. Use Personalized Paths with an Experiment Path step to hold a portion of users in a delay group while Braze tests the remaining paths against each other.

### Data flexibility

#### Searching your Braze dashboard

{% multi_lang_include release_type.md release="General availability" %}

You can use the [search bar]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/) to find your work and other information within your Braze dashboard. The search bar is at the top of your Braze dashboard. 

#### Blocklisting custom attributes and events

{% multi_lang_include release_type.md release="General availability" %}

You can now blocklist up to 10 custom attributes or events at a time. For more information, refer to [Custom event and attribute management]({{site.baseurl}}/user_guide/administrative/app_settings/custom_event_and_attribute_management/).

#### New help article: Universal links and App links

Apple universal links and Android App Links are mechanisms devised to provide a seamless transition between web content and mobile apps. While universal links are specific to iOS, Android App Links serve the same purpose for Android applications. 

Learn more about this topic in our dedicated [Universal links and App Links]({{site.baseurl}}/help/help_articles/email/universal_links/) article.

### New Braze partnerships

#### Olo – Channel Extensions

The Braze and [Olo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/olo/) integration allows you to update user profiles in Braze to keep them consistent with Olo user profiles. You can also send the right messaging from Braze based on Olo events.

#### Typeform – Customer Data Platform

The Braze and [Typeform]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/typeform/) integration allows you to update user profiles in Braze with data collected from their Typeform response, trigger messaging in Braze based on a user’s engagement with a typeform, and personalize Braze messaging based on a user’s Typeform responses.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Web SDK v4.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Web SDK v5.0.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 29.0.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.1.0-7.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `Braze.Configuration.DeviceProperty.pushDisplayOptions` has been deprecated. Providing this value no longer has an effect.
- [React Native SDK 8.0.0-8.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Updates the native Android bridge from Braze Android SDK 27.0.1 to 29.0.0.
    - Updates the native iOS bridge from Braze Swift SDK 6.6.0 to 7.0.0.
    - Renames the `Banner` Content Card type to ImageOnly:
        - `BannerContentCard` to `ImageOnlyContentCard`
        - `ContentCardTypes.BANNER` to `ContentCardTypes.IMAGE_ONLY`
    - On Android, if the XML files in your project contain the word `banner` for Content Cards, it should be replaced with `image_only`.
    - `Braze.getFeatureFlag(id)` will now return `null` if the feature flag does not exist.
    - `Braze.Events.FEATURE_FLAGS_UPDATED` will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.

## October 17, 2023 release

### Copying to workspaces

[Copying campaigns across a workspace]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/) allows you to get a jumpstart on your message composition by starting with a copy of a campaign in a different workspace. This copy will remain as a draft until you edit and launch, helping you keep and build off your successful messaging strategies.

### Test Currents connectors

[Test Currents connectors]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/#test-currents-connectors) are free versions of our existing connectors that can be used for testing and trying out different destinations. Test Currents have:

- No limit to the number of Test Currents connectors you may build.
- An aggregate maximum of 10,000 events per 30-day rolling period. This event total is updated hourly on the dashboard.

### Feature flags

[Feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/) allow you to remotely enable or disable functionality for a specific or random selection of users. Importantly, they let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence.

### Feature flag experiments

[Feature flag experiments]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/) let you A/B test changes to your applications to optimize conversion rates. Marketers can use feature flags to determine whether a new feature positively or negatively impacts conversion rates, or which set of feature flag properties is most optimal.

### Merging user profiles

If your search on the **Search Users** page returns multiple user profiles, you can [merge user profiles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#merge-profiles) by clicking the **Merge duplicates** button. You can select which user profile to keep, meaning this profile will be kept and will gain attributes from the merged profile.

### Performance data by segment

You can now use Query Builder report templates to [break down performance data]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment) by segments for campaigns, Canvas, variants, and steps.

### Updating user profiles

You can now use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to update a user profile by phone number or email.

## SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Braze Segment Swift Plugin v2.1.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
- [Web SDK v4.10.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Web SDK v5.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - The [`subscribeToFeatureFlagsUpdates()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetofeatureflagsupdates) callback will now always be called, regardless of refresh success/failure. If there is a failure in receiving updates, the callback will be called with currently cached feature flags.
    - The [`getFeatureFlag()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getfeatureflag) method now returns a null if the feature flag does not exist, or if feature flags are disabled.
    - Removed `logContentCardsDisplayed()` method that was previously deprecated in 4.0.4.
    - Removed the deprecated initialization option `enableHtmlInAppMessages`. This should be replaced with the `allowUserSuppliedJavascript` option instead.
    - Removed Banner class that was previously deprecated in 4.9.0 in favor of [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html).
    - Removed `ab-banner` CSS classname as part of `Banner` class removal. CSS customizations should instead target the `ab-image-only` class.
    - The SDK no longer throws runtime errors anywhere. If Braze methods are called prior to initialization, a warning will be logged to the console instead.
    - The SDK no longer adds default Braze in-app message styles to custom HTML in-app messages. These styles were previously used by legacy in-app message types.
- [Android SDK 29.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - Renamed `BannerImageCard`, `BannerImageCardView`, and `BannerImageContentCardView` to `ImageOnlyCard`, `ImageOnlyCardView`, and `ImageOnlyContentCardView`.
    - All styles used for Banner Cards have been updated to Image Only Cards. All keys with the word `banner` should be replaced with `image_only`.
    - Device brand information is now sent. If you want to block this, see Blocking data collection.
- [Flutter SDK 7.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Updates the native Android bridge [from Braze Android SDK 26.1.1 to 27.0.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701).
    - Adds support for Gradle 8.
- [Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - The `useUUIDAsDeviceId` configuration is now enabled by default.
        - For more details on the impacts, refer to this [Collecting IDFV - Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/swift_idfv/).
    - The Banner Content Card type and corresponding UI elements have been renamed to `ImageOnly`. All member methods and properties remain the same.
        - `Braze.ContentCard.Banner` → `Braze.ContentCard.ImageOnly`
        - `BrazeContentCardUI.BannerCell` → `BrazeContentCardUI.ImageOnlyCell`
    - Refactors some text layout logic in BrazeUI into a new Braze.ModalTextView class.
    - Updates the behavior for Feature Flags methods.
        - `FeatureFlags.featureFlag(id:)` now returns nil for an ID that does not exist.
        - `FeatureFlags.subscribeToUpdates(:)` will trigger the callback when any refresh request completes with a success or failure.
            - The callback will also trigger immediately upon initial subscription if previously cached data exists.
- [AppboyKit iOS SDK 4.6.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.6.0)
    - This release requires Xcode `14.x`.
    - Drops support for iOS 9 and iOS 10.
    - Removes support for the outdated `.framework` assets when importing via Carthage in favor of the modern `.xcframework` assets.
        - Use the command `carthage update --use-xcframeworks` to import the appropriate Braze asset.
        - Removes support for `appboy_ios_sdk_full.json` in favor of using `appboy_ios_sdk.json`

## September 19, 2023 release

### BigQuery for Cloud Data Ingestion

You can now create Cloud Data Ingestion integrations with [BigQuery](https://cloud.google.com/bigquery), a serverless enterprise data warehouse. For more information, refer to [Cloud Data Integestion integrations]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=bigquery).

### Braze Data Transformation

[Braze Data Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/) allows you to build and manage webhook integrations to automate data flow from external platforms into Braze user profiles. This newly integrated user data can then power even more sophisticated marketing use cases.

### Commenting in Canvas

[Comments in Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_comments/) can be a great collaborative space for your marketing team to identify, discuss, and review the finer details of your Canvases. As you build out a Canvas, you can make and manage comments to identify these areas that may require additional feedback from your colleagues.

### Deliverability Center

The [Deliverability Center]({{site.baseurl}}/user_guide/data_and_analytics/analytics/deliverability_center) provides more insight into your email performance by supporting the use of Gmail Postmaster Tools to track data on emails sent and gather data about your sending domain. 

Email deliverability is the core of campaign success. Using the Deliverability Center in the Braze dashboard, you can view your domains by IP reputation or delivery errors to discover and troubleshoot any potential issues with email deliverability.

### Drag-and-drop editor for in-app messages

These additional features have been added to the [drag-and-drop editor for in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/):

- Text links that do not dismiss the message
- Button action to request push primer
- Custom code editor block

To take advantage of all features available in the drag-and-drop editor, update your SDKs to the recommended SDK versions.

#### Save custom templates (early access)

In the drag-and-drop editor for in-app messages, early access participants can create and save custom in-app message templates using the **Save as template** button, available after you exit the editor. Before you can save it as a template, you must first launch the campaign OR save it as a draft. 

You can also create and save in-app message templates by navigating to **Templates** > **In-App Message Templates**.

{% alert important %}
The ability to save custom templates is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

### Disabling dark mode for in-app messages

Developers can prevent in-app messages from adopting dark mode styling when the user device has dark mode turned on. For steps on how to implement this, refer to the following documentation by platform:

- [Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/#disabling-dark-mode)
- [Objective-C]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handling_in_app_display/#disabling-dark-mode)

### New fields for message archiving

[Message archiving]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/) lets you save a copy of messages sent to users for archival or compliance purposes to your S3 bucket. The following fields have been added to the JSON payload delivered to your S3 bucket each time a message is sent:

- `user_id`
- `campaign_name`
- `canvas_name`
- `canvas_step_name`

### New Liquid personalization tags

For in-app messages, you can use the following app attributes within Liquid. The values are based on which SDK API key your apps use to request messaging:

- {% raw %}`{{app.${api_id}}}`{% endraw %}
- {% raw %}`{{app.${name}}}`{% endraw %}

For more, refer to [Supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags#targeted-app-information).

### New Braze partnerships

#### Antavo Loyalty Cloud – Channel Extensions

The [Antavo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/antavo/) and Braze integration allows you to use loyalty program-related data to build personalized campaigns to enhance the customer experience. Antavo supports loyalty data synchronization between the two platforms—this is a one-way data synchronization only from Antavo to Braze.

#### Ketch – Customer Data Platform

The Braze and [Ketch]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/ketch/) integration allows you to control customer communication preferences within the Ketch preference center and automatically propagate these changes to Braze.

#### Redpoint – Customer Data Platform

Redpoint is a technology platform that provides marketers with a fully integrated campaign orchestration platform. The Braze and [Redpoint]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/redpoint/) integration allows you to create Braze segments based on your Redpoint CDP data. 

#### Simon Data – Customer Data Platform
 
Use the Braze and [Simon Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/simondata/) integration to create and sync sophisticated audiences to Braze for orchestration in real-time and without code. With this integration, you can leverage the best of Simon’s campaign prioritization and identity-matching capabilities, complex aggregate support, and more to elevate your Braze campaigns downstream.

#### OfferFit – Dynamic Content

The [OfferFit]({{site.baseurl}}/partners/message_personalization/dynamic_content/offerfit/) and Braze integration allows you to automatically discover the right message, channel, and timing for every customer based on your customer data. You can optimize your campaigns to existing identified customers with business goals such as cross-sell, upsell, repurchase, retention, renewal, referral, and winback.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Swift SDK 6.6.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#661)
- [Web SDK 4.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#490)
- [Android SDK 28.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2800)
    - Updated minimum SDK version to 21 (Lollipop).
    - Feature Flags functions have been modified.
    - `Braze.getFeatureFlag(id)` will now return null if the feature flag doesn't exist.
    - `Braze.subscribeToFeatureFlagsUpdates()` will only callback when a refresh request completes, and initially if previously cached data exists. It will also be called with cached feature flags for any refresh failures.
        - If you want the cached value immediately at app startup, use `Braze.getFeatureFlag(id)`.
    - Refactored `DefaultInAppMessageViewWrapper.createButtonClickListener()` into `DefaultInAppMessageViewWrapper.createButtonClickListeners()`.
- [React Native SDK 7.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#700)
    - Updates the native Android bridge from [Braze Android SDK 26.3.2 to 27.0.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701).
- [Cordova SDK 7.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2800)
    - Updates the native Android bridge from [Braze Android SDK 26.3.2 to 27.0.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701).
- [Roku SDK 2.0.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md#200)
    - `getFeatureFlag` will return invalid when the flag does not exist.
    - `BrazeTask` now observes `BrazeFeatureFlagsUpdated` to know when feature flags refreshes succeed or fail. Data values may not always be different.

## August 22, 2023 release

## Shopify catalogs 

Shopify catalogs allow you to import your products from your Shopify store into a Braze catalog, automating the process to bring in product data for deeper personalization of your messages. You can enrich your abandoned cart, order confirmation, and more with the most up-to-date product details and information.

### Merging users by email

You can now [merge users by email]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merging-users-by-email) using the `/users/merge` endpoint. 

{% alert important %}
Merging users by email and using `/users/merge` with mismatched identifiers are currently in early access. Contact your Braze account manager if you’re interested in participating in the early access.
{% endalert %}

## Best practices for WhatsApp

Before sending your WhatsApp messages, you can reference suggested [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/) to maintain a high phone quality rating, avoid blocks and reports, and opt-in and out-out users.

### Domain reputation

In the Deliverability Center, you can now view and monitor your [domain reputation]({{site.baseurl}}/user_guide/data_and_analytics/analytics/deliverability_center#domain-reputation) to help avoid being filtered into a spam folder.

### Customization guides 

We're excited to introduce a reorganization of the Developer Portal. Now, customization options for our SDKs, starting with [Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards), are consolidated into dedicated customization guides. This change streamlines your access to detailed instructions, making it easier to tailor experiences to your specific needs.

### Card creation in Canvas

You can choose when Braze evaluates audience eligibility and personalization for new Content Card campaigns and Canvas steps by specifying when the card is created.

{% alert important %}
Control over card creation in Canvas steps is in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

### Copying to workspaces

[Copying campaigns across a workspace]({{site.baseurl}}/copying_to_workspaces/) allows you to get a jumpstart on your message composition by starting with a copy of a campaign in a different workspace. This copy will remain as a draft until you edit and launch, helping you keep and build off your successful messaging strategies.

{% alert important %}
Copying campaigns across workspaces is currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

### Push Max

[Push Max]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/push_max/) amplifies Android push notifications by tracking failed push notifications and resending the push when the user is more likely to receive it. Learn about Push Max and how you can use this feature to potentially improve the deliverability of Android push notifications to [Chinese OEM devices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/).

{% alert important %}
Push Max is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Xamarin SDK 2.0.0–2.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Updated the Android binding to use Braze Android SDK 26.3.2
- [Flutter SDK 6.0.1](https://pub.dev/packages/braze_plugin/changelog)
    - Updated the native Android bridge from Braze Android SDK 26.1.0 to 26.1.1.
- [Android SDK 27.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 6.5.0–6.6.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Fixed an issue in HTML in-app messages where custom event and purchase properties would always convert values for `1` and `0` to become `true` and `false`, respectively. These property values will now respect their original form in the HTML.
- [React Native SDK 6.0.0–6.0.2](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Updated the native Android bridge from Braze Android SDK 26.3.1 to 26.3.2.
- [Cordova SDK 6.0.0-6.0.1](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Updated the native Android version from Braze Android SDK 26.3.1 to 26.3.2
- [Expo Plugin 1.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/1.1.2/CHANGELOG.md)
- [Unity 4.3.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Segment Kotlin 1.4.1](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
- [Segment-Android 15.0.1](https://github.com/Appboy/appboy-segment-android/blob/master/CHANGELOG.md)

## July 25, 2023 release

### Canvas approval 
The new Canvas approval workflow setting adds a review process prior to launching a new Canvas. Note that this feature is turned off by default, giving you control over its implementation. Explore more details about activating this workflow in [Canvas approvals and permissions]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_approval/).
 
### Feature flags in Canvas
Feature flags allow you to experiment and confirm your hypotheses around new features by turning them off and on for different sections of your user base. The new feature flag component in Canvas allows you to segment your audience in a Canvas based on whether a feature flag is on or off for a user. Moreover, Experiment Paths allow you optimize these conversions by testing different messages or paths against each other and determining which is most effective. See the [feature flag overview]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/) for information about feature flags generally, or learn more about [using feature flags in Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/).

### Managing Segments article
The new [Managing Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/) article covers the actions you can take to configure your segments, such as filtering a list of segments, creating segments, and editing segments.
 
### Row component Content Block
You can now save a row component as a Content Block that can then be used in all email campaigns and email messages in a Canvas. For more information on drag-and-drop Content Blocks, refer to [Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).

### Sage AI
Sage AI by Braze powers a collection of accessible, easy-to-use tools that lower the barriers to entry for creativity, personalization and optimization for your engagement strategy. Learn more about our Sage AI features and capabilities in our [documentation]({{site.baseurl}}/user_guide/sage_ai).

### Updating a user profile by phone number
Using the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) endpoint, you can update a user profile using their phone number. 

{% alert important %}
This feature is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

### Whitespace after email preheader 
The new **Add whitespace after preheader** checkbox hides the text or HTML of the email body in the email preheader. Learn more about adding email headers in [Creating an email]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email).

### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 26.2.0-26.3.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2620) 
- [Swift SDK 6.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#631)
- [Web SDK 4.8.1–4.8.3](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#481)
- [Flutter SDK 6.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/master/CHANGELOG.md#600)
    - Updates the native Android bridge from Braze Android SDK 25.0.0 to 26.1.0.
- [React Native SDK 5.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#520)
- [Roku SDK 1.0.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md#100)
- [Unity 4.2.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#420)
    - Updated the Android plugin to use Braze Android SDK 26.2.0.

## June 27, 2023 release

### Drag & Drop Email Preference Center

Setting up a preference center provides a one-stop shop for your users to edit and manage their notification preferences for your email messaging. With the drag-and-drop editor, you can now create and customize a preference center to help manage which users receive certain types of communication. See [Create an email preference center with drag-and-drop]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/) to learn more.

### Saving drafts for Canvas

As you create and launch Canvases, you can also make edits to an active Canvas and save it as a draft, allowing you to pilot your changes prior to another launch. If you have an active Canvas that requires large scale changes, you can use this feature to create separate drafts for these edits. See [Saving drafts for Canvas]({{site.baseurl}}/save_as_draft) to learn more.

### Winning Path with one-time entry

When using [Winning Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#one-time-entry) in a Canvas where users are allowed to enter only once, a Delay Group is now automatically included. This means you no longer need to perform a workaround for one-time entry Canvases to use Winning Paths in your Experiment Paths.

### Refreshing Content Card rate limits

For customers onboarded after June 14, 2023, the default rate limit for manually calling `requestContentCardsRefresh()` is 3 calls per 10 minutes per device to prevent performance degradation and errors. For more information on refreshing Content Cards, see the respective documentation for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration#refreshing-content-cards), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/refreshing_the_feed), and [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/refreshing_the_feed).

### Audience sync to Facebook

If you use [Audience Sync to Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/), please be aware that starting in July 2023, Meta is rolling out Meta work accounts to a small set of businesses who are interested in adopting this new account type. If you have a Business Account integrated with Braze, ensure you disconnect and reconnect to the [Facebook partner page]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook) with your Business Account in order to preserve this implementation and not disrupt any active Canvases.

### Cloud Data Ingestion for Databricks

Braze Cloud Data Ingestion for Databricks allows customers to directly sync user data (attributes, events, purchases) as well as user deletes from Databricks to Braze. After this data is synced to Braze, it can be used just like any other data in the Braze platform. This feature is an extension of our [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/) product and is currently in early access.

### Privacy Portal

The new [Braze Privacy Portal]({{site.baseurl}}/user_guide/privacy_portal) provides useful information about how Braze can help you be good custodians of your customers’ data and, importantly, enable you to take measures to comply with data protection rules relevant to your business. We have brought together information and links to documentation that may assist you in your use of the Braze Services in compliance with applicable data protection laws and regulations.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 26.0.0–26.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2610)
	- {% raw %}Added the ability to configure link target behavior for HTML In-App Messages through `BrazeConfig.setIsHtmlInAppMessageHtmlLinkTargetEnabled()` or via adding `<bool name="com_braze_html_in_app_message_enable_html_link_target">true</bool>` to your `braze.xml`. Defaults to enabled.{% endraw %}
		- {% raw %}When enabled, a link in an in-app message that has the link target set (for example, `<a HREF="https://www.braze.com" target="_blank">Please Read</a>`) will open the link in a browser, but will not close the in-app message.{% endraw %}
- [Web SDK 4.7.2–4.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#480)
- [Swift SDK 6.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#630)
- [Unity SDK 4.1.1](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#411)
- [React Native SDK 5.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#510)

<br><br>
