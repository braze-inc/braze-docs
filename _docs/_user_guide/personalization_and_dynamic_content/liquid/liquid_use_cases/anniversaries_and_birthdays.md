---
nav_title: Anniversaries and Birthdays
page_order: 1

page_type: reference
description: "This reference article lists Liquid use cases for special dates, like anniversaries and birthdays."
---

# Anniversaries and Birthdays

Here are some examples of how you can use Liquid to personalize your campaigns to celebrate anniversaries and birthdays.

## Personalize Messages Based on a User's Anniversary Year {#anniversary-year}

**Goal:** Calculate if it's the anniversary of a user's sign-up date, and display a different message depending on how many years they are celebrating.

{% raw %}

```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${signup_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${signup_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${signup_date}}} | date: "%Y" %}
{% if {{this_month}} == {{anniversary_month}} %}
{% if {{this_day}} == {{anniversary_day}} %}
{% if {{anniversary_year}} == ‘2021’ %}
Happy one year anniversary!
{% elsif {{anniversary_year}} == ‘2020’ %}
Happy two year anniversary!
{% elsif {{anniversary_year}} == ‘2019’ %}
Happy three year anniversary!
{% elsif {{anniversary_year}} == ‘2018’ %}
Happy four year anniversary!
{% elsif {{anniversary_year}} == ‘2017’ %}
Happy five year anniversary!
{% elsif {{anniversary_year}} == ‘2016’ %}
Happy six year anniversary!
{% elsif {{anniversary_year}} == ‘2015’ %}
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

**Explanation:** Here, we use the reserved variable `now` to template in the current date and time in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki") format. The filters `%B` (month, i.e. "May") and `%d` (day, i.e. "18") format the current month and day. We then use the same date and time filters on the `signup_date` values to ensure we can compare the two values using conditional tags and logic.

Then we repeat three more variable statements to get the `%B` and `%d` for the `signup_date`, but also adding `%Y` (year, i.e. "2021"). This forms the date and time of the `signup_date` into just the year. Knowing the day and month lets us check if the user's anniversary is today, and knowing the year tells us how many years it's been—which lets us know how many years to congratulate them on!

{% alert tip %} You can create as many conditions as years you've been collecting signup dates. {% endalert %}  

## Personalize Messages Based on a User's Birthday Week {#birthday-week}

**Goal:** Use the week of a user's birthday to decide whether or not to send a birthday message.

{% raw %}

``` liquid
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

**Explanation:** Similar to the [anniversary year](#anniversary-year) use case, here we take the reserved variable `now` and use the `%W` filter (week, i.e. week 12 out of 52 in a year) to get the number week of the year that the user's birthday falls within. If the user's birthday week matches the current week, we send them a message congratulating them! 

We also include statements for `last_week` and `next_week` to further personalize your messaging.

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

**Explanation:** Similar to the [birthday week](#birthday-week) use case, except here we use the `%B` filter (month, i.e. "May") to calculate which users have a birthday this month. A potential application could be addressing birthday users in a monthly email.
