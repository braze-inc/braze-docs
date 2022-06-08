---
nav_title: November
page_order: 2
noindex: true
page_type: update
description: "This article contains release notes for November 2021."
---
 
# November 2021

## Data points usage dashboard

Use the **Total Data Points Usage** dashboard to track your data point usage pacing in relation to your contract allotment. This dashboard provides information on your contract, current billing cycle, company billing data, and app group billing data. For more information, refer to [Subscriptions and Usage]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard).

## Change to segment extension regeneration

Starting on February 1, 2022, the setting to regenerate extensions daily will be automatically turned off for unused [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Braze defines unused extensions as ones that meet the following criteria:

- Not used in any active campaigns, Canvases, or segments
- Not used in any inactive (draft, stopped, archived) campaigns, Canvases, or segments
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension when this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.

## Android advanced implementation guides

### Content Cards

This optional and advanced [implementation guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/) covers Content Card code considerations, three custom use cases built by our team, accompanying code snippets, and guidance on logging impressions, clicks, and dismissals.

### In-app messaging

This optional and advanced [implementation guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/implementation_guide/) covers in-app message code considerations, three custom use cases built by our team, and accompanying code snippets.

### Push notifications

This optional and advanced [implementation guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/implementation_guide/) covers ways to leverage a custom `FirebaseMessagingService` subclass to get the most out of your push messages. Included is a custom use case built by our team, accompanying code snippets, and guidance on logging analytics.

## New Braze partnerships

### Adobe - Customer Data Platform

Built on the Adobe Experience Platform, Adobe’s Real-time Customer Data Platform (Real-time CDP) helps companies bring together known and anonymous data from multiple enterprise sources in order to create customer profiles that can be used to provide personalized customer experiences across all channels and devices in real-time.

The Braze and [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/) CDP integration allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time. Brands can then act on this data, delivering personalized targeted experiences to those users. 

### Shopify - eCommerce

[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Together, the Braze and Shopify integration allows brands to connect their Shopify store seamlessly with Braze to pass select Shopify webhooks into Braze. Leverage Braze’s cross-channel strategies and Canvas to retarget your users with abandoned checkout messaging and nudge customers to complete their purchase, or retarget users based on their previous purchases.