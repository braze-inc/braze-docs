---
nav_title: Post-Purchase Feedback
article_title: "Tutorial: Post-purchase feedback template"
page_order: 2
page_type: reference
description: "This article describes use a Braze Canvas template to orchestrate personalized experiences that allow you to respond to feedback and build a relationship with your users."
tool: Canvas
---

# Tutorial: Post-purchase feedback template

> This template is designed to gain critical insight into how your customers interact with your brand and ensure they continue to have positive experiences. By leveraging personalized communication and a structured set of messages, you can continue to build and foster your customer relationships.

## Meet your guide

In this tutorial, you'll work alongside **Decorumsoft**, a mobile video game developer founded in 1981 who recently launched "Proxy War 3: War of Thirst". Due to the game's critical success, they want to start gauging interest for their upcoming expansion: "Liquid Mirage".

Together, you'll learn how to use the **Purchase Feedback** template to gain critical insight into how customers interact with your app during the conversion stage of the user lifecycle. When you're finished, you'll be able to:

- Create follow-up feedback messages
- Customize your action path
- Build ad retargeting pipelines
- Use webhooks to trigger support cases

## Prerequisites

Before you start, you'll need to complete the following:

|Prerequisite|Description|
|------------|-----------|
|Custom attribute|You can create a custom attribute value in the Braze dashboard. For more information, see [Managing custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).|
|Ad account|Audience Sync requires an ad account. For more information, see [Audience Sync]({{site.baseurl}}/partners/canvas_steps/overview/#use-cases). |
{: .reset-td-br-1 .reset-td-br-2}

## Customizing the template

### Step 1: Choose and rename the template

When you [create a new Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas), select **Use a Canvas Template**.

![The Canvas page in the Braze dashboard, with 'Use a Canvas Template' highlighted.]({% image_buster /assets/img/canvas_templates/use_a_canvas_template.png %})

Select **Braze templates**, then next to **Feature Adoption**, select **Apply Template**.

![The list of Braze Canvas templates with 'Post-Purchase Feedback' highlighted.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_post_purchase_feedback_template.png %})

To rename the Canvas, select **Edit** next to the existing Canvas name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %})

Enter a new name for your Canvas. Decorumsoft named theirs "Liquid Mirage: Post-Purchase Feedback" to match the name of the upcoming expansion. When you're finished, select **Save Draft**.

![The new name and description for the Canvas. The new description states: 'A post-purchase feedback Canvas to gauge interest for the upcoming expansion for PWD3, Liquid Mirage.']({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %})

### Step 2: Write a follow-up feedback message

Next you'll create a follow-up feedback survey for users you recently purchased your product. Under **Follow-up Feedback**, select **Messages**. 

![The 'Follow-up Feedback' section in the Canvas with the 'Messages' preview window displaying an orange badge to indicate that more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/follow_up_feedback_message.png %})

Decorumsoft doesn't have In-App Messages set up yet, so they're going to remove it as an option from the feedback survey. If you already have In-App Messages configured in [the Braze SDK]($PLACEHOLDER_URL), feel free to leave this option and customize your message. Otherwise, hover your mouse over the **In-App Messages** tab and select **Remove Variant**.

![The 'In-App Messages' tab showing the option to remove the variant.]({% image_buster /assets/img/canvas_templates/remove_iam_for_feedback_survey.png %})

In the **Email** tab, fill out the **Sending info**, then select **Edit message** to start crafting your feedback survey. Decorumsoft used [Braze AI]($PLACEHOLDER_URL) to help write their email. Here's what they wrote:

![$PLACEHOLDER: We'll need an image here of a semi-branded email for Decorumsoft.]()

When you're finished, select **Done** > **Save as draft**.

### Step 3: Customize the action path

Next, you'll add the custom attribute [you created earlier](#prerequisites) to each sentiment Call to Action (CTA) link, so you can capture which option the user choose when they gave feedback.

Under **Feedback Action**, select **Good feedback**.
   
![The 'Feedback Action' section in the Canvas with 'Good feedback' and 'Bad feedback' displaying an orange badge to indicate that more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/feedback_action.png %})

Select the **Choose An Attribute** dropdown, choose the custom attribute [you created earlier](#prerequisites), then select **any new value**.

![The custom attribute set to 'Change Custom Attribute [$PLACEHOLDER] to [any new value]'.]()

Next, select **Bad feedback**. Select the **Choose An Attribute** dropdown, choose the custom attribute [you created earlier](#prerequisites), then select **any new value**.

![The custom attribute set to 'Change Custom Attribute [$PLACEHOLDER] to [any new value]'.]()

When you're finished select **Done**, then **Save as draft**.

### Step 4: Set up ad retargeting

Before you can set up ad retargeting, you need to choose a partner for your Audience Sync. Under **Ad Retargeting**, select **Audience Sync**.

![The 'Ad Retargeting' section in the Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/ad_retargeting_audience_sync.png %})

Choose one or more of the default partners. Alternatively, if you have Audience Sync Pro, you can choose any of the [Braze Audience Sync technology partners]({{site.baseurl}}/partners/canvas_steps/overview).

![The default list of partners for Audience Sync.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/choose_audience_sync_partner.png %})

To finish setting up Audience Sync:

1. Select the ad account [you created earlier](#prerequisites).
2. Choose an audience.
3. Select an action.
4. Choose one or more fields to match.
5. When you're finished select **Done**, then **Save as draft**.

### Step 5: Set up webhook support cases

Next, you'll set up a webhook to trigger potential support cases. Under **Support Case Creation**, select **Messages**.

![The 'Support Case Creation' section in the Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/support_case_creation.png %})

Compose your Webhook. For a full tutorial, see [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook). Here's what Decorumsoft did:

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

### Step 6: Finish personalizing the Canvas

Now that you've created your feedback survey, all required steps to test and launch your Canvas are complete. However, there's still a few more steps you'll need to personalize.

Use the skills you've learned so far and finish personalizing your Canvas. Also, be sure to save often, so you don't lose any work!

<!-- Consider converting this to a table, and writing a short explanation + any relevant links in the right column -->
- Good feedback: Discount offer message
- Bad feedback: Negative experience message
- Everyone else: No offer message

### Step 7: Test and launch the Canvas

Before you launch your Canvas, its always best practice to test it first. To start testing, select **Test Canvas**.

![The Canvas footer with 'Test Canvas', 'Save as draft', and 'Launch Canvas' displayed.]({% image_buster /assets/img/canvas_templates/select_test_canvas.png %})

{% alert tip %}
For a full walkthrough, see [Sending test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/).
{% endalert %}

You can either test your Canvas using a random user or you can search for a specific user instead. When you're ready select **Run Test** and follow the prompts on the screen. After you're finish testing, select **Done**.

![The testing page for the Canvas with a test user selected.]({% image_buster /assets/img/canvas_templates/select_run_test.png %})

If you like what you see and you're ready to officially launch your Canvas, select **Launch Canvas**. Congratulations on launching your first feature adoption Canvas!
