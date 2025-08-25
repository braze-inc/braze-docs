---
nav_title: Export campaign data
article_title: Export Campaign Data
page_order: 0
page_type: reference
description: "This reference article covers how to export campaign results data from single, multi-channel, or multivariate campaigns. The article also lists how to export user data from the recipients."
tool: 
  - Campaigns
  - Reports
  
---

# Export campaign data

> From the **Campaigns** page of the dashboard, select the campaign you want to view and scroll down to the historical performance graphs, which can be exported.<br><br>This page covers how to export campaign results data from single, multi-channel, and multivariate campaigns, and how to export user data from the recipients.

## Multichannel campaigns

For multichannel campaigns, the data that can be exported depends on which messaging channels you used. Here's a list of all the data that can be exported from a campaign that used iOS push, Android push, email, and in-app messages:

- Messages Sent by Date
    - Total Messages Sent
    - Messages Sent Across Campaign's Channels (can include push, email, and in-app message)
- Email Message Engagement by Date
    - Number of Emails Delivered
    - Number of Emails Sent
    - Number of Emails Opened
    - Number of Email Clicks
    - Number of Email Bounces
    - Number of Emails Reported as Spam
- In-App Message Engagement by Date
    - Number of In-App Messages Sent
    - In-App Message Impressions
    - Number of In-App Message Clicks
- iOS Push Engagement by Date
    - Number of iOS Push Notifications Sent
    - Total Opens
    - Direct Opens
    - Bounces
- Android Push Engagement by Date
    - Number of Android Push Notifications Sent
    - Total Opens
    - Direct Opens
    - Bounces

## Multivariate campaigns

For multivariate campaigns, which use just one messaging channel, you can export data that shows how each variant performed on the specific messaging channel's analytics over time. You can view this data grouped by statistic or grouped by message variant.

Push campaign results contain graphs for the following analytics:

- Messages Sent by Date for Each Variant
- Conversions by Date for Each Variant
- Unique Recipients by Date for Each Variant
- Opens by Date for Each Variant
- Direct Opens by Date for Each Variant
- Bounces by Date for Each Variant

Email campaign results contain graphs for the following analytics:

- Number Delivered by Date for Each Variant
- Number Sent by Date for Each Variant
- Opens by Date for Each Variant
- Clicks by Date for Each Variant
- Bounces by Date for Each Variant
- Spam Reports by Date for Each Variant

In-app message campaign results contain graphs for the following analytics:

- Sent by Date for Each Variant
- Impressions by Date for Each Variant
- Clicks by Date for Each Variant

## Campaign recipients

You can export user data for all the recipients of a campaign as a CSV file. To do so, select the **User Data** button in the **Campaign Details** section.

{% alert note %}
Can't see the **User Data** button? To export user data, you need the **Export User Data** [permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) for that workspace.
{% endalert %}

![User Data dropdown on the Campaign Details page]({% image_buster /assets/img/campaign_export_example.png %})

The CSV output contains user profile data for every recipient of the campaign. Braze will generate the report in the background and email it to the user who is currently logged in.

If you've linked your [Amazon S3 credentials]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) to Braze, then the CSV will also be uploaded in your S3 bucket. Otherwise, the link emailed to you will expire in a few hours.

The exported file includes the same user data fields that are included when you [export user data for a segment]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data). In addition to those data fields, if you choose "Export All Recipient Data," then the exported file will also contain the following data for each user:

- Name of campaign variation received
- API ID of campaign variation received
- Whether user is in control group

{% alert tip %}
For help with CSV and API exports, check out [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

