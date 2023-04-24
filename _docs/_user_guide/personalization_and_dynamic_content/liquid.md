---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: featured
search_rank: 3
guide_top_header: "Personalization Using Liquid Tags"
guide_top_text: "Braze can automatically substitute values from a given user into your messages. Put your expression inside of two sets of curly brackets to notify Braze that you'll be using an interpolated value. Inside of these brackets, any user values that you want to substitute must be surrounded by an additional set of brackets with a dollar sign in front of them.<br><br>For more on Liquid, check out our guided <b><a href='https://learning.braze.com/dynamic-personalization-with-liquid'>Dynamic Personalization with Liquid</a></b> Braze Learning course!"
description: "This landing page covers all things Liquid, such as supported personalization tags, filters, setting default values, and more."

guide_featured_title: "Section Articles"
guide_featured_list:
- name: Using Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  fa_icon: fas fa-flask
- name: Supported Personalization Tags
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  fa_icon: fas fa-tag
- name: Operators
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  fa_icon: fas fa-code
- name: Filters
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  fa_icon: fas fa-filter
- name: Advanced Filters
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  fa_icon: fas fa-cog
- name: Setting Default Values
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  fa_icon: fas fa-table
- name: Conditional Messaging Logic
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  fa_icon: fas fa-columns
- name: Aborting Messages
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  fa_icon: fas fa-undo
- name: Liquid Use Cases
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  fa_icon: fas fa-list-ul
---

## About Liquid

Liquid is an open-source template language developed by Shopify and written in Ruby. At Braze, Liquid is used to template data from a user's profile into messages. For example, you can retrieve a custom attribute from a user profile that is an integer data type and round that value to the nearest whole number. For more on Liquid syntax and usage, refer to [**Supported personalization tags**][1].

Liquid templating language supports the use of objects, tags, and filters.

- [**Objects**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) allow you to insert personalized attributes into your messages.
- [**Tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) allow you to insert data into messaging and use conditional logic to send messages if outlines conditions are met. For example, you can use tags to include intelligent logic, such as "if" statements, in your campaigns.
- [**Filters**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) allow you to reformat personalized attributes and dynamic content. For example, you could convert a timestamp, such as *2016-09-07 08:43:50 UTC*, into a date, such as *September 7, 2016*.

{% alert warning %}
Braze does not currently support 100% of Shopify's Liquid, only certain portions which we have attempted to outline in our documentation. We highly recommend testing all messages using Liquid before sending them to reduce the risk of errors or using unsupported Liquid.
{% endalert %}

### What's new with Liquid 5

Braze has updated support to Liquid up to and including **Liquid 5 from Shopify**. 

Liquid implementation now supports syntax and theme personalization tag types and whitespace control. For more information on specific tags, refer to [syntax tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags) and [theme tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#theme-tags). 

The following new array and math filters are available for use in your Liquid as you build your messaging.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Refer to our [Filters]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) article for definitions.

## Terms to know

These terms are reinterpreted from [**Shopify's documentation**](https://shopify.github.io/liquid/basics/introduction/) based on our level of support.

{% raw %}

| Term | Definition | Example |  
|---|---|---|
| Liquid | An open-source, customer-facing template language created by Shopify and written in Ruby; used to load/pull dynamic content. | `{{${first_name}}}` will insert a user's first name into a message. |
| Object | A denotation of a variable and location of the intended variable name that tells Liquid where to show content in the message. | `{{${city}}` will insert a user's city into a message. |
| Conditional logic tag | Tags create logic and control the flow of message content. In Braze's cases, conditional logic tags are used to create exceptions and variations in messages based on certain, predefined criteria. | ```{% if ${language} == 'en' %}``` will trigger your message in a designated way in the event that a user has designated "English" as their language. |
| Filters | Used to change, narrow, or reformat the output of the Liquid object. It is often used to create mathematical operations. | ```{{"Big Sale" | upcase}}``` will cause the words "Big Sale" to appear as "BIG SALE" in the message. |
| Operators | Used in messages to create dependencies or criteria that can affect which message your user receives. | If a user meets the defined criteria in a message tagged with `{% custom_attribute.${Total_Revenue} > 0%}`, they will receive the message. If not, they will receive another designated message (or not), depending on what you set. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}

<br>

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
