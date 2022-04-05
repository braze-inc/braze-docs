---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: featured
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>, listed below. You can also
check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK Changelogs</a>."
page_type: landing
description: "This landing page is home to Braze Release Notes. This is where you can find all updates to the Braze platform and SDKs, as well as a list of deprecated features."

guide_featured_title: "Release Notes"
guide_featured_list:
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

## May 2022

### Email performance dashboard
With the [email performance dashboard]({{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/), you can view aggregate performance metrics for your entire email channel from both campaigns and Canvases for your selected date range.

For more informaation about the analytics dashboards available within Braze, check out the [Your Analytics Dashboards]({{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/) section.

### Global style settings

Introducing [global style settings]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/) for the Drag & Drop Editor! Now, you can easily personalize the look of your email campaigns and Canvases by adding a default theme, setting basic text styling, and more.

### Braze to Braze webhooks
With a Braze to Braze webhook, you can use webhooks to communicate with the Braze REST API, doing anything that our API allows you to do. Essentially, this is a webhook that is communicating from Braze to Braze. For more information, see our [Braze to Braze webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) article.

### Deprecations

#### Windows SDK
As of March 24, 2022, the [Braze Windows SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/initial_sdk_setup/) is deprecated, and no new Windows apps can be created in the Braze dashboard. 

#### Baidu push integration
As of March 24, 2022, the [Braze Baidu Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/baidu_integration/) is deprecated, and no new Baidu apps can be created in the Braze dashboard. 

### New Braze partnerships

#### Tealium for Currents

The Braze and [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents/) integration allows you to seamlessly control the flow of information between the two systems. Now with Currents, you can also connect data to Tealium to make it actionable across the entire growth stack.

## April 2022

### In-app messages for Roku

Braze now supports sending in-app messages to your users on their Roku devices! Please note that this requires additional SDK configuration and is not available out-of-the-box. For more information on integrating in-app messages for Roku, refer to [Roku in-app messages]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).

### Full Filter Mode for Churn Predictions and Purchase Predictions

In order to build a new prediction immediately, only a subset of Braze segmentation filters are supported by default. You can now enable Full Filter Mode to enable all segmentation filters, however this mode limits you to one window when building the prediction. For more, refer to the following articles:

- [Creating a Churn Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#full-filter-mode)
- [Creating a Purchase Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#full-filter-mode)

### Retargeting option for keyword responses

When viewing analytics for an SMS campaign, you can now conveniently create a segment for retargeting based on the users who responded with a specific keyword category. For more information, refer to [Keyword Responses]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#keyword-responses) in SMS reporting.

### Data collection best practices

Have you wondered when and how you should collect user data when you're handling both known and unknown users? We know the lifecycle of a user profile in Braze can be a bit confusing, so we put together some [data collection best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) to help clarify different methods and best practices for collecting new and existing user data.

### Transifex API deprecation

As of April 7, 2022, Transifex is deprecating their API versions 2 and 2.5 to make way for version 3. After this date, v2 and v2.5 will no longer be operational, and relevant requests will fail. If you are leveraging the Transifex API, please update your Connected Content calls accordingly. For more information, refer to [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/).

### New Braze partnerships

#### Toovio - Customer data platform

The Braze and [Toovio]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/toovio/) partnership provides near real-time message triggering, the tools to drive incremental performance, and access to Toovio’s advanced campaign measurement tools.

#### Snowplow - Analytics

The Braze and [Snowplow]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/snowplow/) integration enables users to forward Snowplow events to Braze through Google Tag Manager server-side tagging. The Snowplow Braze tag allows you to send events to Braze while offering additional flexibility and control:

- Full visibility into all transformations on the data
- Ability to evolve sophistication over time
- All data remains in your private cloud until you choose to forward it
- Ease of setup due to rich libraries of tags and familiar Google Tag Manager UI

Leverage Snowplow’s rich behavioral data to drive powerful customer-centric interactions in Braze and deliver personalized messages in real-time.

#### Clarisights - Analytics

The Braze and [Clarisights]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/clarisights/) integration allows you to import data from Braze campaigns and Canvases to help achieve a unified reporting interface of performance and CRM/retention marketing.

#### Wyng - Dynamic content

The Braze and [Wyng]({{site.baseurl}}/partners/message_personalization/dynamic_content/wyng/) integration allows you to leverage Wyng experiences to deliver personalization in Braze campaigns and Canvases. Wyng also includes a customer preference portal so users can control the data and preferences they share with a brand.

#### Grouparoo - Workflow automation

The Braze and [Grouparoo]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/grouparoo/) integration makes it easy to operationalize data stored in a warehouse by sending it to Braze. When you set up automatic sync schedules, you can consistently enhance customer communications with up-to-date information.

#### Lexer - Customer data platform

The Braze and [Lexer]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/lexer/) integration allows you to sync data across the two platforms. Use your Lexer data to create valuable Braze segments or import your existing ones to Lexer to unlock insights.

#### Knak - Email orchestration

The Braze and [Knak]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/knak/) integration allows you to create fully responsive emails in minutes or hours instead of days or weeks and export them as ready-to-use Braze templates. Knak is built for marketers who want to level up their email creation for campaigns managed in Braze, without the need for outside agencies or hand-coding.

## March 2022

### Canvas Action Paths

[Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) allow you to sort your users based on their actions. Using Action Paths, you can:
- Customize user paths based on a specific action. 
- Hold users for a given duration to prioritize their next path based on their actions during this evaluation period. 

Access to Action Paths will be rolled out slowly to all Braze instances. Contact your Braze account manager to learn more.

### API endpoint reference page

Looking for a quick reference page of all available Braze endpoints? Visit our [API endpoint index]({{site.baseurl}}/api/endpoints/).

### Transifex v2 and v2.5 API deprecation
Beginning April 7, 2022, [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#transifex) will be deprecating their API versions 2 and 2.5 to make way for version 3. After this date, v2 and v2.5 will no longer be operational, and relevant requests will fail. Users of this partner integration are urged to update their API version before this date.

### Available custom attribute data types
Coming soon! Object and object array data type support for custom attributes is arriving in Spring 2022.

## February 2022

### Canvas Experiment Paths Step
The new Canvas Experiment Paths Step helps track path performance by testing multiple Canvas paths against each other and a control group at any point in the user journey. Now, you can leverage the analytics gathered here to further determine which path is most effective. Read more about how to create a [Experiment Paths Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).

### Handling invalid phone numbers
You've encountered a scenario where a user has entered an invalid phone number. Here's your solution! Braze marks these invalid phone numbers and will not attempt to send any further communications to those numbers. Read more on how Braze [handles invalid phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers/).

### New SMS endpoints
You can now manage invalid phone numbers using the new [Braze SMS Endpoints]({{site.baseurl}}/api/endpoints/sms/)! This update features:
- [GET: Query or list invalid phone numbers endpoint]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) returns a list of phone numbers that are considered "invalid" by Braze.
- [POST: Remove invalid phone numbers endpoint]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) allows you to remove the "invalid" phone numbers from Braze's invalid list.

### Rate limits
API rate limits have been included for all [Braze Endpoint articles]({{site.baseurl}}/api/basics/#nav_top_endpoints). You can now easily view the rate limits by request type. For more information on rate limits, check out our article on [API rate limits]({{site.baseurl}}/api/api_limits/).

### New REST endpoint
Braze has added a [new EU-02 REST Endpoint]({{site.baseurl}}/api/basics/#api-definitions).

### About email
Email messages are a great way to connect with your customers. For a quick introduction on how you can customize and leverage email messages, check out our new article on [About email]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/). 

### About in-app messages
In-app messages deliver rich content to your users who are active within your app. You can easily engage with your active customers by creating in-app messges for personalized greetings or feature adoption. To learn about the advantages and message types, check out our new article on [About in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/).

## January 2022

Welcome to a new year!

### Update to export users by segment endpoint

Beginning December 2021, the following changes take effect for the [export users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) endpoint:

1. The `fields_to_export` field in this API request will be required. The option to default to all fields will be removed.
2. The fields for `custom_events`, `purchases`, `campaigns_received`, and `canvases_received` will only contain data from the last 90 days.

### New properties for Currents message engagement events

New properties have been added for select [message engagement events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/). This update applies to the following Currents message engagement events and all partners that use them:

- Add `LINK_ID`, `LINK_ALIAS` to:
  - Email Click (all destinations)
- Add `USER_AGENT` to:
  - Email Open
  - Email Click
  - Email Mark As Spam
- Add `MACHINE_OPEN` to:
  - Email Open

### New Liquid personalization tag

We now support targeting users who have foreground push enabled on their device with the following Liquid tags:

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

For more information, refer to [Supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

### About webhooks

Webhooks are powerful, flexible tools—but they can be a bit confusing. If you're wondering what webhooks are and how you can use them in Braze, check out our new article on [About webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

### Amazon Personalize

Amazon Personalize is like having your very own all day Amazon machine learning recommendation system. Based on over 20 years of recommendation experience, Amazon Personalize enables you to improve customer engagement by powering real-time personalized product and content recommendations and targeted marketing promotions. 

If you'd like to learn more, visit our new [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/amazon_personalize/) article to understand the use cases Amazon Personalize offers, data it works with, how to configure the service, and how to integrate it with Braze.

### New Braze partnerships

#### Yotpo – eCommerce

The [Yotpo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/yotpo/) and Braze integration allows you to dynamically pull and display star ratings, top reviews, and visual user-generated content on products within emails and other communication channels within Braze. You can also include customer-level loyalty data in emails and other communication methods to create a more personalized interaction, boosting sales and loyalty.

#### Zeotap – Customer data platform

With the [Zeotap]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/zeotap/) and Braze integration, you can extend the scale and reach of your campaigns by syncing Zeotap customer segments to map Zeotap user data to Braze user accounts. You can then act on this data, delivering personalized target experiences to your users.

## December 2021

### Click-to-Open Rate reporting metric
Braze has added a new email metric, Click-to-Open Rate, available in the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/). This metric represents the percentage of open emails that have been clicked.

### Machine Open reporting metric

A new email metric, [Machine Opens]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens), is available on the Canvas and Campaign Analytics pages for emails. This metric identifies email opens that are non-human (i.e., opened by Apple's servers), displayed as a subset of total opens.

### random_bucket_number Liquid variable
A variable `random_bucket_number` has been added to the list of [supported Liquid variables]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) for message personalization. 

### iOS 15 rich push notification guidelines
New [iOS push notification guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) have been added to the iOS rich docs, including info about notification states and a breakdown of text truncation variables.

### IPs to whitelist in EU for webhooks and Connected Content
Additional IPs to whitelist in EU for webhooks and Connected Content have been added to our [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) and [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) article. These new IPs include `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188`, and `3.70.107.88`.

### Export purchases endpoint
A new [GET: list product IDs]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) endpoint has been added to Braze. This endpoint returns paginated lists of product IDs.

### New Braze partnerships

#### Adobe - Customer data platform
The Braze and [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) integration allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time. Brands can then act on this data, delivering personalized, targeted experiences to those users. 

#### BlueConic - Customer data platform
With [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic), Braze users can unify data into persistent, individual profiles and then sync it across customer touchpoints and systems in support of a wide range of growth-focused initiatives, including customer lifecycle orchestration, modeling and analytics, digital products and experiences, audience-based monetization, and more.

#### Worthy - Dynamic content
The Braze and [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) integration allows you to easily create personalized, rich in-app experiences using Worthy’s drag and drop dynamic content editor and deliver them through Braze.

#### Judo - Dynamic content
The [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) and Braze integration allows you to overwrite components of your campaign and replace them with Judo experiences. Data from Braze may be used to support personalized content in a Judo experience. User events and data from the experience can feedback into Braze for attribution and targeting.

#### Line - Messaging
The [Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) and Braze integration allows you to leverage Braze webhooks, advanced segmentation, personalization, and triggering features to message your users in Line through the [Line Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/).

#### RevenueCat - Payments
The [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) and Braze integration allows you to automatically sync your customer's purchase and subscription lifecycle events across platforms. This allows you to build campaigns that react to the subscription lifecycle stage of your customers, such as engaging with customers that opted out during their free trial or sending reminders to customers with billing issues.

#### Punchh - Loyalty
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) has partnered with Braze to sync data across the two platforms for gifting and loyalty purposes. Data published in Braze will be available for segmentation and can sync user data back into Punchh via webhook templates setup in Braze. 

## November 2021

### Data points usage dashboard

Use the **Total Data Points Usage** dashboard to track your data point usage pacing in relation to your contract allotment. This dashboard provides information on your contract, current billing cycle, company billing data, and app group billing data. For more information, refer to [Subscriptions and Usage]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard).

### Change to Segment Extension regeneration

Starting on February 1, 2022, the setting to regenerate extensions daily will be automatically turned off for unused [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Braze defines unused extensions as ones that meet the following criteria:

- Not used in any active campaigns, Canvases, or segments
- Not used in any inactive (draft, stopped, archived) campaigns, Canvases, or segments
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension when this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.

### Android advanced implementation guides

#### Content Cards

This optional and advanced [implementation guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/) covers Content Card code considerations, three custom use cases built by our team, accompanying code snippets, and guidance on logging impressions, clicks, and dismissals.

#### In-app messaging

This optional and advanced [implementation guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/implementation_guide/) covers in-app message code considerations, three custom use cases built by our team, and accompanying code snippets.

#### Push notifications

This optional and advanced [implementation guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/implementation_guide/) covers ways to leverage a custom `FirebaseMessagingService` subclass to get the most out of your push messages. Included is a custom use case built by our team, accompanying code snippets, and guidance on logging analytics.

### New Braze partnerships

#### Adobe - Customer Data Platform

Built on the Adobe Experience Platform, Adobe’s Real-time Customer Data Platform (Real-time CDP) helps companies bring together known and anonymous data from multiple enterprise sources in order to create customer profiles that can be used to provide personalized customer experiences across all channels and devices in real-time.

The Braze and [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/) CDP integration allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time. Brands can then act on this data, delivering personalized targeted experiences to those users. 

#### Shopify - eCommerce

[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Together, the Braze and Shopify integration allows brands to connect their Shopify store seamlessly with Braze to pass select Shopify webhooks into Braze. Leverage Braze’s cross-channel strategies and Canvas to retarget your users with abandoned checkout messaging and nudge customers to complete their purchase, or retarget users based on their previous purchases.


<br><br>

[support]: {{site.baseurl}}/support_contact/
