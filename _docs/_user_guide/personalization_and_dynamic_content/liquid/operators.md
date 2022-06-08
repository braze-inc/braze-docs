---
nav_title: Operators
article_title: Liquid Operators
page_order: 2
description: "This reference page notes the operators that Liquid supports, as well as relevant examples."

---

# Operators

Liquid supports many [operators][25] that can be used in your conditional statements.

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
{: .reset-td-br-1 .reset-td-br-2}

## Operator examples

Here are some examples of how these operators could be helpful for your marketing campaigns:

### Choose message via integer custom attribute

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

![][13]{: width="100%"}

In this example, if a customer’s "Total Spend" custom attribute is greater than `0`, they will get the message:

```
Thanks for purchasing! Here's another 10% off!
```
If a customer’s "Total Spend" custom attribute does not exist or is equal to `0`, they will get the following message:

```
Buy now! Would 5% off convince you?
```


### Choose message via string custom attribute

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == Game1 %}
You played our Game! We're so happy!
{% elsif{{custom_attribute.${Game}}} == Game2 %}
You played our other Game! Woop!
{% else %}
Hey! Get in here and play this Game!
{% endif %}
```
{% endraw %}

![][14]

In this example, if you have played a certain game, you'll receive the following message:

```
You played our Game! We're so happy!
```

If you played another specified game:

```
You played our other Game! Woop!
```

If you haven’t played any games, or that custom attribute doesn’t exist on your profile, you’d get the following message:

```
Hey! Get in here and play this Game!
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

![][26]

You can also [abort messages][1] based on Connected Content.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
