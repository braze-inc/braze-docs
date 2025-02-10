---
nav_title: Context 
article_title: Context 
alias: /context/
page_order: 1.5
page_type: reference
description: "This reference article covers how to create and use Context steps in your Canvas."
tool: Canvas

---

# Context

> Context steps allow you to use dynamic user information and set variables using Liquid. By adding a Context step as part of your user journey, you can do things like delay messages based on user attributes, or segment your users based on event properties in the [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) step.

{% alert important %}
Context steps are currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

## How it works

Each Context step is composed of a property name and associated data type, or context properties (previously referred to as Canvas entry properties). These properties will follow a user through a Canvas. These properties can be accessed using the Liquid `canvas_properties`.

![A Context step as the first step of a Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

There are two ways to set context properties:

- **At Canvas entry:** Properties of events or API calls that trigger a user's entry into a Canvas are stored as context properties.
- **Using a Context step:** You can create or update context properties in the step editor.

## Creating a Context step

To create a Context step, add a step to your Canvas. Then, drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Context**.

### Defining context properties

1. Give your Context property a name.
2. Select a data type.
3. Enter a Liquid expression or select the **Add Personalization** button. This generates a Liquid snippet to use in your Liquid expression.
4. Select **Preview** to view the context property.
5. Select **Done** to save the step.

You can use Context properties anywhere you can use Liquid, such as in Message and User Update steps, with the **Add Personalization** button.

## Context property types

Canvas Context properties that are created or updated in the step can be assigned types. Note that if the Liquid expression at runtime returns a value that doesn’t match the type, the context property won’t be updated.

For example, if the context property data type is set to **Date** but the value isn’t a date, then the property won’t be updated. This means the following will occur:

- The user will either advance to the next step or exit the Canvas if it’s the last step in the Canvas.
- In your Canvas step analytics, this will be counted as *Not Updated*.

## Using context properties with other Canvas steps

You can add personalized delay options with the information from the Context step, meaning you can select the property that delays users.

Let's say we want to remind our customers to purchase toothpaste 30 days from now. Using a combination of a Context step and a Delay step, we can select this context property to delay by. In this case, our Context step would have the following fields:

- **Context property name:** product_reminder_interval
- **Data type:** Time
- **Value:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![The "product_reminder_interval" and its value.][2]

Next, because we want to remind our customers 30 days from now, we'll select **Until a specific day** as the delay option and select **Personalize delay** to use the information from our Context step. This means our users will be delayed until the selected Context property.

![Example of using context properties with a Delay step to delay users based on the "product_reminder_interval".][3]


[1]: {% image_buster /assets/img/context_step3.png %}
[2]: {% image_buster /assets/img/context_step1.png %}
[3]: {% image_buster /assets/img/context_step2.png %}