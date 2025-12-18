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

For a full reference on context variables, including data types, usage, and best practices, see the [Context variables reference]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

Within a Context step, you can define or update up to 10 context variables. These variables can be used to personalize delays, segment users dynamically, and enrich messaging throughout the Canvas. For example, you could create a context variable for a user's scheduled flight time, then use it to set personalized delays and send reminders.

You can set context variables in two ways:

- **At Canvas entry:** Data from the event or API trigger can automatically populate context variables.
- **In a Context step:** Define or update context variables manually by adding a Context step.

Each context variable requires a name, a data type, and a value (set using Liquid or the Add Personalization tool). When defined, you can reference context variables throughout the Canvas using Liquid, such as {% raw %}`{{context.${flight_time}}}`{% endraw %}.

Each Canvas entry redefines context variables based on the latest entry data and Canvas setup, allowing users to have multiple active journeys with their own context. For example, if a customer has two upcoming flights, they'll have two separate journey states running simultaneously&#8212;each with its own flight-specific context variables like departure time and destination. This allows you to send personalized reminders about their 2 pm flight to New York while sending different updates about their 8 am flight to Los Angeles tomorrow, so that each message stays relevant to the specific booking.

## Considerations

- You can define up to 10 context variables per Context step.
- Each variable requires a unique name (letters, numbers, underscores only, up to 100 characters).
- The total size of all variables in a step cannot exceed 50 KB.
- Variables passed in using API triggers share the same namespace as those created in Context steps; redefining a variable in a Context step overrides the API value.

For more details and advanced usage, see [Context variables reference]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

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
5. (Optional) To add more variables, select **Add Context variable** and repeat steps 1–4.
6. When you're finished, select **Done**.

Now you can use your context variable anywhere you use Liquid, such as in Message and User Update steps, by selecting **Add Personalization**. For a full walkthrough, see [Context variables reference]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

### Context variable filters

You can create filters using context variables in [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) and [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) steps. For filter setup, comparison logic, and advanced examples, see [Context variables reference]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

## Previewing user paths

We recommend testing and [previewing your user paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) to make sure your messages are sent to the right audience and context variables are evaluated to the expected outcomes.

{% alert note %}
If you're previewing your Canvas in the **Preview & Test Send** section of the editor, the timestamp in the test message preview **will not** be standardized to UTC because this panel generates previews as strings. This means if a Canvas is set up to accept a `time` object, the message preview won't accurately preview what occurs when the Canvas is live. To test your Canvas most accurately, we recommend previewing user paths instead.
{% endalert %}

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

While most event properties using the timestamp type are already in UTC in Canvas, there are some exceptions. With the addition of Canvas Context, all default timestamp event properties in action-based Canvases will consistently be in UTC. This change is part of a broader effort to ensure a more predictable and consistent experience when editing Canvas steps and messages. Note that this change will impact all action-based Canvases, whether the specific Canvas is using a Context step or not.

{% alert important %}
In all circumstances, we strongly recommend using [Liquid time_zone filters]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) for timestamps to be represented in the desired time zone. You can reference this [frequently asked question](#faq-example) for an example.
{% endalert %}


## Troubleshooting

A context variable is considered invalid when:

- A call to an embedded Connected Content fails.
- The Liquid expression at runtime returns a value that doesn't match the data type or is empty (null).

For example, if the context variable data type is **Number** but the Liquid expression returns a string, it is invalid.

In these circumstances: 
- The user will advance to the next step. 
- The Canvas step analytics will count this as _Not Updated_.

When troubleshooting, monitor the _Not Updated_ metric to check that your context variable is updating correctly. If the context variable is invalid, your users can continue in your Canvas past the Context step, but may not qualify for later steps.

Refer to [Data types]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) for the example setups for each data type.

## Frequently asked questions

### What will be changing when Canvas Context becomes generally available?

When Canvas Context becomes generally available, the following details will apply:

- All timestamps with a [datetime type]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) from [trigger event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) in action-based Canvases will always be in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). 
- This change will impact all action-based Canvases, whether the specific Canvas is using a Context step or not.

#### What is the reason for this change?

This change is part of a broader effort to create a more predictable and consistent experience when editing Canvas steps and messages.

#### When is this change taking effect?

- If you're participating in the Canvas Context early access, this change has already been applied. 
- If you're not participating in the Canvas Context early access, this change will apply when you join the early access or when Canvas Context becomes generally available.

#### Are API-triggered or scheduled Canvases impacted by this change?

No.

#### Will this change impact Canvas entry properties?

Yes, this will impact `canvas_entry_properties` if the `canvas_entry_property` is being used in an action-based Canvas and the property type is `time`. In all circumstances, we recommend using Liquid `time_zone` filters for timestamps to be represented in the desired timezone.

Here is an example on how to do this:

| Liquid in Message step | Output | Is this the way to represent time zones correctly in Liquid? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | No |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | No
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### What is a practical example of how the new timestamp behavior might affect my messages? {#faq-example}

Let’s say we have an action-based Canvas that has the following content in a Message step:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

This will result in the following message: 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Because no time zone is specified using Liquid, the timestamp here is in UTC. 

To specify a time zone clearly, we can use Liquid `time_zone` filters like this: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

This will result in the following message: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Because the America/Los Angeles time zone is specified using Liquid, the timestamp here is in PST.

The preferred time zone can also be sent in the event properties payload like this and used in Liquid logic:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### How do context variables differ from Canvas entry properties?

If you’re participating in the Context step early access, Canvas entry properties are now included as Canvas context variables. This means you can send Canvas entry properties using the Braze API and reference them in other steps, similar to using a context variable with the Liquid snippet.

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
