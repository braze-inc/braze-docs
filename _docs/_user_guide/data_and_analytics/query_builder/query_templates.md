---
nav_title: Query Templates
article_title: Query Builder Templates
page_order: 0
page_type: reference
toc_headers: h2
description: "This reference article lists the types of reports you can create using Braze data from Snowflake in the Query Builder."
tool: Reports
---

# Query Builder Templates

> Access [Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) templates by selecting **Query Template** when creating a report. All templates surface data from the last 60 days. 

## Campaign templates

### Campaign revenue by country

This report provides revenue per country for a specific campaign. To run this report, you'll need to specify the API identifier for a campaign. You can find a campaign's API identifier at the bottom of that campaign's details page.

For each country, you'll see the amount of revenue generated, number of orders, number of returns, net revenue, and gross revenue.

#### Metrics

- *Orders:* Number of purchase events
- *Returns:* Number of purchase events with negative revenue values
- *Net revenue:* Revenue of all non-returns 
- *Gross revenue:* Revenue that includes the value of returns

![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"}

## Canvas templates

### Canvas revenue by country

This report provides revenue per country for a specific Canvas. To run this report, you'll need to specify the API identifier for a Canvas. You can find the Canvas API identifier under **Analyze Variants**.

For each country, you'll see the amount of revenue generated, number of orders, number of returns, net revenue, and gross revenue.

#### Metrics

- *Orders:* Number of purchase events
- *Returns:* Number of purchase events with negative revenue values
- *Net revenue:* Revenue of all non-returns 
- *Gross revenue:* Revenue that includes the value of returns

![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"}

## Email templates

### Email bounces per domain

The number of bounces per email domain.

![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:50%;"}

### Email delivery metrics by day

This report provides metrics for the messages sent on particular days, such as how many emails were sent, delivered, soft bounced, and hard bounced. 

All metrics are unique over the entirety of the reporting period. For example, if a welcome email soft bounced one time on Nov 21, two times on Nov 22, and was never delivered:
- The *Soft Bounces* metric for Nov 21 increases by one.
- The *Soft Bounces* metric for Nov 22 is not affected.

![]({% image_buster /assets/img_archive/email_delivery_day.png %})

### Email engagement metrics by segment

This report provides metrics for the messages sent to each specific segment, such as how many emails were sent, delivered, soft bounced, and hard bounced. 

All metrics are unique over the entirety of the reporting period. For example, if a welcome email soft bounced one time on Nov 21, two times on Nov 22, and was never delivered:
- The *Soft Bounces* metric for Nov 21 increases by one.
- The *Soft Bounces* metric for Nov 22 is not affected.

![]({% image_buster /assets/img_archive/email_engagement_segment.png %})

### Email engagement metrics for variants or steps, by segment

Each row of this report contains metrics about the messages sent for variants or Canvas steps within a specific segment. These metrics include how many emails were sent, delivered, soft bounced, and hard bounced. 

All metrics are unique over the entirety of the reporting period. For example, if a welcome email soft bounced one time on Nov 21, two times on Nov 22, and was never delivered:
- The *Soft Bounces* metric for Nov 21 increases by one.
- The *Soft Bounces* metric for Nov 22 is not affected.

### Email performance by country

For each country, you'll see the following metrics: sends, indirect open rate, and direct open rate. Country is the country of the user at the time of push send.

![]({% image_buster /assets/img_archive/query_builder_q3.png %})

### Email Subscription Change Logs

For each user, you'll see the metrics that were logged about their subscription change, such as their email address, subscription status, the time their status was changed, and the associated Canvas or campaign.

### Email subscription group opt-ins and opt-outs

For each week, you'll see the number of unique user opt-ins and opt-outs of any email subscription groups.

![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"}

### Email URLs clicked

This report shows the number of clicks each link in an email had. To run this report, you'll need to specify the API identifier for a campaign or Canvas. You can find a campaign's API identifier at the bottom of that campaign's details page, and you can find the Canvas API identifier under **Analyze Variants**. 

For each de-personalized link, you'll see a count of clicks. Your CSV download will include the user IDs of all users that clicked, the link they clicked on, and a timestamp of when they clicked.

#### Metrics

*De-personalized URLs:* URLs that are stripped of Liquid tags.

![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"}

### Top/bottom messaging for email engagement

This report shows email engagment metrics for the top or bottom campaigns, Canvases, or Canvas steps. Each row is a campaign, Canvas, or Canvas step. You must specify whether to display the top or bottom performers, and the specific metric to run this analysis for (such as *Sent*, *Soft Bounces*, and *Unique Opens*).

The rows in top performer reports will be ordered from best to worst, while the rows in bottom performer reports will be ordered from worst to best.

![]({% image_buster /assets/img_archive/top-bottom-email.png %})

## Mobile templates

### Device carriers

The number of users per device carrier, such as Verizon and T-Mobile.

![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:40%;"}

### Device models

The number of users per device model, such as iPhone 15 Pro and Pixel 7.

![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:40%;"}

### Device operating systems

The number of users per operating system, such as 17.4 and Android 14.

![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:40%;"}

### Device screen resolutions

The number of users per device screen resolution, such as 1179x2556 and 750x1334.

![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"}

### SMS Error Codes

For each SMS error code, you'll see the error type and number of errors.

![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"}

### SMS Provide Errors by User

This report provides SMS error codes for a specific user.

## Push templates

### Push performance by country

For each country, you'll see the following metrics: deliveries, open rate, and click rate. Country is the country of the user at the time of email send.

![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"}

## Channel templates

### Channel engagement and revenue

For each channel, you'll see all engagement metrics for that channel (such as opens and clicks), revenue, number of transactions, and average price.

#### Metrics

- *Transactions:* Number of purchase events
- *Average price:* Revenue divided by transactions

![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %})

### Purchases and revenue by segment

Each row of this report contains metrics about the messages sent for a specific segment.

Purchase metrics are unique over the entirety of the reporting period. One user can generate at most one purchase. Revenue takes into account every purchase from the reporting period.

### Purchases and revenue for variants or steps, by segment

Each row of this report contains metrics about the messages sent for variants or Canvas steps within a specific segment.

Purchase metrics are unique over the entirety of the reporting period. One user can generate at most one purchase. Revenue takes into account every purchase from the reporting period.

### Top/bottom messaging for purchases

This report shows purchase metrics for the top or bottom campaigns, Canvases, or Canvas steps. Each row is a campaign, Canvas, or Canvas step. You must specify whether to display the top or bottom performers, and the specific metric to run this analysis for (such as *Unique purchases upon receipt*, *Revenue upon receipt*, *Unique recipients*).

The rows in top performer reports will be ordered from best to worst, while the rows in bottom performer reports will be ordered from worst to best.