---
nav_title: Custom Event
page_order: 4

page_type: reference
description: "This reference article lists Liquid use cases based on custom events."
---

# Custom Event

Here are some examples of how you can use Liquid to personalize your campaings based on custom events:

## Abort Push Notification if a Custom Event is Within Two Hours of Now

This use case calculates the time until a specific event, and depending on the amount of time left, will display different personalized messages.

For example, you may want to prevent a push from going out if a custom event property will pass in the next two hours. This example uses the scenario of an abandoned cart for a train ticket.

{% raw %}

```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don’t forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```

{% endraw %}

## Send a Campaign Each Time a User Performs a Custom Event Three Times

**Goal:** Send a campaign to a user when they abandon their cart three times in a row.

{% raw %}

```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message('error calculating cadence') %}
{% elsif cadence != 0 %}
{% abort_message('skip message') %}
{% endif %}
Did you forget something in your shopping cart?
```

{% endraw %}

{% alert important %} You must have an event property of the custom event count, or use a webhook to your Braze endpoint. This is so you can increment a custom attribute (`example_event_count`) every time the user performs the event. This example uses a cadence of three (1, 4, 7, 10, etc).{% endalert %}

## Send a Message to Users Who Have Only Purchased from One Category

This use case captures a list of the categories a user has purchased from, and if only one purchase category exists, will display a personalized message.

{% raw %}

```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1%}
{{uniq_cat}}
{% else %}
{% abort_message() %}
{% endif %}
```

{% endraw %}
