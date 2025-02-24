---
nav_title: In-App Messages
article_title: In-App Messages in Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "This reference article describes features and nuances specific to in-app messages that you can add to your Canvas to show rich messaging."
tool: Canvas
channel: in-app messages

---

# In-app messages in Canvas

> You can add in-app messages as part of your Canvas journey to show rich messaging when your customer engages with your app.


## How it works

Before you can use in-app messages in your Canvas, be sure to have a [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) set up with delay and audience options.

After any delays pass and the audience options are checked, the in-app message will be set live, and users will see it if they open the app. In-app messages in Canvas can only be triggered by the `start session` trigger event—they can't be triggered by custom events in a Canvas component.

For Canvas steps that have action-triggered entry, users can enter the Canvas mid-session. However, as noted above, in-app messages won't trigger until the next session starts, so these users would miss the initial in-app message since they weren't eligible to enter the Canvas before the session started.

## Adding an in-app message to your user journey

To add an in-app message to your Canvas, do the following:

1. Add a [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) step to your user journey.
2. Select **In-App Message** for your **Messaging Channel**. 
3. Determine [when your message will expire](#in-app-message-expiration) and which [advancement behavior](#advancement-behavior-options) it will have.

### In-app message expiration

In the in-app message editor, you can choose when the in-app message will expire. During this time, the in-app message will "sit" and wait to be viewed until it has reached the expiry date. After the in-app message is sent, it can be viewed one time.

![][1]

| Option | Description | Example |
|---|---|---|
| Message expires after specified period | The first option allows you to expire the in-app message relative to when the step becomes available to the user. | For example, an in-app message with a two-day expiration would become available after the step's delay elapses and audience options are checked. It would then be available for 2 days (48 hours) and during those two days, users may see the in-app message if they open the app. |
| Message expires by specified date | The second option allows you to choose a specific date and time when the in-app message will be no longer available. | For example, if you have a sale that ended at a specific date and time, you might select this option so that users no longer see the associated in-app message when the sale ends. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Use cases

You can use in-app messages in your promotional and onboarding Canvases.

{% tabs %}
  {% tab Promotional %}

Promotions, coupons, and sales often have hard expiration dates. The following Canvas should alert your users at the most opportune times that there is a promotion they may use, and perhaps influence a purchase. This promotion expires on February 28, 2019, at 11:15 am in the company's time zone.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Canvas Step</th>
    <th>Delay</th>
    <th>Audience</th>
    <th>Channel</th>
    <th>Expiration</th>
    <th>Advancement</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Day 1: 50% off</td>
    <td>None</td>
    <td>All from entry</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Advance Audience After Delay</td>
    <td>Initial push that alerts your users of the promotion. This is meant to drive users to your app to take advantage of the promotion.</td>
  </tr>
  <tr>
    <td>In-app: 50% off</td>
    <td>None</td>
    <td>All from entry</td>
    <td>In-app message</td>
    <td><b>Expires by:</b> 2/28/2019 11:15 AM Company Time</td>
    <td>In-App Message Viewed</td>
    <td>The user has now opened the app and will receive this message whether or not that was because of the push message before.</td>
  </tr>
  <tr>
    <td>50% off reminder</td>
    <td>1 day after the user receives the previous step</td>
    <td>All from entry <br><br><b>Filter:</b> Last made a purchase more than one week ago</td>
    <td>In-app message</td>
    <td><b>Expires by:</b> 2/28/2019 11:15 AM Company Time</td>
    <td>None (last message in Canvas)</td>
    <td>The user has received the in-app message in the previous step but has not made a purchase despite being in the app. <br><br>This message is meant to further draw the user to make a purchase using the promotion.</td>
  </tr>
</tbody>
</table>

As you can see, the in-app messages expire when the promotion expires to prevent any discrepancies between the messaging and the customer experience.

  {% endtab %}
  {% tab User Onboarding %}

Your first impression with a user is, perhaps, your most critical one. It can make or break future visits to your app. Your initial communications with your user should be sensibly timed and encourage frequent visits to your app to promote usage.

<table class="tg">
<thead>
  <tr>
    <th>Canvas Step</th>
    <th>Delay</th>
    <th>Audience</th>
    <th>Channel</th>
    <th>Expiration</th>
    <th>Advancement</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Welcome email</td>
    <td>None</td>
    <td>All from entry</td>
    <td>Email</td>
    <td>N/A</td>
    <td>Advance Audience after Delay</td>
    <td>Initial email that welcomes your users to a project, membership, or other onboarding program. <br><br>This is intended to drive users to your app to begin their onboarding.</td>
  </tr>
  <tr>
    <td>Day 3–6 in-app message</td>
    <td>3 days after the user receives the previous step</td>
    <td>All from entry</td>
    <td>In-app message</td>
    <td><b>Expires:</b> 3 days after the step becomes available</td>
    <td>In-App Message Live</td>
    <td>If the user has acted upon the email and been driven to the app, they will receive the desired in-app message to continue or remind them of their onboarding and any requirements associated with it.</td>
  </tr>
  <tr>
    <td>Day 5 push </td>
    <td>2 days after the user receives the previous step</td>
    <td>All from entry</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Message Sent</td>
    <td>After users have received their in-app message, they will receive a follow-up push to continue their onboarding.</td>
  </tr>
</tbody>
</table>

As you can see, the push messages are spaced around an in-app message to ensure that the user has visited the app and begun their onboarding. This will prevent any annoying spam or out-of-order messaging that could dissuade users from visiting your app, and instead create a flowing, sensible order to their initial experiences with your app.

  {% endtab %}
{% endtabs %}

### Advancement behavior options

In Canvas, Message steps automatically advance all users who enter the step. To use the **Advance when message sent** option, add a separate [Audience Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) to filter users that didn't receive the previous step.

{% details Original Canvas editor behavior %}

{% alert important %}
You can no longer create or duplicate Canvases using the original editor. This section is available for reference when understanding how advancement behavior works for steps with in-app messages.
{% endalert %}

Canvases created in the original editor need to specify an advancement behavior—the criteria for advancement through your Canvas component. [Steps with only in-app messages](#steps-iam-only) have different advancement options than [steps with multiple message types](#steps-multiple-channels) (push, email, etc.). For in-app messages in a Canvas Flow workflow, this option is set to always immediately advance the audience.

Action-based delivery is not available for Canvas steps with in-app messages. Canvas steps with in-app messages must be scheduled. Instead, Canvas in-app messages will appear the first time that your user opens the app (triggered by the start session) after the scheduled message in the Canvas component has been sent to them.

If you have multiple in-app messages within one Canvas, a user must start multiple sessions to receive each of those individual messages.

{% alert important %}
In-app messages can't be triggered by events in Canvas.
{% endalert %}

![][2]

{% alert important %}
When **Advance When In-App Message Live** is selected, the in-app message will be available until it expires, even if the user has moved to subsequent steps. If you do not want the in-app message to be live when the next steps in the Canvas are delivered, ensure that the expiration is shorter than the delay on subsequent steps.
{% endalert %}

#### Steps with multiple channels {#steps-multiple-channels}

Steps with an in-app message and another channel have the following advancement options:

| Option | Description |
|---|---|---|
| Advance When Message Sent | Users must be sent an email, webhook, or push notification, or view the in-app message to advance to subsequent steps in the Canvas.  <br> <br>  If the in-app message expires and the user hasn't been sent the email, webhook, or push, or hasn't viewed the in-app message, they will exit the Canvas and will not advance to subsequent steps. |
| Immediately Advance Audience | Everyone in the step's audience advances to the next steps after the delay elapses, whether they have seen the noted message or not.  <br> <br> Users must match the step's segment and filter criteria to advance to the next steps. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

{% alert important %}
When **Entire Audience** is selected, the in-app message will be available until it expires, even if the user has moved to subsequent steps. If you don't want the in-app message to be live when the next steps in the Canvas are delivered, check that the expiration is shorter than the delay on subsequent steps.
{% endalert %}

{% enddetails %}

## Prioritizing in-app messages

A customer may trigger two in-app messages within your Canvas at the same time. When this happens, Braze will adhere to the following priority order to determine which in-app message is displayed. Drag different Canvas steps to reorder their priority. By default, steps earlier in a Canvas variant will display before later steps.

![]({% image_buster /assets/img_archive/step_priority.png %}){: style="max-width:80%"}

Go to the **Send Settings** of the Canvas section to prioritize in-app messages from a Canvas against in-app messages from other Canvases and campaigns.

![]({% image_buster /assets/img_archive/canvas_send_settings.png %})

By default, Canvas component priority is set to medium, with the most recently created steps having the highest relative priority. Canvas and campaign-level priorities also default to medium, with the highest relative priority defaulting to the most recently created items.

![]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="max-width:85%"}

### Drafts of an active Canvas

When editing a draft of an active Canvas, changes to the in-app message priority within **Send Settings** are not saved with a draft. These changes are applied directly to the active Canvas when the priority sorter modal is closed. However, in a Message step, the priority sorter will be updated when a user launches the draft since step settings apply at a step level.

## Custom event properties in a Canvas

Action-based delivery isn't available for Canvas steps with in-app messages. This means you also can't use custom event properties for these steps. 

To template event properties in Canvas, we recommend storing your event properties as custom attributes in your first Canvas step and personalizing your in-app message with the custom attributes in the second step.


[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
[2]: {% image_buster /assets/img/iam-advancement-behavior.png %} "IAM Live"
[3]: {% image_buster /assets/img/push-advancement-behavior.png %} "IAM Live"
