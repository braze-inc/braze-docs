---
nav_title: Using Liquid
article_title: Liquid Use Case and Overview
page_order: 0
description: "Liquid can elevate the personalization in your messages to impressive heights. Liquid tags act as placeholders in your messages that can pull in consented information from your user's account and enable personalization and relevant messaging practices."

---

# Liquid use cases and overview

{% raw %}

There are a variety of user attributes that you can use to dynamically insert personal info into your messaging. 

If you include the following text in your message: `{{${first_name}}}`, the user's first name (pulled from the user's profile) will be substituted when the message is sent. If you would like to use the value of a custom attribute, you must add the namespace "custom_attribute" to the variable. For example, to use a custom attribute named "zip code", you would include `{{custom_attribute.${zip code}}}` in your message.

The following values can be substituted into a message, depending on their availability:

- [Basic User Information][1] (e.g. `first_name`, `last_name`, `email_address`)
- [Custom Attributes][2]
- [Custom Event Properties][11]
- [Most Recently Used Device Information][39]
- [Target Device Information][40]

You can also pull content directly from a web server via Braze's [Connected Content][9] feature.
{% endraw %}

{% alert important %}
Braze currently supports Liquid up to and including __Liquid 3 from Shopify__. We do not currently support Liquid 4 and beyond.
{% endalert %}

## Using liquid

{% raw %}

Once you know the [Liquid tags available][1], using Liquid can elevate the personalization in your messages to impressive heights. Liquid tags act as placeholders in your messages that can pull in consented information from your user's account and enable personalization and relevant messaging practices. 

In the block below, you can see that a dual usage of a Liquid tag to call the user's first name, as well as a default tag in the event that a user would not have their first name registered.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

To a user named Janet Doe, the message would appear to the user as either:

```
Hi Janet, thanks for using the App!
```

Or...

```
Hi Valued User, thanks for using the App!
```

### Liquid syntax

Liquid follows a specific structure, or syntax, that you'll need to keep in mind as you're crafting dynamic personalization. Here are a few basic rules to keep in mind:

1. **Use straight quotes in Braze:** There is a difference between curly quotes (**‘’**) and straight quotes (**''**). Use straight quotes (**''**) in your Liquid in Braze. You may see curly quotes when copying and pasting from certain text editors, which can cause issues in your Liquid. If you're inputting quotes direclty into the Braze dashboard, you'll be fine!
2. **Brackets come in pairs:** Every bracket must both open and close **{ }**. Make sure to use curly brackets!
3. **If statements come in pairs:** For every `if`, you need an `endif` to indicate the `if` statement has ended.

### Inserting tags

You can insert tags by typing `{{` in any message, which will trigger an auto-completion feature that will continue to update as you type. You can even select a variable from the options that appear as you type.

If you're using a custom tag, you can copy and paste the tag into whatever message you desire.

{% endraw %}

{% alert note %}

If you choose to use Liquid in your Email messages, be sure to:

1. Insert it using the HTML editor as opposed to the classic editor. The Classic Editor may parse the Liquid as plaintext.
2. Place Liquid code within the `<body>` tag only. Placing it outside this tag may cause inconsistent rendering upon delivery.

{% endalert %}

{% raw %}


### Pre-Formatted Variables

You can insert pre-formatted variables with defaults through the "Insert Personalization Attribute" modal located on the top-right of any templated text field.

![Modal buttons][44]{: style="max-width:70%;"}

The modal will insert Liquid with your specified default value at the point that your cursor was. The insertion point is also specified via the preview box, which has the before and after text. If a block of text is highlighted, the highlighted text will be replaced.

![Modal][45]

{% endraw %}

### Assigning variables

{% raw %}
Some operations in Liquid require you to store the value you want to manipulate as a variable. This is often the case if your Liquid statement includes multiple attributes, event properties, or filters. 

For example, let's say you want to add two custom data integers together. You can't simply use:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}} 
```

This Liquid doesn't work because you can't reference multiple attributes in one line; you would need to assign a variable to at least one of these values before the math functions take place. Adding two custom attributes would require two lines of Liquid: one to assign the custom attribute to a variable, and one to perform the addition.

#### Example

for example, let's calculate a user's current balance by adding their gift card balance and rewards balance:

First, use the `assign` tag to subsitute the custom attribute of `current_rewards_balance` with the term "balance". This means that you now have a variable named `balance`, which you can manipulate.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Next, we're using the `plus` filter combine each user's gift card balance with their reawards balance, signified by `{{balance}}`.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend! 
```
{% endraw %}

{% alert tip %}
Find yourself assigning the same variables in every message? Instead of writing out the `assign` tag over and over again, you can save that tag as a Content Block and put it at the top of your message instead.

1. [Create a Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Give your Content Block a name (no spaces or special characters).
3. Click **Edit** at the bottom of the page.
4. Type in your `assign` tags.

As long as the Content Block is at the top of your message, every time the variable is inserted into your message as an object, it will refer to your chosen custom attribute!
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[9]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[39]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information
[40]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
