---
nav_title: FAQ
article_title: Frequently Asked Questions
page_order: 11
description: "This article provides answers to frequently asked questions about Liquid."

---

# Frequently asked questions

> On this page, you'll find answers to some frequently asked questions about Liquid.<br><br>Braze does not currently support 100% of Shopify’s Liquid, only certain portions which we have attempted to outline in our documentation. We highly recommend testing all messages using Liquid before sending them to reduce the risk of errors or using unsupported Liquid.

### How do I use Liquid snippets in Braze?

In many cases, you can incorporate Liquid snippets to [personalize the messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) in your campaigns and Canvases. 

#### Where can I learn more?

For more on Liquid, check out our guided [Dynamic Personalization with Liquid](https://learning.braze.com/dynamic-personalization-with-liquid) Braze Learning course!

### What is Liquid templating?

This is the most common way of using Liquid in Braze. Liquid templating involves pulling data from a user's profile into a message. This data can range from a user's first name to custom events from an event triggered message.

Refer to [Supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) for a complete list of the supported Liquid tags.

### How do I assign variables with Liquid?

You can create and assign variables by using the `assign` tag. This creates a variable in the message composer that can also be referenced throughout your message.

### What is abort logic, and how can I use it?

Abort logic allows you to stop a message from being sent if the conditions are met. This is especially helpful in preventing incomplete messages from being sent to your users. For examples of abort logic in your marketing campaigns, read more at [Aborting messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/).

### What is for loop logic, and how can I use it?

For loops are also known as [iteration tags](https://shopify.github.io/liquid/tags/iteration/). Using for loop logic in your Liquid snippets allows you to cycle through blocks of Liquid until a condition is met. 

In Braze, this could be used for checking items in an array custom attribute, or a list of values and objects returned by a [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) or [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) call response. Specifically, you can use for loop logic as part of your messaging to check whether a product is in stock, or if a product has a minimum rating. 

For example, if you wanted to search a catalog with 100 rows and include all images for a shoe company named Get Going, you could use this Liquid snippet:

{% raw %}
```
{% for item in catalog %}
{% if {{item.brand}} = "GetGoing %}
{{item.image}}
{% endif %}
{% endfor %}
```
{% endraw %}

Once the set conditions are met, your message can proceed. Using this logic is a helpful way to save time, instead of repeating Liquid blocks for different conditions.

### Does using Liquid consume data points?

No.
