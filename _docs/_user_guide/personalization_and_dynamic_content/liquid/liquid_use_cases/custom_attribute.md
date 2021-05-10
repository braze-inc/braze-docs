---
nav_title: Custom Attribute
page_order: 3
description: "Liquid use cases based on custom attributes."
---

# Custom Attribute

Here are some ways you can use Liquid to personalize your campaigns based on custom attributes:

## Send a Message if a User Meets Two or More Custom Attributes

**Goal:** Use "if this AND that" logic to personalize a message based on multiple custom attributes.

{% raw %}

```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead end of a dirt road. The road goes to the east. In the distance you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```

{% endraw %}

## Subtract Two Custom Attributes to Display the Difference as a Monetary Value

**Goal:** Calculate the difference between two Custom Attributes as a monetary value to let a user know how far they have to reach a goal.

{% raw %}

```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
{% endif %}
```

{% endraw %}

## Reference a User's First Name if Their Full Name is Stored in the first_name Field

**Goal:** If a user has their first and last name stored in the `first_name` field, use this Liquid to only pull the first word listed.

{% raw %}

```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

{% endraw %}