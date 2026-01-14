---
nav_title: October
page_order: 3
noindex: true
page_type: update
description: "This article contains release notes for October 2016."
---

# October 2016

## New security settings
We've added enhanced security features to Braze, including password expiration rules, password length rules, password complexity rules, dashboard IP login allowlisting, and two-factor authentication.

> Update: Braze's **Security Settings**, accessed from your **Company Settings** page, also includes rules for password reusability and expiration.

## CSV download after import
Braze users can now download CSVs of recently imported users. This gives you more visibility in the data sync from your systems. Learn more on [CSV importing]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

## Anniversary filter
In addition to the [birthday filter]({{site.baseurl}}/user_guide/Engagement_Tools/Segments/Segmentation_Filters/), Braze now supports an anniversary filter which gives you the ability to target users based on a calendar date for loyalty milestones, refill notices, and more! Access this feature by selecting the "Date of Custom Attribute" filter on the Segments page. Learn more about [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Frequency capping updates
Previously, a campaign or Canvas that ignored the frequency capping restrictions would still count toward frequency caps. We've changed the behavior so that by default new campaigns and Canvases that do not obey frequency caps will also not count toward them. This is configurable for each campaign and Canvas. Learn more about [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping).

## In-app message color profiles
We've added [color profiles]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) for in-app messages, allowing customers to reuse on-brand color schemes when creating new messages in Braze.
