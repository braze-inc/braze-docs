---
nav_title: Data Retention
alias: /data_retention/
description: "This reference article covers general Braze data retention information."
page_type: reference
page_order: 2.5
---

# Braze Data Retention Information

*Last revised in December 2020*

> This article covers general Braze data retention information.

## Data Retention Handled by Customers Through Braze’s Dashboard or API

Braze enables its customers to delete entire User Profiles and Attribute data themselves from their app group.

This means you can: 
- Delete user profiles using the Braze User Delete API Endpoint: 
[https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)
- Delete (null) or amend attributes on user profiles using the Braze User Track API Endpoint:
[https://www.braze.com/docs/api/endpoints/user_data/post_user_track/]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Behavioral events cannot be deleted from a User Profile (custom events, sessions, campaigns, purchases). In order to remove those events, you must delete the entire User Profile.

For privacy compliance, you may need to delete all personal data pertaining to a User upon the User’s request. You can find instructions on our [data protection technical assistance]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure) page.

{% alert note %}
A User may have multiple profiles, and you may need to delete multiple profiles to delete all data pertaining to a single User. Follow instructions on the data protection technical assistance page on how to fully delete all data regarding a User.
{% endalert %}

## Data Retention Handled by Braze

In some cases we store data for a predetermined period of time before it is automatically deleted. For each type of data, we set retention timeframes based on the reason for its collection.

{% alert important %} The time frames outlined in this section are not customizable. {% endalert %}

#### Braze Database: Automatic Archiving/Deletion of Churned Users

Each week, Braze runs a process to remove Inactive Users and Dormant Users from the Braze Services. You can read more about this process on our [user archival definitions]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/) page.

{% alert note %} While archival of Inactive or Dormant User profiles is automated and the data retention is not customizable, you can run a data point on such profiles to prevent archiving, thus keeping them active. {% endalert %}

#### Braze Servers: Short-term Retention for Recovery Purposes

Data sent from the Braze Services to the Data Lake via Braze servers is retained in such Braze servers for up to 90 days for recovery purposes.

#### Braze Data Lake Data Retention

Data available to you within the Braze dashboard is mostly aggregated. Detailed logs are kept in a separate database created by Braze (the “Data Lake”, also known as the “BI Database”).

Braze has instituted processes to enable a custom retention policy scheduled to clear events at an app group or event level. This automatic deletion process applies to:

- Events
- Purchases
- Campaign Engagement Events (e.g., sends, opens, clicks)
- Sessions data

Deletion of data in the Data Lake will not affect your segmentation.

#### Braze Backup Servers

When data is deleted from your production instance, the data remains in Braze’s backup servers for 6 months and is then deleted according to our internal processes.

## Data Retention Handled by Braze for Specific Features of the Braze Services
 
#### Campaign Interactions Data 
 
<br>**What is it?** Campaign Interactions are data related to end users’ interactions with a Campaign. They are used for retargeting filters and to determine Campaign re-eligibility.
 
**When is it deleted?** Braze automatically deletes the Campaign Interactions for Campaigns that have not sent any messages in 25 calendar months and are not used for retargeting in any Campaigns, Canvases, or Cards in an active status. 
 
**What happens after deletion?**
 - Campaigns with no Campaign Interactions cannot be used in retargeting filters for Campaigns, Canvases, and Segments.
 - Any active Campaign that has not sent any messages in 25 months, and is not being used for retargeting in any active Campaigns, Canvases, or Cards, will be stopped because Campaign eligibility resets. You may re-launch the Campaign after reviewing the re-eligibility setting.
 
**How to reset the clock to avoid deletion?** To retain Campaign Interactions for a particular Campaign, you can send a message using that Campaign at least once within the 25 months since the last message was sent or use that Campaign in a retargeting filter in any active Campaign, Canvas, or Card.
 
You can request a shorter data retention than 25 months via your CSM.

