---
nav_title: Time Zones
page_order: 9

page_type: reference
description: "Liquid use cases based on time zones and timestamps."
---

# Time Zones

Here are some examples of ways you can use Liquid to personalize messages based on a user's local time zone:

## Append the CST Timezone to a Custom Attribute

**Goal:** Display a custom date attribute in Central Standard Time (CST), or UTC -6.

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

**Goal:** Insert a timestamp in the format of your choosing. The example provided below will display the date as YYYY-mm-dd HH:MM:SS, such as 2021-05-03 10:41:04.

{% raw %}

```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | timezone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```

{% endraw %}

## Only Send a Canvas Push During a Window of Time in a User's Local Time Zone

**Goal:** Only send a Canvas push between a set window of time, in the user's local time zone.  

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

## Personalize Messages Based on a User's Local Time Zone

**Goal:** Use time zones to segment users based on the region they are in.

{% raw %}

```liquid
{% if {{${time_zone}}} == ‘America/Chicago’ %}

Here's a message for users in UTC -6.

{% else %}
{% abort_message() %}
{% endif %}
```

{% endraw %}

## Send a Reoccuring In-App Message Campaign Between a Window of Time in a User's Local Time Zone

**Goal:** Schedule a reocurring campaign to send based on a set a window of time in a user's local time zone. For example, the scenario below lets a user know that a store is closed.

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

**Goal:** Send different messages to users on weekdays versus the weekend, in a user's local time zone.

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

**Goal:** Send a message only during a certain time period, based on the user's local time zone. For example, you may want to tell a user about a time sensitive opportunity that depends on the time of day.

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

{% alert note %} This is the opposite of [Quiet Hours](1). {% endalert %}

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns