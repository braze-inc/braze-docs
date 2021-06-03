---
nav_title: Export Campaign Results Data
page_order: 0

page_type: reference
description: "This reference article covers how to export campaign analytics."
tool: 
- Campaigns
- Reports
---

# Campaign Results Data

All of the analytics from your Braze campaigns can be exported to a CSV. From the Campaigns page of the Dashboard, select the campaign you wish to view and scroll down to the historical performance graphs, which can be exported.

## Multi-Channel Campaigns

For multichannel campaigns, the data that can be exported will depend on which messaging channels were used. Here's a list of all the data that can be exported from a campaign that used iOS push, Android push, email, and in-app messages:

- Messages Sent by Date
    - Total Messages Sent
    - Messages Sent Across Campaign's Channels (can include Push, Email and In-App Message)
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
- Windows Phone 8 Push Engagement by Date
    - Number of Windows Phone 8 Push Notifications Sent
    - Total Opens
    - Direct Opens
    - Bounces

## Multivariate Campaigns

For multivariate campaigns, which use just one messaging channel, you'll be able to export data that shows how each variant performed on the specific messaging channel's analytics over time. You can view this data grouped by statistic or grouped by message variant.

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

## Campaign Recipients

You can export user data for all the recipients of a campaign as a CSV file. To do so, click the __User Data__ button in the __Campaign Details__ block.

![Export icon][6]

The CSV output contains user profile data for every recipient of the campaign. Braze will generate the report in the background and email it to the user who is currently logged in.

If you have [linked your Amazon S3 credentials to Braze][26], then the CSV will also be uploaded in your S3 bucket. Otherwise, the link emailed to you will expire in a few hours.

The exported file includes the same user data fields which are included when you [export user data for a segment][40]. In addition to those data fields, if you choose "Export All Recipient Data," then the exported file will also contain the following data for each user:

- Name of campaign variation received
- API ID of campaign variation received
- Whether user is in control group

{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[6]: {% image_buster /assets/img/campaign_export_example.png %}
[26]: {{site.baseurl}}//partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration
[40]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
