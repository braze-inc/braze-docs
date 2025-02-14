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

> Use Context steps to create or update a set of variables that represent the context of a user (or insights into that user's behavior) as they move through a Canvas. Each context variable includes a name, data type, and a value that can include Liquid. By setting context as part of your user journey, you can do things like delay messages or filter users based on context variables.

{% alert important %}
Context steps are currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

## How it works

Each Context step is composed of a variable name and associated data type, or context variables (previously referred to as Canvas entry properties). These variables will follow a user through a Canvas and can be be accessed using the Liquid `canvas_variables`.

![A Context step as the first step of a Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

There are two ways to set context variables:

- **At Canvas entry:** Variables of events or API calls that trigger a user's entry into a Canvas are stored as context variable.
- **Using a Context step:** You can create or update context variables in the step editor.

## Creating a Context step

To create a Context step, add a step to your Canvas. Then, drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Context**.

### Defining context variables

1. Give your Context variable a name.
2. Select a data type.
3. Enter a Liquid expression or select the **Add Personalization** button. This generates a Liquid snippet to use in your Liquid expression.
4. Select **Preview** to view the context variable.
5. Select **Done** to save the step.

You can use Context variables anywhere you can use Liquid, such as in Message and User Update steps, with the **Add Personalization** button.

## Context variable types

Canvas Context variables that are created or updated in the step can be assigned types. Note that if the Liquid expression at runtime returns a value that doesn’t match the type, the context variable won’t be updated.

For example, if the context variable data type is set to **Date** but the value isn’t a date, then the variable won’t be updated. This means the following will occur:

- The user will either advance to the next step or exit the Canvas if it’s the last step in the Canvas.
- In your Canvas step analytics, this will be counted as *Not Updated*.

## Using context variables with other Canvas steps

You can add personalized delay options with the information from the Context step, meaning you can select the variable that delays users.

Let's say we want to remind our customers to purchase toothpaste 30 days from now. Using a combination of a Context step and a Delay step, we can select this context variable to delay by. In this case, our Context step would have the following fields:

- **Context variable name:** product_reminder_interval
- **Data type:** Time
- **Value:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![The "product_reminder_interval" and its value.][2]

Next, because we want to remind our customers 30 days from now, we'll select **Until a specific day** as the delay option and select **Personalize delay** to use the information from our Context step. This means our users will be delayed until the selected Context variable.

![Example of using context variables with a Delay step to delay users based on the "product_reminder_interval".][3]


[1]: {% image_buster /assets/img/context_step3.png %}
[2]: {% image_buster /assets/img/context_step1.png %}
[3]: {% image_buster /assets/img/context_step2.png %}