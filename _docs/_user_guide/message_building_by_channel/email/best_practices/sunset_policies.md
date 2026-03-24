---
nav_title: Sunset policies
article_title: Sunset Policies for Email
page_order: 8
page_type: reference
description: "This article covers best practices surrounding sunset policies and understanding situations when it's better to discontinue messages to disengaged users."
channel: email

---

# Sunset policies

> While you may be tempted to send campaigns to as many users as you can, there are situations when it's actually advantageous to stop messages to disengaged users. 

For emails, your sending IP has a reputation score that factors in engagement, spam reporting, blocklisting, and more. You can use tools like [Sender Score](https://www.senderscore.org/) or [Outlook's Smart Network Data Service](https://postmaster.live.com/snds/) to monitor your reputation score. If your reputation score is consistently low, ISP and mailbox filters might automatically sort your emails into a spam or low priority folder for all recipients, even engaged ones. Creating a sunset policy helps to deliver your emails to only active recipients. 

Segmentation filters help prevent your messaging from appearing like spam by letting you easily implement sunset policies for emails, push, and in-app notifications. Here are some things to consider when you create a sunset policy:

- What counts as an "unengaged" user? 
- Is engagement defined by clicks, purchases, app usage, or a combination of these behaviors? 
- How long does the lapse in engagement need to be for you to stop sending messages?
- Will you deliver any special campaigns to users before excluding them from your segments?
- Which messaging channels will your sunset policy apply to? 

For example, if you have users who opt in to [Apple's Mail Privacy Protection (MPP)]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/), consider how this may impact your email campaigns and deliverability metrics and determine how to best structure your sunset policy.

To incorporate sunset policies into your campaigns, create a [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) that automatically excludes users who have marked your emails as spam or have not interacted with a your messages for a certain period of time.  

To set up these segments, choose the `Has Marked You As Spam` and `Last Engaged With Message` filters located under the **Retargeting** section in the filter dropdown. 

When you apply the `Last Engaged With Message` filter, specify the type of messaging (push, email, or in-app notification) that the user has or has not interacted with, as well as the number of days it has been since the user last interacted. After you create a segment, choose to target this segment with any [messaging channel]({{site.baseurl}}/user_guide/message_building_by_channel/).

![Segment Details page with the filter "Last Engaged with Message" selected.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

While Braze automatically stops sending emails to users who have marked you as spam, the `Has Marked You As Spam` filter allows you to also send these users targeted push messages and in-app notifications. This filter is useful for [retargeting campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). For instance, you can send unengaged users messages that remind them of the features and deals that they are missing out on when they don't open your emails.

Sunset policies can be especially helpful in email campaigns that target lapsing users. While these campaigns focus on segments that have not interacted with your app for a period of time, they can put the deliverability of your emails at risk if they repeatedly include unengaged recipients. Sunset policies allow you to target lapsing users without landing in the spam folder.

