---
nav_title: October
page_order: 3
noindex: true
page_type: update
description: "This article contains release notes for October 2016."
---

# October 2016

## New Security Settings
We’ve added enhanced security features to Braze, including password expiration rules, password length rules, password complexity rules, Dashboard IP login whitelisting, and two-factor authentication.

> Update: Braze's security settings, accessed from your [company settings page](https://dashboard-01.braze.com/company_settings/company_settings), also includes rules for password reusability and expiration.

## CSV Download After Import
Braze users can now download CSVs of recently imported users. This gives you more visibilty in the data sync from your systems. Learn more on CSV importing on Braze [here]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/).

## Anniversary Filter
In addition to the [birthday filter]({{site.baseurl}}/user_guide/Engagement_Tools/Segments/Segmentation_Filters/), Braze now supports an anniversary filter which gives you the ability to target users based on a calendar date for loyalty milestones, refill notices, and more! Access this feature by selecting the "Date of Custom Attribute" filter on the Segments page. Learn more on filters in Braze [here]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Frequency Capping Updates
Previously, a campaign or Canvas that ignored the Frequency Capping restrictions would still count towards frequency caps. We’ve changed the behavior so that by default new campaigns and Canvases that do not obey Frequency Caps will also not count towards them. This is configurable for each campaign and Canvas. Learn more about Frequency Capping [here]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping).

## In-App Message Color Profiles
We’ve added Color Profiles for in-app messages, allowing customers to reuse on-brand color schemes when creating new messages in Braze. Learn about color profiles [here]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile).
