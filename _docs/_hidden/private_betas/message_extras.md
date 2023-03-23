---
nav_title: Message Extras Tag
permalink: "/message_extras_tag/"
hidden: true
---

# Message extras Liquid tag

Using the `message_extras` Liquid tag, you can annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. This Liquid tag appends key-value pairs to the corresponding send event in Currents.

{% alert important %}
This Liquid tag is currently in beta for email, SMS, and push send events. Contact your Braze customer success manager if you're interested in participating in the beta.
{% endalert %}

To send dynamic or extra data back to your Currents send event, insert the proper Liquid tag in the body of your email message. The following is an example of the `message_extras` Liquid tag:

{% raw %}
```
{% message_extras :key test :value 123 %}
```
{% endraw %}

You can add these tags as needed for your key-value pairs in the message body. However, the length of all keys and values should not exceed 1kb. In Currents, you'll see a new event field called, `message_extras`, for your send events. This will generate a JSON serialized string in one field. 

## Considerations

- If your key-values exceed 1kb, they'll truncate. 
- Whitespace will count towards the character count. Note that Braze omits the leading and trailing whitespaces.
- The resulting JSON will output only string values.
- Liquid variables can be included as a key or value, but Liquid tags are not supported directly. 