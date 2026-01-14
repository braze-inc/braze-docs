---
nav_title: Re-eligibility
article_title: Re-eligibility
page_order: 8
page_type: reference
description: "This reference article defines re-eligibility for campaigns and Canvases."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Re-eligibility for campaigns and Canvas

> When you schedule a recurring or triggered campaign or Canvas, you have the option of allowing users to become re-eligible for it. Re-eligibility means users can enter the campaign or Canvas multiple times based on the trigger.

## How it works

By default, Braze sends a message to a user only once, even if they re-qualify multiple times as re-eligibility needs to be turned on separately. After it's turned on, qualified members will be allowed to receive messages again after they've received the first instance of the campaign or Canvas. You can state the timeline on which users would ultimately become re-eligible.

## Turning on re-eligibility

{% tabs local %}
{% tab campaign %}
To turn on re-eligibility for a campaign, select the **Allow users to become re-eligible to receive campaign** checkbox in the **Delivery Controls** section. The maximum time for re-eligibility for a campaign is 720 days.

For triggered campaigns with re-eligibility turned on, users who [did not actually receive the campaign message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (despite completing the trigger event) will automatically qualify for the message the next time they complete the trigger event. This is because re-eligibility is based on message receipt and not campaign entry. By making users re-eligible for a triggered campaign, you are allowing them to actually receive (and not simply trigger) the message more than once.

Additionally, if you're trying to send a message immediately with a re-eligibility of zero minutes, we'll always attempt to schedule it right away, regardless of how a user has received previous versions of the campaign or Canvas.

#### Re-eligibility with API-triggered campaigns

The number of times a user receives an API-triggered campaign can be limited using re-eligibility settings. This means the user will receive the campaign only once or once in a given window, regardless of how many times the API trigger is fired.

For example, let’s say you’re using an API-triggered campaign to send the user a campaign about an item they recently viewed. In this case, you can limit the campaign to send up to one message per day, regardless of how many items they viewed, while firing the API trigger for each item. On the other hand, if your API-triggered campaign is transactional, you will want to make sure that the user receives the campaign every time they do the transaction by setting the delay to zero minutes.
{% endtab %}

{% tab canvas %}

To turn on re-eligibility for a Canvas, select **Allow users to re-enter this Canvas** in the **Entry Controls** section. You can choose between allowing users to re-enter after the maximum duration of the Canvas or after a specified window.

Re-eligibility for Canvas variants is tied to Canvas entry rather than message receipt. Users who enter a Canvas and don't receive any messages will not be able to re-enter the Canvas unless re-eligibility is turned on.

Note that a user doesn't need to exit a Canvas first before re-entering if re-eligibility is set to zero seconds, meaning a user can enter the same Canvas again. As another example, if the Canvas duration is set to 7 days and the re-eligibility period is set to 3 days, a user can re-enter the Canvas before completing their first journey through it.

You can add additional filters to prevent users from receiving the same step or message multiple times. However, when a user re-enters a Canvas for the second time, the steps previously received during their first time in the Canvas aren't visible to the user. This means the user may still receive the same message again. To prevent this, you can configure the Canvas to prevent re-entry or set the re-eligibility for the maximum duration of the Canvas.

You can also use a [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) for the user receiving the step to log this as a custom attribute, which can be used to filter out users who have received the step during their Canvas journey.

### Example

For example, suppose a user without an email address enters a daily recurring Canvas that contains one step in the user journey. This step only contains an email message, so the user does not get the engagement. This user won't be able to enter the Canvas again unless the Canvas has re-eligibility turned on. 

If you have an active recurring or triggered Canvas without re-eligibility, and you'd like users to re-enter the Canvas until they receive a message from it, you can consider allowing users to be re-eligible for entry by adding a filter to the entry criteria that excludes customers who've received a message from the Canvas.

If re-eligibility for a Canvas is set to shorter than the duration of the Canvas, it's possible for users to enter the Canvas more than once, which can lead to misleading behavior for Canvases that use in-app messages with particularly long delays. Since multiple Canvas in-app messages could be triggered by the same session start, the user could potentially have the experience of receiving the same message repeatedly if a specific component renders faster than others.
{% endtab %}
{% endtabs %}

## Re-eligibility delay calculations

Re-eligibility for both campaigns and Canvases is calculated in seconds, not calendar days. That means that a day counts as 24 hours (or 86,400 seconds) from when a user receives the message, not the next calendar day at midnight. Similarly, a month counts as exactly 2,592,000 seconds, equal to approximately 30 days.

### Example

Consider the following scenario:

* A campaign is set to send monthly on the 15th with re-eligibility set to 30 days.
* There are fewer than 30 days between February 15 and March 15. 

This means users who received the campaign on February 15 will not be eligible for the campaign to be sent on March 15. If the campaign is set to send daily at 8 am with re-eligibility of 1 day, and there's a latency in sending the message, users who received the campaign at 8:30 am will not be re-eligible yet on the following day at 8 am.

## Multivariate testing

For multivariate testing, Braze determines variant re-eligibility for all campaigns, triggered in-app messages, and Canvases using the following rules:

- When variant percentages are not changed, each user will always enter the same variant of a campaign, triggered in-app message, or Canvas entry every time they are re-eligible.
- If the variant percentages change, users may be redistributed to other variants.
- Control groups will remain consistent if the variant percentage is unchanged, and no users who previously received messages will ever enter the control group on a later send, nor will any user in the control group ever receive a message.
