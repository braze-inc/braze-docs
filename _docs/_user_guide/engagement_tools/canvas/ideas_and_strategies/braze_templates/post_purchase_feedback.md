---
nav_title: Post-Purchase Feedback
article_title: Post-Purchase Feedback
page_order: 2
page_type: reference
description: "This article describes how to use a Braze Canvas template to orchestrate personalized experiences that allow you to respond to feedback and build a relationship with your users."
tool: Canvas
---

# Post-purchase feedback

> Use the post-purchase feedback template to gain critical insight into how your customers interact with your brand and ensure they continue to have positive experiences. By leveraging personalized communication and a structured set of messages, you can continue to build and foster your customer relationships.

This article will walk you through a use case for the **Post-Purchase Feedback** template, which is designed for the conversion step of the user lifecycle. When you’re finished, you’ll have created a Canvas that encourages users to provide feedback for your app.

## Prerequisites

To successfully use this template, you'll need the following:

- A custom attribute to reference. This can be created in the Braze dashboard. For more information, see [Managing custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).
- A configured [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps) with the partners and audiences you use.

## Tailoring the template to your needs

Let's say we're working for Decorumsoft, a mobile video game developer. We can use the post-purchase feedback to gauge interest for "Liquid Mirage", an expansion for their most recent success, "Proxy War 3: War of Thirst".

Before creating the Canvas, we set up the [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) integration so that we can add user data from Braze to Google Audiences to send advertisements based on behavioral triggers, segmentation, and more.

Now, we can go through the template to fit it for our needs.

### Step 1: Set up Canvas details

In Braze, go to **Messaging** > **Canvas**. Select **Create Canvas**, then select **Use a Canvas Template**.

![The Canvas page in the Braze dashboard, with 'Use a Canvas Template' highlighted.]({% image_buster /assets/img/canvas_templates/use_a_canvas_template.png %}){: style="max-width:90%;"}

Select **Braze templates**, then next to **Feature Adoption**, select **Apply Template**.

![The list of Braze Canvas templates with 'Post-Purchase Feedback' highlighted.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_post_purchase_feedback_template.png %}){: style="max-width:90%;"}

To rename the Canvas, select **Edit** next to the existing Canvas name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:60%;"}

Update the Canvas name to specify that the Canvas is for targeting users who recently interacted with your brand. Then, update the description to specify that the Canvas is for encouraging users to submit feedback for the new Liquid Mirage video game.

![The new name and description for the Canvas. The new description states: 'A post-purchase feedback Canvas to gauge interest for the upcoming expansion for PWD3, Liquid Mirage.']({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Step 2: Write a follow-up feedback message

Next, you'll create a follow-up feedback survey for users you recently purchased your product. Under **Follow-up Feedback**, select **Messages**. 

![The 'Follow-up Feedback' section in the Canvas with the 'Messages' preview window displaying an orange badge to indicate that more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/follow_up_feedback_message.png %}){: style="max-width:25%;"}

In our scenario, we'll remove in-app messages as an option from the post-purchase feedback survey and only use email. In the **Email** tab, fill out the **Sending info**, then select **Edit message** to start crafting the feedback survey. When you're finished, select **Done** > **Save as draft**.

### Step 3: Customize the action path

Next, you'll add the custom attribute [you created earlier](#prerequisites) to each sentiment Call to Action (CTA) link, so you can capture which option the user choose when they gave feedback. Under **Feedback Action**, select **Good feedback**.
   
![The 'Feedback Action' section in the Canvas with 'Good feedback' and 'Bad feedback' displaying an orange badge to indicate that more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/feedback_action.png %}){: style="max-width:25%;"}

Select the **Choose An Attribute** dropdown, choose the custom attribute [you created earlier](#prerequisites), then select **any new value**.

![The custom attribute set to 'Change Custom Attribute [$PLACEHOLDER] to [any new value]'.]()

Next, select **Bad feedback**. Select the **Choose An Attribute** dropdown, choose the custom attribute [you created earlier](#prerequisites), then select **any new value**. When you're finished select **Done**, then **Save as draft**.

![The custom attribute set to 'Change Custom Attribute [$PLACEHOLDER] to [any new value]'.]()

### Step 4: Set up ad retargeting

Before you can set up ad retargeting, you need to choose a partner for your Audience Sync. Under **Ad Retargeting**, select **Audience Sync**.

![The 'Ad Retargeting' section in the Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/ad_retargeting_audience_sync.png %}){: style="max-width:25%;"}

Choose one or more of the default partners. Alternatively, if you have Audience Sync Pro, you can choose any of the [Braze Audience Sync technology partners]({{site.baseurl}}/partners/canvas_steps/overview).

![The default list of partners for Audience Sync.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/choose_audience_sync_partner.png %}){: style="max-width:65%;"}

To finish setting up Audience Sync:

1. Select the ad account [you created earlier](#prerequisites).
2. Choose an audience.
3. Select an action.
4. Choose one or more fields to match.

### Step 5: Set up webhook support cases

Next, you'll set up a webhook to trigger potential support cases. Under **Support Case Creation**, select **Messages**.

![The 'Support Case Creation' section in the Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/support_case_creation.png %}){: style="max-width:25%;"}

Compose your Webhook. For a full tutorial, see [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook). Here's what we did:

<table>
  <tr>
    <td><strong>Webhook URL</strong></td>
    <td>$PLACEHOLDER</td>
  </tr>
  <tr>
    <td><strong>HTTP method</strong></td>
    <td>$PLACEHOLDER</td>
  </tr>
  <tr>
    <td><strong>Request Body</strong></td>
    <td>$PLACEHOLDER</td>
  </tr>
  <tr>
    <td><strong>Key 1 and Value 1</strong></td>
    <td>$PLACEHOLDER</td>
  </tr>
  <tr>
    <td><strong>Key 2 and Value 2</strong></td>
    <td>$PLACEHOLDER</td>
  </tr>
  <tr>
    <td><strong>Key 3 and Value 3</strong></td>
    <td>$PLACEHOLDER</td>
  </tr>
  <tr>
    <td><strong>Request headers</strong></td>
    <td>$PLACEHOLDER</td>
  </tr>
</table>

When you're finished select **Done**, then **Save as draft**.

### Step 6: Test and launch the Canvas

After testing and reviewing our Canvas to make sure it works as expected, select **Launch Canvas** to launch the Canvas. Now, we can mindfully target users with a personalized user journey to encourage them to respond with feedback!

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}
