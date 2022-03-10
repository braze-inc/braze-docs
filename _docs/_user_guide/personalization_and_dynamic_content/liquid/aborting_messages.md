---
nav_title: Aborting Messages
article_title: Aborting Liquid Messages
page_order: 7
description: "Messages may now be aborted within conditional statements. In this reference article, we list some example use cases for this functionality."

---

# Aborting Liquid messages

Optionally, you can also abort messages within conditionals. Here are some examples of how this feature can be used in marketing campaigns:

## Abort message if "Number Games Attended" = 0

For example, let’s say that you did not want to send a message to customers who have not attended a game:

{% raw %}
```liquid
{% if customer_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif customer_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

This message will only send to customers who are known to have attended a game.

## Message English speaking customers only

You can message English speaking customers only by creating an "if" statement that'll match when a customer's language is English and an else statement that'll abort the message for anyone who does not speak English or does not have a language on their profile.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

By default Braze will log a generic error message to your Developer Console log:

```text
{% abort_message %} called
```

You can also have the abort message log something to your Developer Console log by including a string inside the parentheses:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Message error log in the Developer Console with an abort message of "language was nil".][26]

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
