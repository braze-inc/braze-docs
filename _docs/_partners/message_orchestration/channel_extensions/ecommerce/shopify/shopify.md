---
nav_title: Overview
article_title: "Shopify"
description: "This article outlines the partnership with Braze and Shopify, a global commerce company that allows you to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze. Leverage Braze's cross-channel strategies and Canvas to nudge customers to complete their purchases, or retarget users based on their previous purchases."
page_type: partner
search_tag: Partner
alias: "/shopify_overview/"
page_order: 0
---

# Shopify

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Shopify makes commerce better for everyone with a platform and services engineered for reliability while delivering a better shopping experience for consumers everywhere. 

The Shopify and Braze integration allows brands to connect their Shopify store seamlessly to pass select Shopify events and customers into Braze. Leverage Braze’s cross-channel strategies and Canvas to engage new leads, message new customers, or retarget your users with abandoned checkout messaging to nudge them to complete their purchase

## Prerequisites

All Braze customers looking to utilize the Shopify integration must sign Braze's Shopify order form. Reach out to your account executive for more details.

This integration will create alias user profiles if we are unable to match Shopify data using the email or phone number ([see here for more details on Shopify user reconciliation]({{site.baseurl}}/shopify_processing/#shopify-user-syncing)). Consult with your development teams around the downstream impacts and need to merge these user profiles as part of your user lifecycle before you enable the integration. 

| Requirement | Description |
| ----------- | ----------- |
| Shopify store | You must have an active [Shopify](https://www.shopify.com) store.<br><br>Note that at this time, you are only able to connect one Shopify store per app group. |
| Event property segmentation enabled | To ensure you can segment your Shopify events properties, you must work with your customer success manager or [Braze support]({{site.baseurl}}/braze_support/) to confirm that you have event property segmentation enabled for your dashboard. |
| Nested custom attribute support | This will be enabled with the Spotify integration.<br><br>You will be given access to this feature to receive Shopify marketing opt-in custom attributes. |
| User permissions | You have to be either a:<br>• Store owner<br> • Staff<br>• Member with all **General** and **Online Store** settings, as well as these additional admin permissions selected:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Manage settings<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• View apps developed by staff and collaborators<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Manage and install apps and channels |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

With Braze's turnkey Shopify integration, you can:
- Seamlessly connect your Shopify store within Braze
- Allow Braze to ingest and process Shopify user data
- Sync Shopify user profiles into Braze
- Collect email and SMS opt-ins from your Shopify store to sync to Braze

#### Web SDK integration via Shopify ScriptTag (optional)

Braze also allows you to embed our [Web SDK integration]({{site.baseurl}}/scripttag_web_sdk_integration/) via ScriptTag on to your Shopify store. This integration requires the above [prerequisites](#prerequisites), as well as the ones found on the [ScriptTag]({{site.baseurl}}/scripttag_web_sdk_integration/#prerequisites) integration page.

Embedding our Web SDK via ScriptTag supports tracking the following:
  - [Anonymous user tracking]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) to track guest activity in your store
  - [Monthly active user]({{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/#monthly-active-users) tracking as the Web SDK is capable of tracking session data from your store visitors
  - Option to collect Shopify on-site activity users which will count toward your [data point]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points) consumption
  - Option to enable [in-browser messaging]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) as a channel on your Shopify store
