---
nav_title: July
page_order: 6

page_type: update
description: "This article contains release notes for July 2016."
---

# July 2016

## Filtering the Developer Console’s error log by error type
This upgrade makes it easier for you to use the Message Error Log on the Developer Console to troubleshoot issues with their Braze integrations. This is a usability update allows you to filter the Message Error Log by type and makes it much easier to find and identify specific integration problems.

## Added Timestamp for Last Uninstall Tracking Push Sent
Braze detects uninstalls by sending a silent push to a customer’s apps to see which devices respond. This feature adds an unobtrusive timestamp indicating when uninstall tracking last ran. This timestamp can be found on your Settings page where uninstall tracking is configured. Learn more about Uninstall Tracking [here]({{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking).

![uninstall tracking checkbox][6]

## Added Webhook Testing Enhancements
You can now test-send a live webhook message from Braze prior to setting a Campaign to go live. Sending a test message will allow you to verify your messages and server endpoints have been configured properly in a safe sandbox environment. Learn more about webhooks [here]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook).

## Added Message Variation Received To Campaign Recipients CSV Export
We've added a column indicating the message variation received to the Campaign Recipients CSV export. Learn more about exporting data from Braze [here]({{site.baseurl}}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-dashboard-data).

## Approximate Limit on Number of Impressions
Once an In-App Message has received a certain number of impressions, Braze will stop allowing users to become eligible to receive the message. Learn more about setting approximate limits on impressions [here]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap).

![IAM impression cap][11]

[6]: {% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %}
[11]: {% image_buster /assets/img_archive/approx_limit_for_IAM.png %}
