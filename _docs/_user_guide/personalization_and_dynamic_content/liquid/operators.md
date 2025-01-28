---
nav_title: Operators
article_title: Liquid Operators
page_order: 2
description: "This reference page notes the operators that Liquid supports, as well as relevant examples."

---

# Operators

> Liquid supports many [operators][25] that can be used in your conditional statements. This page covers the operators that Liquid supports and provides use cases of how you can use them in your messages.

This table lists the operators that are supported. Note that parentheses are invalid characters in Liquid and prevents your tags from working.

|   Syntax| Operator Description|
|---------|-----------|
| ==  | equals        |
| !=  | does not equal|
|  >  | greater than  |
| <   | less than     |
| >=| greater than or equal to|
| <= | less than or equal to |
| or | condition A or condition B|
| and | condition A and condition B|
| contains | checks to see if a string or string array contains a string|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tutorials

Let's go through a few tutorials to learn how use these operators for your marketing campaigns:

### Choose message with an integer custom attribute

Let's send push notifications with personalized promotional discounts to users who have and haven't made purchases. This will use an integer custom attribute called `total_spend` to check a user's total spend.

1. Begin a conditional statement that checks if a user's total spend is greater than `0` to capture users who've made purchases. Then, create a message to send to those users.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2. Add the {% raw %}`{% else %}`{% endraw %} tag to capture users whose total spend equals `0` or doesn't exist. Then, create a message to send to those users.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3. Close the conditional logic with the {% raw %}`{% endif %}`{% endraw %} tag.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![A push notification composer with the full Liquid code from the tutorial.][13]{: width="100%"}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Now if a user's "Total Spend" custom attribute is greater than `0`, they will get the message:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
If a user's "Total Spend" custom attribute does not exist or is equal to `0`, they will get the following message:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Choose message with a string custom attribute

Let's send push notifications to users, and personalize the message based on each user's most recently played game. This will use an string custom attribute called `recent_game` to check which game a user has last played.

1. Begin a conditional statement that checks if a user's most recent game is Awkward Dinner Party. Then, create a message to send to those users.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2. Use the `eslif` tag to check if user's most recent game is Proxy War 3: War of Thirst. Then, create a message to send to those users.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3. Add the {% raw %}`{% else %}`{% endraw %} tag to capture users whose recent game isn't Awkward Dinner Party or Proxy War 3: War of Thirst, and users who don't have a recent game. Then, create a message to send to those users.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="4"}
4. Close the conditional logic with the {% raw %}`{% endif %}`{% endraw %} tag.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![A push notification composer with the full Liquid code from the tutorial.][14]

Now, if a user last played Awkward Dinner Party, they'll receive this message:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

If a user's most recent game is Proxy War 3: War of Thirst, they will receive this message:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

If a user hasn't played any games, or that custom attribute doesn't exist on their profile, they'll get this message:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Abort message based on location

You can abort a message based on just about anything. The following example shows how you can abort a message if a user is not based in a specified area, as they might not qualify for the promotion, show, or delivery.

{% raw %}
```liquid
{% if {{${time_zone.$}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

![A push notification composer with the full Liquid code from the tutorial.][26]

You can also [abort messages][1] based on Connected Content.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
