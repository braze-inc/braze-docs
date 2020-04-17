---
nav_title: Viewing and Understanding Segment Data
page_order: 4
---
# Viewing and Understanding Segment Data

## Accessing Segment Data

The Segments section of your Braze Dashboard contains a summary of all of your segments and allows you to examine detailed data for each one. To learn how to create a segment, go to our Quick Wins [page][3].

![View segment][1]

After clicking on the name of a segment, you'll be able to view, at the top of the page, segment statistics and filters. You can edit your segment by adding or deleting filters. Be sure to save any changes!

![Segment data][2]

## Turning Analytics Tracking On and Off

When you turn analytics tracking on for a segment, Braze will let you view sessions, custom events, and revenue over time by this segment.

![Analytics tracking][16]

On the Revenue page of the Dashboard, you'll be able to view data on [revenue and purchases over time for this segment][14]. By adding or removing segments from the graph, you can visually compare segment data for any custom time range.

![Revenue data by segment][17]

Similarly, data on [sessions over time for this particular segment][13] can be found on the App Usage page.

![Session data by segment][18]

Braze also provides the ability to view data on [Custom Events over time for segments][20], via the Custom Events page.

If you don't turn analytics tracking on for a segment, you will still be able to access [realtime statistics][11] for that segment and target its users with campaigns. The only difference is the access to the specific analysis tools mentioned above.

An app can have tracking turned on for at most 25 segments. Braze recommends tracking segments that are important for you to analyze when understanding your campaigns' effects on sessions, revenue, and purchases.

## Segment Statistics

You will see the following segment statistics, which update in real-time as you add or delete filters:

| Statistic | Description |
| --------- | --- |
| **Total Users** | How many users your app has in total. |
| **Selected Users** | How many users are in your segment and what percentage of your total user base they are. |
| **LTV (Paying Users)** | The lifetime value per user (LTV) in this segment and the lifetime value per paying user in this segment. The LTV is calculated by dividing your lifetime revenue by lifetime users. |
| **Emailable (Opted In)** | Emailable refers to all users who can be reached via email. These users have provided an email address and have not opted out. Opted In refers to users who have explicitly opted in to email. Due to [spam regulations][6], it's often a good idea to ask your users to explicitly opt in by implementing a double opt-in policy where users must click a link in an initial confirmation email. To encourage more users to opt in, you can target a message at [those who have neither opted in nor out][5]. |
| **Push Enabled (Opted In)** | Push enabled refers to the number of users with at least one push token. Some users may have multiple push tokens (e.g. if they own an iPhone and iPad), so the number of push notifications you send to this segment may be greater than the number of "push enabled" users. Opted In refers to the number of users who have explicitly opted in to push notifications. On iOS and Windows, users must always explicitly opt in for you to send them pushes. Because of how permissions are granted on Android, users don't always need to explicitly opt in to receive pushes. |

## Messaging Use and Historical Membership

If you scroll down the page, you will see segment data on Messaging Use and Historical Membership. Under the Messaging Use category, you can view the campaigns and News Feed items that have been targeted at this segment. Under Historical Membership, you can see how the size of this segment changed over time.

![More segments data][4]

## User Preview

Lastly, you can view detailed, user-specific information about your segments by selecting the 'User Preview' button on your segment page.

![User Specific Info][7]

On this page, you can view a number of user-specific attributes as shown below:

![User Preview][8]

[1]: {% image_buster /assets/img_archive/Segments.png %}
[2]: {% image_buster /assets/img_archive/A_Tracking.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[4]: {% image_buster /assets/img_archive/Historical_Membership2.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions
[6]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[7]: {% image_buster /assets/img_archive/Preview_Users.png %}
[8]: {% image_buster /assets/img_archive/User_Preview.png %}
[11]: #segment-statistics
[13]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
[14]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[16]: {% image_buster /assets/img_archive/A_Tracking_2.png %}
[17]: {% image_buster /assets/img_archive/Revenue.png %}
[18]: {% image_buster /assets/img_archive/Events_Over_Time2.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
