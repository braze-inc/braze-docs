---
nav_title: "Shopify Historical Backfill"
permalink: "/shopify_historical_backfill/"
hidden: true
---

# Shopify Historical Backfill 

The Shopify Historical Backfill feature allows brands to sync over customers and purchase data in an automated and seamless way, so you can immediately start engaging with one of your most valuable segments – purchasers. As part of this backfill, Braze will import all customers, orders, and purchase events from the last 90 days prior to your Shopify integration connection.

This feature will import historical data and events that could result in users receiving unintended messages for any affected Campaigns/Canvases. Campaigns/Canvases using the following trigger events could be impacted if they are using any of the Shopify data this feature is syncing over:
- Change Custom Attribute Value
- Update Subscription Status 
- Add an Email Address
- Make Purchase*
- Perform Custom Event*

We recommend you audit your current active Campaigns/Canvases for any messages that may potentially trigger the above event using data from our Shopify Historical Backfill. 

*For "Make Purchase" and "Perform Custom Event", you can update the [Start Time duration]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/?redirected=true#step-4-assign-duration) to any date and time after your Shopify store was connected in Braze. Now any past events prior to this new Start Time will not trigger any messages. 

For all other events above, you can temporarily "Stop" them before activating the backfill to guarantee no messages get sent. Please note that when a campaign is stopped:
- Any messages scheduled to be sent while this campaign is stopped will be permanently canceled.
- If there is an A/B test and the initial test has already been sent, the A/B test will be permanently canceled. If the initial test hasn't been sent yet, the A/B test will resume with the campaign.
- Events for messages that have already been sent (e.g., opens, clicks) will still be tracked.
- You will be able to restart this campaign by clicking **Resume**.
- Once resumed, this campaign will resume sending messages, but any messages that were missed will not be re-sent or re-scheduled.

## Setting Up Shopify Historical Backfill

### Step 1: Start the Shopify backfill process

On the Shopify partner page, select "Start Data Backfill" to kickstart the process. For existing Shopify customers, you will need to "Reauthorize Access" in order for Braze to collect all past order events before you can "Start Data Backfill".

![][3]

### Step 2: Toggle on the backfill of Shopify Data

The Braze's setup wizard will pop up, and you have the option to optionally enable the "Backfill historical Shopify data". As part of this backfill, Braze will sync only the following Shopify data for the last 90 days prior to your Shopify integration by default:
- Order Created Event
- Braze Purchase Event
- Customer Data

To see what specific customer data is being backfilled, see [Supported Shopify Customer Data](https://docs.google.com/document/d/1TYubX19ypA21DTClKytUBYqzRLHWg6y5PQUC--wiHNc/edit#heading=h.gi1xg2ysvuaq). Once you hit **Next**, the backfill will activate and start syncing over past data.

![][1]

Note: Historical backfill can only be completed once, so you will not be able to run this import again once the data has finished syncing.
Note: This feature will count towards your data point usage. 

### Step 3: Backfill in progress

You will receive a Dashboard notification, and your "Status" on the page will display as "In Progress" to indicate the backfill has started. Please note the amount of time it takes for the backfill to finish will depend on how many customers and orders Braze will need to sync over from Shopify. During this time, you can leave this page and wait for a notification via the Dashboard and email to notify you of when the backfill is complete.

![][2]

### Step 4: Backfill completed
You will receive a Dashboard notification and an email once the Shopify backfill has been completed. The Shopify partner page will also update the "Status" under Historical Backfill to "Complete".

## Supported Shopify Customer Data

### Shopify custom attributes

| Attribute name | Descriptiopn |
| --- | --- |
| shopify_order_count | This custom attribute corresponds to the total orders this customer has completed in Shopify. This is only available for users that were backfilled as part of this process. |
| shopify_total_spent | This custom attribute corresponds to the total amount spent by this customer in Shopify. This is only available for users that were backfilled as part of this process. |
| shopify_tags | This attribute corresponds to the customer tags set by Shopify admins. |

### Shopify standard attributes
- Email
- First Name
- Last Name
- Phone
- City
- Country

[1]: {% image_buster /assets/img/Shopify/backfill1.png %} 
[2]: {% image_buster /assets/img/Shopify/backfill2.png %} 
[3]: {% image_buster /assets/img/Shopify/backfill3.png %} 