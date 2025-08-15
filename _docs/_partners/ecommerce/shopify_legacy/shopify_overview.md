---
nav_title: Shopify overview (legacy)
article_title: "Shopify Overview (Legacy)"
description: "This reference article outlines the partnership with Braze and Shopify, a global commerce company that allows you to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze. Leverage Braze cross-channel strategies and Canvas to nudge customers to complete their purchases or retarget users based on their previous purchases."
page_type: partner
search_tag: Partner
alias: /shopify_overview_legacy/
page_order: 0
---

# Shopify overview (legacy)

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Shopify makes commerce better for everyone with a platform and services engineered for reliability while delivering a better shopping experience for consumers everywhere.

The Shopify and Braze integration allows you to connect your Shopify store to seamlessly pass your Shopify data into Braze. You can leverage cross-channel strategies and Canvas in Braze to engage new leads, message new customers, or retarget your users with abandoned checkout messaging to nudge them to complete their purchases.

{% multi_lang_include alerts/important_alerts.md alert='Shopify deprecation' %}

## Supported features

- Track onsite behavior and anonymous users via the Braze Web SDK
- Assist with syncing and reconciling Shopify customers in Braze via the Braze Web SDK
- Sync Shopify customer data
- Collect Shopify email and SMS subscriber opt-in subscription states
- Backfill historical Shopify purchase data 
- Shopify catalog sync 
- Use in-app messages as a channel 

## Supported use cases 

- Path-to-purchase campaigns and Canvas user journeys, including: 
  - Browse abandonment 
  - Abandoned cart 
  - Abandoned checkout 
- Post-purchase campaigns and Canvas user journeys, including:
  - Order confirmations 
  - Fulfillment updates 
  - Order cancellations 
  - Order refunds
- Product recommendations
- Cross-sell and upsells
- [Back-in-stock]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## Requirements

| Requirement | Description |
| --- | --- |
| Shopify store | You have an active [Shopify](https://www.shopify.com/) store.<br><br>You can connect one Shopify store per workspace. If you are interested in connecting multiple stores to one workspace, contact your customer success manager to join the Shopify Multiple Stores beta. |
| Shopify user permissions | You have one of the following permissions to your Shopify store:{::nomarkdown}<ul><li>Store owner</li><li>Staff</li><li>Member with all General and Online Store settings, as well as these additional admin permissions:<ul><li>Orders</li><li>View (located under <b>Products</b>)</li><li>Customers</li><li>Manage settings</li><li>View apps developed by staff and collaborators</li><li>Manage and install apps and channels</li></ul></li></ul>{:/} |
| Braze Web SDK Implementation | To track onsite behavior and anonymous users, you must implement the Braze Web SDK either through our default Shopify integration or manually. <br><br>For more information on your implementation options, see [Implementing the Web SDK on your Shopify site]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify). |
| Event property segmentation enabled | To confirm you can segment your Shopify events properties, work with your customer success manager or [Braze Support]({{site.baseurl}}/braze_support/) to confirm that event property segmentation is turned on for your Braze dashboard. |
{: .reset-td-br-1 .reset-td-br-2 }

## General Data Protection Regulation (GDPR)

Concerning personal data submitted to Braze services by or on behalf of its customers, Braze is the data processor, and our customers are the data controllers. Accordingly, Braze processes such personal data solely at the instruction of our customers and, when applicable, notifies our customers of data subject requests. As the data controllers, our customers respond directly to Data subject requests. As part of the Braze platform’s Shopify integration, Braze automatically receives [Shopify’s GDPR webhooks](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). However, Braze customers are ultimately responsible for responding to data subject requests from their Shopify customers through the use of [Braze SDKs]({{site.baseurl}}/developer_guide/home/) or [REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) in accordance with our [GDPR compliance]({{site.baseurl}}/dp-technical-assistance/) policies.
