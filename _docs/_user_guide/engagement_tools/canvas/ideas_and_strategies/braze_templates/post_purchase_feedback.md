---
nav_title: Post-Purchase Feedback
article_title: Post-purchase feedback template
page_order: 2
page_type: reference
description: "This article describes use a Braze Canvas template to orchestrate personalized experiences that allow you to respond to feedback and build a relationship with your users."
tool: Canvas
---

# Post-purchase feedback template

> This template is designed to gain critical insight into how your customers interact with your brand and ensure they continue to have positive experiences. By leveraging personalized communication and a structured set of messages, you can continue to build and foster your customer relationships.

## Tutorial overview

In this tutorial, you'll learn how to use the **Purchase feedback** template, which is intended for the $PLACEHOLDER stage of the user lifecycle, to gain critical insight into how your customers interact with your app $PLACEHOLDER-APP-NAME, a $PLACEHOLDER-APP-DESCRIPTION. After this article, you'll have $PLACEHOLDER-ACCOMPLISHMENTS.

As a member of the marketing team at $PLACEHOLDER-COMPANY, your goal is to $PLACEHOLDER-GOALS. To do so, you want to focus on $PLACEHOLDER-STEPS.

## Prerequisites

Before you start, you'll need to:

- [Create a custom attribute value]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) for $PLACEHOLDER-WHY?
- An ad account?
- $PLACEHOLDER

## Step 1: Choose the template

When you [create a new Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas), select **Use a Canvas Template**.

![ALT_TEXT]()

Select **Braze templates**. Next to **Post-Purchase Feedback**, select **Apply Template**.

![ALT_TEXT]()

## Step 2: Write a follow-up feedback message

<!-- Since IAM requires pre-set up, lets remove IAM references and only use email -->

Why $PLACEHOLDER? Under **Follow-up Feedback**, select **Messages** > **In-App Message**. 

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

## Step 3: Add custom attributes to the action path

Next add the custom attribute [you created earlier](#prerequisites) to each sentiment CTA link, so you can capture which option the user choose when they gave feedback. To add custom attributes:

1. Under **Feedback Action**, select **Good feedback**, then choose your custom attribute value.
   
![ALT_TEXT]()

{:start="2"}
2. Next, select **Bad feedback**, then choose your custom attribute value.

![ALT_TEXT]()

{:start="3"}
3. When you're finished select **Done**, then **Save as draft**.

## Step 4: Create messages for each feedback path

Why $PLACEHOLDER? Under the **Feedback Action** step, create a message for **Good feedback**, **Bad feedback**, and **Everyone else** by selecting **Messages** and filling out a message. When you're finished select **Done**, then **Save as draft**.

![ALT_TEXT]()

## Step 4: Set up ad retargeting

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

## Step 5: Set up webhook support cases

Why $PLACEHOLDER? Under **Support Case Creation**, select **Messages**.

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

## Step 6: Test and launch the Canvas

Before you launch your Canvas, its always best practice to test it first. <!-- (Does testing actually send to someone?) --> To start testing, select **Test Canvas**.

![ALT_TEXT]()

You can either test your Canvas using a random user or you can search for a specific user instead. For a random user, select **Get Random User**. When you're ready select **Run Test**.

![ALT_TEXT]()

If you like what you see and you're ready to launch, select **Launch Canvas**.

![ALT_TEXT]()
