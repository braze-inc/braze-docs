---
nav_title: Aborting Connected Content
article_title: Aborting Connected Content
page_order: 2
description: "Using Liquid templating, you have the option to abort messages with conditionals. This reference article covers some message aborting best practices."

---

# Aborting messages {#aborting-connected-content}

Using Liquid templating, you have the option to abort messages with conditionals. For example:

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```

In the example above, the conditionals `connected.recommendations.size < 5` and `connected.foo.bar == nil` specify situations that would cause the message to be aborted.

You can also specify an abort reason, which will be saved to the __Message Activity Log__ in your __Developer Console__. This abort reason must be a string and cannot contain Liquid.

`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze does not count Aborted Messages towards the send count in your Braze account or in Currents.
{% endalert %}
