---
nav_title: Aborting Connected Content
article_title: Aborting Connected Content
page_order: 2
description: "This reference article covers some message aborting best practices for Connected Content."
---

# Aborting Connected Content {#aborting-connected-content}

> When you use Liquid templating, you have the option to abort messages with conditional logic. This page covers best practices when doing so.

In the following example, the conditionals `connected.recommendations.size < 5` and `connected.foo.bar == nil` specify situations that would cause the message to be aborted.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Specify an abort reason

You can also specify an abort reason, which will be saved to the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). This abort reason must be a string and cannot contain Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze doesn't count aborted messages toward the send count in your Braze account or in Currents.
{% endalert %}
