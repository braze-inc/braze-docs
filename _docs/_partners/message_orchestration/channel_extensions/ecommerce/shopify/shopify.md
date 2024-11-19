---
nav_title: Shopify Overview
article_title: "Shopify Overview"
description: "This reference article outlines the partnership with Braze and Shopify, a global commerce company that allows you to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze. Leverage Braze cross-channel strategies and Canvas to nudge customers to complete their purchases or retarget users based on their previous purchases."
page_type: partner
search_tag: Partner
permalink: "/shopify_integration_overview/"
page_order: 0
hidden: true
---

# Shopify overview

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a business of any size. Shopify makes commerce better for everyone with a platform and services engineered for reliability while delivering a better shopping experience for consumers everywhere.

The standard Braze integration with Shopify provides a powerful solution for ecommerce businesses looking to enhance their customer engagement and drive personalized marketing efforts. This integration seamlessly connects Shopify's robust ecommerce capabilities with our advanced customer engagement platform, enabling you to deliver targeted, relevant, and timely messages to your users based on real-time shopping behaviors and transactional data.

**Supported features**
- Track onsite behavior and anonymous users using the Braze Web SDK and JavaScript SDK
- Sync and reconcile Shopify user data in Braze
- Collect email and SMS subscribers from Shopify
- Backfill historical purchase data from Shopify
- Sync your Shopify product catalog

## Requirements

| Requirement | Description |
| --- | --- |
| Shopify store | You have an active Shopify store. <br><br> This beta only supports a single store per workspace. |
| Shopify store owner or staff member permissions | {::nomarkdown}<ul><li>Access to all General and Online Store settings.</li><li> Additional Admin Permissions:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2}

## How the integration works

After you set up the integration, Braze will automatically download historical data from your Shopify store, capturing all relevant information up to that point. Following the initial data sync, Braze will continuously track new data and updates, directly from Shopify and Braze SDKs.

### Initial data sync

After you implement the Shopify integration, Braze will automatically backfill your Shopify customers, orders, and products based on your configuration settings.
- Braze will import all customers and order placed events from the last 90 days prior to your Shopify integration connection.
- The Shopify customer ID will be set as the Braze `external_id`. 
- To see what specific customer data is being backfilled, refer to [Shopify features]({{site.baseurl}}/shopify_features/#shopify-data).

{% alert note %}
Note the following:
- If you’re an existing Braze customer with active campaigns or Canvases, review [Shopify historical backfill]({{site.baseurl}}/shopify_features#historical-backfill) for important information.
- Website visits (sessions) count towards your Monthly Active User (MAU) allotments. 
{% endalert %}

### User and data syncing

After the integration is live, Braze will gather user data from two key sources through the Shopify integration:
- **Braze Web SDK and JavaScript SDK:** For general on-site tracking, identity management, and native messaging channels
- **Shopify Web Pixel API and Webhooks:** For eCommerce activity

During integration onboarding, you will need to select when the Braze Web SDK and JavaScript SDK initialize and load onto a Shopify site: 
- Upon site visit (such as session start)
    - **What it does:** Anonymous user tracking for access to more data for deeper personalization 
- Upon account signup (such as account login) 
    - **What it does:** Prevents anonymous user tracking for a more conservative, privacy-oriented approach, so user activity is tracked *after* the user signs into their account

{% alert note %}
Note the following:
- If you’re a Shopify headless customer or require more advanced initialization capabilities, you must implement the Braze Web SDK and JavaScript SDK directly onto your Shopify website.
- Website visits (sessions) count towards your Monthly Active User (MAU) allotments.
{% endalert %}

The Braze SDKs are designed to elevate your customer engagement by:
- Automatically collecting session and device data
- Capturing marketing engagement and custom business data
- Unlocking access native messaging channels

{% alert note %}
Messaging channels aren’t included in the default integration at this time. You must work with your development teams to implement and test each messaging channel for proper functionality.
{% endalert %}

Through the Shopify integration, the Braze SDKs will be able to streamline identity management:

| Shopify identifier | In Braze |
| --- | --- |
| Client ID | Device ID |
| Customer ID | External ID |
| Cart token | Added as an alias to attribute cart events |
| Checkout token | Added as an alias to attribute Shopify checkout events |
{: .reset-td-br-1 .reset-td-br-2 }

{% alert note %}
If you’re integrating the SDKs directly, you must manually implement and test the setup for proper functionality.
{% endalert %}

The integration requires Braze SDKs and Shopify services to work together to appropriately track and attribute Shopify data to the right users in near-real time. To find more details on the data tracked through the integration, see [Shopify data]({{site.baseurl}}/shopify_features#shopify-data).

## How to integrate

The [standard integration]({{site.baseurl}}/shopify_standard_integration/) is tailored for Shopify online stores, providing a seamless and straightforward setup process. This option allows you to quickly connect your Shopify store to Braze, enabling you to leverage powerful customer engagement tools without extensive technical expertise. With this integration option, you can easily sync customer data, automate personalized messaging, and enhance your marketing efforts through comprehensive Braze features.

## General Data Protection Regulation (GDPR)

Concerning personal data submitted to Braze services by or on behalf of its customers, Braze is the data processor, and our customers are the data controllers. Accordingly, Braze processes such personal data solely at the instruction of our customers and, when applicable, notifies our customers of data subject requests. As the data controllers, our customers respond directly to Data subject requests. As part of the Braze platform’s Shopify integration, Braze automatically receives [Shopify’s GDPR webhooks](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). However, Braze customers are ultimately responsible for responding to data subject requests from their Shopify customers through the use of [Braze SDKs]({{site.baseurl}}/developer_guide/home/) or [REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) in accordance with our [GDPR compliance policies]({{site.baseurl}}/help/dp-technical-assistance/).

## Considerations

### In-app messages

In-app messages are currently not supported through the standard integration at this time. If you wish to see this supported in the future, submit a product request through the [Product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/). 

### Web Push

Shopify doesn’t support service workers because they can’t be installed in the root folder, which is necessary to enable web push notifications. As a result, web push notifications aren’t supported by default for this integration. However, you can still use service workers by registering them on the app proxy sub-path instead of the root directory.

### Content Cards

Content Cards are currently not supported through the standard integration at this time. If you wish to integrate this channel, refer to [Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/). 

### Feature flags 

Feature flags are currently not supported through the standard integration at this time. If you wish to integrate this channel, refer to [Feature Flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/). 
