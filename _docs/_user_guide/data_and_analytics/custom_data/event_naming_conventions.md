---
nav_title: Event Naming Conventions
article_title: Event Naming Conventions
page_order: 0
page_type: reference
description: "This reference article covers proper event naming conventions and best practices."

---

# Event naming conventions

Ensuring consistency in your event and attribute taxonomy during your Braze integration will keep your data clean and usable by new and existing users of the Braze platform. This helps to avoid issues later on that can result in triggering a campaign to the wrong audience or discrepancies in results from using the wrong event.

## Best practices

- Keep your naming convention clear.
- Consistent casing and formatting of event names.
- Avoid giving events similar names.
- Avoid long event attribute strings which will be truncated or cut off in the Braze dashboard.

## Naming conventions

### Use event groups

__Use groups to differentiate parts of your product to name events.__ By categorizing your product into groups any user can clearly understand what the event is referring to and what it does.

### Event naming structure

The most common naming structure is `group_noun_action`. Events should all be lower case to avoid casing instrumentation errors and identifying properties.

### Properties

Is it an event or a property? __tag one event and then identify differences by using properties.__

This is helpful for events that are inherently the same but have minor differences, such as channels for a campaign. We can also easily see how users flow through events. Aggregation of these events will be more tedious as we will have to create a custom event to group them together.
