---
nav_title: Data Retention
article_title: Data Retention
alias: /data_retention/
description: "This reference article covers general Braze data retention information."
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Braze data retention information

*Last revised in October 2021*

> This article covers general Braze data retention information.

## Data retention handled by customers through braze’s dashboard or api

Braze enables its customers to delete entire User Profiles and Attribute data themselves from their app group.

This means you can: 
- Delete user profiles using the Braze [User Delete API Endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) 
- Delete (null) or amend attributes on user profiles using the Braze [User Track API Endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Behavioral events cannot be deleted from a User Profile (custom events, sessions, campaigns, purchases). In order to remove those events, you must delete the entire User Profile.

For privacy compliance, you may need to delete all personal data pertaining to a User upon the User’s request. You can find instructions on our [data protection technical assistance]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure) page.

{% alert note %}
A User may have multiple profiles, and you may need to delete multiple profiles to delete all data pertaining to a single User. Follow instructions on the data protection technical assistance page on how to fully delete all data regarding a User.
{% endalert %}

## Data retention handled by braze

In some cases we store certain data only for a predetermined period of time before it is automatically deleted based on certain criteria. For each type of data, we set retention timeframes outlined below.

{% alert important %} The timeframes outlined in this section are not customizable. {% endalert %}

#### Braze database: automatic archiving/deletion of churned users

Each week, Braze runs a process to remove Inactive Users and Dormant Users from the Braze Services. You can read more about this process on our [user archival definitions]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/) page.

{% alert note %} While archival of Inactive or Dormant User profiles is automated and the data retention is not customizable, you can run a data point on such profiles at regular intervals to prevent archiving, thus keeping them active. {% endalert %}

#### Braze servers: short-term retention for recovery purposes

Data sent from the Braze Services to Braze's Snowflake Data Lake via Braze servers is retained in such Braze servers for up to 90 days for recovery purposes.

#### Braze data lake data retention

Data available to Customers within the Braze dashboard is mostly aggregated. Detailed logs are kept in a separate database created by Braze (the “Data Lake”, formerly known as “BI Database”).

Braze has instituted processes to ensure regularly scheduled deletions of PII from the “Data Lake” at an app group or event level. If you use our APIs to delete user profiles, or delete or amend attributes from user profiles, within two weeks this automatic deletion process will apply to:

- Events
- Purchases
- Campaign Engagement Events (e.g., sends, opens, clicks)
- Sessions data

Deletion of data in the Data Lake will not affect your segmentation.

#### Braze backup servers

When data is deleted from your production instance, the data remains in Braze’s backup servers for 6 months and is then deleted according to our internal processes.

## Data retention handled by braze for specific features of the braze services
 
#### Campaign interactions data 
 
<br>**What is it?** Campaign Interactions are data related to End Users’ interactions with a campaign. They are used for retargeting filters and to determine campaign re-eligibility.
 
**When is it deleted?** Braze automatically deletes from the Customer's App Groups the Campaign Interactions for campaigns that have not sent any messages in 25 calendar months and are not used for retargeting in any campaigns, Canvases, or Content Cards in an active status.
 
**What happens after deletion?**
 - Campaigns with no Campaign Interactions cannot be used in retargeting filters for campaigns, Canvases, and Segments.
 - Any active campaign that has not sent any messages in 25 months, and is not being used for retargeting in any active campaigns, Canvases, or Cards, will be stopped because campaign eligibility resets. You can re-launch the campaign after reviewing the re-eligibility setting.
 
**How to reset the clock to avoid deletion?** To retain Campaign Interactions for a particular campaign, you can send a message using that campaign at least once within the 25 months since the last message was sent or use that campaign in a retargeting filter in any active campaign, Canvas, or Card.
 
You can request a shorter data retention than 25 months via your CSM.

