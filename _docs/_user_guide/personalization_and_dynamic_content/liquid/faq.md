---
nav_title: FAQ
article_title: Frequently Asked Questions
page_order: 12
description: "This article provides answers to frequently asked questions about Liquid."

---

# Frequently asked questions

> On this page, you'll find answers to some frequently asked questions about Liquid.<br><br>Braze does not currently support 100% of Shopify’s Liquid, only certain portions which we have attempted to outline in our documentation. We highly recommend testing all messages using Liquid before sending them to reduce the risk of errors or using unsupported Liquid.

### How do I use Liquid snippets in Braze?

In many cases, you can incorporate Liquid snippets by navigating to your campaigns or Canvases, and inserting Liquid in the personalization modal in areas such as the email message body or in your segments. 

#### Where can I learn more?

For more on Liquid, check out our guided [Dynamic Personalization with Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze Learning path! You can also reference the [Liquid use case library]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) for inspiration and a range of personalization examples using Liquid.

### What’s the difference between using Liquid and Connected Content for personalization?

Braze Connected Content is an example of a Liquid tag. It's also used for personalization, but this data comes from an external endpoint rather than stored data within Braze. Check out our dedicated [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) section to learn more about expanding how you can personalize your messages.

### What is Liquid templating?

This is the most common way of using Liquid in Braze. Liquid templating involves pulling data from a user's profile into a message. This data can range from a user's first name to custom events from an event triggered message.

Refer to [Supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) for a complete list of the supported Liquid tags.

### How do I assign variables with Liquid?

You can create and assign variables by using the `assign` tag. This creates a variable in the message composer that can also be referenced throughout your message.

### Does using Liquid consume data points?

No.

### How can I use Liquid to send a personalized greeting?

For a personalized greeting using a user's first name, you can pull the standard user profile attributes such as {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

You can also use a Liquid `{% if X %}` {% endraw %}statement to do conditional rendering based on anything, such as the day of the week or custom attributes. For more information on the supported Liquid operators that can be used in conditional statements, check out [Operators]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/).

### How can I personalize a message based on a customer’s location?

{% raw %}
There is a default attribute for the user’s location: `{{${most_recent_location}}}`.

### What's the difference between {{campaign.${name}}} and {{campaign.${message_name}}}?

Both `{{campaign.${name}}}` and `{{campaign.${message_name}}}` are supported Liquid personalization tags. Both tags reference campaign attributes. `{{campaign.${name}}}` denotes the name of your campaign, and `{{campaign.${message_name}}}` is the name of your message variant.
{% endraw %}

### How do I use Liquid with nested objects?

Braze has a built-in feature that generates Liquid code for segments that can be used in a message. Specifically, you can create a segment that matches multiple criteria in an object.

For more information, check out [Multi-criteria segmentation]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### How do I use event attributes to personalize a message that an event is triggering?

{% raw %}
You can access properties of API triggered events with the `api_triggered_property` tag: `{{api_trigger_properties.${attribute_key}}}`.  
{% endraw %}

### What is abort logic, and how can I use it?

Abort logic allows you to stop a message from being sent if the conditions are met. This is especially helpful in preventing incomplete messages from being sent to your users. For examples of abort logic in your marketing campaigns, read more at [Aborting messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/).

### What is for loop logic, and how can I use it?

For loops are also known as [iteration tags](https://shopify.github.io/liquid/tags/iteration/). Using for loop logic in your Liquid snippets allows you to cycle through blocks of Liquid until a condition is met. 

In Braze, this could be used for checking items in an array custom attribute, or a list of values and objects returned by a [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), [selection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/), or [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) call response. Specifically, you can use for loop logic as part of your messaging to check whether a product is in stock, or if a product has a minimum rating. 

For example, let's say you have a catalog called "Games" that has a selection called "cheap_games". To pull the titles of the games in "cheap_games", you could use this Liquid snippet:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Once the set conditions are met, your message can proceed. Using this logic is a helpful way to save time, instead of repeating Liquid blocks for different conditions.
