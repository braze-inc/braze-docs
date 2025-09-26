---
nav_title: Data retention
article_title: Data Retention
alias: /data_retention/
description: "This reference article covers general Braze data retention information."
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Braze Data Retention Information

*Last revised on April 1, 2024*

> This article covers general Braze data retention information.<br><br>Data stored in Braze is retained and usable for segmentation, personalization, and targeting for the lifetime of the Customer's account. This means data such as user profile attributes, custom attributes, custom events, and purchases are stored indefinitely for active users unless removed by the Customer, for the duration of the contract.<br><br>Braze has features, processes, and APIs in place to automatically implement good data hygiene practices for compliance with GDPR and other best practices. These are described below.

## Data Retention Handled by Customers Through Braze's Dashboard or API

Braze enables its customers to delete entire User Profiles and Attribute data themselves from their workspace.

This means you can: 
- Delete user profiles using the Braze [Delete user API endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) 
- Delete (null) or amend attributes on user profiles using the Braze [Track user API endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Behavioral events cannot be deleted from a User Profile (custom events, sessions, campaigns, purchases). To remove those events, you must delete the entire User Profile.

For privacy compliance, you may need to delete all personal data pertaining to a User upon the User's request. You can find instructions on our [data protection technical assistance]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure) page.

{% alert note %}
A User may have multiple profiles, and you may need to delete multiple profiles to delete all data pertaining to a single User. Follow instructions on the data protection technical assistance page on how to fully delete all data regarding a User.
{% endalert %}

## Data Retention Handled by Braze for Specific Features of the Braze Services

#### Braze Database: Automatic Archiving/Deletion of Churned Users

Each week, Braze runs a process to remove Inactive and Dormant Users from the Braze Services. In general, these are users who are not reachable (for example, have no email address, no phone number, no push token, do not use your apps or visit your websites), have had no activity recorded on their user profile, and have not been messaged or engaged with using Braze. This is done to adhere to GDPR principles and best practices. You can read more about this process on our [user archival definitions]({{site.baseurl}}/user_archival/) page.

{% alert note %} 
Customers have full control over whether or not a user is Inactive or Dormant and can prevent archiving of user profiles by recording a data point at regular intervals. Braze Canvas offers the ability to do this automatically, allowing you to effectively turn off this functionality for some or all of your Inactive or Dormant Users. 
{% endalert %}

#### Campaign and Canvas Interactions Data 

Messaging interaction data refers to how a user interacts with a campaign or Canvas they received (for example, when a user opens campaign A or a user receives variant A). This data is used for retargeting. You can read more about messaging interaction data availability on [About messaging interaction data availability]({{site.baseurl}}/messaging_interaction_data/).

## Data Retention Handled by Braze

The below retention policies pertain to Braze's compliance with GDPR and privacy regulations and are regarding transient data storage as it passes through our internal systems. These retention policies do not impact the Braze Services and are informational for your legal and privacy teams.

#### Braze Servers: Short-term Retention for Recovery Purposes

Data sent by Braze to certain subprocessors may still exist in Braze's internal systems for up to 90 days.

#### Braze Data Lake Data Retention

Data available to Customers within the Braze dashboard is mostly aggregated. Detailed logs are kept in a separate database created by Braze (the "Data Lake"). Data Lake data is used for aggregate reporting and other advanced functionality. Braze removes personally identifiable information from events data stored in the Data Lake after two years (see more information in our [Snowflake Data Retention]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention#snowflake-data-retention/) page).

If you use our APIs to delete user profiles or delete or amend attributes from user profiles, it may take up to three weeks for that data to be deleted from Braze's Data Lake. Deletion of data in the Data Lake will not affect segmentation or personalization but rather ensures the data is removed from all Braze systems.

#### Braze Backup Servers

When data is deleted from your production instance, the data remains in Braze's backup servers for six months and is then deleted according to our internal processes.
