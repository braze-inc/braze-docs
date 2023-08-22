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

We're excited to introduce a reorganization of the Developer Portal. Now, customization options for our SDKs, starting with [Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards), are consolidated into dedicated customization guides. This change streamlines your access to detailed instructions, making it easier tailor experience to your specific needs.

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

If you use [Audience Sync to Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/), please be aware that starting in July 2023, Meta is rolling out Meta work accounts to a small set of businesses who are interested in adopting this new account type. If you have a Business Account integrated with Braze, ensure you disconnect and reconnect to the [Facebook partner page]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook) with your Business Account in order to perserve this implementation and not disrupt any active Canvases.

### Cloud Data Ingestion for Databricks

Braze Cloud Data Ingestion for Databricks allows customers to directly sync user data (attributes, events, purchases) as well as user deletes from Databricks to Braze. After this data is synced to Braze, it can be used just like any other data in the Braze platform. This feature is an extension of our [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/) product and is currently in early access.

### Privacy Portal

The new [Braze Privacy Portal]({{site.baseurl}}/user_guide/privacy_portal) provides useful information about how Braze can help you be good custodians of your customers’ data and, importantly, enable you to take measures to comply with data protection rules relevant to your business. We have brought together information and links to documentation that may assist you in your use of the Braze Services in compliance with applicable data protection laws and regulations.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 26.0.0–26.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2610)
	- {% raw %}Added the ability to configure link target behavior for HTML In-App Messages through `BrazeConfig.setIsHtmlInAppMessageHtmlLinkTargetEnabled()` or via adding `<bool name="com_braze_html_in_app_message_enable_html_link_target">true</bool>` to your `braze.xml`. Defaults to enabled.{% endraw %}
		- {% raw %}When enabled, a link in an in-app message that has the link target set (e.g., `<a HREF="https://www.braze.com" target="_blank">Please Read</a>`) will open the link in a browser, but will not close the in-app message.{% endraw %}
- [Web SDK 4.7.2–4.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#480)
- [Swift SDK 6.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#630)
- [Unity SDK 4.1.1](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#411)
- [React Native SDK 5.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#510)

## May 30, 2023 release

### Redesigned Braze navigation

We’ve updated the Braze navigation to help you create and access your content more quickly and efficiently. Features are now organized into intuitive categories familiar and relevant to a marketer’s workflow in Braze. For the next few months, you can switch back and forth between the old and new navigation experiences. For more information on what’s changed, refer to [Braze navigation]({{site.baseurl}}/navigation).

### New Currents events

The following WhatsApp Currents events have recently been released and added to the [message engagement event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) glossaries:

Message abort events:
- `users.messages.whatsapp.Send`
- `users.messages.whatsapp.Abort`
- `users.messages.whatsapp.Delivery`
- `users.messages.whatsapp.Failure`
- `users.messages.whatsapp.Read`
- `users.messages.whatsapp.InboundReceive`

### In-browser catalog editing and catalog selections 

Catalogs now support in-browser editing and [selections](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/selections). Selections are groups of data that can be used to personalize a message for each user in your campaign. After creating a [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalog/), you can further reference this data by incorporating selections in your Braze campaigns.

### Currents and Snowflake Data Sharing message_extras Liquid tag

Using the [`message_extras` Liquid tag](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/), you can annotate your send events with dynamic data from Connected Content, Catalogs, custom attributes (such as language, country), Canvas entry properties, or other data sources, and send the extra data back to Currents or Snowflake Data Sharing.

### New Braze partnerships

#### Tangerine - Localization
The Braze and [Tangerine](https://www.braze.com/docs/partners/message_personalization/location/tangerine/) integration allows you to integrate raw campaign and impression data from Braze into Store360 through Snowflake Secure Data Sharing. Brands can now measure the impact of these campaigns on physical store visits and in-store engagement.

#### Personalize.AI - Dynamic Content
The Braze and [Personalize.AI](https://www.braze.com/docs/partners/message_personalization/dynamic_content/personalize/) integration allows you to export data from Personalize.AI into the Braze platform for message personalization and targeting.

#### Regal - Messaging
By integrating [Regal](https://www.braze.com/docs/partners/message_orchestration/additional_channels/messaging/regal/) and Braze, you can create a more consistent and personalized experience across all your customer touchpoints.
- Send the right next best email or push notification from Braze based on what’s said in a phone conversation on Regal.
- Trigger a call in Regal when a high-value customer clicks through a marketing email from Braze but doesn’t convert.

#### Sendbird - Messaging
The Braze and [Sendbird](https://www.braze.com/docs/partners/message_orchestration/additional_channels/messaging/sendbird) integration allows Braze users to:
- Utilize Braze’s segmentation and triggering capabilities to initiate personalized in-app notifications.
- Create tailored in-app notifications on the Sendbird Notifications platform, which are then delivered within the app environment, enhancing user engagement.

#### Fresh Relevance - Dynamic Content
The Braze and [Fresh Relevance](https://www.braze.com/docs/partners/message_personalization/dynamic_content/fresh_relevance/) integration allows you to include personalized content in triggered emails, such as product recommendations based on the customer’s browsed product or items within the same category, Send advanced triggered email campaigns such as price drop, back in stock, multi-stage browse, or cart abandoned messages, and more!

#### Smartling - Localization
The Braze and [Smartling](https://www.braze.com/docs/partners/message_personalization/localization/smartling/) integration allows you to translate email templates and Content Blocks. Smartling provides linguists with the benefit of visual context during translation, which reduces errors and maintains quality.

#### SalesWings - Analytics
The Braze and [SalesWings](https://www.braze.com/docs/partners/data_and_infrastructure_agility/analytics/saleswings#saleswings) integration allows you to sync data across the two platforms in a flexible way to qualify leads with lead scoring and lead grading capabilities.

#### Kognitiv Inspire - Loyalty
The Braze and [Kognitiv](https://www.braze.com/docs/partners/message_orchestration/channel_extensions/loyalty/kognitiv/) integration allows you to implement and evaluate your loyalty strategy, offering innovative capabilities and tailored member communications for enhanced program efficacy.

#### OneTrust - Data Privacy
The Braze and [OneTrust](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_privacy/onetrust/) integration allows you to use the OneTrust workflow builder to create security workflows for your product.

#### Stylitics - Dynamic Content
Your Braze and [Stylitics](https://www.braze.com/docs/partners/message_personalization/dynamic_content/stylitics/) integration allows you to enhance your existing email campaigns with engaging and relevant bundled content, creating a personalized customer experience.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Swift SDK 6.1.0-6.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#620)
- [Web SDK 4.7.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#471)
- [React Native SDK 5.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#500)
  - Updates the native iOS bridge from Braze Swift SDK 5.13.0 to 6.2.0.
  - Removes `setSDKFlavor` and `setMetadata`, which were no-ops starting from version 2.0.0.
  - On iOS, these fields must be set using the `Braze.Configuration` object at SDK initialization.
  - On Android, these fields must be set via the braze.xml file.
- [Cordova SDK 4.0.0-5.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#500)
  - **Cordova SDK 4.0.0**
    - Renamed instances of Appboy to Braze.
      - To ensure that your project is properly migrated to the new naming conventions, note and replace the following instances in your project:
        - The plugin has been renamed from `cordova-plonugin-appboy` to `cordova-plugin-braze`.
          - Ensure that you run the Cordova plugin, remove `cordova-plugin-appboy` and then re-add the plugin using the instructions in the [README](https://github.com/braze-inc/braze-cordova-sdk/blob/master/README.md).
        - This GitHub repository has been moved to the URL https://github.com/braze-inc/braze-cordova-sdk.
        - In your project's config.xml file, rename instances of com.appboy to com.braze for each of your configuration property keys.
        - The JavaScript class interface `AppboyPlugin` has been renamed `BrazePlugin`.
    - Updated to Braze Android SDK 25.0.0.
    - Updated to Braze Swift SDK 5.13.0.
      - This update fixes the iOS behavior introduced in version 2.33.0 when logging clicks for content cards. Calling `logContentCardClicked` now only sends a click event for metrics instead of sending a click event and redirecting to the associated URL field.
  - **Cordova SDK 5.0.0**
    - Updated these Feature Flag methods to return promises instead of using a callback parameter
      - `getAllFeatureFlags()`
      - `getFeatureFlag(id)`
      - `getFeatureFlagBooleanProperty(id, key)`
      - `getFeatureFlagStringProperty(id, key)`
      - `getFeatureFlagNumberProperty(id, key)`
- [Unreal SDK 2.5.0](https://github.com/braze-inc/braze-unreal-sdk/blob/master/CHANGELOG.md#250)
- [Unity SDK 4.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#410)

## May 2, 2023 release

### Redesigned Braze UI/UX

_Generally available on May 16, 2023_

Save time and find exactly what you need with the newly redesigned UI/UX and information architecture. Quickly navigate throughout the platform, complete tasks, and discover new features with ease. To make this transition easier for you and your team, check out our dedicated [navigation guide]({{site.baseurl}}/navigation) to learn what has changed and what you can expect next.

### Query builder

With the [query builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder), you can generate reports using Braze data in Snowflake. The query builder comes with pre-built SQL query templates to get you started, or you can write your own custom SQL queries to unlock even more insights.

### Canvas version history

[Version history]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_version_history/) allows you to view and access Canvas analytics and the user journeys for any previous version of your Canvas. Referencing your Canvas version history can be especially helpful to maintain a record of the evolution of a Canvas.

### Incremental refresh for SQL Segments

You can now create [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) that use incremental refresh, which only refreshes the last 2 days worth of data. This is more cost-efficient and uses up fewer SQL Segment credits each time the segment membership refreshes. Unlike full refresh extensions, you can set incremental refresh extensions to automatically regenerate membership daily.

### Deliverability Center for email

The [Deliverability Center]({{site.baseurl}}/user_guide/data_and_analytics/analytics/deliverability_center#deliverability-center) provides more insight into your email performance by supporting the use of Gmail Postmaster Tools to track data on emails sent and gather data about your sending domain.

{% alert important %}
The Deliverability Center is currently in early access. Contact your Braze customer success manager if you’re interested in participating in the early access.
{% endalert %}

### Update for catalog limitations

As of May 1, 2023, there have been updates for [catalogs storage limits]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits). To request an upgrade for catalogs storage, contact your Braze account manager.

### New API and SDK endpoints article

Braze manages a number of different instances for our dashboard, SDK, and REST endpoints, which we call "clusters." Check out [API and SDK endpoints]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) for a list of dashboard URLs, API endpoints, and SDK endpoints for available Braze instances.

### Liquid FAQ

We’ve answered some [frequently asked questions for Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/faq/). 

### iOS SDK deprecation - Swift

Braze's legacy iOS SDK is being deprecated in favor of the new Swift SDK. This brings improved performance, new features, and many improvements—including [new documentation](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview)!

Looking to upgrade? Check out our [migration guide](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/) for details.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [React Native SDK v4.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Android SDK 25.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 5.14.0-6.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#600)
- [Flutter SDK 5.0.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity 4.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Segment Kotlin 1.3.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)


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
[Shopify Historical Backfill](https://www.braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_backfill/) allows Braze to import all customers, orders, and purchase events from the last 90 days prior to your Shopify integration connection.

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

Link shortening also allows you to use your own domain to personalize the look and feel of your shortened URLs, helping portray a consistent brand image. After link shortening is configured, [custom domains]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#custom-domains) can be assigned to one or multiple SMS subscription groups.

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

The [Sisu Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/business_intelligence/sisu_data/) and Braze integration allows you to understand across all campaigns or at a campaign level why metrics (e.g., open rate, click-through rate, conversion rate, etc.) are changing and what drives the most optimal outcomes. After these segments are identified, Braze users can materialize the outputs in their data warehouse or send them directly from Sisu to Braze to retarget and reengage users.

#### Loplat - Contextual location

The Braze and [loplat]({{site.baseurl}}/partners/message_personalization/location/loplat/) integration allows you to use loplat’s location services (store POI and custom geofence) to trigger geo-contextual marketing campaigns and create custom events using offline segmentation. When users visit the targeted location you set in loplat X, the campaign and location information are sent immediately to Braze.

#### ActionIQ - Customer data platform

The Braze and [ActionIQ]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/actioniq/) integration allows brands to sync and map their ActionIQ data directly to Braze, empowering the delivery of extraordinary customer experiences based on the entire breadth of their customer data. The integration enables the users to:

- Map audience segments or custom attributes to Braze directly from ActionIQ
- Forward the events tracked by ActionIQ to Braze in real time to trigger personalized and targeted campaigns

#### Komo - Dynamic content

The Braze and [Komo]({{site.baseurl}}/partners/message_personalization/dynamic_content/komo/) integration allows you to gather first and zero-party data through Komo Engagement Hubs. These hubs are dynamic microsites that offer interactive content and gamification features. The user data collected from these hubs are then transmitted to the Braze API.

- Ingest first and zero-party user data gather from Komo to Braze in real-time
- Ingest market research and user preference data when they answer surveys, polls, and quiz questions
- Progressively build user profiles in Braze over time as the user continues to engage and share more data about themselves
- Standardize the look and feel of transactional emails sent through Braze

#### Phrase - Localization

The [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase/) and Braze integration allow you to translate email templates and Content Blocks without leaving the Braze interface. With the Phrase TMS integration for Braze, you can increase customer engagement and drive growth into new markets with seamless localization.

#### Nift - Loyalty

The Braze and [Nift]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/nift/) integration allows you to automatically trigger “thank-yous” containing Nift gifts at key moments in the customer lifecycle and identify which customers used their gift. Nift gift cards can be used to access products and services supplied by brands relying on Nift’s matchmaking technology to acquire new customers cost-effectively at scale.

#### Sageflo - Message templates

The Braze and [Sageflo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/sageflo/) integration empowers local teams to easily send their own emails using marketing-approved templates, images, and audience segments through API integrations with Braze.

#### Airbyte - Workflow automation

The Braze and [Airbyte]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/airbyte/) integration allows users to create a data pipeline to collect and analyze Braze data by connecting all of your applications and databases to a central warehouse. After data has been collected in the central warehouse, data teams can explore Braze data effectively using their preferred business intelligence tools.

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

Use the [Update user alias endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) to update existing user aliases.

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


[support]: {{site.baseurl}}/support_contact/
[1]: {% image_buster /assets/img/doc-breadcrumbs.png %} 

<br><br>
