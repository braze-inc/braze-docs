---
nav_title: Message Extras Tag
article_title: Message Extras Tag
page_order: 1
description: "This article explains how to use the message extras Liquid tag and how to check for syntax."
---

# Message extras Liquid tag

Using the `message_extras` Liquid tag, you can annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. This Liquid tag appends key-value pairs to the corresponding send event in Currents.

{% alert important %}
This Liquid tag is currently in beta for email, SMS, and push send events. Contact your Braze customer success manager if you're interested in participating in the beta.
{% endalert %}

To send dynamic or extra data back to your Currents send event, insert the proper Liquid tag in the body of your email message. The following is an example of the standard Liquid tag format for `message_extras`: 

{% raw %}
```
{% message_extras :key test :value 123 %}
```
{% endraw %}

You can add these tags as needed for your key-value pairs in the message body. However, the length of all keys and values should not exceed 1KB. In Currents, you'll see a new event field called `message_extras` for your send events. This will generate a JSON serialized string in one field. 

## Checking syntax

Any other input that doesn't match the aforementioned tag standard may fail to pass to Currents. Check that your syntax or formatting doesn't include any of the following:

- Non-existent, empty, or mistyped delimiters
- Duplicate keys (Braze will default to sending the key-value pair that is encountered first)
- Extra text before keys or values are defined
- Out of order keys and values 
  - {% raw %}For example, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Considerations

- If your key-values exceed 1KB, they'll truncate. 
- Whitespace will count towards the character count. Note that Braze omits the leading and trailing whitespaces.
- The resulting JSON will output only string values.
- Liquid variables can be included as a key or value, but Liquid tags are not supported directly. 
  - For example, {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}