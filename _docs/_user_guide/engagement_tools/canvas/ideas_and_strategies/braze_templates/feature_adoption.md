---
nav_title: Feature Adoption
article_title: Feature adoption template
page_order: 3
page_type: reference
description: "This article describes use a Braze Canvas template to deliver timely personalized messages to highlight the benefits and usage tips."
tool: Canvas
---

# Feature adoption template

> This template is designed to drive usage of your new features, existing products, additional offerings, or any other area you'd like your customers to experience. By leveraging personalized communication and a structured set of messages, you can seamlessly introduce new features to users and get valuable feedback from them.

## Tutorial overview

In this tutorial, you'll learn how to use the **Feature adoption** template, which is intended for the retention and loyalty stages of the user lifecycle, to drive usage of a new feature in your app $PLACEHOLDER-APP-NAME, a $PLACEHOLDER-APP-DESCRIPTION. Your new feature is $PLACEHOLDER-FEATURE. After this article, you'll have $PLACEHOLDER-ACCOMPLISHMENTS.

As a member of the marketing team at $PLACEHOLDER-COMPANY, your goal is to $PLACEHOLDER-GOALS. To do so, you want to focus on $PLACEHOLDER-STEPS.

## Prerequisites

Before you start, you'll need to:

- [Create a custom event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events) for your new feature
- $PLACEHOLDER
- $PLACEHOLDER

## Step 1: Choose the template

When you [create a new Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas), select **Use a Canvas Template**.

![ALT_TEXT]()

Select **Braze templates**. Next to **Feature Adoption**, select **Apply Template**.

![ALT_TEXT]()

## Step 2: Define a conversion event

<!-- Is a conversion event different from the custom event for the new feature that's used in the previous step? If so, how? -->

<!--
UX note: I keep seeing alerts in my template that i need a conversion event, but it doesn't point me to where that is or what that is. after searching in braze docs, none of the pages that mention conversion events actually show an image of this feature so i still don't know what i'm looking for. 

Follow up: I was able to figure this out. See the next paragraph below for how to do this.
-->

To use an experiment path, you need to define a conversion event. Ideally, the conversion event is the event that signals feature adoption. If the top window isn't already open, select **Expand**. Next to **Conversion Events**, select **Edit**.

![ALT_TEXT]()

Under **Assign Conversion Events**, select **Add Conversion Event** and fill out your conversion event. When you're finished, select **Save as draft**.

## Step 3: Exclude existing users

First, edit your entry rules to exclude users who have already used it. This is important because $PLACEHOLDER. To do so, under **Entry Rules**, select **Audience**, then add a new filter using the [custom event you created for this feature](#prerequisites).

For example, $PLACEHOLDER company let a few users beta test their new wishlist feature a few weeks ago, so they'll exclude them by using their **Add item to wishlist** custom event as a filter.

![The 'Target Audience' step with the filter: 'Has [Add item to wishlist] exactly 0 times.]()

When you're finished, select **Save as draft**.

<!-- Should we show them out to set up exit criteria? -->

## Step 4: Add events to the action path

Why $PLACEHOLDER? Under **Action Path**, select **Activated Feature**, then choose a custom event.

<!-- What kind of custom event? -->

![ALT_TEXT]()

Next, select **Taken Tour**. Rename this action to better match your feature, then choose a custom event for this action step. For example, $PLACEHOLDER company named theirs **Added Item to Wishlist**. When you're finished, select **Done**.

<!-- What kind of custom event? -->

![ALT_TEXT]()

Under **Assess Usage**, select **Used Feature >3x**, then choose a custom event. When you're finished, select **Done**.

<!-- What kind of custom event? Also, should they rename this "Action Group Name" and add a trigger? -->

![ALT_TEXT]()

## Step 5: Create a feedback survey

<!-- Since IAM requires pre-set up, lets remove IAM references and only use email -->

Why $PLACEHOLDER? Under **Feedback Survey**, select **Message** > **In-App Messages**.

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

## Step 6: Create an FAQ

Why $PLACEHOLDER? Under **FAQ Copy**, select **Messages**, then write your FAQ message. To use a Braze template, select **Choose new template**.

For example, $PLACEHOLDER company wrote the following:

![ALT_TEXT]()

## Step 7: Create a reminder

Why $PLACEHOLDER? Under **Reminder Copy**, select **Messages**.

![ALT_TEXT]()

For example, $PLACEHOLDER company wrote the following:

![ALT_TEXT]()

## Step 8: Test and launch the Canvas

Before you launch your Canvas, its always best practice to test it first. <!-- (Does testing actually send to someone?) --> To start testing, select **Test Canvas**.

![ALT_TEXT]()

You can either test your Canvas using a random user or you can search for a specific user instead. For a random user, select **Get Random User**. When you're ready select **Run Test**.

![ALT_TEXT]()

If you like what you see and you're ready to launch, select **Launch Canvas**.

![ALT_TEXT]()
