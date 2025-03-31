---
nav_title: Tangerine
article_title: Tangerine
description: "This article outlines the partnership between Braze and Tangerine Store360, an omnichannel platform that connects physical stores with online stores to provide superior in-store experiences for consumers and store employees. Through this integration, Braze raw campaign and impression data are available on Store360 via Snowflake Secure Data Sharing, and brands can measure how their campaigns affect in-store engagement and store traffic."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine designs, builds, and operates an omnichannel platform called Store360. Store360 is an omnichannel enabler platform connecting physical stores with online stores to improve consumer and store employee in-store experience. Store360 tracks and analyzes physical store visit traffic, including retailers' mobile app users and their in-store engagement.

The Braze and Tangerine integration allows you to integrate raw campaign and impression data from Braze into Store360 through Snowflake Secure Data Sharing. Brands can now measure the impact of these campaigns on physical store visits and in-store engagement.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Store360 account | A Store360 account is required to take advantage of this partnership. |
| Braze account ID | Your Braze app group ID. |
| Matching user IDs | Your customer data in Store360 and Braze must have matching user IDs across the two platforms. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

### Analyze campaign impact on physical store visit

Brands use Braze to send campaign messages to consumers to increase store visits. During the campaign, Store360 captures mobile app user visits identified by user ID.

Using Store360 Insight analytic capability, brands can visualize campaign impact details from messages sent and read (data from Braze) to who and how many recipients visited physical stores (data from Store360).

## Integration

### Step 1: Enable Snowflake Secure Data Share

Work with your Braze team to enable and configure Snowflake Secure Data Share.

### Step 2: Configure Store360 to get Braze Data

Configure your Braze app group ID to your Store360 service account using the Store360 admin manager web console. This will request the Tangerine admin team to sync Braze data to Store360 using Snowflake Data Sharing.

### Step 3: Integrate Store360 SDKs to mobile app

To track and analyze mobile app user store visits and in-store activities along with Braze campaign and impression data, you must integrate the Store360 SDK in your mobile app using the steps provided in the Store360 SDK install documentation. This documentation will be provided to you after signing a client contract between Tangerine Store 360.

## Analyze Braze data in Store360

Take advantage of Snowflake secure data sharing to share your Braze raw campaign and impression data with Store360 Insight analytics, providing a full picture of users' lifecycle and activities from online to offline.

For reference, here are all the [Braze fields]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) available to be incorporated into Store360 analytics. The details of this step are very customer-specific and require special configurations. Talk to your Store360 account manager or support@tangerine.io to learn more.

## Important information and limitations

### Service Availability

Currently, the Store360 service is commercially available in Japan and Indonesia.

Tangerine is planning a Store360 product launch in the following countries in 2023.
- United States of America
- Thailand
- Singapore
- Vietnam
- Korea

### Data Retention

There is a two-year retention policy for your Braze data for Snowflake data sharing.

### Time lag in populating Braze event data

Braze events are processed with streaming technology and are available in near real-time. Generally, events are made available within 30 minutes of happening.
