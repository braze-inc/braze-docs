---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: featured
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the following <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>. You can also check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK Changelogs</a>."
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

## July 2022

### Inbox Vision

With Inbox Vision, you can check that your drag & drop email campaigns are aligned across all your email clients and mobile platforms before sending. To learn more, check out [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/).

### Updated HTML engine

The underlying engine that produces HTML from the Drag & Drop Editor has been optimized and updated, resulting in benefits related to HTML file compression and rendering. For more details on the updates, check out [Updated HTML engine]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#updated-html-engine/) 

### Event property segmentation

[Event property segmentation]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#event-property-segmentation/) allows you to target users based on custom events taken and the properties associated with those events. This feature adds additional filtering options when segmenting purchase and custom events.

### Audience sync to Google

The Braze Audience Sync to Google implementation process has been simplified when granting Braze access to your Google Ads account. For more information, see [Audience Sync to Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/). 

### New Braze partnerships

#### Amperity - Customer data platform

The Braze and [Amperity]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/) integration offers a unified view of your customers across the two platforms. With this integration, you can sync user lists to map Amperity user data to Braze user accounts by creating an Amperity user list. 

#### Dynamic 365 Customer Insights - Customer data platform

The Braze and [Dynamics 365 Customer Insights]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/dynamics_365_customer_insights/) integration allows you to export customer segments to Braze to use in campaigns or Canvases.

#### Extole - Loyalty

With the Braze and [Extole]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/extole/) integration, you can pull customer events and attributes from Extole refer-a-friend and growth programs into Braze, empowering you to create more personalized marketing campaigns that boost customer acquisition, engagement, and loyalty. You can also dynamically pull Extole content attributes, such as personalized share codes and links, into Braze communications.

#### Heap - Cohort import

The Braze and [Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/) integration enables you to import Heap data to Braze, create user cohorts, as well as export Braze data to Heap](#data-export-integration to create segments.

#### Hightouch - Workflow automation

The Braze and [Hightough]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/) integration allows you to import user cohorts to Braze, sending targeted campaigns based on data that may only exist in your warehouse.

#### Peak - Dynamic content

The Braze and [Peak]({{site.baseurl}}/partners/message_personalization/dynamic_content/peak/) integration allows you to take predicted churn probability and attributes based on customer behaviors and interactions, and import them into Braze to use in customer segmentation and targeting. 

#### Shopify - eCommerce

The Braze and [Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) integration allows Braze to ingest and process Shopify user data. You can update an abandoned cart checkout delay and set your preferred product identifier.

#### Survicate - Surveys

The Braze and [Survicate]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/survicate/) integration allows you to include survey links in your emails or directly embed survey snippets to increase the response rate. After surveys have been completed, return to Survicate to identify and analyze the attributes and responses of your survey responders.

#### Viralsweep - Loyalty

The Braze and [ViralSweep]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/viralsweep/) integration allows you to hold sweepstakes and contests on the ViralSweep platform (growing your email and SMS lists) and then send sweepstake or contest entry information into Braze to use in campaigns or Canvases. 

## June 2022

### Campaign approval

Campaign approval adds a review process to your workflow before launching a campaign. Now, you can ensure that each confirmation is approved in order to launch the campaign. To learn more about the approval process, check out [Campaign approval]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/).

### Canvas Message Step

Message Steps allow you to add a standalone message where you want in your Canvas Flow. Visit our [message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) article to learn more.

### AI copywriting assistant

The Braze [AI copywriting assistant]({{site.baseurl}}/user_guide/intelligence/ai_copywriting#ai-copywriting-assistant) passes a brief product name or description to OpenAI's GPT3 copy generation tool to generate human-like marketing copy for use in your messaging. This functionality is available out-of-the-box for most message composers in the Braze dashboard.

### iOS push notification unit testing guide

An [iOS unit testing guide for push notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests#unit-tests) has been added to the developer guide. This guide will provide unit tests that will verify whether your app delegate is correctly set up. 

### Google privacy questionnaire

As of April 2022, Android developers must complete Google Play's [Data safety form][4] to disclose privacy and security practices. [This guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/google_play_privacy#google-play-privacy-questionnaire) provides instructions on how to fill out this new form with information on how Braze handles your app data. 

### RelayState SAML SSO

Initial single sign-on set-up instructions have been updated to recommend use of a `RelayState` API key. For more information, refer to [SAML SSO setup]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) and cooresponding [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/), [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), and [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/) articles. 

### Talon.One integration updates

Our [Talon.One]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/talonone#talonone) partnership article now has updated integration steps, endpoints, and examples. If you are leveraging the Talon.One partnership, we recommend updating your integration accordingly.

### Braze Web SDK V4 released

The Braze SDKs team has released Web SDK v4. For a list of breaking changes, updates, and additions, visit our Web SDK [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md). An [upgrade guide](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md) has been created for those upgrading from V3 to V4.

### Grouparoo deprecation

Support for Grouparoo has been discontinued as of April 2022.

## May 2022

### Filter by campaign or Canvas attribution
You can now filter for users who have replied to a specific SMS campaign or Canvas step, keyword category, or tag. For more information, see [SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/).

### Email performance dashboard
With the [email performance dashboard]({{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/), you can view aggregate performance metrics for your entire email channel from both campaigns and Canvases for your selected date range.

For more information about the analytics dashboards available within Braze, check out the [Your Analytics Dashboards]({{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/) section.

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

Braze now supports sending in-app messages to your users on their Roku devices! Note that this requires additional SDK configuration and is not available out-of-the-box. For more information on integrating in-app messages for Roku, refer to [Roku in-app messages]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).

### Full Filter Mode for Churn Predictions and Purchase Predictions

In order to build a new prediction immediately, only a subset of Braze segmentation filters are supported by default. You can now enable Full Filter Mode to enable all segmentation filters, however this mode limits you to one window when building the prediction. For more, refer to the following articles:

- [Creating a Churn Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#full-filter-mode)
- [Creating a Purchase Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#full-filter-mode)

### Retargeting option for keyword responses

When viewing analytics for an SMS campaign, you can now conveniently create a segment for retargeting based on the users who responded with a specific keyword category. For more information, refer to [Keyword Responses]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#keyword-responses) in SMS reporting.

### Data collection best practices

Have you wondered when and how you should collect user data when you're handling both known and unknown users? We know the lifecycle of a user profile in Braze can be a bit confusing, so we put together some [data collection best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) to help clarify different methods and best practices for collecting new and existing user data.

### Transifex API deprecation

As of April 7, 2022, Transifex is deprecating their API versions 2 and 2.5 to make way for version 3. After this date, v2 and v2.5 will no longer be operational, and relevant requests will fail. If you are leveraging the Transifex API, update your Connected Content calls accordingly. For more information, refer to [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/).

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

The Braze and [Grouparoo]({{site.baseurl}}/help/release_notes/deprecations/grouparoo) integration makes it easy to operationalize data stored in a warehouse by sending it to Braze. When you set up automatic sync schedules, you can consistently enhance customer communications with up-to-date information.

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

[support]: {{site.baseurl}}/support_contact/
