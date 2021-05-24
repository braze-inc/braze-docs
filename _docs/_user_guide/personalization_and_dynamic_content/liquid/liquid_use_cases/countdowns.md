---
nav_title: Countdowns
page_order: 5

page_type: reference
description: "This reference article lists Liquid use cases based on countdowns, or to calculate the difference in time."
---

# Countdowns

You can use Liquid to create countdowns both big and small—take a look through some of our sample use cases to learn how.

## Add X Days to Today's Date

**Goal:** Tell a user information about what's coming up a few days from now. For example, you may want to send a mid-week message that shows events in the area for the weekend, like "Here are the movies we're showing in 3 days!"

{% raw %}

```liquid
{{ “now” | date:‘%s’ | plus:259200 | date:“%F” }}
```

{% endraw %}

{% alert important %} You may want to include a URL or Deeplink to a list of events in your message so you can send the user to a list of actions that are happening in the future. The `plus` value will always be in seconds. {% endalert %}

## Calculate a Countdown From a Set Point in Time

**Goal:** Calculate the difference in days between today and a specific date.

{% raw %}

```liquid
{% assign event_date = '2020-08-19' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```

{% endraw %}

## Create a Countdown for Specific Shipping Dates and Priorities

**Goal:** Specify a countdown for standard, express, and overnight shipping for your users based on specific time frames.

{% raw %}

```liquid
{% assign standard_shipping_start = "2019-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2019-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2019-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2019-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
difference s days: {{difference_s_days}}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
difference e days: {{difference_e_days}}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif%}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message() %}
{% endif %}
```

{% endraw %}

## Create a Countdown in Days

**Goal:** Tell a user how many days until an event will happen, such as their order arriving or a coupon expiring.

{% raw %}

```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```

{% endraw %}

{% alert important %} You will need a Custom Attribute field with a `date` value. {% endalert %}

## Create a Countdown From Days to Hours to Minutes

**Goal:** Tell a user how much time is left until an event will happen, and change the time value (days, hours, minutes) depending upon when the missage is sent relative to the expiration date. For example, if there's two days until the order arrives: "Your order will arrive in 2 days." If there's less than a day: "Your order will arrive in 17 hours."

{% raw %}

```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```

{% endraw %}

{% alert important %} You will need a Custom Attribute field with a `date` value. You will also need to set time thresholds of when you want the time to be displayed in days, hours, and minutes. {% endalert %}

## Create a Countdown to a Future Date

**Goal:** Tell a user how much time (days, hours, or minutes) until a specific event starts. 

{% raw %}

```liquid
{% assign event_date = '2019-02-19' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
There are difference_days until your birthday!
{% endif %}
```

{% endraw %}

## Display Different Messages Depending on Whether There are Minutes, Hours, or Days Left

**Goal:** Have a countdown get increasingly granular by going from days to hours to minutes depending on how much time is left.

<!---is this a duplicate of "Create a Countdown from Days to Hours to Minutes?" --> 

{% raw %}

```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left in the scheme!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left in the scheme!
{% else %}
You have {{difference_days}} days left in the scheme!
{% endif %}
{{today]]
```

{% endraw %}

## Display How Many Days Left Until a Custom Date Attribute Will Arrive

**Goal:** Have a recurring campaign send every day that evaluates certain criteria, but aborts if certain logic is not met. In this example, a user will receive a message if it is within two days of the custom date attribute. Otherwise, the message will not send.

{% raw %}

```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

## Display How Much Time Is Left, and Abort the Message if There’s Only X Time Left

**Goal:** Tell a user that they have a certain amount of time left, but don't send the message if it's within two hours of the event ending. For example, "You have 10 hours left to buy your ticket for London", but don't send the message if it's within two hours of flight time for London.

{% raw %}

```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don’t forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```

{% endraw %}

{% alert important %} You will need a Custom Event Property. {% endalert %}

## In-App Message to Send X Days Before Users' Membership Ends

**Goal:** Nudge your users to renew or upgrade their membership before it expires using an in-app message.

{% raw %}

```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% else %}
You have few days left in your trial, make sure to upgrade!
{% endif %}
```

{% endraw %}

## Personalize In-App Messages Based on Users' Date and Language

**Goal:** Use Liquid logic to consolidate existing in-app message campaigns. For example, you might send a series of upsell messages to users once a month to let them know how long an offer is still valid with four in-app messages:

- Initial
- 2 days left
- 1 day left
- Final day

These in-app messages are sent in multiple languages, depending on the user's language preference.

{% raw %}

```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message('calculation failed') %}
{% endif %}
```

{% endraw %}

{% alert important %} You will need to assign a `date` value and include abort logic if the given date falls outside of the date range. For exact day calculations, the assigned end date must include 23:59:59. {% endalert %}

## Template in the Date 30 Days from Now, Formatted as Month and Day

**Goal:** Display the date 30 days from now as "Month Day". For example: "Your membership expires in 30 days, on January 5." 

{% raw %}

```liquid
{% assign today
 = 'now' | date: "%s" %}
{% assign thirty_days = {{today}} | plus: 2592000 | date: "%B %d" %}
```

{% endraw %}

