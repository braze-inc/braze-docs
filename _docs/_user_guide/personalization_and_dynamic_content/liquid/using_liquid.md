---
nav_title: Using Liquid
page_order: 0
---

# Using Liquid

{% raw %}

Once you know the [liquid tags available][1], using liquid can elevate the personalization in your messages to impressive heights. Liquid tags act as placeholders in your messages that can pull in consented information from your user's account and enable personalization and relevant messaging practices. In the block below, you can see that a dual usage of a liquid tag to call the user's first name, as well as a default tag in the event that a user would not have their first name registered.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

To a user named Janet Doe, the message would appear to the user as either:

```
Hi Janet, thanks for using the App!
```

Or...

```
Hi Valued User, thanks for using the App!
```

## Inserting Tags

You can insert tags by typing `{{` in any message, which will trigger an auto-completion feature that will continue to update as you type. You can even select a variable from the options that appear as you type.

If you're using a custom tag, you can copy and paste the tag into whatever message you desire.

{% endraw %}

{% alert note %}

If you choose to use Liquid in your Email messages, be sure to insert it using the HTML editor, as opposed to the classic editor. The Classic Editor may parse the liquid as plaintext.

{% endalert %}

{% raw %}


### Pre-Formatted Variables

You can insert pre-formatted variables with defaults through the "Insert Personalization Attribute" modal located on the top-right of any templated text field.

![Modal buttons][44]

The modal will insert Liquid with your specified default value at the point that your cursor was. The insertion point is also specified via the preview box, which has the before and after text. If a block of text is highlighted, the highlighted text will be replaced.

![Modal][45]

{% endraw %}




[1]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
