---
nav_title: Post-purchase feedback
article_title: Post-Purchase Feedback
page_order: 6
page_type: reference
description: "This article describes how to use a Braze Canvas template to orchestrate personalized experiences that allow you to respond to feedback and build a relationship with your users."
tool: Canvas
---

# Post-purchase feedback

> Use the post-purchase feedback template to gain critical insight into how your customers interact with your brand and ensure they continue to have positive experiences. By leveraging personalized communication and a structured set of messages, you can continue to build and foster your customer relationships.

This article will walk you through a use case for the **Post-Purchase Feedback** template, which is designed for the conversion step of the user lifecycle. When you’re finished, you’ll have created a Canvas that encourages users to provide feedback for your app.

## Prerequisites

To successfully use this template, you'll need the following:

- A [custom attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) to reference for feedback survey results.
- A configured [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) with the partners and audiences you use.

## Tailoring the template to your needs

Let's say we're working for Decorumsoft, a mobile video game developer. We'll use the post-purchase feedback template to gauge feedback for our latest video game launch, Proxy War 3: War of Thirst. Using this feedback, we'll inform our development plans for the expansion pack, Liquid Mirage.

Before creating the Canvas, we set up the [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) integration so that we can add user data from Braze to Google Audiences to send advertisements based on behavioral triggers, segmentation, and more.

To access the post-purchase feedback template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Post-Purchase Feedback**, select **Apply Template**. Now, we can go through the template to fit it for our needs.

### Step 1: Set up Canvas details

Let's adjust the Canvas details to reflect our goal.

1. Select **Edit** next to the template name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2. Update the Canvas name to specify that the Canvas is for targeting recent users. 
3. Update the description to specify that the Canvas is for encouraging users to submit feedback.
4. Add the tag **Feedback** to filter for it on the Canvas home page.

![The new name and description for the Canvas. The new description states: 'A post-purchase feedback Canvas to gauge interest for the upcoming expansion for PWD3, Liquid Mirage.']({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### Step 2: Assign conversion events

Next, let's assign our conversion events. Update the **Primary Conversion Event - A** to **Make a specific purchase** and select **Proxy War**.

!["Assign Conversion Events" section for the conversion event type of purchasing Proxy War game product.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

We'll keep the template's conversion deadline of three days because we want to target our most recent users.

### Step 3: Set an entry schedule

1. Keep the entry schedule type as **Action-Based**.
2. Set the **Start Time** for the entry window to the date the game launches.

### Step 4: Determine who enters the Canvas

Our target audience for feedback is users who have recently purchased Proxy War 3.

1. Select our target segment, "Purchased Proxy War 3", which consists of users who’ve purchased the game.
2. Select a filter to include users who have purchased "Proxy War 3" more than “0” times.

![A segment named "Purchased Proxy War 3" that segments users who have purchased the game.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3. Update the entry controls to not allow users to re-enter the Canvas after the Canvas’s maximum duration.

### Step 5: Select your send settings

We’ll keep the default subscription settings, so we only send to users who have subscribed or opted into receiving messages or notifications. 

Because we want to be mindful with our sending, we'll select **Enable Quiet Hours** to avoid requesting feedback between 11 pm and 10 am in our users' time zone and only send at the next available time.

!["Send Settings" step targeting users who are subscribed or opted in. Quiet Hours are turned on.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

For our example, we'll skip the other settings (frequency capping and seed groups).

### Step 6: Customize your Canvas

Next, we'll build our Canvas by customizing the messaging channels and the content that will send to users. Because we're only seeking feedback using email, in-app message, and webhook channels, we'll go through the template and remove the SMS variants from the Message steps.

We'll begin our customization by going through each messaging component to update the content. Our custom attribute to reference is `Experience Feedback`.

1. In the Canvas builder, select the first Message step in the user journey.
2. Select the **Email** variant.
3. Fill out the **Sending info** with a subject that encourages user feedback. 
4. Select **Edit message** to replace the template's email message with our feedback survey message. This includes replacing the links for each call-to-action to capture which option is selected, which will be referenced in the Action Path step of our user journey.

{% alert tip %}
You can use [Canvas entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) to customize the messages in your Canvas based on which product you're referring to.
{% endalert %}

#### Set up feedback survey

Next, we'll need to fill out the details for the **In-App Message** variant. This is where we need to specify our `Experience Feedback` custom attribute that indicates the sentiment of our user feedback. (We'll also reference this in the subsequent Action Path step.)

1. In the same first Message step, select the **In-App Messages** variant. We'll keep the message controls as is. 
2. For the header and body, we'll use language to encourage users to be honest about their experience with Proxy War 3.
3. Because we want their survey responses to be logged with their profiles, we'll keep the survey as **Single-choice selection** and **Log attributes upon submission**.
4. For each of the three survey choices, select **Experience Feedback** as our custom attribute. 
5. We'll keep the attribute values on the user profile as is since these values align with our custom attribute.

![A survey that asks the user if they enjoyed their recent purchase of Proxy War 3 with three options: "Loved it", "It was OK", and "Not for me".]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Build out the Action Path

Using our custom attribute `Experience Feedback` and the attribute values from the previous section, we'll update the template's Action Path to match our attribute and values.

![The "Good feedback" group for the Action Path step that includes users who responded "Loved it" to our survey.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Set up ad retargeting

We'll make sure our Google Audience sync is set up in our **Ad Retargeting** step. This will include selecting our ad account, an existing audience, and the option to add users to the audience.

### Set up webhook support cases

Next, let's set up the webhook to trigger potential support cases. This can be especially insightful in combination with analyzing our user feedback.

For Message step named **Support Case Creation**, we'll update the template to compose a webhook for users who are unsatisfied with their purchase and want a refund.

![A webhook that creates support cases for customers who have a negative sentiment and want a refund for their purchase of Proxy War 3.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### Step 6: Test and launch the Canvas

After testing and reviewing our Canvas to make sure it works as expected, select **Launch Canvas** to launch the Canvas. Now, we can mindfully target users with a personalized user journey to encourage them to respond to our feedback survey based on their recent purchase of Proxy War 3!

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}
