---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "This article contains release notes for April 2022."
---

# April 2022

## In-app messages for Roku

Braze now supports sending in-app messages to your users on their Roku devices! Please note that this requires additional SDK configuration and is not available out-of-the-box. For more information on integrating in-app messages for Roku, refer to [Roku in-app messages]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).

## Full Filter Mode for Churn Predictions and Purchase Predictions

In order to build a new prediction immediately, only a subset of Braze segmentation filters are supported by default. You can now enable Full Filter Mode to enable all segmentation filters, however this mode limits you to one window when building the prediction. For more, refer to the following articles:

- [Creating a Churn Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#full-filter-mode)
- [Creating a Purchase Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#full-filter-mode)

## Retargeting option for keyword responses

When viewing analytics for an SMS campaign, you can now conveniently create a segment for retargeting based on the users who responded with a specific keyword category. For more information, refer to [Keyword Responses]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#keyword-responses) in SMS reporting.

## Data collection best practices

Have you wondered when and how you should collect user data when you're handling both known and unknown users? We know the lifecycle of a user profile in Braze can be a bit confusing, so we put together some [data collection best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) to help clarify different methods and best practices for collecting new and existing user data.

## Transifex API deprecation

As of April 7, 2022, Transifex is deprecating their API versions 2 and 2.5 to make way for version 3. After this date, v2 and v2.5 will no longer be operational, and relevant requests will fail. If you are leveraging the Transifex API, please update your Connected Content calls accordingly. For more information, refer to [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/).

## New Braze partnerships

### Toovio - Customer data platform

The Braze and [Toovio]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/toovio/) partnership provides near real-time message triggering, the tools to drive incremental performance, and access to Toovio’s advanced campaign measurement tools.

### Snowplow - Analytics

The Braze and [Snowplow]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/snowplow/) integration enables users to forward Snowplow events to Braze through Google Tag Manager server-side tagging. The Snowplow Braze tag allows you to send events to Braze while offering additional flexibility and control:

- Full visibility into all transformations on the data
- Ability to evolve sophistication over time
- All data remains in your private cloud until you choose to forward it
- Ease of setup due to rich libraries of tags and familiar Google Tag Manager UI

Leverage Snowplow’s rich behavioral data to drive powerful customer-centric interactions in Braze and deliver personalized messages in real-time.

### Clarisights - Analytics

The Braze and [Clarisights]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/clarisights/) integration allows you to import data from Braze campaigns and Canvases to help achieve a unified reporting interface of performance and CRM/retention marketing.

### Wyng - Dynamic content

The Braze and [Wyng]({{site.baseurl}}/partners/message_personalization/dynamic_content/wyng/) integration allows you to leverage Wyng experiences to deliver personalization in Braze campaigns and Canvases. Wyng also includes a customer preference portal so users can control the data and preferences they share with a brand.

### Grouparoo - Workflow automation

The Braze and [Grouparoo]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/grouparoo/) integration makes it easy to operationalize data stored in a warehouse by sending it to Braze. When you set up automatic sync schedules, you can consistently enhance customer communications with up-to-date information.

### Lexer - Customer data platform

The Braze and [Lexer]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/lexer/) integration allows you to sync data across the two platforms. Use your Lexer data to create valuable Braze segments or import your existing ones to Lexer to unlock insights.

### Knak - Email orchestration

The Braze and [Knak]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/knak/) integration allows you to create fully responsive emails in minutes or hours instead of days or weeks and export them as ready-to-use Braze templates. Knak is built for marketers who want to level up their email creation for campaigns managed in Braze, without the need for outside agencies or hand-coding.