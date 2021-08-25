---
nav_title: Active In-App Message Campaign Limits
article_title: Active In-App Messaging Campaign limits
page_order: 5
page_type: reference
description: "This reference goes over the limits surrounding the number of active in-app message campaign you may have at once."
tool: Campaigns
channel: in-app messages

---

> TO BE MERGED WITH 'CREATING A CAMPAIGN'

# Active In-App Message Campaign Limits

Braze values reliability and speed. Just like we suggest you send only the data you need to Braze, we also recommend __turning off__ any campaigns that are no longer adding any value to your brand.

Processing action-based in-app message campaigns that are still in an active state but no longer sending messages or are no longer needed slows down the overall performance of the Braze services for you and other customers. This extra time needed to process these large numbers of idle campaigns means that any in-app messages will take longer to appear on the end-users’ devices, which impacts the end user’s experience.

We have implemented a limit of **200 active, action-based in-app message campaigns per app group** to optimize the speed of message delivery and to prevent timeouts.

The 200 count includes active IAM campaigns that have not yet reached end time and those that have no end time. Active IAM campaigns that have passed their end times will not be counted.

The average Braze customer has a total of 26 campaigns active at once - so it is unlikely that this limitation will impact you.
