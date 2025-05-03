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

> Context steps allow you to create and update one or more variables for a user as they move through a Canvas. For example, if you have a Canvas that manages seasonal discounts, you can use a context variable to store a different discount code each time a user enters the Canvas.

{% alert important %}
Context steps are currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

## How it works

![A Context step as the first step of a Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Context steps allows you to create and use temporary data during a user's journey through a specific Canvas. This data exists only within that Canvas journey and doesn't persist across different Canvases or outside the session.

Within this framework, each Context step can define multiple context variables&mdash;temporary pieces of data that enable you to personalize delays, segment users dynamically, and enrich messaging without permanently altering a user's profile information.

For example, if you're managing flight bookings, you could create a context variable for each user's scheduled flight time. You could then set delays relative to each user’s flight time and send personalized reminders from the same Canvas.

You can set context variables in two ways:

- **At Canvas entry:** When users enter a Canvas, data from the event or API trigger can automatically populate context variables.
- **In a Context step:** You can define or update context variables manually inside the Canvas by adding a Context step.

Each context variable includes:

- A name (such as `flight_time` or `subscription_renewal_date`)
- A [data type](#context-variable-types) (such as number, string, time, or array)
- A value you assign using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) or through the **Add Personalization** tool.

When defined, you can use a context variable throughout the Canvas by referencing it in this format: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

For example,
{% raw %}`{{context.${flight_time}}}{% endraw %}` could return the user’s scheduled flight time.

Each time a user enters the Canvas&#8212;even if they have entered it before&#8212;the context variables will be redefined based on the latest entry data and Canvas setup. This allows journeys to stay personalized and accurate, even for users with multiple entries.

## Creating a Context step

### Step 1: Add a step

Add a step to your Canvas, then drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button and select **Context**.

### Step 2: Define the variables

{% alert note %}
You can define up to 10 context variables for each Context step.
{% endalert %}

To define a context variable:

1. Give your context variable a **name**.
2. Select a [data type](#context-variable-types).
3. Write a Liquid expression manually or use **Add Personalization** to create a Liquid snippet from pre-existing attributes.
4. Select **Preview** to check the value of your context variable.
5. (Optional) To additional variables, select **Add Context variable** and repeat steps 1–4.
6. When you're finished, select **Done**.

Now you can use your context variable anywhere you use Liquid, such as in Message and User Update steps, by selecting **Add Personalization**. For a full walkthrough, see [Using context variables](#using-context-variables).

### Step 3: Test user paths (optional)

If the context variable is valid, you can reference the variable throughout your Canvas. However, if the context variable wasn't created correctly, future steps in your Canvas won't perform correctly either. We recommend testing and [previewing your user paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) to make sure your messages are sent to the right audience. Look out for common scenarios that create [invalid context variables](#troubleshooting).

For example, if you create a Context step to assign users an appointment time but set the appointment time's value to a past date, the reminder email you craft in your Message step will never be sent. 

## Context variable data types {#context-variable-types}

Context variables that are created or updated in the step can be assigned the following data types.

{% alert note %}
Context variables have the same expected formats for data types as [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format), but context variables do not support nested objects.
{% endalert %}

| Data type | Example variable name | Example value |
|---|---|---|
|Boolean| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Number| credit_score |{% raw %}<code>740{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Time| last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Object (flattened) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Using context variables {#using-context-variables}

For example, let's say you want to notify passengers about their VIP lounge access before their upcoming flight. This message should only be sent to members of the Rewards Club or passengers who purchased a first-class ticket. Whereas membership status is something you'd track on the user profile, a first-class ticket purchase is more temporary. A context variable is a flexible way to track this information.

Users will enter the Canvas when they check in for their flight. To determine lounge access eligibility, we'll create a context variable called `lounge_access_granted` in a Context step, then reference that context variable in subsequent steps of the user journey.

![Context variable set up to track if a passenger qualifies for VIP lounge access.][2]{: style="max-width:90%"}

In this Context step, we'll use decision logic to set `lounge_access_granted` to `true` if either:

- The user is a Rewards Club member (checked against their user profile attribute)
- The user has purchased a first-class ticket (determined from the Canvas entry event data)

Next, we'll create an audience group to target users where {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} is `true`. Then, we'll set up a Message step for this audience to create a push notification that includes personalized lounge information. 

Based on this context variable, eligible passengers will receive information about accessing the exclusive VIP lounge before their flight.

![An audience group step with lounge_access_granted set to true.][3]{: style="max-width:90%"}

{% alert tip %}
You can add [personalized delay options]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) with the information from the Context step, meaning you can select the variable that delays users.
{% endalert %}

## Converting Connected Content strings to JSON

When making a [Connected Content call]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) in a Context step, JSON returned from the call will be evaluated as a string data type for consistency and error prevention. If you want to convert this string into JSON, convert it by using `as_json_string`. For example:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Troubleshooting {#troubleshooting}

### Invalid context variables

A context variable is considered invalid when:
- A call to an embedded Connected Content fails.
- The Liquid expression at runtime returns a value that doesn't match the data type or is empty (null).

For example, if the context variable data type is **Number** but the Liquid expression returns a string, it is invalid.

In these circumstances: 
- The user will advance to the next step. 
- The Canvas step analytics will count this as _Not Updated_.

When troubleshooting, monitor the _Not Updated_ metric to check that your context variable is updating correctly. If the context variable is invalid, your users can continue in your Canvas past the Context step, but may not qualify for later steps.

Refer to [Context variable data types](#context-variable-types) for the example setups for each data type.

## Frequently asked questions

### How do context variables differ from Canvas entry properties?

If you're participating in the Context step early access, Canvas entry properties are now included as Canvas context variables. This means you can send Canvas entry properties using the Braze API and reference them in other steps, similar to using a context variable with the Liquid snippet.

### Can variables reference each other in a singular Context step?

Yes. All variables in a Context step are evaluated in a sequence, meaning you could have the following context variables setup:

| Context variable | Value | Description |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | A user's favorite type of cuisine. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | The available discount code for a user. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{promo_code}} "on delivery from your favorite" {{favorite_cuisine}} restaurants!"`{% endraw %} | A personalized message that combines the previous variables. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

In a Message step, you could use the Liquid snippet {% raw %}`{{context.${personalized_message}}}`{% endraw %} to reference the context variable to deliver a personalized message to each user.

This also applies across multiple Context steps. For example, imagine this sequence:
1. An initial Context step creates a variable called `JobInfo` with the value `job_title`.
2. A Message step references {% raw %}`{{context.${JobInfo}}}`{% endraw %} and displays `job_title` to the user.
3. Later, a Context step updates the context variable, changing the value of `JobInfo` to `job_description`.
4. All subsequent steps that reference `JobInfo` will now use the updated value `job_description`.

Context variables use their most recent value throughout the Canvas, with each update affecting all following steps that reference that variable.


[1]: {% image_buster /assets/img/context_step3.png %}
[2]: {% image_buster /assets/img/context_example1.png %}
[3]: {% image_buster /assets/img/context_example2.png %}