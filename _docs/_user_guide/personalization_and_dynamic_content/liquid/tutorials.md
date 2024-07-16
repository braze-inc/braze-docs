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

| Tutorial | Learning objective |
| --- | --- |
| [Personalize messages for user segments](#segments) | default values, conditional logic |
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

## 