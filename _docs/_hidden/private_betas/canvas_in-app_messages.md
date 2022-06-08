---
nav_title: In-App Messages in Canvas
permalink: "/canvas_in-app_messages/"
hidden: true
---

# In-app messages in Canvas

{% include video.html id="6X8E20BlblI" align="right" %}

Once you've set up delay and audience options, you can add an in-app message to your Canvas by selecting **In-App Message** in the **Messaging Channels** panel. Once a step's delay has passed and the audience options have been checked, the in-app message will be set live, and users will see it if they open the app.

You can customize when your message will [expire](#in-app-message-expiration) and which [advancement behavior](#advancement-behavior-options) it will have.

{% alert important %}
In-app messsages for Canvas is currently in beta. Contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

## In-app message expiration

In the in-app message composer, you have the option to choose when the in-app message will expire.

![In-App Message Expiration section with the in-app message set to expire in one day afrer the step becomes available.][1]

| Option | Description |
|---|---|---|
| `Message Expires ... After` | The first option allows you to expire the in-app message relative to when the step becomes available to the user. <br> <br> For example, an in-app message with a two day expiration would become available after the step's delay elapses and audience options are checked. It would then be available for 2 days (48 hours) and during those two days users may see the in-app message if they open the app. |
| `Message Expires By ...` | The second option allows you choose a specific date and time when the in-app message will longer be available. <br> <br> For example, if you have a sale that ended at a specific date and time, you might select this option so that once the sale ends users no longer see the associated in-app message. |
{: .reset-td-br-1 .reset-td-br-2}

### Use cases

When should you use this feature? Braze highly recommends that you consider using this feature in your Promotional and Onboarding campaigns.

{% tabs %}
  {% tab Promotional %}
**Promotional Canvases**

Promotions, coupons, and sales often have hard expiration dates. The following Canvas should alert your users at the most opportune times that there is a promotion they may use, and perhaps influence a purchase. This promotion expires by 2/28/2019 at 11:15am in the company's time zone.

| Canvas Step | Delay | Audience | Channel | Expiration | Advancement | Details |
|---|---|---|
| Day 1: 50% Off | None | All from Entry | Push | N/A | Entire Audience after Delay | Initial push that alerts your users of the promotion. <br>  <br> This is intended to drive users to your app to take advantage of the promotion. |
| In-App: 50% Off | None | All from Entry | In-app Message | Expires by: <br> 2/28/2019 <br> 11:15 AM <br> Company Time | In-app Message Viewed | The user has now opened the app and will receive this message whether or not that was because of the push message before. |
| 50% Off Reminder | 1 Day <br> After the user receives the previous step. | All from Entry <br> _Filter: Last made a purchase more than one week ago._ | In-app Message |  Expires by: <br> 2/28/2019 <br> 11:15 AM <br> Company Time  | None. <br> Last message in Canvas. | The user has received the in-app message in the previous step, but has not made a purchase despite being in the app.  <br>  <br> This message is meant to further draw the user to make a purchase using the promotion. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

As you can see, the in-app messages expire when the promotion expires to prevent any discrepancies between the messaging and the customer experience.

  {% endtab %}
  {% tab Onboarding %}

**User onboarding Canvases**

Your first impression with a user is, perhaps, your most critical one. It can make or break future visits to your app. Your initial communications with your user should be sensibly timed and encourage frequent visits to your app to promote usage.

| Canvas Step | Delay | Audience | Channel | Expiration | Advancement | Details |
|---|---|---|
| Welcome Email | None | All from Entry | Email | N/A | Entire Audience after Delay | Initial email that welcomes your users to a project, membership, or other onboarding program. <br>  <br> This is intended to drive users to your app to begin their onboarding. |
| Day 3-6 in-app message | 3 Days <br> After the user receives the previous step. | All from Entry | In-app message | Expires three days after the step becomes available. | In-app message Live | If the user has acted upon the email and been driven to the app, they will receive the desired in-app message to continue or remind them of their onboarding and any requirements associated with it. |
| Day 5 Push | 2 Days <br> After the user receives the previous step. | All from Entry | Push |  N/A  | Only Advance If Message Received | After users have received their in-app message, they will receive a follow-up push to continue their onboarding. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

As you can see, the push messages are spaced around an in-app message to ensure that the user has visited the app and begun their onboarding. This will prevent any annoying spam or out-of-order messaging that could dissuade users from visiting your app, and instead create a flowing, sensible order to their initial experiences with your app.

  {% endtab %}
{% endtabs %}

## Advancement behavior options

Braze's Advancement Behavior feature allows you to choose the criteria for advancement through your Canvas step. [Steps with only in-app messages](#steps-with-in-app-messages-only) have different advancement options than [steps with multiple message types](#steps-with-multiple-message-channels) (push, email, etc.).

Action-based delivery is not available for Canvas steps with in-app messages. Canvas steps with in-app messages must be scheduled. Instead, Canvas in-app messages will appear the first time that your user opens the app after the scheduled message in the Canvas step has been sent to them.

### Steps with in-app messages only

Steps with in-app messages have specific advancement options that allow you to specify the exact situation when your message would be sent.

| Option | Description |
|---|---|---|
| In-App Viewed | When **In-App Viewed** is selected, users will advance to the next steps of the Canvas when they view the in-app message in your application and log an in-app message impression.  <br> <br> Users who do not view the in-app message before it expires will exit the Canvas and will not advance to subsequent steps. |
| In-App Live | When **In-App Live** is selected, users will advance to the next steps in the Canvas as soon as the in-app message becomes live. In-app messages are live once the delay for the step has elapsed and the audience options for the step have been checked.  <br> <br> When this option is selected, all users who match the step's segment and filter criteria will be advanced to subsequent steps in the Canvas. Use this option when you want users to advance regardless of whether the in-app message is viewed or expires. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
When **In-App Live** is selected, the in-app message will be available until it expires, even if the user has moved to subsequent steps. If you do not want the in-app message to be live when next steps in the Canvas are delivered, ensure that the expiration is shorter than the delay on subsequent steps.
{% endalert %}

### Steps with multiple channels

Steps with an in-app message and another channel have the following advancement options:

| Option | Description |
|---|---|---|
| Message Received | When message received is selected, users must be sent an email/webhook/push or view the in-app message in order to advance to subsequent steps in the Canvas. <br> <br> If the in-app message expires and the user hasn't received the email, webhook, or push, or viewed the in-app message, they will exit the Canvas and will not advance to subsequent steps. |
| Advance Entire Audience After Delay | When this option is selected, every user in the step's audience will advance to next steps after the delay elapses.  <br> <br> Users must match the step's segment and filter criteria in order to advance to next steps. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
When **Entire Audience** is selected, the in-app message will be available until it expires, even if the user has moved to subsequent steps. If you do not want the in-app message to be live when next steps in the Canvas are delivered, ensure that the expiration is shorter than the delay on subsequent steps.
{% endalert %}

[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
