---
nav_title: Segment Data
article_title: Viewing and Understanding Segment Data
page_order: 2
page_type: reference
description: "This reference article explains the Segments section of your Braze Dashboard, and includes a summary the statistics provided."
tool: 
  - Segments
  - Reports
  
---
# Viewing and Understanding Segment Data

> This reference article explains the Segments section of your Braze Dashboard, and includes a summary the statistics provided.

## Accessing Segment Data

The **Segments** page of your Braze Dashboard contains a summary of all of your segments and allows you to examine detailed data for each one. On this page, search for and click the name of a segment to edit and view it's data. To learn how to create a segment, check out [Creating a Segment][3].

![Segments page][1]

After clicking on the name of a segment, you'll be able to view segment statistics and filters. You can edit your segment by adding or deleting filters. Be sure to save any changes!

![Segment data][2]

When you turn [analytics tracking on for a segment][9], Braze will let you view sessions, custom events, and revenue over time by this segment.

## Segment Statistics

You will see the following segment statistics, which update in real-time as you add or delete filters:

| Statistic | Description |
| --------- | --- |
| **Total Users** | How many users your app has in total. |
| **Selected Users** | How many users are in your segment and what percentage of your total user base they are. |
| **LTV (Paying Users)** | The lifetime value per user (LTV) in this segment and the lifetime value per paying user in this segment. The LTV is calculated by dividing your lifetime revenue by lifetime users. |
| **Emailable (Opted In)** | Emailable refers to all users who can be reached via email. These users have provided an email address and have not opted out. Opted In refers to users who have explicitly opted in to email. Due to [spam regulations][6], it's often a good idea to ask your users to explicitly opt-in by implementing a double opt-in policy where users must click a link in an initial confirmation email. To encourage more users to opt-in, you can target a message at [those who have neither opted in nor out][5]. |
| **Push Enabled (Opted In)** | Push enabled refers to the number of users with at least one push token. Some users may have multiple push tokens (e.g. if they own an iPhone and iPad), so the number of push notifications you send to this segment may be greater than the number of "push enabled" users. Opted In refers to the number of users who have explicitly opted in to push notifications. On iOS and Windows, users must always explicitly opt-in for you to send them pushes. Because of how permissions are granted on Android, users don't always need to explicitly opt-in to receive pushes. |
{: .reset-td-br-1 .reset-td-br-2}

## Messaging Use and Historical Membership

If you scroll down the page, you will see segment data on Messaging Use and Historical Membership. Under the **Messaging Use** section, see which campaigns and News Feed items have targeted this segment. Under **Historical Membership**, you see how the size of this segment changed over time. Use the dropdown to filter segment membership by date range.

![Under Messaging Use, view the campaigns that your segment is being used in.][4]
![Use the Historical Membership dropdown to filter segment membership by date range.][10]

## User Preview

To view detailed, user-specific information about your segments, click **User Data** and select **User Preview**.

![User Specific Info][7]

On this page, you can view a number of user-specific attributes, such as gender, age, number of sessions, and whether they have opted into push and email.

![User Preview][8]

[1]: {% image_buster /assets/img_archive/segments.png %}
[2]: {% image_buster /assets/img_archive/A_Tracking.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[4]: {% image_buster /assets/img_archive/historical_membership1.png %}
[10]: {% image_buster /assets/img_archive/historical_membership2.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions
[6]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[7]: {% image_buster /assets/img_archive/preview_users.png %}
[8]: {% image_buster /assets/img_archive/user_preview.png %}
[9]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/