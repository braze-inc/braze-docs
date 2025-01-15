---
nav_title: Event Naming Conventions
article_title: Event Naming Conventions
page_order: 10
page_type: reference
description: "This reference article covers proper event naming conventions and best practices."

---

# Event naming conventions

> This page covers proper event naming conventions and best practices. By maintaining consistency in your event and attribute taxonomy, you'll keep your data clean and usable for new and existing users of the Braze platform. This helps avoid issues later, such as triggering a campaign to the wrong audience or generating wrong results after using the wrong event.

## Best practices

- Keep your naming convention clear.
- Use consistent casing and formatting of event names.
- Avoid giving events similar names.
- Avoid long event attribute strings, which will be truncated or cut off in the Braze dashboard.

## Naming conventions

### Use event groups

Use groups to differentiate parts of your product to name events. By categorizing your product into groups, any user can clearly understand what the event is referring to and what it does.

### Event naming structure

The most common naming structure is `group_noun_action`. Events should all be lowercase to avoid casing instrumentation errors and identifying properties.

### Properties

Tag one event and then identify differences by using properties. This is helpful for events that are inherently the same but have minor differences, such as channels for a campaign. We can also easily see how users flow through events. Refer to the [event properties object]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) for an example and additional context.
