---
nav_title: Time Zones
page_order: 9

page_type: reference
description: "Liquid use cases based on time zones and timestamps."
---

# Time Zones

Here are some examples of ways you can use Liquid to personalize messages based on a user's local time zone:

## Append the CST Timezone to a Custom Attribute

This use case displays a custom date attribute in a given time zone.

Option 1:
{% raw %}

```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```

{% endraw %}

Option 2:
{% raw %}

```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```

{% endraw %}

## Insert a Timestamp

This use case displays a message that includes a timestamp in their current timezone.

The example provided below will display the date as YYYY-mm-dd HH:MM:SS, such as 2021-05-03 10:41:04.

{% raw %}

```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | timezone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```

{% endraw %}

## Only Send a Canvas Push During a Window of Time in a User's Local Time Zone

This use case checks a user's time zone, and if it matches, will display a specific message.

{% raw %}

```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8am and 8pm!
```

{% endraw %}

## Send a Reoccuring In-App Message Campaign Between a Window of Time in a User's Local Time Zone

This use case will display a message if a user's current time falls within a set window.

For example, the scenario below lets a user know that a store is closed.

{% raw %}

```liquid
{% assign time = 'now' | time_zone: ${time_zone} %} 
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11am and 9pm!

{% else%} 
{% abort_message("not sent because the store is open") %}
{% endif %}
```

{% endraw %}

## Send Different Messages on Weekdays vs Weekends in a User's Local Time Zone

This use case will check if a user's current day of the week is Saturday or Sunday, and depending on the day, will display different messages.

{% raw %}

```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It’s {{today}}, why don’t you open the app for your transactions?

{% else %}
It’s {{today}}, why don’t you visit the store?
{% endif %}
```

{% endraw %}

## Send Different Messages Based on Time of Day in a User's Local Time Zone

This use case will display a message if a user's current time falls outside a set window.

For example, you may want to tell a user about a time sensitive opportunity that depends on the time of day.

{% raw %}

```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```

{% endraw %}

{% alert note %} This is the opposite of [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns). {% endalert %}
