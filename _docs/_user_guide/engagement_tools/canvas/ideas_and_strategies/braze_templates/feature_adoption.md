---
nav_title: Feature Adoption
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

To successfully use this template, you'll need the following:

- A custom attribute to reference. This can be created in the Braze dashboard. For more information, see [Managing custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).

To access this template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates** > **Feature Adoption**. 

## Tailoring the template to your needs

Let's say you're a marketer at Calorie Rocket, a food delivery app, that recently launched Cruise Control, a feature for scheduling recurring food deliveries, and you want to encourage your users to adopt this new feature.

### Step 1: Set up details

In the template, we'll do the following:

1. Update the Canvas name to specify that the Canvas is for targeting users to collect user feedback.
2. Update the description to specify that the Canvas is for encouraging users to submit feedback and track user sentiment for the new Cruise Control feature.

![The new name and description for the Canvas. The new description states: 'A feature adoption Canvas to track adoption and user sentiment for Cruise Control, a feature for scheduling recurring food deliveries.']({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %})

### Step 2: Assign a conversion event

Next, let's assign our conversion event. For **Conversion event type**, select **Performs Custom Event**, choose the event [you created earlier](#prerequisites), then fill out the details of your conversion event.

Here's what we filled out for Calorie Rocket:

<table>
  <tr>
    <td><strong>Conversion event type</strong></td>
    <td>Performs Custom Event</td>
  </tr>
  <tr>
    <td><strong>Custom event name</strong></td>
    <td>Scheduled recurring delivery</td>
  </tr>
  <tr>
    <td><strong>Conversion deadline</strong></td>
    <td>2 days</td>
  </tr>
</table>

### Step 3: Exclude existing users

In our scenario, Calorie Rocket previously allowed a few users to beta test their new feature, so we want to exclude these users from entering the Canvas.

To do so, go to **Entry Rules** and select **Audience**.

![The 'Entry Rules' section of the Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_audience_entry_rules.png %})

In **Additional Filters**, create a filter using the event [you created earlier](#prerequisites).

<table>
  <tr>
    <td><strong>Filter</strong></td>
    <td>Custom Event</td>
  </tr>
  <tr>
    <td><strong>Custom Event</strong></td>
    <td>Scheduled recurring delivery</td>
  </tr>
  <tr>
    <td><strong>Frequency</strong></td>
    <td>Exactly 0 times</td>
  </tr>
</table>

### Step 4: Customize the Action Path

The Action Path lets you define your user paths based on a specific action, including user engagement events and custom events. In **Action Path**, select **Activated Feature**.

![The action path in the Canvas with 'Activated Feature' and 'Taken Tour' displaying an orange badge to indicate that more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_1.png %})

Replace the **Action Group Name** to the action that _precedes_ the custom event [you created earlier](#prerequisites), then select the preceding action from the **Perform Custom Event** dropdown.

Since the Cruise Control feature is only available after an order has been added to a cart, we named the first action group **"Added to cart"** and assigned the `added_to_cart` custom event.

![The action group name set to "Added to cart" and the "Perform Custom Event" set to "added_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %})

Next, select **Taken Tour**. Replace the **Action Group Name** to the custom event [you created earlier](#prerequisites), then select that event from the **Perform Custom Event** dropdown.

![The action group name set to 'Scheduled recurring delivery' and the 'Perform Custom Event' set to 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_scheduled_recurring_delivery.png %})

For **Assess Usage**, select **Used Feature >3x**. Next, select the **Preform Custom Event** dropdown, then choose the custom event [you created earlier](#prerequisites).

![The action group name set to 'Used Feature >3x' and the 'Perform Custom Event' set to 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %})

### Step 5: Create a feedback survey

Next, create a feedback survey for users to fill out after they've used your new feature for the first time. Under **Feedback Survey**, select **Messages**.

![The 'Feedback Survey' section in the Canvas with the 'Messages' preview window displaying an orange badge indicating more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_feedback_survey.png %})

In our scenario, we'll remove in-app messages as an option from the feedback survey and only use email. In the **Email** tab, fill out the **Sending info**, then select **Edit message** to start crafting the feedback survey.

Now that you've created your feedback survey, all required steps to test and launch your Canvas are complete.

### Step 6: Test and launch the Canvas

After testing and reviewing our Canvas to make sure it works as expected, select **Launch Canvas** to launch the Canvas. Now, we can mindfully target users with a personalized user journey to encourage them to adopt new features for your app!

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}
