---
nav_title: Context 
article_title: Context 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "This reference article covers how to create and use Context steps in your Canvas."
tool: Canvas

---

# Context

> Context steps allow you to create and update one or more variables for a user as they move through a Canvas. For example, if you have a Canvas that manages seasonal discounts, you can use a context variable to store a different discount code each time a user enters the Canvas.

{% alert important %}
Context steps are currently in early access. Contact your Braze account manager if you're interested in participating in this early access.<br><br>Note that opting into the Canvas Context step early access will make changes to how timestamps are handled across all your Canvases. To learn more about this, refer to [Time zone consistency standardization](#time-zone-consistency-standardization).
{% endalert %}

## How it works

![A Context step as the first step of a Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Context steps allow you to create and use temporary data during a user's journey through a specific Canvas. This data exists only within that Canvas journey and doesn't persist across different Canvases or outside the session.

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
{% raw %}`{{context.${flight_time}}}{% endraw %}` could return the user's scheduled flight time.

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

## Context variable data types {#context-variable-types}

Context variables that are created or updated in the step can be assigned the following data types.

{% alert note %}
Context variables have the same expected formats for data types as [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>For nested objects and array of objects, use the [`as_json_string` Liquid filter](#converting-connected-content-strings-to-json). If you're creating the same object in a Context step, you'll need to render the object using `as_json_string`, such as {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Data type | Example variable name | Example value |
|---|---|---|
|Boolean| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Number| credit_score |{% raw %}<code>740{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Time (in UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Object (flattened) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

By default, the time data type is in UTC. If you use a string data type to store a time value, you can define the time as a different time zone like PST. 

For example, if you're sending a message to a user the day before their birthday, you would save the context variable as a time data type because there's Liquid logic associated with sending the day before. However, if you're sending a holiday message on Christmas Day (December 25), you wouldn't need to reference the time as a dynamic variable, so using a string data type would be preferable.

## Using context variables {#using-context-variables}

For example, let's say you want to notify passengers about their VIP lounge access before their upcoming flight. This message should only be sent to passengers who purchased a first-class ticket. A context variable is a flexible way to track this information.

Users will enter the Canvas when they purchase a plane ticket. To determine lounge access eligibility, we'll create a context variable called `lounge_access_granted` in a Context step, then reference that context variable in subsequent steps of the user journey.

![Context variable set up to track if a passenger qualifies for VIP lounge access.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

In this Context step, we'll use {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} to determine if the type of flight they've purchased is `first_class`.

Next, we'll create a Message step to target users where {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} is `true`. This message will be a a push notification that includes personalized lounge information. Based on this context variable, the eligible passengers will receive the relevant messages before their flight.

- First-class ticket passengers will receive: "Enjoy exclusive VIP lounge access!"
- Business and economy ticket passengers will receive: "Upgrade your flight for exclusive VIP lounge access."

![A Message step with different messages to send, depending on the type of plane ticket purchased.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
You can add [personalized delay options]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) with the information from the Context step, meaning you can select the variable that delays users.
{% endalert %}

### For Action Paths and exit criteria

You can leverage comparing property filters with either context variables or custom attributes in these trigger actions: **Perform Custom Event** and **Make Purchase**. These action triggers also support property filters for both basic and nested properties. 

- When comparing against basic properties, the available comparisons will match the type of the property defined by the custom event. For example, string properties will have exactly equal, regex matches. Boolean properties will be true or false. 
- When comparing against nested properties, types are not pre-defined, so you can select comparisons across multiple data types for booleans, numbers, strings, time, and day of year, similar to the comparisons for nested custom attributes. If you select a data type that doesn't match the actual data type of the nested property at the time of comparison, the user will not match the Action Path or exit criteria.

#### Action Path examples

{% alert important %}
For custom attribute comparisons, we'll use the custom attribute value at the time the action is performed. This means a user won't match the Action Path group if a user doesn't have this custom attribute populated at the time of comparison, or if the custom attribute value doesn't match the defined property comparisons. This is the case even if the user would have matched when they entered the Action Path step.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

The following Action Path is set up to sort users who performed the custom event `Account_Created` with the basic property `source` to the context variable `app_source_variable`.

![An example Action Path that references a context variable when performing a custom event.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

The following Action Path is set up to match the basic property `brand` for the specific product name `shoes` to a context variable `promoted_shoe_brand`.

![An example Action Path that references a context variable when making a purchase.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exit criteria examples

{% tabs %}
{% tab Perform custom event %}

The exit criteria states that at any point in a user's journey in the Canvas, they'll exit the Canvas if:

- They perform the custom event **Abandon Cart**, and
- The basic property **Item in Cart** matches the string value of the context variable `cart_item_threshold`.

![Exit criteria set up to exit a user if they perform a custom event based on the context variable.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

The exit criteria states that at any point in a user’s journey in the Canvas, they'll exit the Canvas if:

- They make a specific purchase for the "book" product name, and
- That purchase's nested property "loyalty_program" is equal to the user's custom attribute "VIP".

![Exit criteria set up to exit a user if they make a purchase.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Context variable filters

You can create filters that use previously declared context variables in [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) and [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) steps.

{% alert important %}
Context variable filters are only available for Audience Paths and Decision Split steps. 
{% endalert %}

Context variables are declared and only accessible in the scope of a Canvas, meaning they can't be referenced in segments. Context variable filters function similarly in Audience Paths and Decision Split steps—Audience Path steps represent multiple groups, while Decision Split steps represent binary decisions.

![Decision Split step example with the option to create a filter with a context variable.]({% image_buster /assets/img/context_decision_split.png %})

Similar to how Canvas context variables have pre-defined types, the comparisons between context variables and static values must have [matching data types]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). The context variable filter allows comparisons across multiple data types for booleans, numbers, strings, time, and day of year, similar to the comparisons for [nested custom attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

Here is an example of a context variable filter comparing the context variable `product_name` to the regex `/braze/`.

![A filter setup for the context variable "product_name" to match the regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparing to context variables or custom attributes

By selecting the **Compare to a context variable or custom attribute** toggle, you can construct context variable filters that compare against previously-defined context variables or user custom attributes. This can be useful for performing comparisons that are dynamic per user, like API-triggered `context`, or to condense complex comparison logic defined across context variables.

{% tabs %}
{% tab Example 1 %}

Let's say you want to send a personalized reminder to users after a dynamic period of inactivity, which includes anyone who hasn't logged into your app in the last three days should get a message.

You have a context variable `re_engagement_date` that is defined as `{{now | minus: 3 | append: ' days'}}`. Note that `3 days` can be a variable amount that is also stored as a user's custom attribute. So if the `re_engagement_date` is after the `last_login_date` (stored as a custom attribute on the user profile), they'll be sent a message.

![A filter setup with custom attributes as the personalization type for the context variable "re_engagement_date" after the custom attribute "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

The following filter compares the context variable `reminder_date` to be before the context variable `appointment_deadline`. This can help group users in an Audience Paths step to determine whether they should receive additional reminders before their appointment deadline.

![A filter setup with context variables as the personalization type for the context variable "reminder_date" on the context variable "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Previewing user paths

We recommend testing and previewing your user paths to make sure your messages are sent to the right audience and context variables are evaluated to the expected outcomes.

Be sure to observe any common scenarios that create invalid context variables. When previewing your user path, you can view the outcomes of personalized Delay steps using context variables, and any audience, decision, or Action Path step comparisons that match users to any context variables.

If the context variable is valid, you can reference the variable throughout your Canvas. However, if the context variable wasn’t created correctly, future steps in your Canvas won’t perform correctly either. For example, if you create a Context step to assign users an appointment time but set the appointment time's value to a past date, the reminder email in your Message step will never be sent. 

## Converting Connected Content strings to JSON

When making a [Connected Content call]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) in a Context step, JSON returned from the call will be evaluated as a string data type for consistency and error prevention. If you want to convert this string into JSON, convert it by using `as_json_string`. For example:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Time zone consistency standardization

With the addition of Canvas Context, all timestamps with a [datetime type]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) from [trigger event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) in action-based Canvases will always be normalized to [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Previously, timestamps for event properties were normalized to UTC with [some exceptions]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know). Now, this will provide a more consistent experience for editing Canvas steps and messages.

Consider this example of how this change might affect a timestamp in Canvas. Let's say we have an action-based Canvas that uses an event property in the first step of the Canvas with the following Message step: 

{% raw %}
`Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!`
{% endraw %}

![Context journey with a Message step as the first step.]({% image_buster /assets/img/context_timezone_example.png %}){: style="max-width:50%"}

The step will also have an event payload like: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
}
```

Historically, the message would be: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

With the Canvas Context early access, the message will now be: `Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!` This is due to the timestamp being in UTC, which is 8 hours ahead of Pacific Time (the time zone specified in the original payload with `-08:00`).

{% alert important %}
To account for this timestamp change, in all circumstances, we strongly recommend [using Liquid filters]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) for timestamps are represented in the desired time zone.
{% endalert %}

### Using Liquid to denote a timestamp in your preferred time zone

Consider the following Liquid snippet:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

This logic results in the following output: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

The preferred time zone can also be sent in the event properties payload and used in Liquid logic: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

This is an example of the Liquid snippet:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: canvas_entry_properties.${user_timezone} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

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
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | A personalized message that combines the previous variables. In a Message step, you could use the Liquid snippet {% raw %}`{{context.${personalized_message}}}`{% endraw %} to reference the context variable to deliver a personalized message to each user. You could also use a Context step to save the [promo code]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) value and template it in other steps throughout a Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

This also applies across multiple Context steps. For example, imagine this sequence:
1. An initial Context step creates a variable called `JobInfo` with the value `job_title`.
2. A Message step references {% raw %}`{{context.${JobInfo}}}`{% endraw %} and displays `job_title` to the user.
3. Later, a Context step updates the context variable, changing the value of `JobInfo` to `job_description`.
4. All subsequent steps that reference `JobInfo` will now use the updated value `job_description`.

Context variables use their most recent value throughout the Canvas, with each update affecting all following steps that reference that variable.

### Does the Canvas Context time zone consistency standardization impact API-triggered Canvases?

No, this change only impacts action-triggered Canvases. All API trigger properties have the string type, not the time type, so the original time zone is always preserved. However, we still recommend using an explicit time zone filter in Liquid when the property is used.

### How does this relate to the exceptions noted in Canvas entry properties and event properties?

Participating in the Canvas Context early access removes [those exceptions]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know), regardless if you're using a Canvas Context step.
