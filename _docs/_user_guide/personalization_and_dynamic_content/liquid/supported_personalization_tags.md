---
nav_title: Supported Personalization Tags
article_title: Supported Liquid Personalization Tags
page_order: 1
description: "This reference article covers a complete list of supported Liquid personalization tags."
search_rank: 1
---

# Supported personalization tags

> This reference article covers a complete list of supported Liquid personalization tags.

As a convenience, a summary of supported personalization tags are provided. For more detail on each kind of tag and best practices, continue reading.

{% raw %}

| Personalization Tag Type | Tags |
| -------------  | ---- |
| Standard (Default) Attributes | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Device Attributes | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| [Email List Attributes][43] | `{{${set_user_to_unsubscribed_url}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| [SMS Attributes][48] | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| Campaign Attributes | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Canvas Attributes | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Canvas Step Attributes | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Card Attributes | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Geofencing Events | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Event Properties <br> (These are custom to your app group.)| `{{event_properties.${your_custom_event_property}}}` |
| Canvas Entry Properties| `{{canvas_entry_properties}}` |
| Custom Attributes <br> (These are custom to your app group.) | `{{custom_attribute.${your_custom_attribute}}}` |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

Refer to this help article to learn more about [how some of these attributes differ across sources in Braze]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

{% alert important %}
Campaign, Card, and Canvas attributes are only supported in their corresponding messaging templates (for example, `dispatch_id` is not available in in-app message campaigns).
{% endalert %}

#### Canvas and campaign tag differences 

The behavior for the following tags differs between Canvas and campaigns:
{% raw %}
- `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps as triggered events, even when they are "scheduled" (except for Entry Steps, which can be scheduled). To learn more, refer to [Dispatch ID behavior][50].
- Using the `{{campaign.${name}}}` tag with Canvas will display the Canvas component name. When using this tag with campaigns, it will display the campaign name.
{% endraw %}

## Most recently used device information

You can template in the following attributes for the user's most recent device across all platforms. If a user has not used your application (e.g., you imported the user via REST API), then these values will all be `null`.

{% raw %}

|Tag | Description |
|---|---|
|`{{most_recently_used_device.${browser}}}` | The most recently used browser on the user's device. Examples include "Chrome" and "Safari". |
|`{{most_recently_used_device.${id}}}` | This is Braze's device identifier. On iOS, this can be the Apple Identifier for Vendor (IDFV) or a UUID. For Android and other platforms it is a randomly generated UUID. |
| `{{most_recently_used_device.${carrier}}}` | The most recently used device's telephone service carrier, if available. Examples include "Verizon" and "Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | If the device has ad tracking enabled or not. This is a boolean value (`true` or `false`). |
| `{{most_recently_used_device.${idfa}}}` | For iOS devices, this value will be the Identifier for Advertising (IDFA) if your application is configured with Braze's [optional IDFA collection][40]. For non-iOS devices, this value will be null. |
| `{{most_recently_used_device.${google_ad_id}}}` | For Android devices, this value will be the Google Play Advertising Identifier if your application is configured with Braze's optional Google Play Advertising ID collection. For non-Android devices, this value will be null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | For Roku devices, this value will be the Roku Advertising Identifier that is collected when your application is configured with Braze. For non-Roku devices, this value will be null. |
| `{{most_recently_used_device.${model}}}` | The device's model name, if available. Examples include "iPhone 6S" and "Nexus 6P" and "Firefox". |
| `{{most_recently_used_device.${os}}}` | The device's operating system, if available. Examples include "iOS 9.2.1" and "Android (Lollipop)" and "Windows". |
| `{{most_recently_used_device.${platform}}}` | The device's platform, if available. If set, the value will be one of `ios`, `android`, `kindle`, `android_china`, `web`, or `tvos`. |
{: .reset-td-br-1 .reset-td-br-2}


Because there are such a wide range of device carriers, model names, and operating systems, we advise that you thoroughly test any Liquid that conditionally depends on any of those values. These values will be `null` if they are not available on a particular device.

## Targeted device information

For push notification and in-app message channels, you can template in the following attributes for the device to which a message is being sent. That is, a push notification or in-app message can include device attributes of the device on which the message is being read. Note that these attributes will not work for Content Cards. 

|Tag | Description |
|------------------|---|
| `{{targeted_device.${id}}}` | This is Braze's device identifier. On iOS, this can be the Apple Identifier for Vendor (IDFV) or a UUID. For Android and other platforms it is a randomly generated UUID. |
| `{{targeted_device.${carrier}}}` | The most recently used device's telephone service carrier, if available. Examples include "Verizon" and "Orange". |
| `{{targeted_device.${idfa}}}` | For iOS devices, this value will be the Identifier for Advertising (IDFA) if your application is configured with Braze's [optional IDFA collection][40]. For non-iOS devices, this value will be null. |
| `{{targeted_device.${google_ad_id}}}` | For Android devices, this value will be the Google Play Advertising Identifier if your application is configured with Braze's [optional Google Play Advertising ID collection]. For non-Android devices, this value will be null. |
| `{{targeted_device.${roku_ad_id}}}` | For Roku devices, this value will be the Roku Advertising Identifier that is collected when your application is configured with Braze. For non-Roku devices, this value will be null. |
| `{{targeted_device.${model}}}` | The device's model name, if available. Examples include "iPhone 6S" and "Nexus 6P" and "Firefox". |
| `{{targeted_device.${os}}}` | The device's operating system, if available. Examples include "iOS 9.2.1" and "Android (Lollipop)" and "Windows". |
| `{{targeted_device.${platform}}}` | The device's platform, if available. If set, the value will be one of `ios`, `android`, `kindle`, `android_china`, `web`, or `tvos`. You can also use the `most_recently_used_device` personalization tag. |
| `{{targeted_device.${foreground_push_enabled}}}` | This value will be `true` when the targeted device is enabled for foreground push, `false` otherwise. |
{: .reset-td-br-1 .reset-td-br-2}


{% endraw %}


Because there are such a wide range of device carriers, model names, and operating systems, we advise that you thoroughly test any logic that conditionally depends on any of those values. These values will be `null` if they are not available on a particular device. Furthermore, for push notifications, it is possible that Braze may be unable to discern the device attached to the push notification under certain circumstances such as if the push token was imported via API, resulting in values being `null` for those messages.

![Example of using a default value of "there" when using a first name variable in a push message.][4]

In some circumstances, you may opt to use [conditional logic][17] instead of setting a default value. Conditional logic allows you to send messages that differ based on the value of a custom attribute.

Additionally, you can use conditional logic to [abort messages][18] to customers with null or blank attribute values.

For example, if you're sending a rewards balance notification to customers, there isn't a good way to account for customers with low and null balances using default values.

In this case, there are two options that may work better than setting a default value:

1. Abort the message for customers with low, null, and blank balances.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Send a completely different message to these customers, perhaps something along the lines of:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

In this example, a user with a blank or null first name will get the message "Thanks for downloading". You should include a [default value][47] for first name to ensure that your customer does not see Liquid in the event of a mistake.

{% endraw %}

## Variable tags

You can use the `assign` tag to create a variable in the message composer. Once you create a variable, you can reference that variable in your messaging logic or message.

Let's say that you allow your customers to cash in their rewards points for prizes once they accrue 100 rewards points. So, you only want to message customers who would have a points balance greater than or equal to 100 if they made that additional purchase:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
This tag comes in handy when you want to reformat content that is returned from our [Connected Content][4] feature. You can read more in Shopify's documentation on [variable tags][31].

{% endraw %}

{% alert tip %}
Find yourself assigning the same variables in every message? Instead of writing out the `assign` tag over and over again, you can save that tag as a Content Block and put it at the top of your message instead.

1. [Create a Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Give your Content Block a name (no spaces or special characters).
3. Click **Edit** at the bottom of the page.
4. Type in your `assign` tags.

As long as the Content Block is at the top of your message, every time the variable is inserted into your message as an object, it will refer to your chosen custom attribute!
{% endalert %}

## Iteration tags

{% raw %}
Iteration tags can be used to run a block of code repeatedly. This example features the `for` tag.

Let's say that you're having a sale on Nike sneakers and want to message customers who've expressed interest in Nike. You have an array of product brands viewed on each customer's profile. This array could contain up to 25 product brands, but you only want to message customers who viewed a Nike product as one of their 5 most recent product views.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

In this example, we check the first five items in the sneaker brands viewed array. If one of those items is converse, we create the converse_viewer variable and set it to true.

Then, we send the sale message when converse_viewer is true. Otherwise, we abort the message.

This is a simple example of how iteration tags can be used in Braze's message composer. You can find more information in Shopify's documentation on [iteration tags][32].

## Syntax tags

Syntax tags can be used to control how Liquid is rendered. You can use the `echo` tag to return an expression. This is the same as wrapping an expression using curly brackets, except you can use this tag within Liquid tags. You can also use the `liquid` tag to have a block of Liquid without any delimiters on each tag. Each tag has to be in its own line when using the `liquid` tag. Check out Shopify's documentation on [syntax tags][33] for more information and examples.

With [whitespace control][49], you can remove whitespaces around your tags, helping you further control what the Liquid output looks like.

## HTTP status codes {#http-personalization}

You can utilize the HTTP status from a [Connected Content][38] call by first saving it as a local variable and then using the `__http_status_code__` key. For example:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
  This key will only be automatically added to the Connected Content object if the endpoint returns a JSON object. If the endpoint returns an array or other type, then that key cannot be set automatically in the response.
{% endalert %}

## Sending messages based on language, most recent locale, and time zone

In some situations you may wish to send messages that are specific to particular locales. For example, Brazilian Portuguese is typically different than European Portuguese.

Here's an example of how you can use most recent locale to further localize an internationalized message.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

In this example, customers with a most recent locale of 'pt_BR' will get a message in Brazilian Portuguese, and customers with a most recent locale of 'pt_PT' will get a message in European Portuguese. Customers who don't meet the first two conditions but have their language set to Portuguese will get a message in whatever you'd like the default Portuguese language type to be.

You can also target users by their time zone. For example, send one message if they are based in EST and another if they are PST. To do this, save the current time in UTC, and compare an if/else statement with the user's current time to ensure you're sending the right message for the right time zone. You should set the campaign to send in the user's local time zone, to ensure they are getting the campaign at the right time. See the following example for how to write a message that will go out between 2 pm and 3 pm and will have a specific message for each time zone.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

[30]: https://shopify.dev/api/liquid/tags#syntax-tags
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[33]: https://shopify.dev/api/liquid/tags#syntax-tags
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[4]: {% image_buster /assets/img_archive/personalized_firstname_.png %}
[17]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/
[43]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[47]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#trigger-messages-by-keyword
[49]: https://shopify.github.io/liquid/basics/whitespace/
[50]: {{site.baseurl}}/help/help_articles/data/dispatch_id/
