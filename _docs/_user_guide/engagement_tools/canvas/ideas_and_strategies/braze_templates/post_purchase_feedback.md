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
|Ad account|$PLACEHOLDER. For more information, see [$PLACEHOLDER](). |
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

<!-- Since IAM requires pre-set up, lets remove IAM references and only use email -->

Under **Follow-up Feedback**, select **Messages** > **In-App Message**. 

![ALT_TEXT]()

Fill out the **Compose** step. $PLACEHOLDER company wrote the following:
<!-- not sure if 'step' is the right word here? -->

|Field|Description|
|-----|-----------|
|Header|$PLACEHOLDER|
|Body|$PLACEHOLDER|
|Helper text|$PLACEHOLDER|
|Choice 1|$PLACEHOLDER|
|Choice 2|$PLACEHOLDER|
|Submit button text|$PLACEHOLDER|
|Submit on-click behavior|$PLACEHOLDER|
{: .reset-td-br-1 .reset-td-br-2}

Next, select **Email**. Fill out your sending info, then select **Edit message** to craft your email. $PLACEHOLDER company wrote the following:

![ALT_TEXT]()

When you're finished, select **Done**.

### Step 3: Add custom attributes to the action path

Next add the custom attribute [you created earlier](#prerequisites) to each sentiment CTA link, so you can capture which option the user choose when they gave feedback. To add custom attributes:

1. Under **Feedback Action**, select **Good feedback**, then choose your custom attribute value.
   
![ALT_TEXT]()

{:start="2"}
2. Next, select **Bad feedback**, then choose your custom attribute value.

![ALT_TEXT]()

{:start="3"}
3. When you're finished select **Done**, then **Save as draft**.

### Step 4: Create messages for each feedback path

Under the **Feedback Action** step, create a message for **Good feedback**, **Bad feedback**, and **Everyone else** by selecting **Messages** and filling out a message. When you're finished select **Done**, then **Save as draft**.

![ALT_TEXT]()

### Step 5: Set up ad retargeting

Before you can set up ad retargeting, you need to select a partner for Audience Sync. To choose a partner, under **Ad Retargeting**, select **Audience Sync**.

![ALT_TEXT]()

Choose one or more of the listed partners. If you have Audience Sync Pro, you can add any of our [Audience Sync technology partners]({{site.baseurl}}/partners/canvas_steps/overview).

![ALT_TEXT]()

1. Select the ad account [you created earlier](#prerequisites).
2. Choose an audience. Why for each $PLACEHOLDER?
3. Select an action. Why for each $PLACEHOLDER?
4. Choose one or more fields to match.
5. When you're finished select **Done**, then **Save as draft**.

![ALT_TEXT]() 

### Step 6: Set up webhook support cases

Under **Support Case Creation**, select **Messages**.

![ALT_TEXT]()

Compose your Webhook. $PLACEHOLDER company wrote the following:
<!-- not sure if 'step' is the right word here? -->

|Field|Description|
|-----|-----------|
|Webhook URL|$PLACEHOLDER|
|HTTP method|$PLACEHOLDER|
|REquest Body|$PLACEHOLDER|
|Key 1 and Value 1|$PLACEHOLDER|
|Key 2 and Value 2|$PLACEHOLDER|
|Key 3 and Value 3|$PLACEHOLDER|
|Request headers|$PLACEHOLDER|
{: .reset-td-br-1 .reset-td-br-2}

When you're finished select **Done**, then **Save as draft**.

### Step 7: Test and launch the Canvas

Before you launch your Canvas, its always best practice to test it first. <!-- (Does testing actually send to someone?) --> To start testing, select **Test Canvas**.

![ALT_TEXT]()

You can either test your Canvas using a random user or you can search for a specific user instead. For a random user, select **Get Random User**. When you're ready select **Run Test**.

![ALT_TEXT]()

If you like what you see and you're ready to launch, select **Launch Canvas**.

![ALT_TEXT]()
