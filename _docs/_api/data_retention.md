---
nav_title: Data Retention
alias: /data_retention/
description: "This reference article covers general Braze data retention information."
page_type: reference
page_order: 2.5
---

# Braze Data Retention Information

(Last revised in December 2020)

## 1. Data retention handled by Customer through Braze’s Dashboard or API

Braze enables its customers to delete certain data themselves from their group app: entire User Profiles and Attributes. 

Customers can: 
- Delete user profiles using the Braze User Delete API Endpoint: 
[https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)
- Delete (null) or amend attributes on user profiles using the Braze User Track API Endpoint:
[https://www.braze.com/docs/api/endpoints/user_data/post_user_track/]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Behavioral events cannot be deleted from a User Profile (custom events, sessions, campaigns, purchases). In order to remove those events, the entire User Profile must be deleted.

For privacy compliance, customers may need to delete all personal data pertaining to a User upon the User’s request. Customers can find instructions on our data protection technical assistance page at:
[https://www.braze.com/docs/help/dp-technical-assistance/#the-right-to-erasure]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure) 

{% alert note %}
A User may have multiple profiles, and you may need to delete multiple profiles to delete all data pertaining to a single User. Follow instructions on the data protection technical assistance page on how to fully delete all data regarding a User.
{% endalert %}

## 2. Data retention handled by Braze

#### a) Braze database: automatic archiving/deletion of churned users - NOT CUSTOMIZABLE

Online documentation:
[https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_archival/]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/)

Note: While archival of Inactive or Dormant User profiles is automated and the data retention is not customizable, customers can prevent archiving by running a data point on such profiles, thus keeping them active.

#### b) Braze servers: short time retention for recovery purposes - NOT CUSTOMIZABLE

Data sent from the Braze Services to the Data Lake via Braze servers is retained in such Braze servers for up to 90 days for recovery purposes.

#### c) Braze Data Lake data retention - NOT CUSTOMIZABLE

Data available to Customers within the Braze dashboard is mostly aggregated. Detailed logs are kept in a separate database created by Braze (the “Data Lake”, fka “BI Database”).

Braze has instituted processes to enable a custom retention policy scheduled to clear events at an app group or event level. This automatic deletion process applies to: Events, Purchases, Campaign Engagement Events (e.g., sends, opens, clicks), and Sessions data. Deletion of data in the Data Lake will not affect Customer’s segmentation.

Customers may request such a custom retention policy be set up via a request to their CSM. 

#### d) Braze back-up servers - NOT CUSTOMIZABLE

When data is deleted from a Customer’s production instance, the data remains in Braze’s back-up servers for 6 months and is then deleted according to our internal processes.