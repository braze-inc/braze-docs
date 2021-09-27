---
nav_title: Aborting Messages
article_title: Aborting Liquid Messages
page_order: 7
description: "Messages may now be aborted within conditional statements. In this reference article, we list some example use cases for this functionality."

---

# Aborting Messages
Optionally, you can also now abort messages within conditionals. Here are some examples of how this feature can be used in marketing campaigns:

**Aborting message if "Number Games Attended" = 0:**

For example, let’s say that you did not want to send the above message to customers who had not attended a game:

![Liquid Abort Message Example][15]

This message will only send to customers who are known to have attended a game.

**Messaging English speaking customers only:**

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

You can also have the abort_message log something to your Developer Console log by including a string inside the parentheses:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![developer_console][26]

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
