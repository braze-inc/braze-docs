---
nav_title: Miscellaneous
page_order: 7

page_type: reference
description: "This reference article lists Liquid use cases based on data types and other miscellaneous goals."
---

# Miscellaneous

Here are some more ways to personalize your campaigns using Liquid:

## Capitalize the First Letter of Every Word in a String

This use case takes a string of words, splits them into an array, and capitalizes the first letter of each word.

{% raw %}

```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```

{% endraw %}

## Compare Custom Attribute Value Against an Array

This use case takes a list of favorite stores, checks if any of a user's favorite stores are in that list, and if so, will display a special offer from those stores.

{% raw %}

```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No Attribute Found") %}
{% endif %}
{% endfor %}
```

{% endraw %}

{% alert important %} This sequence has a `{% break %}` tag in the primary conditional statement. This causes the loop to stop when a match is found. If you want to display many or all matches, remove the `{% break %}` tag. {% endalert %}

## Create an Upcoming Event Reminder

This use case allows users to set up upcoming reminders based on custom events. The example scenario allows a user to set a reminder for a policy renewal date that is 26 or more days away, where reminders are sent 26, 13, 7, or 2 days before the policy renewal date.

{% raw %}

```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, then the number of days could have an impact on whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties that are being sent to Braze.
{% endcomment %}

{% comment %}
When testing, ensure the Campaign ID, Campaign API Endpoint or Canvas ID, Canvas API Endpoint are entered correctly. In this example, Canvas ID and Canvas API endpoint have been set up for sharing with client; in practice this can be testing using a Campaign ID and Campaign API endpoint..
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: "%s" %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: "%s" %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away, if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: "%Y-%m-%dT%H:%M" }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: "%Y-%m-%dT%H:%M:%S+0000}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_x}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: "%Y-%m-%dT%H:%M:%S+0000" }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away, but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 < {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: "%Y-%m-%dT%H:%M:%S+0000}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_x}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "2021-03-24T20:04:00+0000"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away, but more than 7 days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 < {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: "%Y-%m-%dT%H:%M:%S+0000}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_x}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: "%Y-%m-%dT%H:%M:%S+0000" }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 7 days away, but more than 2 days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% else {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: "%Y-%m-%dT%H:%M:%S+0000}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_x}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: "%Y-%m-%dT%H:%M:%S+0000" }}"
}
}
{% endif %}
```

{% endraw %}

{% alert important %} You will need a custom event `reminder_capture`, and the custom event properties must include at least:

- `reminder-id`: Identifier of the custom event
- `reminder_date`: User-submitted date when their reminder is due
- `message_personalisation_X`: Any properties needed to personalize the message at time of send

{% endalert %}

## Find a String Within an Array

This use case checks if a custom attribute array contains a specific string, and if it exists, will display different messages.

{% raw %}

```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.

{% elsif custom_attribute.${airportCompleted} == false %}
Clear helps you breeze through airport security. Complete your one-time in-person setup next time you are at the airport. It only takes about 5 minutes.

{% else %}
Your account is all setup
{% endif %}
```

{% endraw %}

## Find the Largest Value in an Array

This use case calculates the highest value in a given custom attribute array to use in user messaging.

For example, you may want to show a user what the current high score is, or highest bid on an item.

{% raw %}

```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```

{% endraw %}

{% alert important %} You must use a custom attribute that has an integer value and is part of an array (list). {% endalert %}

## Find the Smallest Value in an Array

This use case calculates the lowest value in a given custom attribute array to use in user messaging.

For example, you may want to show a user what the lowest score is, or the cheapest item.

{% raw %}

```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```

{% endraw %}

{% alert important %} You must use a custom attribute that has an integer value and is part of an array (list). {% endalert %}

## Query the End of a String

This use case queries the end of a string to use in messaging.

{% raw %}

```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}} | first } %}
{% assign marketplace = {{{{interest}} | split: "" | reverse | join: "" |  truncate: 4, ""}} %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```

{% endraw %}

## Query Values in an Array From a Custom Attribute with Multiple Combinations

This use case takes a list of soon to be expired shows, checks if any of a user's favorite shows are in that list, and if so, will display a message notifying the user that they will expire soon.

{% raw %} 

```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not Found") %}
{% endif %}
```

{% endraw %}

{% alert important %} You will need to find matches between the arrays first, then build logic at the end to split up the matches. {% endalert %}
