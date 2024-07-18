---
nav_title: Tutorials
article_title: "Tutorials: Writing Liquid code"
page_order: 12
description: "This reference page contains beginner-friendly tutorials to help you get started with Liquid code."
page_type: tutorial
---

# Tutorials: Writing Liquid code

> New to Liquid? These tutorials will help you get started with writing Liquid code for common use cases.

When you’re finished with these tutorials, you’ll be able to:

- Write Liquid code for common use cases
- String together Liquid conditional logic to personalize messages based on user data

| Tutorial | Learning objectives |
| --- | --- |
| [Personalize messages for user segments](#segments) | default values, conditional logic |
| [Abandoned cart reminders](#reminders) | operators, conditional logic |
| [Event countdown](#countdown) | variables, date filters |
{: .reset-br-td-1 .reset-br-td-2}

## Personalize messages for user segments {#segments}

Let’s customize messages for different user segments, like VIP customers and new subscribers.

1. Open the message with personalized greetings to send when you have and don’t have a user’s first name. To do this, create a Liquid tag that includes the attribute `first_name` and a default value to use if `first_name` is blank. In this scenario, let’s use “traveler” as the default value.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2. Now, let’s provide the message to send if the user is a VIP customer. We’ll need to use a conditional logic tag for this: `if`. This tag will say that if the `vip_status` custom attribute is equal to `VIP`, the following Liquid will be carried out. In this case, a specific message will send.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3. Let’s send a customized message for users who are new subscribers. We’ll use the conditional logic tag `elsif` to specify that if the user’s `vip_status` is `new`, the following message will send.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4. What about the users who aren’t VIP or new? We can send a message to all other users with the `else` tag, which specifies that the following message should be sent if the previous conditions aren’t met. Then we can close the conditional logic with the `endif` tag, as there aren’t any more VIP statuses to consider.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## Abandoned cart reminders {#reminders}

Let’s send personalized messages to remind users of items left in their cart. We’ll customize them to send based on how many items are in their cart.

1. Let’s check if their cart is empty by opening a Liquid conditional logic with the operator `!=`, which means “does not equal”. In this case, we’ll set the condition to the custom attribute `cart_items` not equaling a blank value.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2. Let’s check if the cart has more than three items by using the operator `>’, which means “greater than”.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3. Write a message that greets the user by their first name, or if that’s not available, use “there” as a replacement for their name. Include what should be stated if there are more than three items in the cart. Because we don’t want to overwhelm the user with a complete list, let’s list the first three `cart_items`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4. Use `else` to specify what should happen in all other cases (if `cart_items` is fewer than three), and then provide the message to send. Because three items don’t take up a lot of space, we can list them all. We’ll use the Liquid operator `join` and `,` to specify that the items should be listed with a comma separating them. Close the logic with `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you. 
{% endif %}
```
{% endraw %}

{: start="5"}
5. Use `else` and then an `abort_message` to tell the Liquid code to not send a message if the cart doesn’t meet any of the previous conditions. In other words, if the cart doesn’t have fewer or more than three items (and is empty). Close the logic with `endif`.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Event countdown {#countdown}

Let’s send users a message that states how many days are left until an anniversary sale.

1. First, let’s assign a variable, `sale_date`, to the custom attribute `anniversary_date` and apply the `date` filter of `%s`. This assigns the variable `event_date` the value of the `last_selected_event_date`’s seconds, which allows us to manipulate the value in later Liquid code lines.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2. We also need to assign a variable to today to define what today’s value should be. Let’s assign the variable `today` the value of `now`, and use the `date` filter of `%s` to specify that we’re using seconds.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3. We’ll assign the variable of `difference` to equal the value of `event_date` minus `today`.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4. Now we can assign the variable we’ll reference in our message. Let’s assign `difference_days` to the `event_date` divided by `86400`. This will give us the number of days until the Anniversary Sale.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5. Finally, let’s create the message to send.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}
