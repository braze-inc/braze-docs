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

> Use Context steps to create or update a set of variables for a user as they move through a Canvas. <br><br>Context variables exist only within the user's journey through the Canvas, providing a lightweight way to define data without adding to user profiles. This means a user can have different context variables each time they enter the Canvas. For example, if you have a Canvas that manages flight bookings, you could use a context variable to store a different flight confirmation code each time a user enters the Canvas.

{% alert important %}
Context steps are currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

## How it works

![A Context step as the first step of a Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Each Context step defines a context variable: a piece of custom data that only follows a user throughout their user journey in this Canvas. A context variable includes a variable name and an associated data type, and can be referenced in a Canvas using the Liquid snippet {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

There are two ways to set context variables:

- **At Canvas entry:** Variables from events or API calls that trigger a user's entry into a Canvas are stored as context variables.
- **Using a Context step:** You can create or update context variables in the step editor.

## Creating a Context step

### Step 1: Add a step

Add a step to your Canvas, then drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button and select **Context**.

### Step 2: Define the variable

To define Context step's variable:

1. Give your context variable a name.
2. Select a [data type](#context-variable-types).
3. Write a Liquid expression or select **Add Personalization** to create a Liquid snippet from pre-existing attributes.
4. To view the context variable, select **Preview**.
5. When you're finished, select **Done**.

{% alert note %}
You can define up to 10 context variables for each Context step.
{% endalert %}

Now you can use your Context variable anywhere you use Liquid, such as in Message and User Update steps, by selecting **Add Personalization**. For a full walkthrough, see [Using a context variable](#using-context-variables).

### Step 3: Test exit criteria (optional)

If the context variables are valid, you can reference the variables throughout your Canvas. However, your users can exit the steps in a user journey after a Context step for the following reasons:

- The context variable doesn't return any value (is null).
- A call to an embedded Connected Content fails.
- The context variable types don't match.

We recommend testing and [previewing your user paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) to make sure your messages are sent to the right audience.

## Context variable data types {#context-variable-types}

Canvas Context variables that are created or updated in the step can be assigned the following data types.

{% alert note %}
Context variables have the same expected formats for data types as [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format), but context variables do not support nested objects.
{% endalert %}

| Data type | Example value and format | 
|---|---|
|Boolean| {::nomarkdown}<ul><li><b>Context variable name:</b> loyalty_program</li><li><b>Value:</b> {% raw %}<code>{{custom_attribute.${active_member}}}</code>{% endraw %}</li><li><b>Expected value:</b> `true`</li></ul>{:/} |
|Number| {::nomarkdown}<ul><li><b>Context variable name:</b> credit_score</li><li><b>Value:</b> {% raw %}<code>{{custom_attribute.${Credit Score}}}</code>{% endraw %}</li><li><b>Expected value:</b> 751</li></ul>{:/} |
|String| {::nomarkdown}<ul><li><b>Context variable name:</b> product_name</li><li><b>Value:</b> {% raw %}<code>{{custom_attribute.${Product}}}</code>{% endraw %}</li><li><b>Expected value:</b> lotion</li></ul>{:/} |
|Array| {::nomarkdown}<ul><li><b>Context variable name:</b> favorite_products</li><li><b>Value:</b> {% raw %}<code>{{custom_attribute.${Favorites}}}</code>{% endraw %}</li><li><b>Expected value:</b> <code>["moisturizer", "serum", "lipstick"]</code></li></ul>{:/} |
|Time| {::nomarkdown}<ul><li><b>Context variable name:</b> last_purchase_date</li><li><b>Value:</b> {% raw %}<code>{{custom_attribute.${Last Purchase Date}}}</code>{% endraw %}</li><li><b>Expected value:</b> 2025-01-28T17:02:43.032Z</li></ul>{:/} |
|Object| {::nomarkdown}<ul><li><b>Context variable name:</b> customer_profile</li><li><b>Value:</b> {% raw %}<code>{{custom_attribute.${Product}}}</code>{% endraw %}</li><li><b>Expected value:</b> lotion</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Using context variables {#using-context-variables}

For example, let's say you want to send your users personalized recommendations about discounts for cosmetic products in your retail brand. These users will enter the Canvas if they haven't made a purchase yet. The first step of the user journey will be a Delay step for one day to allow time for users to consider their purchase.

To provide these recommendations based on their preferences, we'll create two context variables in the Context step to reference in the subsequent steps of the user journey:

- `favorite_category`
- `discount_code`

![Two context variables set up to track a user's favorite category and the associated discount code.][2]{: style="max-width:90%"}

Next, we'll set up a Message step for push notifications that includes the discount code for their favorite product category. The Liquid snippets for the context variables will be:

{% raw %}
- `{{context.${discount_code} | default: 'SPRING10'}}` 
- `{{context.${favorite_category} | default: 'sitewide'}}`
{% endraw %}

Based on the user's favorite category, they'll receive an exclusive discount code to use.

![A Message step for a push notification with a discount code for a user's favorite product category.][3]{: style="max-width:90%"}

{% alert tip %}
You can add [personalized delay options]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) with the information from the Context step, meaning you can select the variable that delays users.
{% endalert %}

## Converting strings to JSON

For consistency and error prevention, JSON returned by a [Connected Content call]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) will be evaluated as a string data type. If you want to convert this string into JSON, convert it by using `as_json_string`. For example:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Troubleshooting

### Mismatched data types

If the Liquid expression at runtime returns a value that doesn't match the data type, the context variable won't be updated. For example, if the data type is set to **Number** but the value returns a string, the variable won't be updated, and the following will occur:

- The user will either advance to the next step or exit if it's the last step in the Canvas. 
- The Canvas step analytics will count this as _Not Updated_.

Refer to [Context variable data types](#context-variable-types) for the expected values and examples for each data type.

## Frequently asked questions

### How do context variables differ from Canvas entry properties?

If you're participating in the Context step early access, Canvas entry properties are now part of Canvas context variables, meaning `canvas_entry_properties` is now referenced as `context`. This also means you can send Canvas entry properties using the Braze API and reference them in other steps, similar to using a context variable with the Liquid snippet.

### Can variables reference each other in a singular Context step?

Yes. All variables in a Context step are evaluated in a sequence, meaning you could have the following context variables setup:

| Context variable | Value | Description |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | A user's favorite type of cuisine. |
|`promo_code`| {% raw %}`{{custom_attribute.${coupon_code}}}`{% endraw %} | The available discount code for a user. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{promo_code}} "on delivery from your favorite" {{favorite_cuisine}} restaurants!"`{% endraw %} | A personalized message that combines the previous variables. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

In a Message step, you could use the Liquid snippet {% raw %}`{{context.${personalized_message}}}`{% endraw %} to reference the context variable to deliver a personalized message to each user.

This also applies to multiple Context steps. For example, if Context step A defines Variable A as `job_title`, and Message step A uses Variable A, then Context step C updates Variable A to be `job_description`, then all subsequent steps referencing Variable A will have the value of `job_description`.

[1]: {% image_buster /assets/img/context_step3.png %}
[2]: {% image_buster /assets/img/context_example1.png %}
[3]: {% image_buster /assets/img/context_example2.png %}
