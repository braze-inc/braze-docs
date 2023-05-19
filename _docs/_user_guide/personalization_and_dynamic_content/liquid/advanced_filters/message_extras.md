---
nav_title: Message Extras Tag
article_title: Message Extras Tag
page_order: 1
description: "This article explains how to use the message extras Liquid tag and how to check for syntax."
alias: "/message_extras_tag/"
---

# Message extras Liquid tag

> Using the `message_extras` Liquid tag, you can annotate your send events with dynamic data from Connected Content, Catalogs, custom attributes (such as language, country), Canvas entry properties, or other data sources. 

The `message_extras` Liquid tag appends key-value pairs to the corresponding send event in Currents. This is supported for all message types with a send event.

To send dynamic or extra data back to your Currents send event, insert the proper Liquid tag into your message body. The following is an example of the standard Liquid tag format for `message_extras`: 

{% raw %}
```
{% message_extras :key test :value 123 %}
```
{% endraw %}

You can add these tags as needed for your key-value pairs in the message body. However, the length of all keys and values should not exceed 1&nbsp;KB. In Currents, you'll see a new event field called `message_extras` for your send events. This will generate a JSON serialized string in one field. 

## How to use

1. In the message body for the channel, input the `message_extras` Liquid tag. Or, you can use the **Add Personalization** modal and select **Message Extras** for the personalization type. <br>![The Add Personalization modal with Message Extras selected as the personalization type.][1]{: style="max-width:70%;"}
2. Enter the [key-value pair]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) for each `message_extras` tag. <br>![An example of key-value pairs for the message extras tag. The title field reads "Your New Favorites." The message reads key-value pairs for the message extras tag and the following sentence: "We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites"][2]{: style="max-width:70%;"}
3. After your campaign or Canvas has been sent, Braze will attach the dynamic data at the send time via the Currents send events to the `message_extras` field.

## Checking syntax

Any other input that doesn't match the aforementioned tag standard may fail to pass to Currents. Check that your syntax or formatting doesn't include any of the following:

- Non-existent, empty, or mistyped delimiters
- Duplicate keys (Braze will default to sending the key-value pair that is encountered first)
- Extra text before keys or values are defined
- Out of order keys and values 
  - {% raw %}For example, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Considerations

- If your key-values exceed 1&nbsp;KB, they'll truncate. 
- Whitespace will count towards the character count. Note that Braze omits the leading and trailing whitespaces.
- The resulting JSON will output only string values.
- Liquid variables can be included as a key or value, but Liquid tags are not supported directly. 
  - For example, {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Frequently asked questions

#### How can I associate the message_extras field in the send events to my engagement events like opens and clicks? 

A `dispatch_id` is generated and provided in your send events, which can be used as a unique identifier to tie to specific click, open or delivered events. You will be able to utilize and query this field in Currents or Snowflake. Learn more about [`dispatch_id` behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

[1]: {% image_buster /assets/img_archive/message_extras1.png %}
[2]: {% image_buster /assets/img_archive/message_extras2.png %}
