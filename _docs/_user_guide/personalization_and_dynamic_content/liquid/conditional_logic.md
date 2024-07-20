---
nav_title: Conditional Messaging Logic
article_title: Conditional Liquid Messaging Logic
page_order: 6
description: "This reference article covers how tags can and should be used in your campaigns."

---

# Conditional messaging logic

> [Tags](https://docs.shopify.com/themes/liquid-documentation/tags) allow you to include programming logic in your messaging campaigns. Tags can be used for executing conditional statements as well as for advanced use cases, like assigning variables or iterating through a block of code.

{% raw %}
A tag must be wrapped in `{% %}`.
{% endraw %}

{% alert tip %}
To make your life a bit easier, Braze has included color-formatting that will activate in green and purple if you've correctly formatted your Liquid syntax. Green formatting can help identify tags, while purple formatting highlights areas that contain personalization.
<br><br>
If you're having a hard time using conditional messaging, try writing out the conditional syntax before you insert your custom attributes and other Liquid elements.
<br><br>
For example, add the following into the message field first:  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Be sure it highlights in green, then replace the `X` with your chosen Liquid or Connected Content using the blue `+` in the message field corner, and the `0` with your desired value.
<br><br>
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

## Conditional logic

You can include many types of [intelligent logic within messages](http://docs.shopify.com/themes/liquid-documentation/basics), such as a conditional statement. See the following example which uses [conditionals](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags") to internationalize a campaign:
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

### Step by step example

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

You can specify as many conditional statements as you'd like. Subsequent conditions will be checked if the previous conditions are not met. In this example, if a customer's device is not set to English this code will check to see if the customer's device is set to Spanish or Chinese. If the customer's device meets one of these conditions, the customer will receive a message in the relevant language.

```liquid
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
```

You have the option to include an `{% else %}` statement in your conditional logic. If none of the conditions that you set are met, the `{% else %}`  statement specifies the message that should send. In this case, we default to English if a customer's language is not English, Spanish, or Chinese.

```liquid
{% endif %}
```

The `{% endif %}`  tag signals that you've finished your conditional logic. You must include the
`{% endif %}`  tag in any message with conditional logic. If you do not include an `{% endif %}`  tag in your conditional logic, you'll get an error as Braze will be unable to parse your message.

{% endraw %}

## Accounting for null, nil, and blank attribute values

Conditional logic is a useful way to account for attribute values that aren't set in user profiles.

### Null and nil attribute values

A null or nil value occurs when the value of a custom attribute has not been set. For example, a user who has not yet set their first name will not have a first name logged in Braze.

In some circumstances, you may wish to send a completely different message to users who have a first name set and users who do not have a first name set.

The following tag allows you to specify a message for users with a null "first name" attribute:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

![]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Note that a null attribute value isn't strictly associated with a value type (for example, a "null" string is the same as a "null" array), so in the example above, the null attribute value is referencing an unset first name, which would be a string.

{% endraw %}

### Blank attribute values

A blank value occurs when the attribute on a user profile isn't set, is set with a whitespace string (` `), or is set as `false`. Blank values should be checked before other variables to avoid a Liquid processing error.

The following tag allows you to specify a message for users that have a blank "first name" attribute.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## Referencing custom attributes

After you have [created custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes), you can reference these custom attributes in your Liquid messaging.

When using conditional logic, you'll need to know the custom attribute's data type to ensure you're using the correct syntax. From the **Custom Attributes** page in the dashboard, look for the data type associated with your custom attribute, then reference the following examples listed for each data type.

![Selecting a data type for a custom attribute. The example provided shows an attribute of Favorite_Category with a data type of string.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
Strings and arrays require straight apostrophes around them, while booleans and integers will never have apostrophes.
{% endalert %}

#### Boolean

[Booleans]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans) are binary values, and can be set to either `true` or `false`, such as `registration_complete: true`. Boolean values don't have apostrophes around them.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Number

[Numbers]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers) are numeric values, which can be integers or floats. For example, a user may have `shoe_size: 10` or `levels_completed: 287`. Number values don't have apostrophes around them.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

You can also use other [basic operators](https://shopify.dev/docs/themes/liquid/reference/basics/operators) such as less than (<) or greater than (>) for integers:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### String

A [string]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings) is made up of alphanumeric characters and stores a piece of data about your user. For example, you may have `favorite_color: red` or `phone_number: 3025981329`. String values must have apostrophes around them.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

For strings, you can use both "==" or "contains" in your Liquid.

#### Array

An [array]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays) is a list of information about your user. For example, a user may have `last_viewed_shows: stranger things, planet earth, westworld`. Array values must have apostrophes around them.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

For arrays, you must use "contains" and can't use "==". 

#### Time

A time stamp of when an event took place. [Time]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) values must have a [math filter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters) on them to be used in conditional logic.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


[36]:{% image_buster /assets/img/value_null.png %}
[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags"
[9]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans
[10]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings
[12]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time
[20]: {% image_buster /assets/img_archive/custom_attribute_data_type.png %}
