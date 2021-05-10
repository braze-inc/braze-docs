---
nav_title: Anniversaries and Birthdays
page_order: 1
description: "Liquid use cases for special dates, like anniversaries and birthdays."
---

# Anniversaries and Birthdays

Here are some examples of how you can use Liquid to personalize your campaigns to celebrate anniversaries and birthdays:

## Personalize Messages Based on a User's Anniversary Year

**Goal:** Calculate if it's the anniversary of a user's sign up date, and display a different message depending on how many years they are celebrating.

{% raw %}

```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${Signup Date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${Signup Date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${Signup Date}}} | date: "%Y" %}
{% if {{this_month}} == {{anniversary_month}} %}
{% if {{this_day}} == {{anniversary_day}} %}
{% if {{anniversary_year}} == '2016' %}
Happy one year anniversary!
{% elsif {{anniversary_year}} == '2015' %}
Happy two year anniversary!
{% elsif {{anniversary_year}} == '2014' %}
Happy three year anniversary!
{% elsif {{anniversary_year}} == '2013' %}
Happy four year anniversary!
{% elsif {{anniversary_year}} == '2012' %}
Happy five year anniversary!
{% elsif {{anniversary_year}} == '2011' %}
Happy six year anniversary!
{% elsif {{anniversary_year}} == '2010' %}
Happy seven year anniversary!
{% else %}
{% abort_message(not same month) %}
{% else %}
{% abort_message(not same day) %}
{% else %}
{% abort_message(not same year) %}
{% endif %}
{% endif %}
{% endif %}
```

{% endraw %}

## Personalize Messages Based on a User's Birthday Week

**Goal:** Use the week of a user's birthday to decide whether or not to send a birthday message.

{% raw %}

```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = ${date_of_birth}  | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```

{% endraw %}

## Send Campaigns to Users in Their Birthday Month

**Goal:** Use the month of a user's birthday to decide whether or not to send a birthday message.

{% raw %}

```liquid
{% assign this_month = ‘now’ | date: “%B” %}
{% assign birth_month = {{${date_of_birth}}} | date: “%B” %}
{% if {{this_month}} == {{birth_month}} %}
Message body 
{% else %} 
{% abort_message() %}
{% endif %} 
```

{% endraw %}