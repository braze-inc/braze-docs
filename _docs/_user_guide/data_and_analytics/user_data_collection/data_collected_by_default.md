---
nav_title: Data Collected by Default
page_order: 1
description: "This reference article addresses the data that is collected by default from the Braze SDK."
---

# Data Collected by Default

The following events and attributes are captured and updated automatically by the Braze SDK as part of the Session Start and Session End data points, or by the Braze backend. You don't need to record them separately as Custom events or Custom attributes.

## Usage Information
- First Used App (Date)
- Last Used App (Date)
- Total Session Count (Integer)
- Number of Sessions in the Last Y Days (Integer and Date)
- Email Available (Boolean)
- News Feed View Count (Integer)

## Campaign Retargeting
- Last Received Any Campaign (Date)
- Last Received Email Campaign (Date)
- Last Received Push Campaign (Date)
- Last Viewed News Feed (Date)
- Clicked Card (Integer)
- Received Message from Campaign
  - This filter allows you to target users based on their having (not) received a previous campaign.
- Received Message from Campaign with Tag
  - This filter allows you to target users based on their having (not) received a campaign that currently has a tag.
- Retarget Campaign
  - This filter allows you to target users based on whether or not they have opened, or clicked on a specific email, push, or slide up in the past

## Device Information
- Location Available (Boolean)
- Most Recent Location (if location permission is granted to your app)
- Push Enabled (Boolean)
- Device Locale
- Language (taken from Device Locale)
- Country (first taken from IP Address. If this is not available, taken from Device Locale. 
- Most Recent App Version
- Device Model
- Device OS Version
- Device Resolution
- Device Wireless Carrier
- Device Time Zone
- Uninstalled (Date and Boolean)


{% alert important %}
Braze will ban or block users ("dummy users") with over 5 million sessions and no longer ingest their SDK events because they are usually the result of misintegration. If you find that this has happened for a legitimate user, please reach out to your Braze account manager. 
{% endalert %}
