---
nav_title: Re-eligibility for Campaign and Canvas
article_title: Re-eligibility for Campaign and Canvas
page_order: 3
page_type: reference
description: "This reference article gives an overview of what it means to allow users to become re-eligible to receive or re-enter a campaign or Canvas."
tool:
  - Campaigns
  - Canvas

---

# Re-eligibility with Campaigns and Canvas

Whenever you schedule a recurring or triggered campaign or Canvas, you have the option of allowing users to become re-eligible for it. By default, Braze sends a message to a user only once, even if they re-qualify. If you enable re-eligibility, you are overriding this default behavior and allowing qualified members to receive messages again once they've received the first instance of the campaign or Canvas. You can state the timeline on which users would ultimately become re-eligible.

## Canvas

To enable re-elibility for a Canvas, check **Allow users to re-enter this Canvas** in the **Entry Controls** section of step 3. You can choose between allowing users to re-enter after the maximum duration of the Canvas, or after a specified window.

![Entry Controls][2]

Re-eligibility for Canvas variants is tied to Canvas entry rather than message receipt. Users who enter a Canvas and don't receive any messages will not be able to re-enter the Canvas unless re-eligibility is enabled. 

For example, suppose a user without an email address enters a daily recurring Canvas that contains one step. The Canvas step only contains an email message, so the user does not get the engagement. This user will not be able to enter the Canvas again unless the Canvas has re-eligibility enabled. If you have an active recurring or triggered Canvas without re-eligibility, and you'd like users to re-enter the Canvas until they receive a message from it, you can consider allowing users to be re-eligible for entry by adding a filter to the entry criteria that excludes customers who’ve received a message from the Canvas.

If re-eligibility for a Canvas is set to shorter than the duration of the Canvas, it's possible for users to enter the Canvas more than once, which can lead to misleading behavior for Canvases that use in-app messages with particularly long delays. Since multiple Canvas in-app messages could be triggered by the same session start, the user could potentially have the experience of receiving the same message repeatedly, if a specific step renders faster than others.

## Campaigns

To enable re-eligibility for a campaign, check **Allow users to become re-eligible to receive campaign** in the **Delivery Controls** section of step 2.

![Delivery Controls][1]

In the case of triggered campaigns with re-eligibility turned on, users who [did not actually receive the campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (despite completing the trigger event) will automatically qualify for the message the next time they complete the trigger event, even if you did not make users re-eligible. By making users re-eligible for a triggered campaign, you are enabling them to actually receive (and not simply trigger) the message more than once.

Additionally, if you are trying to send a message immediately with a re-eligibility of 0 minutes, we will always attempt to schedule it right away regardless of how a user has received previous versions of the campaign or Canvas.

![re-eligible][24]

## Re-eligibility Delay Calculations

Re-eligibility for both campaigns and Canvases are calculated in seconds, not calendar days. That means that a day counts as 24 hours (or 86,400 seconds) from when a user receives the message, not the next calendar day at midnight.

Similarly, a month counts as exactly 2,592,000 seconds, equal to approximately 30 days.

## Multivariate Testing

With regards to multivariate testing, Braze determines variant re-eligibility for all campaigns, triggered in-app messages, and Canvases using the following rules:

- When variant percentages are not changed, each user will always enter the same variant of a campaign, triggered in-app message, or Canvas entry every time they are re-eligible.
- If the variant percentages change, users may be redistributed to other variants.
- Control groups will remain consistent if the variant percentage is unchanged, and no users who previously received messages will ever enter the control group on a later send, nor will any user in the control group ever receive a message.

[1]: {% image_buster /assets/img_archive/reeligibility_controls_campaign.png %}
[2]: {% image_buster /assets/img_archive/reeligibility_controls_canvas.png %}

[24]: {% image_buster /assets/img_archive/ReEligible.png %}
