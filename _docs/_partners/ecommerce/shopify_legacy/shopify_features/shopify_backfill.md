---
nav_title: "Shopify Historical Backfill"
article_title: "Shopify Historical Backfill"
alias: "/shopify_historical_backfill_legacy/"
description: "This reference article outlines how to set up Shopify historical backfill, including risks and supported data."
page_type: partner
search_tag: Partner
page_order: 1
---

# Shopify Historical Backfill 

> The Shopify Historical Backfill feature allows brands to sync over customers and purchase data in an automated and seamless way, so you can immediately start engaging with one of your most valuable segments – purchasers. 

{% multi_lang_include alerts/important_alerts.md alert='Shopify deprecation' %}

As part of this backfill, Braze will import all customers, orders, and purchase events from the last 90 days prior to your Shopify integration connection. Note that this feature is ideal for newer customers that don't have any active messages running, given the implications explained in the next section. This feature will log data points.

## Risks

This feature will import historical data and events that could result in unintended consequences such as users receiving irrelevant and untimely messages for any affected campaigns or Canvases. Campaigns and Canvases using the following trigger events could be impacted if they are using any of the Shopify data this feature is syncing over:
- Change Custom Attribute Value
- Perform Conversion Event
- Perform Exception Event for Campaign
- Update Subscription Status
- Update Subscription Group Status
- Add an Email Address
- Make Purchase*
- Perform Custom Event*

{% alert important %}
We recommend you audit your current active campaigns and Canvases for messages that may trigger the above events using data from our Shopify Historical Backfill. 

- For "Make Purchase" and "Perform Custom Event", you can update the [start time duration]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration) to any date and time after your Shopify store was connected in Braze. Any past events before this new start time will not trigger any messages. 
- For all other events above, you can [temporarily stop]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign) them before activating the backfill to guarantee no messages get sent. 
{% endalert %}

## Setting up Shopify Historical Backfill

### Prerequisites

The following events need to be enabled before turning on the backfill or their data won't be imported:

- `shopify_created_order`
- Braze Purchase Event 

The above events can be enabled while setting up Shopify during [event selection]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection).

{% alert important %}
You can activate the Backfill feature only once in your integration. 
{% endalert %}

### Step 1: Start the Shopify backfill process

On the Shopify partner page, select **Start Data Backfill**. For existing Shopify customers, you will need to reauthorize access for Braze to collect all past order events before you can start data backfill.

![]({% image_buster /assets/img/Shopify/backfill3.png %}){: style="max-width:75%;"}

### Step 2: Toggle on the backfill of Shopify data

Next, the setup composer will pop up, and you can optionally enable the backfill of historical Shopify data. As part of this backfill, Braze will sync only the following Shopify data for the last 90 days prior to your Shopify integration by default:
- Order Created Event
- Braze Purchase Event
- Customer Data

To see what specific customer data is being backfilled, you can visit the [Supported Shopify customer data](#supported-shopify-customer-data) section.

{% alert note %}
This feature will only sync email and SMS subscription states for new users created during the backfill. This will not sync subscription states for existing users in Braze to avoid overriding your users' current statuses.<br><br>If you have feedback on the current behavior, submit it through the product portal, listed in the **Dashboard** under **Resources** as **Product Roadmap** (If you are using our [updated navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), select **Community** > **Product Roadmap**).
{% endalert %}

Once you hit **Next**, the backfill will activate and start syncing over past data. Note that Historical Backfill can only be completed **once**, so you will not be able to run this import again after the data has finished syncing.

![]({% image_buster /assets/img/Shopify/backfill1.jpg %}){: style="max-width:75%;"}

### Step 3: Backfill in progress

You will receive a dashboard notification, and your status will display as "In Progress" to indicate the backfill has started. Note that the time it takes for the backfill to finish will depend on how many customers and orders Braze will need to sync over from Shopify. During this time, you can leave this page and wait for a dashboard notification or email to notify you of when the backfill is complete.

![]({% image_buster /assets/img/Shopify/backfill2.png %}){: style="max-width:75%;"}

### Step 4: Backfill completed
You will receive a dashboard notification and an email after the Shopify backfill has been completed. The Shopify partner page will also update the status under Historical Backfill to "Complete".

## Supported Shopify customer data

### Shopify custom attributes

| Attribute name | Description |
| --- | --- |
| `shopify_order_count` | This custom attribute corresponds to the total orders this customer has completed in Shopify. This is only available for users that were backfilled as part of this process. |
| `shopify_total_spent` | This custom attribute corresponds to the total amount spent by this customer in Shopify. This is only available for users that were backfilled as part of this process. |
| `shopify_tags` | This attribute corresponds to the [customer tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) set by Shopify admins. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Shopify standard attributes
- Email
- First Name
- Last Name
- Phone
- City
- Country

