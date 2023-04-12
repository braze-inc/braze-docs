---
nav_title: Tangerine
article_title: Tangerine
page_order: 1

description: "This article outlines the partnership between Braze and Tangerine Store360, Omnichannel platform that connects physical stores with online stores to provide superior  in-store experiences for both consumers and store employees. Through this integration, Braze raw campaign and impression data is available on Store360 via Snowflake Secure Data Sharing, and brands can measure how their campaigns affect in-store engagement and store traffic."
alias: /partners/tangerine/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# Tangerine Store360

> Tangerine designs, builds and operates Omnichannel platform called Store360.
Store360 is an Omnichannel Enabler Platform connecting Physical Store with Online Store to improve both Consumer and Store Employee In-Store Experience.
Store360 tracks and analyzes store visits traffic including retailers mobile app users.

Store360 tracks and analyzes physical store visit traffic including retailers' mobile app users and their in-store engagement.
By integrating the raw campaign and impression data from Braze into Store360 through Snowflake Secure Data Sharing, brands can now measure impact of these campaigns to physical store visits and in-store engagement.


## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Store360 Account | A Store360 account is required to take advantage of this partnership. |
| Braze account ID | Your Braze App Group ID |
| Matching User IDs | Your customer data in Store360 and Braze must have matching user IDs across the two platforms. |

## Use cases

### Analyze Campaign Impact to Physical Store Visit
Brands use Braze to send campaign messages to consumers to increase store visits. During the campaign, Store360 captures mobile app user visits identified by user ID.
Using Store360 Insight analytic capability, brands can visualize campaign impact details from messages sent/read (data from Braze) to who/how many recipients visited physical stores (data from Store360).

## Integration

### Step 1: Create Store360 Service Account

In order to take advantage of this partnership, you need to create a Store360 Service Account. Please contact Store360 Account Manager.

### Step 2: Enable Snowflake Secure Data Share

Work with your Braze team to enable and configure Snowflake Secure Data Share.

### Step 3: Configure Store360 to get Braze Data

Configure your Braze App Group ID to your Store360 Service Account using Store360 Admin Manager Web Console.
This will request Tangerine Admin Team to sync Braze Data to Store360 via Snowflake Data Sharing.

### Step 4: Integrate Store360 SDKs to Mobile App

To track and analyze mobile app user store visit and in-store activities along with Braze campaign and impression data, you need to integrate the Store360 SDK in your mobile app using the steps provided in the Store360 SDK Install documentation.

## Customization

Customization is an **optional** section. Here, you could outline specific ways to customize your integration between the two partners.

## Analyze Braze data in Store360

Take advantage of Snowflake secure data sharing to share your Braze raw campaign and impression data with Store360 Insight analytics, providing you a full picture of users’ lifecycle and activities from online to offline.

For reference, here are all the Braze fields which are available to be incorporated into Store360 analytics. The details of this step are very customer-specific and require special configurations. Talk to your Store360 account manager or support@tangerine.io to learn more.

## Important information and limitations

### Service Availability

Currently Store360 Service is commercially available in Japan and Indonesia.
Tangerine is planning Store360 product launch in the following countries in 2023.
- United States of America
- Thailand
- Singapore
- Vietnam
- Korea

### Data Retention

There is a two year retention policy of your Braze data for Snowflake data sharing.

### Time Lag in Populating Braze Event Data

Braze events are processed with streaming technology and are available in near real time. Generally, events are made available within 30 minutes of happening with it often times being much quicker than this.
