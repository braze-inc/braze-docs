---
nav_title: Sunset Policies
page_order: 8
---

# Sunset Policies

While you may be tempted to send campaigns to as many users as you can, there are situations where it's actually wise to discontinue messages to disengaged users.  For instance, in the case of emails, your sending IP has a reputation score that factors in engagement, spam reporting, blacklisting, etc. There are many free tools to monitor your IPs reputation score such as [Sender Score](https://www.senderscore.org/ "Sender Score") or [Outlook's Smart Network Data Service](https://postmaster.live.com/snds/ "Outlook's Smart Network Data Service"). If your reputation score is consistently low, ISP and mailbox filters might automatically sort your emails into a spam or low priority folder for all recipients, even engaged ones.  To prevent this from happening, you need to create a sunset policy that ensures your emails aren't delivered to inactive recipients. Braze's segmentation filters help prevent your messaging from appearing spammy or irrelevant by letting you easily implement sunset policies for emails, pushes, in-app notifications, and News Feed cards

Here are some things to consider when you create a sunset policy:

- What counts as an "unengaged" user? Is engagement defined by clicks and opens, purchases, app usage, or a combination of these behaviors?
- How long does the lapse in engagement need to be for you to stop sending messages?
- Will you deliver any special campaigns to users before excluding them from your segments?
- Which messaging channels will your sunset policy apply to?

To incorporate sunset policies into your campaigns, [create segments][19] that automatically exclude users who have marked your emails as spam or have not interacted with a your messages for a certain period of time.  To set up these segments, choose the "Has Marked You As Spam" and/ or "Last Engaged With Message" filters.  When you apply the "Last Engaged With Message" filter, you can specify the type of messaging (push, email, or in-app notification) that the user has or has not interacted with, as well as the number of days it has been since the user last interacted. After you create a segment, you can then choose to target this segment with any messaging channel.

![Sunset Policy][20]

While Braze's platform automatically stops sending emails to users who have marked you as spam, the "Has Marked You As Spam" filter allows you to also send these users targeted push messages, in-app notifications, and News Feed cards.  This filter is useful for [retargeting campaigns][21] - for instance, you can send unengaged users messages or News Feed updates that remind them of the features and deals that they are missing out on when they don't open your emails.

Sunset policies can be especially helpful in email campaigns that target lapsing users.  While these campaigns focus on segments that have not interacted with your app for a period of time, they can put the deliverability of your emails at risk if they repeatedly include unengaged recipients. Sunset policies allow you to target lapsing users without landing in the spam folder.

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
