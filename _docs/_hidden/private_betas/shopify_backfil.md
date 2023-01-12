---
nav_title: "Shopify Historical Backfill"
permalink: "/shopify_historical_backfill/"
hidden: true
---

# Shopify Historical Backfill 

The Shopify Historical Backfill feature allows brands to sync over customers and purchase data in an automated and seamless way, so you can immediately start engaging with one of your most valuable segments – purchasers. As part of this backfill, Braze will import all customers, orders, and purchase events from the last 90 days prior to your Shopify integration connection. Note that this feature will count towards your data point usage. 

## Considerations

This feature will import historical data and events that could result in users receiving unintended messages for any affected campaigns or Canvases. Campaigns and Canvases using the following trigger events could be impacted if they are using any of the Shopify data this feature is syncing over:
- Change Custom Attribute Value
- Update Subscription Status 
- Add an Email Address
- Make Purchase*
- Perform Custom Event*

{% alert tip %}
We recommend you audit your current active campaigns and Canvases for messages that may trigger the above events using data from our Shopify Historical Backfill. 

- For "Make Purchase" and "Perform Custom Event", you can update the [start time duration]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/?redirected=true#step-4-assign-duration) to any date and time after your Shopify store was connected in Braze. Any past events before this new start time will not trigger any messages. 
- For all other events above, you can [temporarily stop]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign) them before activating the backfill to guarantee no messages get sent. 

{% endalert %}

## Setting up Shopify Historical Backfill

### Step 1: Start the Shopify backfill process

On the Shopify partner page, select **Start Data Backfill**. For existing Shopify customers, you will need to reauthorize access for Braze to collect all past order events before you can start data backfill.

![][3]{: style="max-width:75%;"}

### Step 2: Toggle on the backfill of Shopify data

Next, the setup wizard will pop up, and you can optionally enable the backfill of historical Shopify data. As part of this backfill, Braze will sync only the following Shopify data for the last 90 days prior to your Shopify integration by default:
- Order Created Event
- Braze Purchase Event
- Customer Data

To see what specific customer data is being backfilled, you can visit the [Supported Shopify customer data](#supported-shopify-customer-data) section. Once you hit **Next**, the backfill will activate and start syncing over past data.

![][1]{: style="max-width:75%;"}

{% alert note %}
Historical backfill can only be completed once, so you will not be able to run this import again once the data has finished syncing.
{% endalert %}

### Step 3: Backfill in progress

You will receive a dashboard notification, and your status will display as "In Progress" to indicate the backfill has started. Note that the time it takes for the backfill to finish will depend on how many customers and orders Braze will need to sync over from Shopify. During this time, you can leave this page and wait for a dashboard notification or email to notify you of when the backfill is complete.

![][2]{: style="max-width:75%;"}

### Step 4: Backfill completed
You will receive a dashboard notification and an email once the Shopify backfill has been completed. The Shopify partner page will also update the status under Historical Backfill to "Complete".

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

[1]: {% image_buster /assets/img/Shopify/backfill1.jpg %} 
[2]: {% image_buster /assets/img/Shopify/backfill2.png %} 
[3]: {% image_buster /assets/img/Shopify/backfill3.png %} 