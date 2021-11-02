---
nav_title: Pulling User Profile Data
article_title: Pulling User Profile Data in Connected Content Calls
page_order: 5
description: "This article covers how to pull user profiles into your Connected Content calls, and best practices involving Liquid templating."

---

# Pulling user profile data in Connected Content calls

If a Connected Content response contains user profile fields (within a Liquid personalization tag), these values must be defined earlier in the message via Liquid, before the Connected Content call in order to render the Liquid passback properly. Similarly, the `:rerender` flag must be included in the request. 

{% alert note %}
The `:rerender` flag is only one level deep, meaning that it will not apply to any nested Connected Content tags.
{% endalert %}

For personalization, Braze pulls user profile fields before passing that field to Liquid—so if the response from Connected Content has user profile fields, it must be defined beforehand. 

For example, if this were the Connected Content call:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
And the Connected Content response is {% raw %}`Your language is ${language}`{% endraw %}, the content displayed in this scenario will be `Hi Jon, your language is`. The language itself will not be templated.

In order to render the Liquid passback properly, you must put the {% raw %}`${language}`{%endraw%} tag anywhere in the body, as shown below.
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
Remember that the `:rerender` flag option is only one level deep. If the Connected Content response itself has more Connected Content tags, Braze will not re-render those additional tags.
{% endalert %}
