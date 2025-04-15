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

Each Context step is composed of a variable name and associated data type, or context variables (previously referred to as Canvas entry properties). These variables will follow a user through a Canvas and can be be accessed using the Liquid `context`.

![A Context step as the first step of a Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

There are two ways to set context variables:

- **At Canvas entry:** Variables of events or API calls that trigger a user's entry into a Canvas are stored as context variable.
- **Using a Context step:** You can create or update context variables in the step editor.

Note that any variables included in the context variable aren't automatically stored in the user profile.

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

Braze will exit a user at the step if:

- The context variable doesn't return any value.
- A call to an embedded Connected Content fails.
- The context variable types don't match.

### JSON types and Connected Content responses

Braze evaluates context variables that are expected to be JSON (or Object)-type from Connected Content responses into strings. To prevent context variables from being evaluated as strings, enter these results into this Liquid filter: `as_json_string`. An example is:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Using context variables with Delay steps

You can add [personalized delay options]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) with the information from the Context step, meaning you can select the variable that delays users.

[1]: {% image_buster /assets/img/context_step3.png %}
