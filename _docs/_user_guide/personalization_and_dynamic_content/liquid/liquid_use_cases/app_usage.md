---
nav_title: App Usage
page_order: 2
description: "Liquid use cases for a user's app usage and app habits."
---

# App Usage

Here are some examples of how you can use Liquid to personalize your campaigns based on a user's app habits:

## Send Messages in a User's Language if They've Logged a Session

**Goal:** First determine whether a user has logged a session yet. If they haven't, use a custom attribute (`user_language`) to decide which language to display their campaign in. If they have logged a session, use their automatically collected `language` to decide which language to display the campaign in.

{% raw %}

```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on Custom Attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on Custom Attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```

{% endraw %}

## Personalize Messages Based on When a User Last Opened the App

**Goal:** Change the tone of your message depending on whether a user has recently opened up the app or not. For example, a message for a user who recently opened the app might say "Happy to see you again!", while a message for a user who hasn't opened the app in a while might say "It's been a while, here are some of our latest updates."

{% raw %}

```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while, here are some of our latest updates.
{% endif %}
```

{% endraw %}

## Show a Different Message if a User Last Used the App Less Than Three Days Ago

**Goal:** Personalize your messages based on how active a user is.

{% raw %}

```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```

{% endraw %}