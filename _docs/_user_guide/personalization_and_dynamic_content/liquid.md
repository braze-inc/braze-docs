---
nav_title: Liquid
config_only: false
layout: featured
page_order: 0
---

# Personalization Using Liquid Tags

{% raw %}
Braze can automatically substitute values from a given user into your messages. Put your expression inside of two sets of curly brackets to notify Braze that you'll be using an interpolated value. Inside of these brackets, any user values that you want to substitute must be surrounded by an additional set of brackets with a dollar sign in front of them.

For example, if you include the following text in your message: `{{${first_name}}}`, the appropriate value from the user will be interpolated when the message is sent. If you would like to use the value of a custom attribute, you must add the namespace "custom_attribute" to the variable. For example, to use a custom attribute named "zip code", you would include `{{custom_attribute.${zip code}}}` in your message.

The following values can be substituted into a message, depending on their availability:

- [Basic User Information][1] (e.g. `first_name`, `last_name`, `email_address`)
- [Custom Attributes][2]
- [Custom Event Properties][11]
- [Most Recently Used Device Information][39]
- [Target Device Information][40]

You can also pull content directly from a web server via Braze's [Connected Content][9] feature.
{% endraw %}

{% alert important %}
Braze currently supports liquid up to and including Liquid 3 from Shopify. We do not currently support Liquid 4 and beyond.
{% endalert %}

## Terms to Know

These terms are reinterpreted from [Shopify's documentation][3] based on our level of support.

{% alert warning %}

Braze does not currently support 100% of Shopify's Liquid, only certain portions which we have attempted to outline in our documentation. We highly recommend testing all messages using Liquid before sending to reduce the risk of errors or using unsupported Liquid.

{% endalert %}

{% raw %}

| Term | Definition | Example |  
|---|---|---|
| Liquid | An open-source, customer-facing template language created by Shopify and written in Ruby; used to load/pull dynamic content. | `{{${first_name}}}` will insert a user's first name into a message. |
| Object | A denotation of a variable and location of intended variable name that tells Liquid where to show content in the message. | `{{${first_name}}}` will insert a user's first name into a message. |
| Conditional Logic Tag | Tags create logic and control the flow for templates. In Braze's case, Conditional Logic Tags are Liquid used to consider intelligent or programming logic to create exceptions and variations in messages based on certain, predefined criteria. | ```{% if ${language} == 'en' %}``` will trigger your message in a designated way in the event that a user has designated "English" as their language. |
| Filters | Used to change, narrow, or reformat the output of the Liquid Object. It is often used to create mathematical operations. |  ```{{"Big Sale" | upcase}}``` will cause the words "Big Sale" to appear as "BIG SALE" in the message. |
| Operators | Used in messages to create dependencies or criteria that can affect which message your user receives. | Is a user meets the defined criteria in a messaged tagged with `{% custom_attribute.${Total_Revenue} > 0%}`, they will receive the message. If not, they will receive another designated message (or not), depending on what you set. |

{% endraw %}

[1]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[2]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/
[3]: https://shopify.github.io/liquid/basics/introduction/
[9]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[11]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_events/
[39]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information
[40]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information
