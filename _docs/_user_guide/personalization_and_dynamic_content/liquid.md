---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Personalization Using Liquid Tags"
guide_top_text: "Braze can automatically substitute values from a given user into your messages. Put your expression inside of two sets of curly brackets to notify Braze that you'll be using an interpolated value. Inside of these brackets, any user values that you want to substitute must be surrounded by an additional set of brackets with a dollar sign in front of them.<br><br>For more on Liquid, check out our guided <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Dynamic Personalization with Liquid</a></b> Braze Learning path!"
description: "This landing page covers all things Liquid, such as supported personalization tags, filters, setting default values, and more."

guide_featured_title: "Section articles"
guide_featured_list:
- name: Using Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Supported Personalization Tags
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  image: /assets/img/braze_icons/tag-01.svg
- name: Operators
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  image: /assets/img/braze_icons/code-02.svg
- name: Filters
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  image: /assets/img/braze_icons/flag-02.svg
- name: Advanced Filters
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  image: /assets/img/braze_icons/settings-01.svg
- name: Setting Default Values
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: Conditional Messaging Logic
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: Aborting Messages
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Liquid Use Cases
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
- name: Tutorials
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/tutorials/
  image: /assets/img/braze_icons/book-open-01.svg
- name: Frequently Asked Questions
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## About Liquid

> Liquid is an open-source template language developed by Shopify and written in Ruby. At Braze, Liquid is used to template data from a user's profile into messages. 

For example, you can retrieve a custom attribute from a user profile that is an integer data type and round that value to the nearest whole number. For more on Liquid syntax and usage, refer to [**Supported personalization tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Liquid templating language supports the use of objects, tags, and filters.

- [**Objects**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) allow you to insert personalized attributes into your messages.
- [**Tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) allow you to insert data into messaging and use conditional logic to send messages if certain conditions are met. For example, you can use tags to include intelligent logic, such as "if" statements, in your campaigns.
- [**Filters**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) allow you to reformat personalized attributes and dynamic content. For example, you could use the [`date` filter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) to convert a timestamp, such as *2016-09-07 08:43:50 UTC*, into a date, such as *September 7, 2016*.

{% alert warning %}
Braze currently doesn't support 100% of Shopify's Liquid, only certain portions which we have attempted to outline in our documentation. We highly recommend testing all messages using Liquid before sending them to reduce the risk of errors or using unsupported Liquid.
{% endalert %}

### Liquid 5 support

Braze supports Liquid up to and including **Liquid 5 from Shopify**. Liquid implementation supports syntax personalization tag types and whitespace control. For more information on specific tags, refer to [syntax tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags).

The following new array and math filters are available for use in your Liquid as you build your messaging.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Refer to [Filters]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) for definitions.

### Liquid updates

#### Color labels

Each Liquid element corresponds to a color, allowing you to differentiate your Liquid at-a-glance in your Liquid editor.

![]({% image_buster /assets/img/liquid_color_code.png %})

#### Predictive Liquid

You can also leverage predictive Liquid for custom attributes, attribute names, and more as you build your personalized messages.

![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Terms to know

These terms are reinterpreted from [**Shopify's documentation**](https://shopify.github.io/liquid/basics/introduction/) based on our level of support.

{% raw %}

| Term | Definition | Example |  
|---|---|---|
| Liquid | A commonly-used, customer-facing template language created by Shopify and written in Ruby that is used to load and pull dynamic content. | `{{${first_name}}}` will insert a user's first name into a message. |
| Object | A denotation of a variable and location of the intended variable name that tells Liquid where to show content in the message. | `{{${city}}}` will insert a user's city into a message. |
| Conditional logic tag | Used to create logic and control the flow of message content. In Braze, conditional logic tags are used to create exceptions and variations in messages based on certain, predefined criteria. | ```{% if ${language} == 'en' %}``` will trigger your message in a designated way in the event that a user has designated "English" as their language. |
| Filters | Used to change, narrow, or reformat the output of the Liquid object. It's often used to create mathematical operations. | ```{{"Big Sale" | upcase}}``` will cause the words "Big Sale" to appear as "BIG SALE" in the message. |
| Operators | Used in messages to create dependencies or criteria that can affect which message your user receives. | If a user meets the defined criteria in a message tagged with `{% custom_attribute.${Total_Revenue} > 0%}`, they will receive the message. If not, they will receive another designated message (or not), depending on what you set. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

