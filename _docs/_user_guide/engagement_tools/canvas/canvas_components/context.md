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

> Use Context steps to create or update a set of variables that represent the context of a user (or insights into that user’s behavior) as they move through a Canvas. Each context variable includes a name, data type, and a value that can include Liquid. By setting context as part of your user journey, you can delay messages or filter users based on context variables.

{% alert important %}
Context steps are currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

## How context works

Each Context step is composed of a variable name and associated data type, or context variables. These variables will follow a user through their Canvas journey and can be accessed using the Liquid `context`.

{% alert note %}
You can define up to 10 context variables for each Context step.
{% endalert %}

![A Context step as the first step of a Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

There are two ways to set context variables:

- **At Canvas entry:** Variables of events or API calls that trigger a user’s entry into a Canvas are stored as context variables.
- **Using a Context step:** You can create or update context variables in the step editor.

Any variables included in the context variable aren’t automatically stored in the user profile, as context variables exist only within the context of a user’s journey through a Canvas. This means a user can have different context variables each time they enter a Canvas. For example, if you have a Canvas that manages flight bookings, you could use a context variable to store a different flight confirmation code each time a user enters the Canvas.

## Creating a Context step

To create a Context step, add a step to your Canvas. Then, drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Context**.

### Defining context variables

1. Give your context variable a name.
2. Select a data type.
3. Enter a Liquid expression or select the **Add Personalization** button.
4. Select **Preview** to view the context variable.
5. Select **Done** to save the step.

You can use Context variables anywhere you can use Liquid, such as in Message and User Update steps, with the **Add Personalization** button.

#### Context variable types

Canvas Context variables that are created or updated in the step can be assigned the following data types:

- Boolean
- Number
- String
- Array
- Time
- Object

Note that if the Liquid expression at runtime returns a value that doesn’t match the type, the context variable won’t be updated. For example, if the context variable data type is set to **Number** but the value can’t be parsed as a number and is a string instead, the variable won’t be updated, and the following will occur:

- The user will either advance to the next step or exit the Canvas if it’s the last step in the Canvas. 
- For the Canvas step analytics, this is counted as _Not Updated_. 

### How users exit Context steps

Users can exit a Canvas for the following reasons:

- The context variable doesn't return any value (is null).
- A call to an embedded Connected Content fails.
- The context variable types don't match.

## JSON types and Connected Content responses

For consistency and error prevention, JSON returned by a Connected Content call will be evaluated as a string data type. If you want to convert this string into JSON, convert it by using `as_json_string`. An example is:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Using context variables

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

![A Message step for a push notification with a discount code for a user's favorite product category.][3]{: style="max-width:90%"}

Based on the user's favorite category, they'll receive an exclusive discount code to use.

### Using context variables with Delay steps

You can add [personalized delay options]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) with the information from the Context step, meaning you can select the variable that delays users.

## Frequently asked questions

### How do context variables differ from Canvas entry properties?

If you’re participating in the Context step early access, Canvas entry properties are now part of Canvas context variables, meaning `canvas_entry_properties` is now referenced as `context`. This also means you can send Canvas entry properties using the Braze API and reference them in other steps, similar to using a context variable with the Liquid snippet.

### Can variables reference each other in a singular Context step?

Yes. All variables in a Context step are evaluated in a sequence, meaning you could have the following context variables setup:

| Context variable | Liquid | Description |
|---|---|---|
|`favorite_restaurants`| {% raw %}`{{user.favorite_categories}}`{% endraw %} | A user's favorite restaurant category. |
|`promo_code`| {% raw %}`{{user.favorite_categories}}`{% endraw %} | The available discount code for a user. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{promo_code}} "on delivery from your favorite" {{favorite_restaurants}} restaurants!"`{% endraw %} | A personalized message that combines the previous variables. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

In a Message step, you could use the Liquid snippet {% raw %}`{{context.${personalize_message}}}`{% endraw %} to reference the context variable to deliver a personalized message to each user.

This also applies to multiple Context steps. For example, if Context step A defines Variable A, and Message step A uses Variable A, then Context step C updates Variable A to B, then all subsequent steps referencing Variable A will have the value of B.

[1]: {% image_buster /assets/img/context_step3.png %}
[2]: {% image_buster /assets/img/context_example1.png %}
[3]: {% image_buster /assets/img/context_example2.png %}
