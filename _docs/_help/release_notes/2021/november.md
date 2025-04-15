---
nav_title: November
page_order: 1
noindex: true
page_type: update
description: "This article contains release notes for November 2021."
---
# November 2021

## Click-to-Open Rate reporting metric
Braze has added a new email metric, Click-to-Open Rate, available in the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/). This metric represents the percentage of open emails that have been clicked.

## Machine Open reporting metric

A new email metric, [Machine Opens]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens), is available on the Canvas and Campaign Analytics pages for emails. This metric identifies email opens that are non-human (such as opened by Apple's servers), displayed as a subset of total opens.

## random_bucket_number Liquid variable
A variable `random_bucket_number` has been added to the list of [supported Liquid variables]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) for message personalization. 

## iOS 15 rich push notification guidelines
New [iOS push notification guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) have been added to the iOS rich docs, including information about notification states and a breakdown of text truncation variables.

## IPs to whitelist in EU for webhooks and Connected Content
Additional IPs to whitelist in EU for webhooks and Connected Content have been added to our [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) and [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) article. These new IPs include `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188`, and `3.70.107.88`.

## Export purchases endpoint
A new [`/purchases/product_list` endpoint]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) has been added to Braze. This endpoint returns paginated lists of product IDs.

## New Braze partnerships

### Adobe - Customer data platform
The Braze and [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) integration allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time. Brands can then act on this data, delivering personalized, targeted experiences to those users. 

### BlueConic - Customer data platform
With [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic), Braze users can unify data into persistent, individual profiles and then sync it across customer touchpoints and systems in support of a wide range of growth-focused initiatives, including customer lifecycle orchestration, modeling and analytics, digital products and experiences, audience-based monetization, and more.

### Worthy - Dynamic content
The Braze and [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) integration allows you to easily create personalized, rich in-app experiences using Worthy's drag-and-drop dynamic content editor and deliver them through Braze.

### Judo - Dynamic content
The [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) and Braze integration allows you to overwrite components of your campaign and replace them with Judo experiences. Data from Braze may be used to support personalized content in a Judo experience. User events and data from the experience can feedback into Braze for attribution and targeting.

### Line - Messaging
The [Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) and Braze integration allows you to leverage Braze webhooks, advanced segmentation, personalization, and triggering features to message your users in Line through the [Line Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/).

### RevenueCat - Payments
The [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) and Braze integration allows you to automatically sync your customer's purchase and subscription lifecycle events across platforms. This allows you to build campaigns that react to the subscription lifecycle stage of your customers, such as engaging with customers that opted out during their free trial or sending reminders to customers with billing issues.

### Punchh - Loyalty
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) has partnered with Braze to sync data across the two platforms for gifting and loyalty purposes. Data published in Braze will be available for segmentation and can sync user data back into Punchh via webhook templates setup in Braze.  