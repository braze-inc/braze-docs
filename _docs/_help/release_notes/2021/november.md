---
nav_title: November
page_order: 2
noindex: true
page_type: update
description: "This article contains release notes for November 2021."
---
 
# November 2021

## Data Points Usage Dashboard

Use the **Total Data Points Usage** dashboard to track your data point usage pacing in relation to your contract allotment. This dashboard provides information on your contract, current billing cycle, company billing data, and app group billing data. For more information, refer to [Subscriptions and Usage](/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard).

## Change to Segment Extension Regeneration

Starting on November 1, 2021, the setting to regenerate extensions daily will be automatically turned off for unused [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Braze defines unused extensions as ones that meet the following criteria:

- Not used in any active campaigns, Canvases, or segments
- Not used in any inactive (draft, stopped, archived) campaigns, Canvases, or segments
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension when this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.

## Android Advanced Push Implementation Guide

This optional and advanced [implementation guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/implementation_guide/) covers ways to leverage a custom `FirebaseMessagingService` subclass to get the most out of your push messages. Included is a custom use case built by our team, accompanying code snippets, and guidance on logging analytics.

## New Braze Partnerships

### Shopify - eCommerce

[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Together, the Braze and Shopify integration allows brands to connect their Shopify store seamlessly with Braze to pass select Shopify webhooks into Braze. Leverage Braze’s cross-channel strategies and Canvas to retarget your users with abandoned checkout messaging and nudge customers to complete their purchase, or retarget users based on their previous purchases.