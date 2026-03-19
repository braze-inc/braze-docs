---
nav_title: Pulling user profile data
article_title: Pull User Profile Data in Connected Content Calls
page_order: 3
description: "This article covers how to pull user profiles into your Connected Content calls, and best practices involving Liquid templating."
toc_headers: h2
---

# Pull user profile data

> This page covers how to pull user profiles into your Connected Content calls and best practices involving Liquid templating. 

## Prerequisites

If a Connected Content response contains user profile fields (within a Liquid personalization tag), these values must be defined earlier in the message with Liquid, before the Connected Content call in order to render the Liquid passback properly. Similarly, the `:rerender` flag must be included in the request. Note that the `:rerender` flag is only one level deep, meaning that it will not apply to any nested Connected Content tags.

## Liquid templating in Connected Content calls

For personalization, Braze pulls user profile fields before passing that field to Liquid—so if the response from Connected Content has user profile fields, it must be defined beforehand. 

For example, if this were the Connected Content call:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

The Connected Content response is {% raw %}`Your language is ${language}`{% endraw %}. The content displayed in this example is `Hi Jon, your language is`. 

The language itself won't be templated. This is because Braze needs to know what fields to retrieve from the user before we make the Connected Content call.

To render the Liquid passback properly, you must include the {% raw %}`${language}`{% endraw %} tag anywhere in the request, as shown in the following code snippet. The Liquid preprocessor will know to grab the "language" attribute from the user to have it ready for templating the response.

{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Remember that the `:rerender` flag option is only one level deep. If the Connected Content response itself has more Connected Content tags or any catalog tags, Braze will not re-render those additional tags.
{% endalert %}

## Best practices

### Use `json_escape` with Liquid tags that could break the JSON format

When using `:rerender`, add the `json_escape` filter to any Liquid tag that could potentially break the JSON format. If your Liquid tags contain characters that break the JSON format, the entire Connected Content response will be interpreted as text and be templated into the message, and none of the variables will be saved.

For example, if the `message` event property in the example below contains characters that could break the JSON format, add the `json_escape` filter like in this example:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}