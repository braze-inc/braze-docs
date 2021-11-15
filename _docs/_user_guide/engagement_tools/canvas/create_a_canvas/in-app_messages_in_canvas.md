---
nav_title: In-App Messages In Canvas
article_title: In-App Messages in Canvas
page_order: 6
page_type: reference
description: "This reference article describes features and nuances specific to Canvas In-App Messages, which you can add to your Canvas to show rich messaging."
tool: Canvas
channel: in-app messages

---

# In-app messages in Canvas

{% include video.html id="6X8E20BlblI" align="right" %}

> In-App Messages can be added as part of your Canvas journey to show rich messaging when your customer engages with your app. This article describes features and nuances specific to Canvas In-App Messages.

Once you've set up delay and audience options, you can add an in-app message to your Canvas by selecting in-app message from "messaging channels." Once a step's delay has passed and the audience options have been checked, the in-app message will be set live and users will see it __if they open the app__. Currently, in-app messages in Canvas may only be triggered by the "start session" trigger event.

You can customize [when your message will expire](#in-app-message-expiration) and which [advancement behavior](#advancement-behavior-options) it will have.

## In-app message expiration

In the in-app message composer, you have the option to choose when the in-app message will expire. During this time, the in-app message will sit and wait to be viewed until it has reached the expiry date. Once sent, the in-app message can be viewed at most once.
![Expire After][1]

| Option | Description |
|---|---|---|
| `Message Expires ... After` | The first option allows you to expire the in-app message relative to when the step becomes available to the user. <br> <br> _For example, an in-app message with a two-day expiration would become available after the step's delay elapses and audience options are checked. It would then be available for 2 days (48 hours) and during those two days, users may see the in-app message if they open the app._ |
| `Message Expires By ...` | The second option allows you to choose a specific date and time when the in-app message will longer be available. <br> <br> _For example, if you have a sale that ended at a specific date and time, you might select this option so that once the sale ends users no longer see the associated in-app message._ |
{: .reset-td-br-1 .reset-td-br-2}

### Use cases

When should you use this feature? Braze highly recommends that you consider using this feature in your Promotional and Onboarding campaigns.

{% tabs %}
  {% tab Promotional %}
__Promotional Canvases__

Promotions, coupons, and sales often have hard expiration dates. The Canvas outlined below should alert your users at the most opportune times that there is a promotion they may use, and perhaps influence a purchase. This promotion expires by 2/28/2019 at 11:15 AM in the company's time zone.

| Canvas Step | Delay | Audience | Channel | Expiration | Advancement | Details |
|---|---|---|
| Day 1: 50% Off | None | All from Entry | Push | N/A | Advance Audience after Delay | Initial push that alerts your users of the promotion. <br>  <br> This is intended to drive users to your app to take advantage of the promotion. |
| In-App: 50% Off | None | All from Entry | In-App Message | Expires by: <br> 2/28/2019 <br> 11:15 AM <br> Company Time | In-App Message Viewed | The user has now opened the app and will receive this message whether or not that was because of the push message before. |
| 50% Off Reminder | 1 Day <br> After the user receives the previous step. | All from Entry <br> _Filter: Last made a purchase more than one week ago._ | In-App Message |  Expires by: <br> 2/28/2019 <br> 11:15 AM <br> Company Time  | None <br> _Last message in Canvas._ | The user has received the in-app message in the previous step but has not made a purchase despite being in the app.  <br>  <br> This message is meant to further draw the user to make a purchase using the promotion. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

As you can see, the in-app messages expire when the promotion expires to prevent any discrepancies between the messaging and the customer experience.

  {% endtab %}
  {% tab Onboarding %}

__User Onboarding Canvases__

Your first impression with a user is, perhaps, your most critical one. It can make or break future visits to your app. Your initial communications with your user should be sensibly timed and encourage frequent visits to your app to promote usage.

| Canvas Step | Delay | Audience | Channel | Expiration | Advancement | Details |
|---|---|---|
| Welcome Email | None | All from Entry | Email | N/A | Advance Audience after Delay | Initial email that welcomes your users to a project, membership, or other onboarding program. <br>  <br> This is intended to drive users to your app to begin their onboarding. |
| Day 3-6 In-App Message | 3 Days <br> After the user receives the previous step. | All from Entry | In-App Message | Expires three days after the step becomes available. | In-App Message Live | If the user has acted upon the email and been driven to the app, they will receive the desired in-app message to continue or remind them of their onboarding and any requirements associated with it. |
| Day 5 Push | 2 Days <br> After the user receives the previous step. | All from Entry | Push |  N/A  | Message Sent | After users have received their in-app message, they will receive a follow-up push to continue their onboarding. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

As you can see, the push messages are spaced around an in-app message to ensure that the user has visited the app and begun their onboarding. This will prevent any annoying spam or out-of-order messaging that could dissuade users from visiting your app, and instead create a flowing, sensible order to their initial experiences with your app.

  {% endtab %}
{% endtabs %}

## Advancement Behavior options

Braze's Advancement Behavior feature allows you to choose the criteria for advancement through your Canvas step. [Steps with only in-app messages](#steps-with-in-app-messages-only) have different advancement options than [steps with multiple message types](#steps-with-multiple-message-channels) (push, email, etc.).

Action-based delivery is __not available for Canvas steps with in-app messages__. Canvas steps with in-app messages __must be scheduled__. Instead, Canvas in-app messages will appear the first time that your user opens the app (triggered by the start session trigger) after the scheduled message in the Canvas step has been sent to them.

Note that if you have multiple in-app messages within one canvas, a user must start multiple sessions to receive each of those individual messages.

{% alert important %}
Please note that in-app messages __cannot__ be triggered by events in Canvas.
{% endalert %}

### Steps with in-app messages only

Steps with in-app messages have specific advancement options that allow you to specify the exact situation when your message would be sent.

![iamlive.png][2]

| Option | Description |
|---|---|---|
| In-App Viewed | When "In-App Viewed" is selected, users will advance to the next steps of the Canvas when they view the in-app message in your application and log an in-app message impression.  <br> <br> _Users who do not view the in-app message before it expires will exit the Canvas and will not advance to subsequent steps._ |
| In-App Live | When "In-App Live" is selected, users will advance to the next steps in the Canvas as soon as the in-app message becomes live. In-app messages are live once the delay for the step has elapsed and the audience options for the step have been checked.  <br> <br> _When this option is selected, all users who match the step's segment and filter criteria will be advanced to subsequent steps in the Canvas. Use this option when you want users to advance regardless of whether the in-app message is viewed or expires._ |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
  When "In-App Live" is selected, the in-app message will be available until it expires, even if the user has moved to subsequent steps. If you do not want the in-app message to be live when the next steps in the Canvas are delivered, ensure that the expiration is shorter than the delay on subsequent steps.
{% endalert %}

### Steps with multiple channels

![Push advancement behavior][3]

Steps with an in-app message and another channel have the following advancement options:

| Option | Description |
|---|---|---|
| Message Sent | When the message sent is selected, users must be sent an email/webhook/push or view the in-app message to advance to subsequent steps in the Canvas.  <br> <br>  _If the in-app message expires and the user hasn't been sent the email/webhook/push or viewed the in-app message, they will exit the Canvas and will not advance to subsequent steps._ |
| Immediately Advance Audience | When this option is selected, everyone in the step's audience will advance to the next steps after the delay elapses, whether they have seen the noted message or not.  <br> <br> _Users must match the step's segment and filter criteria to advance to next steps._ |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
  When "Entire Audience" is selected, the in-app message will be available until it expires, even if the user has moved to subsequent steps. If you do not want the in-app message to be live when the next steps in the Canvas are delivered, ensure that the expiration is shorter than the delay on subsequent steps.
{% endalert %}

## Custom event properties in a Canvas

Due to action-based delivery being unavailable for Canvas steps with in-app messages, you similarly cannot use custom event properties for these steps. If you'd like to template event properties in Canvas, we recommend storing your event properties as custom attributes in your first Canvas step, and then personalizing your in-app message with the custom attributes in the second step. 


[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
[2]: {% image_buster /assets/img/iam-advancement-behavior.png %} "IAM Live"
[3]: {% image_buster /assets/img/push-advancement-behavior.png %} "IAM Live"
