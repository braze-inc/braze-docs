---
nav_title: Conditional Messaging Logic
page_order: 6
description: "Tags allow you to include programming logic in your messaging campaigns. This reference article covers how tags can and should be used in your campaigns."
---

# Conditional Messaging Logic (Tags)


[Tags][7] allow you to include programming logic in your messaging campaigns.

{% raw %}
A tag must be wrapped in `{% %}`.
{% endraw %}

Tags can be used for executing conditional statements as well as for advanced use cases, like assigning variables or iterating through a block of code.

{% alert tip %}
To make your life a bit easier, Braze has included color-formatting that will activate in green and purple if you correctly format your Liquid syntax.


If you're having a hard time using conditional messaging, try writing out the conditional syntax before you insert your custom attributes and other Liquid elements.


For example, add the following into the message field first:  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Be sure it highlights in green, then replace the `X` with your chosen Liquid or Connected Content using the blue `+` in the message field corner, and the `0` with your desired value.


Then, add your message variations as you need them between the `else` conditionals:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}
{% endalert %}

## Conditional Logic
You can include many types of [intelligent logic within messages][1] -- one example is a conditional statement. See the following example which uses [conditionals][8] to internationalize a campaign:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

## Conditional Logic: Step By Step

In this example, we use tags with "if", "elsif" and "else" statements to deliver internationalized content.

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
```
If the customer's language is English, the first condition is met and the customer will receive a message in English.

```liquid
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
```

You can specify as many conditional statements as you'd like- subsequent conditions will be checked if the previous conditions are not met. In this example, if a customer's device is not set to English this code will check to see if the customer's device is set to Spanish or Chinese. If the customer's device meets one of these conditions, the customer will receive a message in the relevant language.

```liquid
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
```

You have the option to include an `{% else %}` statement in your conditional logic. If none of the conditions that you set are met, the `{% else %}`  statement specifies the message that should send. In this case, we default to English if a customer's language is not English, Spanish or Chinese.

```liquid
{% endif %}
```

The `{% endif %}`  tag signals that you've finished your conditional logic. You must include the
`{% endif %}`  tag in any message with conditional logic. If you do not include an `{% endif %}`  tag in your conditional logic, you'll get an error as Braze will be unable to parse your message.

{% endraw %}

# Accounting For Null Attribute Values

Conditional logic is a useful way to account for null attribute values. A null value occurs when the value of a custom attribute has not been set. For example, a user who has not yet set their first name will not have a first name in Braze's database.

In some circumstances, you may wish to send a completely different message to users who have a first name set and users who do not have a first name set.

The following tag allows you to specify a message for users with a null "first name" attribute:

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}

```
{% endraw %}


![NullValues][36]

[36]:{% image_buster /assets/img/value_null.png %}
[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags"
