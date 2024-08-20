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

## August 20, 2024 release

### New use cases

#### Catalogs

You can bring in any type of data into a catalog. Typically, the data is metadata about offerings, such as products, discounts, promotions, events, and similar. Read our [use cases]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) and learn how you can use this data to target users with highly relevant messaging.

#### Intelligence Suite

The Intelligence Suite provides powerful features to analyze user history and campaign and Canvas performance, then make automatic adjustments to increase engagement, viewership, and conversions. For a few examples of how these features can benefit different industries, check out our [use cases]({{site.baseurl}}/user_guide/sage_ai/intelligence).

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

#### ZenDesk Chat - Instant Chat

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

The Sage AI Liquid Assistant is a chat assistant powered by Sage AI that helps generate the Liquid you need to personalize message content. You can generate Liquid from templates, receive personalized Liquid suggestions, and optimize existing Liquid with the support of Sage AI. The AI Liquid Assistant also provides annotations explaining the Liquid used, so you can increase your understanding of Liquid and learn to write your own.

To get started, see [AI Liquid assistant]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_liquid).
 
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

You can now create and apply [brand guidelines]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/brand_guidelines/) to customize the style of copy generated by the AI copywriting assistant to fit your brand's voice. Set up multiple guidelines for different scenarios to ensure your tone always matches the context.
 
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

## April 2, 2024 release

### WhatsApp

#### Multiple business accounts

Now you can add multiple WhatsApp Business accounts and subscription groups to each workspace. For a full walkthrough, see [Multiple WhatsApp Business accounts and phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/).

#### Read rates

WhatsApp is testing new approaches, starting with consumers in India, to create more valuable experiences and maximize engagement with businesses’ marketing conversations. This may include limiting the number of marketing conversations a person receives from any business in a given period, starting with a small number of conversations that are less likely to be read. For more information, see [Meta resources]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/).

### Data flexibility

#### Sync Amazon S3 buckets to Braze

{% multi_lang_include release_type.md release="Early access" %}

You can now use Cloud Data Ingestion for S3 to directly integrate one or more S3 buckets in your AWS account with Braze. When new files are published to S3, a message is posted to SQS, and Braze Cloud Data Ingestion takes in those new files. For more information, see [File storage integrations]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_integrations/).

#### Shopify OAuth

{% multi_lang_include release_type.md release="General availability" %}

Shopify  is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Now when you set up Shopify for Braze, you can [enable OAuth for your workspace]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/).

#### Use Expo for iOS push notifications

We [added instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications/?tab=expo) for integrating rich push notifications and Push Stories into your iOS app using Expo with React Native.

#### Remote start iOS live activities

Now you can remote start your live activities on iOS using the [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/) endpoint. For a full walkthrough, see [Live Activities: Start an Activity]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#step-2-start-the-activity).

### AI and ML automation

#### Item recommendations

{% multi_lang_include release_type.md release="Early access" %}

With Sage AI by Braze, you can now calculate the most popular products or create personalized AI recommendations for a specific catalog. For more information, see [About item recommendations]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/).

#### QA in-app message content

{% multi_lang_include release_type.md release="General availability" %}

Previously, you could perform quality assurance on your SMS and push notification content using Sage AI in the Braze dashboard. Now, you can [QA in-app message content]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_content_qa/) too.

### New Braze partnerships

#### Census - Cohort Import

You can now [import cohort users from Braze to Census]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/census/), a data activation platform that connects cloud data warehouses like Snowflake and BigQuery to Braze. Your marketing teams can unlock the power of their first-party data to build dynamic audience segments, sync customer attributes to personalize campaigns, and keep all their data in Braze up-to-date.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [React Native 9.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
  - Updated the minimum React Native version to 0.71.0.
  - Updated the minimum iOS version to 12.0.
  - Updated the iOS bindings to use Braze Swift SDK 8.1.0.
  - Updated the Android bindings to use Braze Android SDK 30.1.1.

## March 5, 2024 release

### Google EU User Consent Policy

Google is updating their [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/) in response to changes to the [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), which is in effect as of March 6, 2024. This new change requires advertisers to disclose certain information to their EEA and UK end users, as well as obtain necessary consents from them. As part of this upcoming change, you can [collect both consent signals in Braze as custom attributes]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users). Braze will sync the data from these custom attributes to the appropriate consent fields in Google.

### Data flexibility

#### Merge duplicate users

{% multi_lang_include release_type.md release="Early access" %}

In the Braze dashboard, you can now [search for and merge duplicate users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users) to maximize the effectiveness of your campaigns and Canvases. You can individually merge user profiles or perform a bulk merge, which merges all profiles with matching identifiers into the most recently updated user profile.

#### Search for archived content

In the Braze dashboard, you can now include [archived content in your search results]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/#filter-for-archived-content) by selecting **Show Archived Content**.

#### Message archiving support for AWS S3 and Google Cloud Storage

You can use [message archiving]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/) to save a copy of your messages sent to users for archival or compliance purposes to your AWS S3 bucket, Azure Blob Storage container or Google Cloud Storage bucket.

#### SQL table reference

Visit the [SQL table reference]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) to see the tables and columns available to be queried in the Query Builder or when generating SQL Segment Extensions.

### Unlocking creativity

#### Tone control for AI copywriting

You can now choose a [message tone]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/#steps) to determine the style of the copy generated with the AI copywriting assistant.

### Robust channels

#### Card creation

You can choose when Braze evaluates audience eligibility and personalization for new Content Card campaigns and Canvas steps by specifying when the card is [created]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/). 

#### Preview user paths

{% multi_lang_include release_type.md release="General availability" %}

Experience the Canvas journey you’ve created for your users, including previewing the timing and messages they will receive. These [test runs]({{site.baseurl}}/preview_user_paths/) act as quality assurance that your messages are sent to the right audience, all before sending the Canvas.

#### Quick push campaigns

{% multi_lang_include release_type.md release="General availability" %}

When creating a push campaign in Braze, you can select multiple platforms and devices to craft one message for all platforms in a single editing experience called [quick push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/). This feature is only available for campaigns.

#### Custom list-unsubscribe header

{% multi_lang_include release_type.md release="General availability" %}

Adding a [custom list-unsubscribe header]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#custom-list-unsubscribe-header) to your email messaging allows your recipients to opt-out. This way, you can add your own configured one-click unsubscribe endpoint and an optional “mailto:”. Braze requires an input for URL to support a custom list-unsubscribe header because the one-click unsubscribe HTTP is a requirement from Yahoo and Gmail for bulk senders.

#### Multiple pages for in-app messages

{% multi_lang_include release_type.md release="Early access" %}

[Adding pages to your in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#multi-page) lets you guide users through a sequential flow, like an onboarding flow or welcome journey. You can manage pages from the **Pages** section of the **Build** tab.

#### Randomize paths for an experiment path

To always [randomize path assignment]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) for an Experiment Path step, select **Randomized Paths in Experiment Paths** in the step. This option is not available when using either Winning or Personalized Paths.

#### Email capture form

[Email capture messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/) allow you to easily prompt users of your site to submit their email address, after which it will be available in their user profile for use in all your messaging campaigns.

### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [AppboyKit iOS SDK 4.7.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.7.0)
    - This will be the final release for the Objective-C SDK before end-of-life on March 1, 2024 (in favor of using the [Swift SDK](https://github.com/braze-inc/braze-swift-sdk/)).
    - Updates the minimum required version of SDWebImage from 5.8.2 to 5.18.7. This version includes the privacy manifest for SDWebImage, which appears on the [privacy-impacting SDKs list](https://developer.apple.com/support/third-party-SDK-requirements/).
- [Flutter SDK 8.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity 5.2.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [React Native SDK 8.4.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.4.0/CHANGELOG.md)
- [Xamarin SDK Version 4.0.2](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.7.0-8.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#801)
- [Android SDK 30.1.0-30.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Web SDK 5.1.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Cordova SDK 8.0.0-Cordova SDK 8.1.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Updated the native Android bridge [from Braze Android SDK 27.0.1 to 30.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v30.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native iOS bridge [from Braze Swift SDK 6.6.0 to 7.6.0](https://github.com/braze-inc/braze-swift-sdk/compare/6.6.0...7.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Renamed the `Banner` Content Card type to `ImageOnly`:
        - `ContentCardTypes.BANNER` to `ContentCardTypes.IMAGE_ONLY`
        - On Android, if the XML files in your project contain the word banner for Content Cards, it should be replaced with `image_only`.
    - `BrazePlugin.getFeatureFlag(id)` will now return `null` if the feature flag does not exist.
    - `BrazePlugin.subscribeToFeatureFlagsUpdates(function)` will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.
    - Removed the deprecated method `registerAppboyPushMessages`. Use `setRegisteredPushToken` instead.

## February 6, 2024 release

### Braze privacy manifest

Braze has released our own privacy manifest, along with new flexible APIs that automatically reroute declared tracking data to dedicated `-tracking` endpoints. For more information, see the [Braze privacy manifest]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).

### Google EU User Consent Policy

Google is updating their [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/) in response to changes to the [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), which goes into effect March 6, 2024. This new change requires advertisers to disclose certain information to their EEA and UK end users, as well as obtain necessary consents from them. As part of this upcoming change, you can [collect both consent signals in Braze as custom attributes]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users). Braze will sync the data from these custom attributes to the appropriate consent fields in Google.

### Data flexibility

#### Google Firebase Cloud Messaging (FCM) API

{% multi_lang_include release_type.md release="General availability" %}

You now can [migrate from Google’s deprecated Cloud Messaging API to their fully-supported Firebase Cloud Messaging (FCM) API]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/). 

#### Braze Cloud Data Ingestion (CDI) endpoints

{% multi_lang_include release_type.md release="General availability" %}

Use Braze CDI endpoints to:
- [Return a list of existing integrations]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/).
- [Return a list of past sync statuses]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) for a given integration.
- [Trigger a sync]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/) for a given integration.

#### Braze Cloud Data Ingestion (CDI) support for Databricks

Braze CDI support for catalogs is now available for [Databricks sources]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/#step-2-integrate-cloud-data-ingestion-with-catalog-data).

#### Manual Swift SDK integration

We added the [Manual integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration) article to the integration guides to describe how to manually integrate the Swift SDK without the use of a package manager.

#### Deprecations

On January 11, 2024, Braze stopped serving messages and collecting data from Windows apps and Baidu apps.

### Unlocking creativity

#### SQL Segment Extensions use cases

The [SQL Segment Extensions use cases]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/use_cases) library contains tested queries for SQL Segment Extensions that you can use for inspiration when creating your own SQL queries.

### Robust channels

#### Custom Code blocks

{% multi_lang_include release_type.md release="General availability" %}

[Custom Code blocks]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/#custom-code) allow you to add, edit, or delete HTML, CSS, and JavaScript for an in-app message.

#### Reduce payload size of push notifications

The new help article [Notification Payload Size]({{site.baseurl}}/help/help_articles/push/reducing_payload_size#reducing-push-notification-payload-size) provides some tips to reduce the payload size of your push notifications if you're unable to launch a campaign or Canvas step due to push payload size limits.

#### Add BCC addresses to your campaign or Canvas

{% multi_lang_include release_type.md release="General availability" %}

You can append a [BCC address]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#outbound-email-settings) to an email message. This will send an identical copy of the message your user receives to your BCC inbox. This allows you to retain copies of messages you sent your users for compliance requirements or customer support issues.

#### One-click unsubscribe links for emails

Using a [list-unsubscribe header]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe-header) allows your recipients to unsubscribe with one click from marketing emails by displaying an **Unsubscribe** button within the mailbox UI, and not the message body.

### New Braze partnerships

#### Criteo - Canvas Audience Sync

Using the [Braze Audience Sync to Criteo]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync/), brands can elect to add user data from their own Braze integration to Criteo customer lists to deliver advertisements based upon behavioral triggers, segmentation and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in your Criteo customer lists.

#### Movable Ink - Dynamic content

The [Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink#movable-ink) Customer Data API integration allows marketers to activate customer event data stored in Braze to generate personalized content within Movable Ink.

#### Scuba Analytics - Analytics

[Scuba Analytics]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/scuba#scuba-analytics) is a full-stack, machine-learning-powered data collaboration platform designed for high-velocity time-series data. Scuba allows you to selectively export users (also called actors) and load them into your Braze platform. In Scuba, custom actor properties are used to analyze behavioral trends, activate your data across various platforms, and conduct predictive modeling using machine learning.

### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Expo Plugin 2.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - Bumps the iOS minimum platform version to `13.4`, per the [Expo SDK 50 requirements](https://expo.dev/changelog/2024/01-18-sdk-50).
    - This version requires version [8.3.0+](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/8.3.0) of the Braze React Native SDK to fully support Expo SDK 50.
- [React Native SDK 8.3.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.3.0/CHANGELOG.md)
- [Unity SDK 5.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Android SDK 30.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - WebViews used for In-App Messages have been updated to use `WebViewAssetLoader`.
        - `WebSettings.allowFileAccess` is now set to false in `InAppMessageHtmlBaseView` and `BrazeWebViewActivity`.
        - If you are using your own `InAppMessageWebViewClient` or `InAppMessageHtmlBaseView`, please compare them against the original classes to make sure you're implementation is correctly loading the assets.
        - If you are not using custom classes, everything will work as before.
- [Braze Swift SDK 6.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/6.6.2/CHANGELOG.md)
- [Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)
- [Xamarin SDK Version 3.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - The NuGet package has been renamed from `AppboyPlatformXamariniOSBinding` to [`BrazePlatform.BrazeiOSBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/).
        - To use the updated package, replace any instances of using `AppboyPlatformXamariniOSBinding;` with: using Braze;
    - This version requires using .NET 6+ and removes support for projects using the Xamarin framework. See [Microsoft's policy](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) around the end of support for Xamarin.
    - Updated the Android binding from [Braze Android SDK 26.3.2 to 29.0.1](https://github.com/braze-inc/braze-android-sdk/compare/v26.3.1...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Xamarin SDK 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - This version updates the iOS binding to use the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/). Most iOS public APIs have changed, please refer to our [migration guide](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/) (Swift) for guidance about replacement to use. We provide compatibility bindings to keep making use of the old public APIs.
        - The iOS binding is now composed of multiple modules:
            - **BrazeKit:** Main SDK library providing support for analytics and push notifications (nuget: [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)).
            - BrazeUI: Braze-provided user interface library for In-App Messages and Content Cards (nuget: [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)).
            - BrazeLocation: Location library providing support for location analytics and geofence monitoring (nuget: [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)).
            - BrazeKitCompat: Compatibility library with support for pre-4.0.0 APIs (nuget: [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat)).
            - BrazeUICompat: Compatibility library with support for pre-4.0.0 UI APIs (nuget: [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)).
        - Refer to the BrazeiOSMauiSampleApp for the new integration, and to BrazeiOSMauiCompatSampleApp for usage of the compatibility modules.
    - Updated the iOS binding to the [Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0).
    - The iOS binding requires using .NET 7 for compatibility with Xcode 15.
- [Xamarin SDK 4.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
