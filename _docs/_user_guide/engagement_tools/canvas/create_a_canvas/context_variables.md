---
nav_title: Context variables
article_title: Context variables
page_type: reference
description: "This reference article explains context variables in Braze Canvases, including their types, usage, and best practices."
---

# Context variables

> Context variables are temporary pieces of data you can create and use within a user's journey through a specific Canvas. They enable you to personalize delays, segment users dynamically, and enrich messaging without permanently altering a user's profile information. Context variables exist only within the Canvas session and do not persist across different Canvases or outside the session.

## How context variables work

Context variables can be set in two ways:

- **At Canvas entry:** When users enter a Canvas, data from the event or API trigger can automatically populate context variables.
- **In a Context step:** You can define or update context variables manually inside the Canvas by adding a [Context step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

Each context variable includes:

- A name (such as `flight_time` or `subscription_renewal_date`)
- A data type (such as number, string, time, or array)
- A value you assign using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) or through the **Add Personalization** tool.

When defined, you can use a context variable throughout the Canvas by referencing it in this format: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

For example, {% raw %}`{{context.${flight_time}}}`{% endraw %} could return the user's scheduled flight time.

Each time a user enters the Canvas—even if they have entered it before—the context variables will be redefined based on the latest entry data and Canvas setup. This stateful approach allows each Canvas entry to maintain its own independent context, allowing users to have multiple active states within the same journey while retaining the specific context for each state.

For example, if a customer has two upcoming flights, they'll have two separate journey states running simultaneously—each with its own flight-specific context variables like departure time and destination. This allows you to send personalized reminders about their 2 pm flight to New York while sending different updates about their 8 am flight to Los Angeles tomorrow, so that each message stays relevant to the specific booking.

## Considerations

You can define up to 10 context variables per [Context step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/). Each variable name can be up to 100 characters and must use only letters, numbers, or underscores.

Context variable definitions can be up to 10,240 characters. If you pass context variables into an API-triggered Canvas, they share the same namespace as variables created in a Context step. For example, if you send a variable `purchased_item` in the [`/canvas/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) context object, you can reference it as {% raw %}`{{context.${purchased_item}}}`{% endraw %}. If you redefine that variable in a Context step, the new value will override the API value for that user's journey.

You can store up to 50 KB per Context step, distributed across up to 10 variables. If the total size of all variables in a step exceeds 50 KB, any variables that exceed the limit will not be evaluated or stored. For example, if you have three variables in a Context step:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

Variable 3 will not be evaluated or stored because the sum of the previous variables exceeds 50 KB.

## Data types

Context variables that are created or updated in the step can be assigned the following data types.

{% alert note %}
Context variables have the same expected formats for data types as [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>When using the array type, Braze tries to parse the value as JSON, which allows arrays of objects to be successfully created. If the objects within your arrays are not valid JSON, the result will be a simple array of strings. <br><br>For nested objects and array of objects, use the [`as_json_string` Liquid filter](#converting-connected-content-strings-to-json). If you're creating the same object in a Context step, you'll need to render the object using `as_json_string`, such as {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Data type | Example variable name | Example value |
|---|---|---|
|Boolean| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Number| credit_score |{% raw %}<code>740</code>{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Array (of objects)| pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
|Time (in UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Object (flattened) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

By default, the time data type is in UTC. If you use a string data type to store a time value, you can define the time as a different time zone like PST. 

For example, if you're sending a message to a user the day before their birthday, you would save the context variable as a time data type because there's Liquid logic associated with sending the day before. However, if you're sending a holiday message on Christmas Day (December 25), you wouldn't need to reference the time as a dynamic variable, so using a string data type would be preferable.

## Using context variables

You can use context variables anywhere you use Liquid in a Canvas, such as in [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) and [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update) steps, by selecting **Add Personalization**.

For example, let's say you want to notify passengers about their VIP lounge access before their upcoming flight. This message should only be sent to passengers who purchased a first-class ticket. A context variable is a flexible way to track this information.

Users will enter the Canvas when they purchase a plane ticket. To determine lounge access eligibility, we'll create a context variable called `lounge_access_granted` in a Context step, then reference that context variable in subsequent steps of the user journey.

![Context variable set up to track if a passenger qualifies for VIP lounge access.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

In this Context step, we'll use {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} to determine if the type of flight they've purchased is `first_class`.

Next, we'll create a Message step to target users where {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} is `true`. This message will be a push notification that includes personalized lounge information. Based on this context variable, the eligible passengers will receive the relevant messages before their flight.

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

The exit criteria state that at any point in a user's journey in the Canvas, they'll exit the Canvas if:

- They perform the custom event **Abandon Cart**, and
- The basic property **Item in Cart** matches the string value of the context variable `cart_item_threshold`.

![Exit criteria set up to exit a user if they perform a custom event based on the context variable.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

The exit criteria state that at any point in a user’s journey in the Canvas, they'll exit the Canvas if:

- They make a specific purchase for the "book" product name, and
- That purchase's nested property "loyalty_program" is equal to the user's custom attribute "VIP".

![Exit criteria set up to exit a user if they make a purchase.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Context variable filters

You can create filters that use previously declared context variables in [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) and [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) steps.

{% alert note %}
Context variable filters are only available for Audience Paths and Decision Split steps. 
{% endalert %}

Context variables are declared and only accessible in the scope of a Canvas, meaning they can't be referenced in segments. Context variable filters function similarly in Audience Paths and Decision Split steps—Audience Path steps represent multiple groups, while Decision Split steps represent binary decisions.

![Decision Split step example with the option to create a filter with a context variable.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Similar to how Canvas context variables have pre-defined types, the comparisons between context variables and static values must have [matching data types]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). The context variable filter allows comparisons across multiple data types for booleans, numbers, strings, time, and day of year, similar to the comparisons for [nested custom attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Use the same data type for your context variable and comparison. For example, if your context variable is a time data type, use time comparisons (such as "before" or "after"). Using mismatching data types (such as string comparisons with a time context variable) may cause unexpected behavior.
{% endalert %}

Here is an example of a context variable filter comparing the context variable `product_name` to the regex `/braze/`.

![A filter setup for the context variable "product_name" to match the regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparing to context variables or custom attributes

By selecting the **Compare to a context variable or custom attribute** toggle, you can construct context variable filters that compare against previously-defined context variables or user custom attributes. This can be useful for performing comparisons that are dynamic per user, like API-triggered `context`, or to condense complex comparison logic defined across context variables.

{% tabs %}
{% tab Example 1 %}

Let's say you want to send a personalized reminder to users after a dynamic period of inactivity, which includes anyone who hasn't logged into your app in the last three days, should receive a message.

You have a context variable `re_engagement_date` that is defined as {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Note that `3 days` can be a variable amount that is also stored as a user's custom attribute. So if the `re_engagement_date` is after the `last_login_date` (stored as a custom attribute on the user profile), they'll be sent a message.

![A filter setup with custom attributes as the personalization type for the context variable "re_engagement_date" after the custom attribute "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

The following filter compares the context variable `reminder_date` to be before the context variable `appointment_deadline`. This can help group users in an Audience Paths step to determine whether they should receive additional reminders before their appointment deadline.

![A filter setup with context variables as the personalization type for the context variable "reminder_date" on the context variable "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Time zone consistency standardization

While most event properties using the timestamp type are already in UTC in Canvas, there are some exceptions. With the addition of Canvas Context, all default timestamp event properties in action-based Canvases will consistently be in UTC. This change is part of a broader effort to ensure a more predictable and consistent experience when editing Canvas steps and messages. Note that this change will impact all action-based Canvases, whether the specific Canvas is using a Context step or not.

{% alert important %}
In all circumstances, we strongly recommend using [Liquid time_zone filters]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) for timestamps to be represented in the desired time zone. You can reference this [frequently asked question](#faq-example) for an example.
{% endalert %}

## Related

- [Context step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalization and dynamic content with Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
