---
nav_title: Reporting & Analytics
page_order: 20
---

# Email Reporting

Braze provides you with a detailed report of each of your email campaigns. Navigate to the 'Campaigns' tab on your dashboard and click on the 'Details' tab of your desired campaign. On this page, you will be able to comprehensively view and analyze the success of your campaign in an organized format.

Additionally, Braze allows you to see how successful different links are within a single email campaign. Clicking on "View Heat Map" brings up a visual view of your email that shows you where and with what frequency users are clicking on certain links.

![email_analytics][63]

# Email Analytics Glossary

|Metric |Calculation |Description
|---|---|---|
|Variation |Named. |Version of a campaign.
|Emailable |Count. Number received from Braze. |Users who have an email address on record and have explicitly opted in or subscribed.
|Audience % |Number of Recipients in Variant / Unique Recipients  <br> Number received from Braze. |Percentage of users who received that particular variant.
|Unique Recipients |Count. Number received from Braze. |Exact number of users who received that particular variant.
|Sends <br> _A.K.A. Messages Sent_ |Count. Number received from Braze. |Number of messages sent.
|Deliveries |Sends - Bounces |The total number of messages sent and received by emailable parties.
|Deliveries % |(Sends - Bounces) / Sends |Percentage of Sends received by emailable parties.
|Bounces |Count. Number received from email delivery partner. |Number of messages designated as “returned” or “not received” (etc.) from send services used. These messages are not received by the intended Emailable users.
|Bounces % <br> _A.K.A. Bounce Rate_ |Bounces / Sends |Percentage of Sends designated as “returned” or “not received” (etc.) from send services used. These messages are not received by the intended Emailable users.
|Spam |Count. Number received from email delivery partner. |Number of messages marked or otherwise designated as spam. Braze [automatically unsubscribes][64] users that marked an email as spam, and those users won’t be targeted by future emails.
|Spam % |Spam / Sends |Percentage of Sends marked or otherwise designated as spam.
|Unique Opens |Count. Number received from email delivery partner. |The number of users who opened a sent message at least once. Note: Unique calculation is tracked over a 7 day (Sendgrid) or 30 day (Mailjet users) period.
|Unique Opens % <br> _A.K.A. Open Rate_ |Unique Opens / Deliveries |The percentage people who open a sent message at least once compared to all who have received the sent message.
|Unique Clicks |Count. Number received from email delivery partner. |The number of users who have clicked within a sent message. Unsubscribe clicks are included as clicks in this count. Note: Unique calculation is tracked over a 7 day (Sendgrid) or 30 day (Mailjet users) period.
|Unique Clicks % <br> _A.K.A. Click Rate_ |Unique Clicks / Deliveries |The percentage of users who have clicked within a sent message compared to all messages delivered.
|Unsubscribers <br> _A.K.A. Unsub_ |Count. Number received from email delivery partner. |Number of messages resulting in an unsubscription. Unsubscriptions occur when a user clicks on the Braze unsubscribe link.
|Unsubscribers % <br> _A.K.A. Unsub Rate_ |Unsubscribes / Deliveries |Percentage of Sends resulting in an unsubscription. Unsubscribe clicks are included as clicks in this count.
|Revenue |Count. Number received from Braze. |Total revenue in dollars from campaign recipients within the [set primary conversion window][65].
|Primary Conversions |Campaigns / Conversion |Number of times a defined event occurred. This defined event is determined by the marketer when building the campaign.
|Primary Conversions % |Primary Conversions / Unique Recipients |The percentage of times a defined event occurred compared to all recipients of a sent message. This defined event is determined by the marketer when building the campaign.
|Confidence |Aggregated from Campaigns / Conversion |A percentage that represents the performance of the listed Variation compared to the Control.|


[18]: {% image_buster /assets/img_archive/Email_IP_Warming_Sends_Limit_new.png %}
[19]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[20]: {% image_buster /assets/img_archive/Email_Sunset_Policies_new.png %}
[21]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[22]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[23]: {{ site.baseurl }}/help/best_practices/spam_regulations/#spam-regulations
[24]: http://tools.ietf.org/html/rfc2822
[25]: {{ site.baseurl }}/help/best_practices/user_onboarding/#user-onboarding
[26]: {% image_buster /assets/img_archive/Livingsocial_email.png %}
[27]: {% image_buster /assets/img_archive/Ideeli_email.png %}
[28]: {% image_buster /assets/img_archive/Restaurant_email.png %}
[29]: {% image_buster /assets/img_archive/Ruelala_email.png %}
[30]: {% image_buster /assets/img_archive/Hailo_social_email.png %}
[31]: {% image_buster /assets/img_archive/Allrecipes_email.png %}
[33]: {% image_buster /assets/img_archive/Multiple_click_tracking_screen_3a.png %}
[34]: {% image_buster /assets/img_archive/Email_HeatMap_new.png %}
[35]: {% image_buster /assets/img_archive/campaign_data_2.png %}
[36]: #deep-linking
[37]: http://googlewebmastercentral.blogspot.com/2015/05/app-deep-linking-with-googl.html
[38]: {{ site.baseurl }}/help/best_practices/email/#unsubscribed-email-addresses
[39]: {{ site.baseurl }}/help/best_practices/email/#bounces--invalid-emails
[40]: {{ site.baseurl }}/help/best_practices/spam_regulations/#spam-regulations
[42]: https://returnpath.com/
[43]: http://www.briteverify.com/
[44]: https://senderscore.org/
[45]: http://www.senderbase.org/
[46]: {{ site.baseurl }}/help/best_practices/email/#email-sunset-policies
[47]: {% image_buster /assets/img_archive/appusage_ipwarming_main.png %}
[48]: {% image_buster /assets/img_archive/campaign_confirmation_ipwarming.png %}
[49]: {% image_buster /assets/img_archive/canvas_ip_warming.png %}
[50]: {% image_buster /assets/img_archive/targeting_campaign_ipwarming.png %}
[60]: {{ site.baseurl }}/help/best_practices/email/#email-sunset-policies
[61]: {% image_buster /assets/img_archive/preheader_example.png %}
[62]: https://www.emailonacid.com/blog/article/email-development/tips-for-coding-email-preheaders
[63]: {% image_buster /assets/img_archive/email_click_results_heatmap.gif %}
[64]: {{ site.baseurl }}/help/best_practices/email/#unsubscribed-email-addresses
[65]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#primary-conversion-event
