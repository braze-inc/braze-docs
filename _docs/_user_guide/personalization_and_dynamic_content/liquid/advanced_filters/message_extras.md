---
nav_title: Message extras tag
article_title: Message Extras Tag
page_order: 1
description: "This article explains how to use the message extras Liquid tag and how to check for syntax."
alias: "/message_extras_tag/"
---

# Message extras Liquid tag

> Use the `message_extras` Liquid tag to annotate your send events with dynamic data from Connected Content, Catalogs, custom attributes (such as language, country), Canvas entry properties, or other data sources.

The `message_extras` Liquid tag appends key-value pairs to the corresponding send event in Currents and Snowflake Data Sharing. 

To send dynamic or extra data back to your Currents or Snowflake Data Sharing send event, insert the proper Liquid tag into your message body. 

Here's an example of the standard Liquid tag format for `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

You can add these tags as needed for your key-value pairs in the message body. However, the length of all keys and values shouldn't exceed 1&nbsp;KB. In Currents and Snowflake Data Sharing, you'll see a new event field called `message_extras` for your send events. This will generate a JSON serialized string in one field.

## Supported channels

The `message_extras` tag is supported for all message types with a send event, along with in-app message impression events. Using `message_extras` with in-app messages requires certain [minimum SDK versions](#iam-sdk) to be met.

## How to use the `message_extras` tag

1. In the message body for the channel, enter the `message_extras` Liquid tag. Or, you can use the **Add Personalization** modal and select **Message Extras** for the personalization type. 

![The Add Personalization modal with Message Extras selected as the personalization type.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Enter the [key-value pair]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) for each `message_extras` tag. 

![An example of key-value pairs for the message extras tag. The title field reads "Your New Favorites." The message reads key-value pairs for the message extras tag and the following sentence: "We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites"]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. After your campaign or Canvas has been sent, Braze will attach the dynamic data at the send time via the Currents or Snowflake Data Sharing send events to the `message_extras` field.

## Checking syntax

Any other input that doesn't match the tag standard discussed above may fail to pass to Currents or Snowflake. Check that your syntax or formatting doesn't include any of the following:

- Non-existent, empty, or mistyped delimiters
- Duplicate keys (Braze will default to sending the key-value pair that is encountered first)
- Extra text before keys or values are defined
- Out of order keys and values 
  - {% raw %}For example, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Sending promotion code information to Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Considerations

- If your key-values exceed 1&nbsp;KB, they'll truncate. 
- Whitespace will count toward the character count. Note that Braze omits the leading and trailing whitespaces.
- The resulting JSON will output only string values.
- You can include Liquid variables as a key or value, but you can't use other Liquid tags within `message_extras`.
  - For example, you could use the following Liquid: {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Frequently asked questions

#### How can I associate the message_extras field in the send events to my engagement events like opens and clicks? 

A `dispatch_id` is generated and provided in your send events, which can be used as a unique identifier to tie to specific click, open or delivered events. You'll be able to use and query this field in Currents or Snowflake. Learn more about [`dispatch_id` behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

#### Can I use message_extras with in-app messages? {#iam-sdk}

Yes, you can use `message_extras` in your in-app messages as long as your users' devices are on the following minimum SDK versions:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

