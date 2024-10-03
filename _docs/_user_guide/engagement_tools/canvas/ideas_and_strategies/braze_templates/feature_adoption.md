---
nav_title: Feature Adoption
article_title: "Tutorial: Feature adoption template"
page_order: 3
page_type: reference
description: "This article describes use a Braze Canvas template to deliver timely personalized messages to highlight the benefits and usage tips."
tool: Canvas
---

# Tutorial: Feature adoption template

> This template is designed to drive usage of your new features, existing products, additional offerings, or any other area you'd like your customers to experience. By leveraging personalized communication and a structured set of messages, you can seamlessly introduce new features to users and get valuable feedback from them.

## Meet your guide

In this tutorial, you'll work alongside **Calorie Rocket**, a food delivery app for when you need your calories and you need 'em fast. Recently they launched Cruise Control, a feature for scheduling recurring food deliveries, and they're looking to start tracking feature adoption and user sentiment in Braze.

Together, you'll learn how to use the **Feature Adoption** template, so you can drive usage for new features during the retention and loyalty stages of the user lifecycle. When you're finished, you'll be able to:

- Create conversion events
- Exclude specific users from entering a Canvas
- Customize your action path
- Collect user feedback

## Prerequisites

Before you start, you'll need to complete the following:

|Prerequisite|Description|
|------------|-----------|
|Custom attribute|You can create a custom attribute value in the Braze dashboard. For more information, see [Managing custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).|
|$PLACEHOLDER|$PLACEHOLDER|
{: .reset-td-br-1 .reset-td-br-2}

## Customizing the template

### Step 1: Choose the template

When you [create a new Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas), select **Use a Canvas Template**.

![The Canvas page in the Braze dashboard, with 'Use a Canvas Template' highlighted.]({% image_buster /assets/img/canvas_templates/use_a_canvas_template.png %})

Select **Braze templates**, then next to **Feature Adoption**, select **Apply Template**.

![The list of Braze Canvas templates with 'Feature Adoption' highlighted.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_feature_adoption_template.png %})

To rename the Canvas, select **Edit** next to the existing Canvas name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %})

Enter a new name and description for your Canvas. Calorie Rocket named theirs "Cruise Control: Feature Adoption" to match the name of their new feature for scheduling recurring deliveries. When you're finished, select **Save Draft**.

![The new name and description for the Canvas. The new description states: 'A feature adoption Canvas to track adoption and user sentiment for Cruise Control, a feature for scheduling recurring food deliveries.']({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %})

### Step 2: Assign a conversion event

Before you can use an experiment path, you need to assign a conversion event that signals feature adoption. To assign a conversion event, select **Expand** if the top window isn't already open. Next to **Conversion Events**, select **Edit**.

![The conversion event window in the Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/edit_conversion_event.png %})

Under **Assign Conversion Events**, select **Add Conversion Event**.

![The 'Assign Conversion Events' section in the Canvas details.]({% image_buster /assets/img/canvas_templates/feature_adoption/add_conversion_event.png %})

For **Conversion event type**, select **Performs Custom Event**, choose the event [you created earlier](#prerequisites), then finish filling out your conversion event. Here's what Calorie Rocket filled out:

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

When you're finished, select **Save as draft**.

### Step 3: Exclude existing users

Calorie Rocket let a few users beta test their new feature a few weeks back, so they want to exclude them from entering the Canvas. This is a good time for you to filter out existing users too.

Under **Entry Rules**, select **Audience**.

![The 'Entry Rules' section of the Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_audience_entry_rules.png %})

Under **Additional Filters**, create a filter using the event [you created earlier](#prerequisites). Here's what Calorie Rocket did:

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

When you're finished, select **Save as draft**.

### Step 4: Customize the action paths

The action paths let you define your user paths based on a specific action, including user engagement events and custom events. Under **Action Path**, select **Activated Feature**.

![The action path in the Canvas with 'Activated Feature' and 'Taken Tour' displaying an orange badge to indicate that more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_1.png %})

Replace the **Action Group Name** to the action that _precedes_ the custom event [you created earlier](#prerequisites), then select the preceding action from the **Perform Custom Event** dropdown. Since Calorie Rocket's "Cruise Control" feature is only available after an order has been added to a cart, they named their first action group "Added to cart" and assigned the "added_to_cart" custom event.

![The action group name set to 'Added to cart' and the 'Perform Custom Event' set to 'added_to_cart'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %})

Next, select **Taken Tour**. Replace the **Action Group Name** to the custom event [you created earlier](#prerequisites), then select that event from the **Perform Custom Event** dropdown. When you're finished, select **Done** > **Save as draft**.

![The action group name set to 'Scheduled recurring delivery' and the 'Perform Custom Event' set to 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_scheduled_recurring_delivery.png %})

Back in the Canvas, connected to **Action Path**, you'll find **Assess Usage**. Select **Used Feature >3x** so you can $PLACEHOLDER_WHY?

![The action path in the Canvas with 'Used Feature >3x' displaying an orange badge to indicate that more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_2.png %})

Select the **Preform Custom Event** dropdown, then choose the custom event [you created earlier](#prerequisites). When you're finished, select **Done** > **Save as draft**.

![The action group name set to 'Used Feature >3x' and the 'Perform Custom Event' set to 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %})

### Step 5: Create a feedback survey

Next you'll create a feedback survey for users to fill out after they've used your new feature for the first time. Under **Feedback Survey**, select **Messages**.

![The 'Feedback Survey' section in the Canvas with the 'Messages' preview window displaying an orange badge indicating more information is needed before the Canvas can be launched.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_feedback_survey.png %})

Calorie Rocket doesn't have In-App Messages set up yet, so they're going to remove it as an option from the feedback survey. If you already have In-App Messages configured in [the Braze SDK]($PLACEHOLDER_URL), feel free to leave this option and customize your message. Otherwise, hover your mouse over the **In-App Messages** tab and select **Remove Variant**.

![The 'In-App Messages' tab showing the option to remove the variant.]({% image_buster /assets/img/canvas_templates/remove_iam_for_feedback_survey.png %})

In the **Email** tab, fill out the **Sending info**, then select **Edit message** to start crafting your feedback survey. Calorie Rocket used [Braze AI]($PLACEHOLDER_URL) to help write their email. Here's what they wrote:

![$PLACEHOLDER: We'll need an image here of a semi-branded email for Calorie Rocket.]()

When you're finished, select **Done** > **Save as draft**.

### Step 6: Finish personalizing the Canvas

Now that you've created your feedback survey, all required steps to test and launch your Canvas are complete. However, there's still a few more steps you'll need to personalize.

Use the skills you've learned so far and finish personalizing your Canvas. Also, be sure to save often, so you don't lose any work!

<!-- Consider converting this to a table, and writing a short explanation + any relevant links in the right column -->
- Feature Introduction Message
- Reminder w/ Tips Message
- FAQ vs. Reminder

### Step 7: Test and launch the Canvas

Before you launch your Canvas, its always best practice to test it first. To start testing, select **Test Canvas**.

![The Canvas footer with 'Test Canvas', 'Save as draft', and 'Launch Canvas' displayed.]({% image_buster /assets/img/canvas_templates/select_test_canvas.png %})

{% alert tip %}
For a full walkthrough, see [Sending test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/).
{% endalert %}

You can either test your Canvas using a random user or you can search for a specific user instead. When you're ready select **Run Test** and follow the prompts on the screen. After you're finish testing, select **Done**.

![The testing page for the Canvas with a test user selected.]({% image_buster /assets/img/canvas_templates/select_run_test.png %})

If you like what you see and you're ready to officially launch your Canvas, select **Launch Canvas**. Congratulations on launching your first feature adoption Canvas!
