---
nav_title: User profile
article_title: User profile
page_order: 0
description: "Learn how to personalize messages with user profile data, including standard attributes, custom attributes, and event properties."
---

# User profile

> Personalize your messages with data stored on each user's profile, including standard attributes, custom attributes, and event properties. Braze makes this data available through Liquid tags that you insert directly into your message content.

## Standard attributes

{% raw %}
Standard attributes are predefined profile fields that Braze tracks automatically, such as `{{${first_name}}}`, `{{${email_address}}}`, and `{{${city}}}`. Because these attributes follow a consistent naming convention, you can reference them in any message without additional setup.

For example, to greet a user by their first name:

```liquid
Hi {{${first_name} | default: 'there'}}, check out our latest picks for you!
```
{% endraw %}

For a complete list of standard attribute tags, see [Supported personalization tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

## Custom attributes

{% raw %}
Custom attributes are profile fields unique to your workspace, such as loyalty tier, favorite category, or account type. Reference them using the `{{custom_attribute.${attribute_name}}}` tag.

For example, to personalize a message based on a user's membership tier:

```liquid
{% if custom_attribute.${membership_tier} == 'gold' %}
  As a Gold member, you get early access to our new collection.
{% else %}
  Upgrade your membership for early access to new collections.
{% endif %}
```
{% endraw %}

For more information about creating and managing custom attributes, see [Custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).

## Event properties

{% raw %}
When a campaign or Canvas is triggered by a custom event or purchase, the event's properties are available for personalization. Reference them using `{{event_properties.${property_name}}}`.

For example, if a custom event `completed_purchase` includes a `product_name` property:

```liquid
Thanks for purchasing {{event_properties.${product_name}}}! Your order is on its way.
```
{% endraw %}

Event properties are available in action-based campaigns and the first step of an action-based Canvas. For more information, see [Custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

## API trigger properties

{% raw %}
For campaigns and Canvases triggered through the API, you can pass additional data using the trigger properties object. Reference these values with `{{api_trigger_properties.${property_name}}}`.

For example:

```liquid
Your verification code is {{api_trigger_properties.${verification_code}}}.
```
{% endraw %}

For more information, see [API trigger properties object]({{site.baseurl}}/api/objects_filters/trigger_properties_object/).

## Device attributes

{% raw %}
You can also reference attributes from the user's most recently used device. For example, `{{most_recently_used_device.${model}}}` returns the device model name, and `{{most_recently_used_device.${os}}}` returns the operating system.
{% endraw %}

For the full list of device attribute tags, see [Supported personalization tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#most-recently-used-device-information).

## Setting default values

If a profile field is empty for a given user, Braze renders a blank string by default. To prevent incomplete-looking messages, set a fallback value using the `default` Liquid filter.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}},
```
{% endraw %}

For more information, see [Setting default values]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/).
