---
nav_title: Setting default values
article_title: Setting Default Liquid Values
page_order: 5
description: "This reference article cover how to set default fallback values for any personalization attribute that you use in your messages."

---

# Setting default values

{% raw %}

> Default fallback values can be set for any personalization attribute that you use in your messages. This article covers how default values work, how to set them up, and how to use them in your messages.

## How they work

Default values can be added by specifying a [Liquid Filter](http://docs.shopify.com/themes/liquid-documentation/filters) (use `|` to distinguish the filter inline, as shown) with the name "default."

```
| default: 'Insert Your Desired Default Here'
```

If a default value isn't provided and the field is missing or not set on the user, the field will be blank in the message.

The following example shows the correct syntax for adding a default value. In this case, the words "Valued User" will replace the attribute `{{ ${first_name} }}` if a user's `first_name` field is empty or unavailable.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

To a user named Janet Doe, the message would appear to the user as either:

```
Hi Janet, thanks for using the App!
```

Or...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
The default value will show for empty values, but not for blank values. An empty value doesn't contain anything, while a blank value contains whitespace characters (such as spaces) and no other characters. For example, an empty string could look like `""` and a blank string could look like `" "`.
{% endalert %}

## Setting default values for different data types

The example above shows how to set a default for a string. You can set default values for any Liquid data type that has the value of `empty`, `nil` (undefined), or `false`, which includes strings, booleans, arrays, objects, and numbers.

### Use case: Booleans

Let's say you have a boolean custom attribute called `premium_user` and you want to send a personalized message based on the user's premium status. Some users don't have a premium status set up, so you'll need to set up a default value to capture those users.

1. You'll assign a variable called `is_premium_user` to the `premium_user` attribute with a default value of `false`. This means that if `premium_user` is `nil`, the value of `is_premium_user` will default to `false`. 

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2. Then, use conditional logic to specify the message to send if `is_premium_user` is `true`. In other words, what to send if `premium_user` is `true`. You'll also assign a default value to the user's first name, in case we don't have the user's name.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3. Finally, specify what message to send if `is_premium_user` is `false` (which means `premium_user` is `false` or `nil`). Then you'll close the conditional logic.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### Use case: Numbers

Let's say you have a numeric custom attribute called `reward_points` and you want to send a message with the user's reward points. Some users don't have reward points set up, so you'll need to set up a default value to account for those users.

1. Begin the message by addressing the user's first name or a default value of `Valued User`, in case you don't have their name.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. End the message with how many reward points the user has by using the custom attribute called `reward_points` and using the default value of `0`. All users whose `reward_points` have a `nil` value will have `0` reward points in the message.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Use case: Objects

Let's say you have a nested custom attribute object called `location` that contains the properties `city` and `state`. If any of these properties aren't set, you want to encourage the user to provide them.

1. Address the user by their first name and include a default value, in case you don't have their name.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Write a message that says you'd like to confirm the user's location.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3. Insert the user's location into the message and assign default values for when the address property isn't set.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### Use case: Arrays

Let's say you have an array custom attribute called `upcoming_trips` that contains trips with the properties `destination` and `departure_date`. You want to send users personalized messages based on whether they have trips scheduled.

1. Write conditional logic to specify that a message shouldn't send if `upcoming_trips` is `empty`.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2. Specify what message to send if `upcoming_trips` has content:<br><br>**2a.** Address the user and include a default value, in case you don't have their name. <br>**2b.** Use a `for` tag to specify that you'll pull properties (or information) for each trip that is contained in `upcoming_trips`. <br>**2c.** List the properties in the message and include a default value for if the `departure_date` isn't set. (Let's say a `destination` is required for a trip to be created, so you don't need to set a default value for that.)<br>**2d.** Close the `for` tag, then close the conditional logic.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
