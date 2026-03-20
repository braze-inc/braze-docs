---
nav_title: Feature adoption
article_title: Feature Adoption
page_order: 3
page_type: reference
description: "This article describes how to use a Braze Canvas template to deliver timely personalized messages to highlight the benefits and usage tips."
tool: Canvas
---

# Feature adoption

> This template is designed to drive usage of your new features, existing products, additional offerings, or any other area you'd like your customers to experience. By leveraging personalized communication and a structured set of messages, you can seamlessly introduce new features to users and get valuable feedback from them. 

In this article, we'll walk you through a use case for the **Feature Adoption** template, which is intended for the retention and loyalty stages of the user lifecycle. After this article, you'll have customized a user journey that encourages users to use new features and collects user sentiment.

## Prerequisites

To successfully use this template, you'll need to a [custom event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) that references when users have used the feature.

## Tailoring the template to your needs

Let's say you work at Calorie Rocket, a food delivery app, that recently launched Cruise Control, a feature for scheduling recurring food deliveries, and you want to encourage more users to adopt this new feature. In our example, we'll use the custom event `scheduled_delivery` to track when users have tried the Cruise Control feature.

To access the back-in-stock template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Feature Adoption**, select **Apply Template**. Now, we can go through the template to fit it for our needs.

### Step 1: Set up the details

Let’s adjust the Canvas details to reflect our goal.

1. Select **Edit** next to the template name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2. Update the Canvas name to specify that the Canvas is for targeting users to collect user feedback.
3. Update the description to specify that the Canvas is for encouraging users to submit feedback and track user sentiment for the new Cruise Control feature.
4. Add the tag **Feature adoption** so that we can filter for it on the Canvas home page.

![The new name and description for the Canvas. The new description states: 'A feature adoption Canvas to track adoption and user sentiment for Cruise Control, a feature for scheduling recurring food deliveries.']({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Step 2: Assign a conversion event

Next, let's add a conversion event for our Canvas to signal feature adoption. This will allow us to tailor the Experiment Path in our user journey later.

1. Under **Assign Conversion Events**, select **Add Conversion Event**.
2. Under **Primary Conversion Event - A**, select **Performs Custom Event** as the **Conversion event type**.
3. Select our custom event `scheduled_delivery`.
4. We'll keep the conversion deadline as three days.

![The conversion event window in the Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Step 3: Tailor the entry schedule

Our goal is to encourage our users to adopt Cruise Control, but we don't want our messaging to be too frequent. So, we'll keep this Canvas as a scheduled delivery and make the following adjustments to the **Time-Based Options** section.

1. Update **Entry Frequency** to **Weekly**.
2. Keep the recurrence as is.
3. Select **Mon** to target users at the beginning of the week.
4. Select the start time for our Canvas.
5. Update the **Ending parameters** to end the Canvas on the last day of the year.

We'll keep the option to allow users to enter the Canvas in their local time zone.

### Step 4: Select the target audience

Now, let's set up our target audience by updating the following details in the template:

1. Select the **All Users** segment.
2. Remove the template's additional filters. 
3. Create this filter using our custom event: `Has scheduled_delivery for exactly 0 times`. This allows us to exclude users who have already used the feature from entering our Canvas.

![The segment for all users who have not used Cruise Control.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4. Keeping in mind that Calorie Rocket previously allowed a few users to beta test the new feature Cruise Control, we'll update the exit criteria to exclude these users from entering the Canvas.

### Step 5: Select your send settings

We’ll keep the default subscription settings, so we only send to users who have subscribed or opted into receiving messages or notifications, and skip the other settings (frequency capping, quiet hours, and seed groups).

### Step 6: Customize your Canvas

#### Build out the Action Path

Next, let's build out the first Action Path step, which is meant to indicate whether our users have an interest in the new feature. We'll make the following adjustments to the template:

1. Since the Cruise Control feature is only available after an order has been added to a cart, we'll name the first action group **Added to cart** and select `added_to_cart` for the custom event.

![The action group name set to "Added to cart" and the "Perform Custom Event" set to "added_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2. Keep the second action group **Taken Tour** as is since we want to evaluate whether users have taken a tour of the app, and if they have, then they'll advance to the second path.
3. For the subsequent Action Path named **Assess Usage**, replace **Used Feature >3x** with **Viewed Cruise Control settings**.
4. Select the **Perform Custom Event** dropdown, then select `scheduled_delivery` for the custom event.

![The action group name set to 'Used Feature >3x' and the 'Perform Custom Event' set to 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Set up feedback survey

Next, we'll go to the Message step named **Feedback Survey** to include our feedback survey for our users to fill out after using Cruise Control for the first time. Our survey response options for our are users are:

- **Loved it!**
- **Not for me.**

1. For the two survey choices, select **Experience Feedback** as our custom attribute to capture and track feedback on Cruise Control. This custom attribute will have two values to represent the survey responses (`good` and `bad`).
2. Update the attribute values to match the survey options. This will allow us to track a user's response.

### Step 7: Test and launch your Canvas

After testing and reviewing our Canvas to make sure it works as expected, select **Launch Canvas** to launch the Canvas. Now, we can target users with a personalized user journey to encourage them to adopt our new feature Cruise Control.

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}
