---
nav_title: Using User Search
article_title: Using User Search
page_order: 5
page_type: reference
tool: 
  - Dashboard
description: "This reference article will go through how to use User Search in the dashboard and showcases some User Search use cases."

---

# Using user search

> This reference article will go through how to use User Search in the dashboard, the different components involved in a user profile, and showcases some examples of how this feature can be used to troubleshoot campaigns. 

## Feature overview

The **User Search** feature allows you to view user profiles. User profiles are a great way to find information about specific users. This feature is located in the **Users** section of the Braze dashboard.

![][7]

You can search your user base using a user's email or user ID. Most of the time, the user search will return one result but do note that if you enter a non-unique email (i.e., an email that belongs to more than one user) into the user search, it will return more than one user profile. Once you've entered an email or user ID into the **User Search**, you'll be able to view the information that you've recorded on this user with the Braze SDK. If you do enter a non-unique email, clicking **Next** will allow you to view the other profiles that are associated with that email.

![][14]

## Use cases

The **User Search** feature is a great resource for troubleshooting and testing because you can easily access information about a user's engagement history, segment membership, device and operating system.

For example, if a user reports a problem and you are not sure what device and operating system they are using, you can use the [Overview tab](#overview-tab) to find this information (as long as you have their email or user ID). You can also view a user's language, which could be helpful if you are troubleshooting a [multi-lingual campaign][13] that did not behave as expected.

You can use the [Engagement tab](#engagement-tab) to verify whether a certain user received a campaign. In addition, if this particular user did receive the campaign, you can see when they received it. You can also verify whether a user is in a certain segment, and whether a user is opted in to push, e-mail, or both. This information is useful for troubleshooting purposes. For example, you should check this information if a user doesn't receive a campaign that you expected them to receive or receives a campaign that you did not expect them to receive.

## Overview tab {#overview-tab}

In the **Overview** tab you can see information about the user's profile, app usage, custom attributes, custom events, purchases, and the most recent device that the user logged in on. For more information on this data, see [User Data Collection][12].

![][8]

## Engagement tab {#engagement-tab}

You can click on the **Engagement** tab to view information about the user's Contact Settings, Campaigns Received, Segments, Communication Stats, Install Attribution, News Feed Cards Clicked and Random Bucket #.

![][9]

## Social tab {#social-tab}

The **Social** tab allows you to see the social accounts that a user has connected to the app. You're also able to view a user's activity on these connected social accounts.

![][11]

[7]: {% image_buster /assets/img_archive/user_search2.png %}
[8]: {% image_buster /assets/img_archive/user_profile2.png %}
[9]: {% image_buster /assets/img_archive/User_Profile_Engagement.png %}
[11]: {% image_buster /assets/img_archive/User_Profile_Social.png %}
[12]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[14]: {% image_buster /assets/img_archive/User_Search_Nonunique.png %}
