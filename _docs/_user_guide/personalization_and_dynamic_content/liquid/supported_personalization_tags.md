---
nav_title: Supported personalization tags
article_title: Supported Liquid Personalization Tags
page_order: 1
description: "This reference article covers a complete list of supported Liquid personalization tags."
search_rank: 1
---

# Supported personalization tags

> This reference article covers a complete list of supported Liquid personalization tags.

## Summary of supported tags

As a convenience, a summary of supported personalization tags are provided. For more detail on each type of tag and best practices, continue reading.

{% raw %}

| Personalization tag type | Tags |
| -------------  | ---- |
| Standard (Default) Attributes | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Device Attributes | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| [Email List Attributes]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) | `{{${set_user_to_unsubscribed_url}}}` <br>This tag replaces the previous `{{${unsubscribe_url}}}` tag. While the older tag will still work in previously created emails, we recommend that you use the newer tag instead. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| [SMS Attributes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#trigger-messages-by-keyword) | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| [WhatsApp Attributes]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/) | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` |
| Campaign Attributes | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Canvas Attributes | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Canvas Step Attributes | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Card Attributes | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Geofencing Events | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Event Properties <br> (These are custom to your workspace.)| `{{event_properties.${your_custom_event_property}}}` |
| Canvas Context Variables | `{{context}}` |
| Custom Attributes <br> (These are custom to your workspace.) | `{{custom_attribute.${your_custom_attribute}}}` |
| [API trigger Properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) |`{{api_trigger_properties}}` |
| Canvas Entry Properties | `{{canvas_entry_properties.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Supported attributes

Campaign, Card, and Canvas attributes are only supported in their corresponding messaging templates (for example, `dispatch_id` isn't available in in-app message campaigns).

Refer to this help article to learn more about [how some of these attributes differ across sources in Braze]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

### Canvas and campaign tag differences 

The behavior for the following tags differs between Canvas and campaigns:
{% raw %}
- `dispatch_id` behavior differs because Braze treats Canvas steps as triggered events, even when they are "scheduled" (except for entry steps, which can be scheduled). To learn more, refer to [Dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- Using the `{{campaign.${name}}}` tag with Canvas will display the Canvas component name. When using this tag with campaigns, it will display the campaign name.
{% endraw %}

## Most recently used device information

You can template the following attributes for the user's most recent device across all platforms. If a user has not used your application (for example, you imported the user via REST API), then these values will all be `null`.

{% raw %}

|Tag | Description |
|---|---|
|`{{most_recently_used_device.${browser}}}` | The most recently used browser on the user's device. Examples include "Chrome" and "Safari". |
|`{{most_recently_used_device.${id}}}` | The Braze device identifier. On iOS, this can be the Apple Identifier for Vendor (IDFV) or a UUID. For Android and other platforms, it's a randomly generated UUID. |
| `{{most_recently_used_device.${carrier}}}` | The most recently used device's telephone service carrier, if available. Examples include "Verizon" and "Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | If the device has ad tracking enabled or not. This is a boolean value (`true` or `false`). |
| `{{most_recently_used_device.${idfa}}}` | For iOS devices, this value will be the Identifier for Advertising (IDFA) if your application is configured with our [optional IDFA collection]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). For non-iOS devices, this value will be null. |
| `{{most_recently_used_device.${google_ad_id}}}` | For Android devices, this value will be the Google Play Advertising Identifier if your application is configured with our optional Google Play Advertising ID collection. For non-Android devices, this value will be null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | For Roku devices, this value will be the Roku Advertising Identifier that is collected when your application is configured with Braze. For non-Roku devices, this value will be null. |
| `{{most_recently_used_device.${model}}}` | The device's model name, if available. Examples include "iPhone 6S" and "Nexus 6P" and "Firefox". |
| `{{most_recently_used_device.${os}}}` | The device's operating system, if available. Examples include "iOS 9.2.1" and "Android (Lollipop)" and "Windows". |
| `{{most_recently_used_device.${platform}}}` | The device's platform, if available. If set, the value will be one of `ios`, `android`, `kindle`, `android_china`, `web`, or `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Because there is such a wide range of device carriers, model names, and operating systems, we advise that you thoroughly test any Liquid that conditionally depends on any of those values. These values will be `null` if they are not available on a particular device.

## Targeted app information

For in-app messages, you can use the following app attributes within Liquid. The values are based on which SDK API key your apps use to request messaging.

|Tag | Description |
|------------------|---|
| `{{app.${api_id}}}` | The API key of the app requesting the message. For example, you use this key in conjunction with `abort_message()` Liquid to avoid sending in-app messages to certain apps, such as TV platforms or development builds that use a separate SDK API key.|
| `{{app.${name}}}` | The name of the app (as defined in the Braze dashboard) requesting the message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For example, this Liquid code will abort a message if the requesting apps are not one of the two API keys in the list:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Targeted device information

For push notifications and in-app message channels, you can template in the following attributes for the device to which a message is being sent. That is, a push notification or in-app message can include device attributes of the device on which the message is being read. Note that these attributes won't work for Content Cards. 

|Tag | Description |
|------------------|---|
| `{{targeted_device.${id}}}` | This is the Braze device identifier. On iOS, this can be the Apple Identifier for Vendor (IDFV) or a UUID. For Android and other platforms, it is a randomly generated UUID. For example, if a user has five devices, a send attempt occurs for all five devices, each using the corresponding device identifier. If a message is configured to send to a user's most recently used device, only one send attempt will occur to the most recently used device identified through Braze. |
| `{{targeted_device.${carrier}}}` | The most recently used device's telephone service carrier, if available. Examples include "Verizon" and "Orange". |
| `{{targeted_device.${idfa}}}` | For iOS devices, this value will be the Identifier for Advertising (IDFA) if your application is configured with our [optional IDFA collection]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). For non-iOS devices, this value will be null. |
| `{{targeted_device.${google_ad_id}}}` | For Android devices, this value will be the Google Play Advertising Identifier if your application is configured with our [optional Google Play Advertising ID collection]. For non-Android devices, this value will be null. |
| `{{targeted_device.${roku_ad_id}}}` | For Roku devices, this value will be the Roku Advertising Identifier that is collected when your application is configured with Braze. For non-Roku devices, this value will be null. |
| `{{targeted_device.${model}}}` | The device's model name, if available. Examples include "iPhone 6S" and "Nexus 6P" and "Firefox". |
| `{{targeted_device.${os}}}` | The device's operating system, if available. Examples include "iOS 9.2.1" and "Android (Lollipop)" and "Windows". |
| `{{targeted_device.${platform}}}` | The device's platform, if available. If set, the value will be one of `ios`, `android`, `kindle`, `android_china`, `web`, or `tvos`. You can also use the `most_recently_used_device` personalization tag. |
| `{{targeted_device.${foreground_push_enabled}}}` | This value will be `true` when the targeted device is enabled for foreground push, `false` otherwise. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

Because there is such a wide range of device carriers, model names, and operating systems, we advise that you thoroughly test any logic that conditionally depends on any of those values. These values will be `null` if they are not available on a particular device. 

Furthermore, for push notifications, it's possible that Braze won't be able to discern the device attached to the push notification under certain circumstances such as if the push token was imported through API, resulting in values being `null` for those messages.

![Example of using a default value of "there" when using a first name variable in a push message.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Using conditional logic instead of a default value

In some circumstances, you may opt to use [conditional logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) instead of setting a default value. Conditional logic allows you to send messages that differ based on the value of a custom attribute. Additionally, you can use conditional logic to [abort messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) to customers with null or blank attribute values. 

#### Use case

For example, let's say you're sending a rewards balance notification to customers. There isn't a good way to account for customers with low and null balances using default values.

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

2. Send a completely different message to these customers, such as:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

In this use case, a user with a blank or null first name will get the message "Thanks for downloading". You should include a [default value]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) for first name to make sure that your customer doesn't see Liquid in the event of a mistake.

{% endraw %}

## Variable tags

You can use the `assign` tag to create a variable in the message composer. We recommend using a unique name for your variable. If you create a variable with a similar name to the supported personalization tags (such as `language`), this may affect your messaging logic.

After you create a variable, you can reference that variable in your messaging logic or message. This tag comes in handy when you want to reformat content that is returned from our [Connected Content]({% image_buster /assets/img_archive/personalized_firstname_.png %}) feature. You can read more in Shopify's documentation on [variable tags](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert tip %}
Find yourself assigning the same variables in every message? Instead of writing out the `assign` tag over and over again, you can save that tag as a Content Block and put it at the top of your message instead.

1. [Create a Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Give your Content Block a name (no spaces or special characters).
3. Select **Edit** at the bottom of the page.
4. Type in your `assign` tags.

As long as the Content Block is at the top of your message, every time the variable is inserted into your message as an object, it will refer to your chosen custom attribute!
{% endalert %}

### Use case

Let's say that you allow your customers to cash in their rewards points for prizes after they accrue 100 rewards points. So, you only want to message customers who would have a points balance greater than or equal to 100 if they made that additional purchase:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Iteration tags

{% raw %}
Iteration tags can be used to run a block of code repeatedly. The use case below features the `for` tag.

### Use case

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

In this use case, we check the first five items in the sneaker brands viewed array. If one of those items is converse, we create the `converse_viewer` variable and set it to true.

Then, we send the sale message when `converse_viewer` is true. Otherwise, we abort the message.

This is a simple example of how iteration tags can be used in the Braze message composer. You can find more information in Shopify's documentation on [iteration tags](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Syntax tags

Syntax tags can be used to control how Liquid is rendered. You can use the `echo` tag to return an expression. This is the same as wrapping an expression using curly brackets, except you can use this tag within Liquid tags. You can also use the `liquid` tag to have a block of Liquid without any delimiters on each tag. Each tag has to be in its own line when using the `liquid` tag. Check out Shopify's documentation on [syntax tags](https://shopify.dev/api/liquid/tags#syntax-tags) for more information and examples.

With [whitespace control](https://shopify.github.io/liquid/basics/whitespace/), you can remove whitespaces around your tags, helping you further control what the Liquid output looks like.

## HTTP status codes {#http-personalization}

You can utilize the HTTP status from a [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) call by first saving it as a local variable and then using the `__http_status_code__` key. For example:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
This key will only be automatically added to the Connected Content object if the endpoint returns a JSON object. If the endpoint returns an array or other type, then that key can't be set automatically in the response.
{% endalert %}

## Sending messages based on language, most recent locale, and time zone

In some situations, you may wish to send messages that are specific to particular locales. For example, Brazilian Portuguese is typically different than European Portuguese.

### Use case: Localize based on recent locale

Here's a use case of how you can use the most recent locale to further localize an internationalized message.

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

In this use case, customers with a most recent locale of `pt_BR` will get a message in Brazilian Portuguese, and customers with a most recent locale of `pt_PT` will get a message in European Portuguese. Customers who don't meet the first two conditions but have their language set to Portuguese will get a message in whatever you'd like the default Portuguese language type to be.

### Use case: Target users by time zone

You can also target users by their time zone. For example, send one message if they are based in EST and another if they are PST. To do this, save the current time in UTC, and compare an if/else statement with the user's current time to send the right message for the right time zone. You should set the campaign to send in the user's local time zone, to give them the campaign at the right time. 

See the following use case for how to write a message that will go out between 2 pm and 3 pm and will have a specific message for each time zone.

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

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
